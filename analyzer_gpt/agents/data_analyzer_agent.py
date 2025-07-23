from autogen_agentchat.agents import AssistantAgent
# from autogen_core import ComponentModel
from analyzer_gpt.prompts.agent_prompts import DATA_ANALYZER_SYSTEM_MESSAGE

def getDataAnalyzerAgent(model_client):
    """
    
    Args:
        model_client (_type_): _description_

    Returns:
        _type_: _description_
    """
    data_analyzer_agent = AssistantAgent(
        name="Data_Analyzer_Agent",
        model_client=model_client,
        description="An Agent that solves Data Analysis problem and gives the code as well",
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE
    )
    return data_analyzer_agent