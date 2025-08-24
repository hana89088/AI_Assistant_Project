import os
import speech_recognition as sr
from dotenv import load_dotenv
from elevenlabs import generate, play, set_api_key

from ai_provider import AIProvider


def main():
    """Simple CLI for interacting with the AI assistant using text or voice."""
    load_dotenv()

    eleven_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("TTS_VOICE_ID", "default")

    if eleven_key:
        set_api_key(eleven_key)

    provider = AIProvider()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    conversation = []

    def ask_ai(prompt: str) -> str:
        conversation.append({"role": "user", "content": prompt})
        answer = provider.chat_completion(conversation)
        conversation.append({"role": "assistant", "content": answer})
        return answer

    def speak(text: str) -> None:
        if not eleven_key:
            return
        audio = generate(text=text, voice=voice_id, model="eleven_monolingual_v1")
        play(audio)

    while True:
        mode = input("Enter 't' for text, 'v' for voice, or 'q' to quit: ").strip().lower()
        if mode == "q":
            break
        if mode == "v":
            print("Listening...")
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            try:
                user_text = recognizer.recognize_google(audio)
                print(f"You said: {user_text}")
            except sr.UnknownValueError:
                print("Could not understand audio.")
                continue
        else:
            user_text = input("You: ")

        try:
            reply = ask_ai(user_text)
        except Exception as exc:
            print(f"Error from AI provider: {exc}")
            continue

        print(f"Assistant: {reply}")
        speak(reply)


if __name__ == "__main__":
    main()
