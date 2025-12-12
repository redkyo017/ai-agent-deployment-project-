from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent, tool
import math

@tool
def take_square_root(input_number: float):
    """Calculate the square root of the given number"""
    return str(math.sqrt(input_number))


app = BedrockAgentCoreApp()
agent = agent = Agent(tools=[take_square_root])

@app.entrypoint
def invoke(payload):
    """Make a simple call to a Strands Agent"""
    user_message = payload.get("prompt")
    result = agent(user_message)
    return result.message

if __name__ == "__main__":
    app.run()