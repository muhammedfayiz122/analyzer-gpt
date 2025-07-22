from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR_DOCKER,TIMEOUT_DOCKER

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
    print("Starting Docker Container......")
    await docker.start()
    print("Docker Container started")

async def stop_docker_container(docker):
    """
    To stop Docker Container
    """
    print("Stopping Docker Container......")
    await docker.start()
    print("Docker Container stopped")
