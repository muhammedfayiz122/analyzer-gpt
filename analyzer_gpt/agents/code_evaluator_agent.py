from autogen_agentchat.agents import AssistantAgent
from analyzer_gpt.prompts.agent_prompts import CODE_EVALUATOR_SYSTEM_MESSAGE

def getCodeEvaluatorAgent(model_client):
    """
    
    Args:
        model_client (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_evaluator_agent = AssistantAgent(
        name="code_evaluator_Agent",
        model_client=model_client,
        description="An Agent that evaluates code before execution",
        system_message=CODE_EVALUATOR_SYSTEM_MESSAGE
    )
    return code_evaluator_agent