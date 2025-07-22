from autogen_ext.models.ollama import OllamaChatCompletionClient
from analyzer_gpt.exception.custom_exception import CustomException
import sys

def load_model_client():
    try:
        ollama_model_client = OllamaChatCompletionClient(model="mistral")
        return ollama_model_client
    except Exception as e:
        raise CustomException(e, sys)
    
if __name__ == "__main__":
    from autogen_core.models import UserMessage
    import asyncio
    async def main():
        model_client = load_model_client()
        message = UserMessage(content="Hello, how are you?", source="user")
        response = await model_client.create([message])
        print(response)
    asyncio.run(main())
    