from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
from analyzer_gpt.exception.custom_exception import CustomException
import sys
import os

load_dotenv()

def load_model_client():
    try:
        open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")
        open_router_model_client =  OpenAIChatCompletionClient(
            base_url="https://openrouter.ai/api/v1",
            model="openrouter/cypher-alpha:free",
            api_key = open_router_api_key,
            model_info={
                "family":'deepseek',
                "vision" :True,
                "function_calling":True,
                "json_output": False
            }
        )
        return gemini_model_client
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
    