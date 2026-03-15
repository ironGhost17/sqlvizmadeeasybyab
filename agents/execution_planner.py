from agents.base_agent import BaseAgent
from config.decorators import log_execution


class ExecutionPlannerAgent(BaseAgent):

    def __init__(self):
        super().__init__("ExecutionPlannerAgent")

    @log_execution
    def run(self, parsed):

        steps = []

        for table in parsed["tables"]:
            steps.append(f"Load table {table}")

        for join in parsed["joins"]:
            steps.append(f"Execute join {join}")

        if parsed["where"]:
            steps.append(f"Apply filter {parsed['where']}")

        if parsed["group_by"]:
            steps.append("Group rows")

        if parsed["having"]:
            steps.append("Apply HAVING filter")

        steps.append("Select columns")

        if parsed["order_by"]:
            steps.append("Sort results")

        if parsed["limit"]:
            steps.append("Limit result rows")

        steps.append("Return result")

        return steps