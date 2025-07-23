from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from analyzer_gpt.logger.logger import logger
from analyzer_gpt.config.loader import Config

docker_config = Config().cfg['docker']
WORK_DIR_DOCKER = docker_config.get('work_dir', '/temp')  
TIMEOUT_DOCKER = docker_config.get('timeout', 20)    

def getDockerCommandLineExecutor():
    """
    """
    docker = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR_DOCKER,
        timeout=TIMEOUT_DOCKER
    )
    return docker

async def start_docker_container(docker):
    """
    To start Docker Container
    """ 
    logger.info("Starting Docker Container......")
    await docker.start()
    logger.info("Docker Container started")

async def stop_docker_container(docker):
    """
    To stop Docker Container
    """
    logger.info("Stopping Docker Container......")
    await docker.start()
    logger.info("Docker Container stopped")
