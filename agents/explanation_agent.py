from agents.base_agent import BaseAgent
from config.openai_client import client
from config.decorators import log_execution


class ExplanationAgent(BaseAgent):

    def __init__(self):
        super().__init__("ExplanationAgent")

    @log_execution
    def run(self, steps):

        explanations = []

        for step in steps:

            prompt = f"""
You are a database execution engine instructor.

Explain the SQL execution step in detail.

Step: {step}

Return JSON:

{{
"what_happens": "...",
"why_this_step_exists": "...",
"data_effect": "..."
}}
"""

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            explanations.append(response.output_text)

        return explanations