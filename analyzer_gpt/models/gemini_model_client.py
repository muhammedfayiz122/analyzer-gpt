from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from analyzer_gpt.exception.custom_exception import CustomException
import sys
import os

load_dotenv()

def load_model_client():
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        gemini_model_client = OpenAIChatCompletionClient(model="gemini-1.5-flash", api_key=api_keyi)
        return gemini_model_client
    except Exception as e:
        raise CustomException(e)
    
if __name__ == "__main__":
    from autogen_core.models import UserMessage
    import asyncio
    async def main():
        model_client = load_model_client()
        message = UserMessage(content="Hello, how are you?", source="user")
        # response = await model_client.create([message])
        print(model_client)
    asyncio.run(main())
    