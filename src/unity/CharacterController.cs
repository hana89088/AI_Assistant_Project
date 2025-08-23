using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using WebSocketSharp;
using Newtonsoft.Json;
using Live2D.Cubism.Framework;
using Live2D.Cubism.Framework.Expression;
using Live2D.Cubism.Framework.Motion;

public class CharacterController : MonoBehaviour
{
    [Header("WebSocket Settings")]
    [SerializeField] private string websocketUrl = "ws://localhost:8080";
    private WebSocket webSocket;

    [Header("Character Model")]
    [SerializeField] private CubismModel characterModel;
    [SerializeField] private Animator characterAnimator;

    [Header("Expressions")]
    [SerializeField] private CubismExpressionController expressionController;
    [SerializeField] private string happyExpression = "Happy";
    [SerializeField] private string sadExpression = "Sad";
    [SerializeField] private string surprisedExpression = "Surprised";
    [SerializeField] private string thinkingExpression = "Thinking";
    [SerializeField] private string neutralExpression = "Neutral";

    [Header("Audio")]
    [SerializeField] private AudioSource audioSource;
    [SerializeField] private OVRLipSync lipSync;
    
    [Header("UI")]
    [SerializeField] private TMPro.TextMeshProUGUI subtitleText;
    [SerializeField] private GameObject speechBubble;
    [SerializeField] private float textDisplayDuration = 5f;

    private Queue<Message> messageQueue = new Queue<Message>();
    private bool isProcessing = false;
    private Coroutine currentSpeechCoroutine;

    [System.Serializable]
    public class Message
    {
        public string type;
        public string text;
        public string emotion;
        public string path;
        public string status;
        public string message;
        public string timestamp;
    }

    void Start()
    {
        InitializeWebSocket();
        ConnectToBackend();
        
        // Initialize character in neutral state
        if (expressionController != null)
        {
            expressionController.CurrentExpressionIndex = 0;
        }
    }

    void InitializeWebSocket()
    {
        webSocket = new WebSocket(websocketUrl);
        
        webSocket.OnOpen += (sender, e) =>
        {
            Debug.Log("WebSocket connected to backend");
            SendMessage(new { type = "unity_connected" });
        };

        webSocket.OnMessage += (sender, e) =>
        {
            Debug.Log($"Received message: {e.Data}");
            try
            {
                Message message = JsonConvert.DeserializeObject<Message>(e.Data);
                messageQueue.Enqueue(message);
            }
            catch (Exception ex)
            {
                Debug.LogError($"Error parsing message: {ex.Message}");
            }
        };

        webSocket.OnError += (sender, e) =>
        {
            Debug.LogError($"WebSocket error: {e.Message}");
        };

        webSocket.OnClose += (sender, e) =>
        {
            Debug.Log("WebSocket connection closed");
            // Attempt to reconnect after 5 seconds
            StartCoroutine(ReconnectAfterDelay(5f));
        };
    }

    void ConnectToBackend()
    {
        if (webSocket != null && webSocket.ReadyState != WebSocketState.Open)
        {
            try
            {
                webSocket.Connect();
            }
            catch (Exception e)
            {
                Debug.LogError($"Failed to connect: {e.Message}");
            }
        }
    }

    IEnumerator ReconnectAfterDelay(float delay)
    {
        yield return new WaitForSeconds(delay);
        ConnectToBackend();
    }

    void Update()
    {
        // Process queued messages
        if (messageQueue.Count > 0 && !isProcessing)
        {
            ProcessNextMessage();
        }

        // Update idle animation
        UpdateIdleAnimation();
    }

    void ProcessNextMessage()
    {
        if (messageQueue.Count == 0) return;

        isProcessing = true;
        Message message = messageQueue.Dequeue();

        switch (message.type)
        {
            case "response":
                HandleAIResponse(message);
                break;
            case "audio":
                StartCoroutine(PlayAudio(message.path));
                break;
            case "status":
                HandleStatus(message);
                break;
            case "connection":
                Debug.Log($"Backend says: {message.message}");
                break;
        }

        isProcessing = false;
    }

    void HandleAIResponse(Message message)
    {
        // Set expression based on emotion
        SetExpression(message.emotion);
        
        // Display text
        if (currentSpeechCoroutine != null)
        {
            StopCoroutine(currentSpeechCoroutine);
        }
        currentSpeechCoroutine = StartCoroutine(DisplaySpeech(message.text));
        
        // Trigger talking animation
        if (characterAnimator != null)
        {
            characterAnimator.SetBool("IsTalking", true);
        }
    }

    void SetExpression(string emotion)
    {
        if (expressionController == null) return;

        string targetExpression = neutralExpression;
        
        switch (emotion.ToLower())
        {
            case "happy":
                targetExpression = happyExpression;
                break;
            case "sad":
                targetExpression = sadExpression;
                break;
            case "surprised":
                targetExpression = surprisedExpression;
                break;
            case "thinking":
                targetExpression = thinkingExpression;
                break;
            default:
                targetExpression = neutralExpression;
                break;
        }

        // Apply expression
        for (int i = 0; i < expressionController.ExpressionsList.CubismExpressionObjects.Length; i++)
        {
            if (expressionController.ExpressionsList.CubismExpressionObjects[i].name == targetExpression)
            {
                expressionController.CurrentExpressionIndex = i;
                break;
            }
        }
    }

    IEnumerator DisplaySpeech(string text)
    {
        // Show speech bubble
        if (speechBubble != null)
        {
            speechBubble.SetActive(true);
        }

        // Animate text appearance
        if (subtitleText != null)
        {
            subtitleText.text = "";
            
            // Type out text character by character
            foreach (char c in text)
            {
                subtitleText.text += c;
                yield return new WaitForSeconds(0.03f);
            }
        }

        // Keep text visible
        yield return new WaitForSeconds(textDisplayDuration);

        // Hide speech bubble
        if (speechBubble != null)
        {
            speechBubble.SetActive(false);
        }

        // Stop talking animation
        if (characterAnimator != null)
        {
            characterAnimator.SetBool("IsTalking", false);
        }
    }

    IEnumerator PlayAudio(string audioPath)
    {
        if (audioSource == null) yield break;

        // Ensure the path is a valid file URL
        string url = audioPath.StartsWith("file://") ? audioPath : $"file://{audioPath}";

        // Load audio file
        using (UnityWebRequest www = UnityWebRequestMultimedia.GetAudioClip(url, AudioType.MPEG))
        {
            yield return www.SendWebRequest();

            if (www.result == UnityWebRequest.Result.Success)
            {
                AudioClip clip = DownloadHandlerAudioClip.GetContent(www);
                audioSource.clip = clip;
                audioSource.Play();

                // Enable lip sync if available
                if (lipSync != null)
                {
                    lipSync.audioSource = audioSource;
                }

                // Wait for audio to finish
                yield return new WaitForSeconds(clip.length);
            }
            else
            {
                Debug.LogError($"Failed to load audio: {www.error}");
            }
        }
    }

    void HandleStatus(Message message)
    {
        Debug.Log($"Status: {message.status} - {message.message}");
        
        // You can add visual indicators here
        if (message.status == "processing")
        {
            // Show thinking animation
            SetExpression("thinking");
        }
    }

    void UpdateIdleAnimation()
    {
        // Add subtle idle movements
        if (characterModel != null)
        {
            // Breathing animation
            float breathingOffset = Mathf.Sin(Time.time * 2f) * 0.02f;
            characterModel.transform.localScale = new Vector3(
                1f + breathingOffset,
                1f - breathingOffset * 0.5f,
                1f
            );

            // Slight swaying
            float swayOffset = Mathf.Sin(Time.time * 0.5f) * 2f;
            characterModel.transform.rotation = Quaternion.Euler(0, swayOffset, 0);
        }
    }

    void SendMessage(object message)
    {
        if (webSocket != null && webSocket.ReadyState == WebSocketState.Open)
        {
            string json = JsonConvert.SerializeObject(message);
            webSocket.Send(json);
        }
    }

    public void OnTextInput(string text)
    {
        // Called from UI input field
        SendMessage(new
        {
            type = "text_input",
            text = text
        });
    }

    public void StartListening()
    {
        SendMessage(new { type = "start_listening" });
    }

    public void StopListening()
    {
        SendMessage(new { type = "stop_listening" });
    }

    void OnDestroy()
    {
        if (webSocket != null && webSocket.ReadyState == WebSocketState.Open)
        {
            webSocket.Close();
        }
    }
}
