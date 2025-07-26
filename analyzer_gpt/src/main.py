import asyncio
from analyzer_gpt.models.gemini_model_client import load_model_client
from analyzer_gpt.utils.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from analyzer_gpt.teams.data_analyzer_team import getDataAnalyzerTeam 
from analyzer_gpt.exception.custom_exception import CustomException
from analyzer_gpt.logger.logger import logger

async def main():
    print("Analyzer GPT CLI Running")
    model_client = load_model_client()
    docker = getDockerCommandLineExecutor()
    team = getDataAnalyzerTeam(docker=docker, model_client=model_client)
    
    try:
        task = input("Enter you query : ")
        logger.info("response: ")
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            # print(message)
            logger.info(message)
    except Exception as e:
        raise CustomException(e)
    finally :
        await stop_docker_container(docker)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        raise CustomException(e) 

            
    
    