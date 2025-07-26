from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, TokenUsageTermination
from analyzer_gpt.agents.code_executor_agent import getCodeExecutorAgent
from analyzer_gpt.agents.code_evaluator_agent import getCodeEvaluatorAgent
from analyzer_gpt.agents.data_analyzer_agent import getDataAnalyzerAgent

def getDataAnalyzerTeam(docker, model_client):
    """_summary_

    Args:
        docker (_type_): _description_
        model_client (_type_): _description_
    """
    code_executor_agent = getCodeExecutorAgent(docker)
    code_evaluator_agent = getCodeEvaluatorAgent(model_client)
    data_analyzer_agent = getDataAnalyzerAgent(model_client)
    
    termination = TextMentionTermination("TERMINATE") | TokenUsageTermination(max_total_token=5000)
    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_evaluator_agent, code_executor_agent],
        max_turns=10,
        termination_condition=termination
    )
    return team