from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from analyzer_gpt.exception.custom_exception import CustomException
from analyzer_gpt.logger.logger import logger
from analyzer_gpt.config.loader import Config
import os

docker_config = Config().cfg['docker']
WORK_DIR_DOCKER = docker_config.get('work_dir', '/temp')  
TIMEOUT_DOCKER = docker_config.get('timeout', 20)    

def getDockerCommandLineExecutor():
    """
    """
    try:
        os.makedirs(WORK_DIR_DOCKER, exist_ok=True)
        docker = DockerCommandLineCodeExecutor(
            work_dir=WORK_DIR_DOCKER,
            timeout=TIMEOUT_DOCKER,
        )
        return docker
    except Exception as e:
        raise CustomException(e) 

async def start_docker_container(docker):
    """
    To start Docker Container
    """ 
    try:
        logger.info("Starting Docker Container......")
        await docker.start()
        logger.info("Docker Container started")
    except Exception as e:
        raise CustomException(e, custom_msg="Failed to start docker container") 

async def stop_docker_container(docker):
    """
    To stop Docker Container
    """
    try:
        logger.info("Stopping Docker Container......")
        await docker.start()
        logger.info("Docker Container stopped")
    except Exception as e:
        raise CustomException(e, custom_msg="Failed to stop docker container") 
