import os
import openai

try:
    import google.generativeai as genai
except Exception:
    genai = None


class AIProvider:
    """Selects and interacts with different AI providers."""

    def __init__(self) -> None:
        self.provider = os.getenv("AI_PROVIDER", "openai").lower()
        self.temperature = float(os.getenv("MODEL_TEMPERATURE", "0.7"))
        self.max_tokens = int(os.getenv("MODEL_MAX_TOKENS", "150"))

        if self.provider in ("openai", "chatgpt"):
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY is not set")
            openai.api_key = api_key
            base = os.getenv("OPENAI_API_BASE")
            if base:
                openai.api_base = base
            self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

        elif self.provider == "mcp":
            api_key = os.getenv("MCP_API_KEY")
            base = os.getenv("MCP_API_BASE")
            if not api_key or not base:
                raise ValueError("MCP_API_KEY and MCP_API_BASE must be set for MCP provider")
            openai.api_key = api_key
            openai.api_base = base
            self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

        elif self.provider == "gemini":
            if genai is None:
                raise ImportError("google-generativeai package is required for Gemini provider")
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY is not set")
            genai.configure(api_key=api_key)
            model_name = os.getenv("GEMINI_MODEL", "gemini-pro")
            self.model = genai.GenerativeModel(model_name)

        else:
            raise ValueError(f"Unsupported AI_PROVIDER '{self.provider}'")

    def chat_completion(self, messages):
        """Return a chat completion from the configured provider."""
        if self.provider in ("openai", "chatgpt", "mcp"):
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content

        elif self.provider == "gemini":
            history = []
            for msg in messages[:-1]:
                role = "user" if msg["role"] == "user" else "model"
                history.append({"role": role, "parts": [msg["content"]]})
            chat = self.model.start_chat(history=history)
            result = chat.send_message(messages[-1]["content"])
            return result.text

        else:
            raise ValueError(f"Unsupported provider '{self.provider}'")
