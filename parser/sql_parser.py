import sqlglot
from agents.base_agent import BaseAgent
from config.logger import logger
from config.decorators import log_execution


class SQLParserAgent(BaseAgent):

    def __init__(self):
        super().__init__("SQLParserAgent")

    @log_execution
    def run(self, query_data):

        query = query_data["query"]
        dialect = query_data["dialect"]

        try:
            parsed = sqlglot.parse_one(query, read=dialect)

        except Exception as e:

            logger.error(f"SQL parsing failed: {e}")

            return {
                "error": True,
                "message": str(e)
            }

        tables = []
        joins = []
        where = None
        group_by = []
        order_by = []
        having = None
        limit = None

        for table in parsed.find_all(sqlglot.expressions.Table):
            tables.append(table.name)

        for join in parsed.find_all(sqlglot.expressions.Join):
            joins.append(join.sql())

        if parsed.args.get("where"):
            where = parsed.args["where"].sql()

        if parsed.args.get("group"):
            group_by = [g.sql() for g in parsed.args["group"].expressions]

        if parsed.args.get("order"):
            order_by = [o.sql() for o in parsed.args["order"].expressions]

        if parsed.args.get("having"):
            having = parsed.args["having"].sql()

        if parsed.args.get("limit"):
            limit = parsed.args["limit"].sql()

        # -------------------------
        # COMPLEXITY SCORE
        # -------------------------

        score = 1

        score += len(joins) * 2

        if where:
            score += 1

        if group_by:
            score += 2

        if having:
            score += 2

        if order_by:
            score += 1

        if limit:
            score += 1

        complexity = "Easy"

        if score > 6:
            complexity = "Medium"

        if score > 10:
            complexity = "Hard"

        return {
            "error": False,
            "tables": tables,
            "joins": joins,
            "where": where,
            "group_by": group_by,
            "order_by": order_by,
            "having": having,
            "limit": limit,
            "complexity_score": score,
            "complexity_level": complexity
        }