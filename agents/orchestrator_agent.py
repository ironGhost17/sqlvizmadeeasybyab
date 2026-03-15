from parser.sql_parser import SQLParserAgent
from agents.execution_planner import ExecutionPlannerAgent
from agents.explanation_agent import ExplanationAgent
from config.openai_client import client
from config.logger import logger


class OrchestratorAgent:

    def __init__(self):

        self.parser = SQLParserAgent()
        self.planner = ExecutionPlannerAgent()
        self.explainer = ExplanationAgent()

    def run(self, query, dialect):

        logger.info("Starting pipeline")

        parsed = self.parser.run({
            "query": query,
            "dialect": dialect
        })

        if parsed.get("error"):

            return {
                "error": True,
                "message": parsed["message"]
            }

        steps = self.planner.run(parsed)

        explanations = self.explainer.run(steps)

        workflow_prompt = f"""
Explain the execution workflow of this SQL query.

Query:
{query}

Execution Steps:
{steps}

Explain in numbered steps in simple English.
"""

        workflow_response = client.responses.create(
            model="gpt-4.1-mini",
            input=workflow_prompt
        )

        workflow_text = workflow_response.output_text

        logger.info("Pipeline complete")

        return {
            "error": False,
            "steps": steps,
            "explanations": explanations,
            "workflow": workflow_text,
            "complexity_score": parsed["complexity_score"],
            "complexity_level": parsed["complexity_level"]
        }