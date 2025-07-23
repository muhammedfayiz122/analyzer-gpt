from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, TokenUsageTermination
from analyzer_gpt.agents.code_executor_agent import getCodeExecutorAgent
from analyzer_gpt.agents.data_analyzer_agent import getDataAnalyzerAgent

def getDataAnalyzerTeam(docker, model_client):
    """_summary_

    Args:
        docker (_type_): _description_
        model_client (_type_): _description_
    """
    code_executor_agent = getCodeExecutorAgent(docker)
    data_analyzer_agent = getDataAnalyzerAgent(model_client)

    termination = TextMentionTermination("TERMINATE")
    team = RoundRobinGroupChat(
        name="",
        particippants=[data_analyzer_agent, code_executor_agent],
        termination_condition=termination
        
    )
    