# 🧠 SQLVizMadeEasyByAB

**SQLVizMadeEasyByAB** is an AI-powered SQL execution visualizer that helps developers and learners understand how SQL queries execute internally.

Instead of reading SQL line-by-line, this tool **breaks the query into execution stages and visualizes the pipeline step-by-step**.

The goal is to make SQL easier to understand for **visual learners, students, and engineers preparing for interviews.**

---

# 🚀 Features

* 🔍 **SQL Query Parsing**
* ⚙ **Execution Pipeline Visualization**
* 🎬 **Animated Query Execution**
* 🧠 **AI-Generated Step Explanations**
* 📊 **Query Complexity Score**
* 🛑 **Invalid SQL Detection**
* 📜 **Full Execution Workflow Explanation**
* 🎮 **Execution Controls (Start / Stop / Restart)**

---

# 🧱 Architecture

The project uses a **multi-agent architecture** where each component performs a dedicated task.

User Query
↓
SQL Parser Agent
↓
Execution Planner Agent
↓
Explanation Agent (LLM)
↓
Visualization Engine
↓
Streamlit UI

---

# 🧩 Tech Stack

| Component       | Technology           |
| --------------- | -------------------- |
| Backend         | Python               |
| UI              | Streamlit            |
| SQL Parsing     | sqlglot              |
| AI Explanations | OpenAI API           |
| Visualization   | Graphviz             |
| Architecture    | Multi-Agent Pipeline |

---

# 📦 Project Structure

```
sqlvizmadeeasybyab
│
├── agents
│   ├── orchestrator_agent.py
│   ├── execution_planner.py
│   ├── explanation_agent.py
│   └── base_agent.py
│
├── parser
│   └── sql_parser.py
│
├── visualizer
│   ├── graph_builder.py
│   └── animation_engine.py
│
├── config
│   ├── logger.py
│   ├── decorators.py
│   └── openai_client.py
│
├── app
│   └── streamlit_app.py
│
├── examples
│   └── sample_queries.sql
│
├── roadmap
│   └── future_versions.md
│
├── requirements.txt
└── README.md
```

---

# 🛠 Installation

Clone the repository:

```
git clone https://github.com/ironGhost17/sqlvizmadeeasybyab.git
cd sqlvizmadeeasybyab
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```
streamlit run app/streamlit_app.py
```

The app will open in your browser.

---

# 🧪 Example Query

```
SELECT c.name, SUM(o.amount)
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.amount > 100
GROUP BY c.name
ORDER BY SUM(o.amount) DESC;
```

### Execution Pipeline

```
Load customers
↓
Load orders
↓
JOIN tables
↓
Apply WHERE filter
↓
GROUP rows
↓
Aggregate SUM
↓
Sort results
↓
Return final result
```

---

# 📊 Query Complexity Score

The system assigns a complexity score based on query features.

| SQL Feature | Score |
| ----------- | ----- |
| JOIN        | +2    |
| GROUP BY    | +2    |
| HAVING      | +2    |
| WHERE       | +1    |
| ORDER BY    | +1    |
| LIMIT       | +1    |

This helps learners estimate **SQL difficulty level**.

---

# 🎬 Execution Visualization

The system animates query execution like a pipeline:

```
Tables → Join → Filter → Group → Aggregate → Sort → Result
```

Each step includes:

* explanation of what happens
* reason the step exists
* effect on the dataset

---

# ⚠ Invalid Query Handling

The system detects invalid SQL queries and prevents execution.

Example:

```
SELEC name FROM employees
```

Output:

```
Invalid SQL Query
Syntax error detected near SELEC
```

---

# 🔮 Future Improvements

Planned features:

* Window function visualization
* Subquery execution diagrams
* Query optimization suggestions
* Data flow simulation
* Support for multiple SQL dialects
* Export execution diagrams

See the roadmap in:

```
roadmap/future_versions.md
```

---

# 👨‍💻 Author

**Anurag Banerjee**

Projects:

* LocatorMadeEasyByAB
* SQLVizMadeEasyByAB

---

# ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

# 📜 License

This project is open source and available under the MIT License.
