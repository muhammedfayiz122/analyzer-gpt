from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):
    """

    Args:
        code_executor (_type_): _description_
    """
    code_executor_agent = CodeExecutorAgent(
        name="Python_Code_Executor",
        code_executor=code_executor
    )
    return code_executor