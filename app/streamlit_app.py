import streamlit as st
import json
import re
import time

from agents.orchestrator_agent import OrchestratorAgent
from visualizer.graph_builder import build_graph


st.set_page_config(
    page_title="SQLVizMadeEasyByAB",
    layout="wide"
)

st.title("🧠 SQLVizMadeEasyByAB")
st.markdown("Visualize SQL execution step-by-step.")


# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "steps" not in st.session_state:
    st.session_state.steps = []

if "explanations" not in st.session_state:
    st.session_state.explanations = []

if "workflow" not in st.session_state:
    st.session_state.workflow = ""

if "current_step" not in st.session_state:
    st.session_state.current_step = 0

if "running" not in st.session_state:
    st.session_state.running = False


# ------------------------------------------------
# SAFE JSON PARSER
# ------------------------------------------------

def parse_llm_json(text):

    try:
        return json.loads(text)

    except:

        what = re.search(r'"what_happens":\s*"([^"]*)"', text)
        why = re.search(r'"why_this_step_exists":\s*"([^"]*)"', text)
        effect = re.search(r'"data_effect":\s*"([^"]*)"', text)

        return {
            "what_happens": what.group(1) if what else "",
            "why_this_step_exists": why.group(1) if why else "",
            "data_effect": effect.group(1) if effect else ""
        }


# ------------------------------------------------
# QUERY INPUT
# ------------------------------------------------

st.markdown("## 📝 SQL Query")

dialect = st.selectbox(
    "SQL Dialect",
    ["mysql", "postgres", "sqlite", "bigquery", "snowflake"]
)

query = st.text_area(
    "Enter SQL Query",
    height=150
)


# ------------------------------------------------
# ANALYZE QUERY
# ------------------------------------------------

if st.button("🚀 Analyze Query"):

    orchestrator = OrchestratorAgent()

    with st.spinner("Analyzing query..."):

        result = orchestrator.run(query, dialect)

    if result["error"]:

        st.error("Invalid SQL Query")
        st.code(result["message"])

    else:

        st.session_state.steps = result["steps"]
        st.session_state.explanations = result["explanations"]
        st.session_state.workflow = result["workflow"]

        st.session_state.current_step = 0
        st.session_state.running = False

        st.markdown("### 📊 Query Complexity")

        st.metric(
            "Complexity Score",
            result["complexity_score"]
        )

        st.success(f"Difficulty Level: {result['complexity_level']}")


# ------------------------------------------------
# EXECUTION CONTROLS
# ------------------------------------------------

if st.session_state.steps:

    st.markdown("## 🎮 Execution Controls")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("▶ Start"):
            st.session_state.running = True

    with col2:
        if st.button("⏹ Stop"):
            st.session_state.running = False

    with col3:
        if st.button("Restart"):
            st.session_state.current_step = 0
            st.session_state.running = True


# ------------------------------------------------
# PLACEHOLDERS (PREVENT DUPLICATION)
# ------------------------------------------------

pipeline_placeholder = st.empty()
step_placeholder = st.empty()
explanation_placeholder = st.empty()


# ------------------------------------------------
# PIPELINE VISUALIZATION
# ------------------------------------------------

if st.session_state.steps:

    step = st.session_state.current_step
    steps = st.session_state.steps
    explanations = st.session_state.explanations

    st.markdown(f"### Step {step+1} / {len(steps)}")

    progress = (step + 1) / len(steps)

    pipeline_placeholder.progress(progress)

    graph = build_graph(steps, highlight=step)

    pipeline_placeholder.graphviz_chart(graph)

    parsed = parse_llm_json(explanations[step])

    with step_placeholder.container():

        st.success(steps[step])

    with explanation_placeholder.container():

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**What Happens**")
            st.write(parsed["what_happens"])

        with col2:
            st.markdown("**Why This Step Exists**")
            st.write(parsed["why_this_step_exists"])

        with col3:
            st.markdown("**Effect On Data**")
            st.write(parsed["data_effect"])


# ------------------------------------------------
# AUTO ANIMATION
# ------------------------------------------------

if st.session_state.running:

    if st.session_state.current_step < len(st.session_state.steps) - 1:

        time.sleep(1.5)

        st.session_state.current_step += 1

        st.rerun()

    else:

        st.session_state.running = False


# ------------------------------------------------
# FINAL WORKFLOW EXPLANATION
# ------------------------------------------------

if st.session_state.workflow:

    st.markdown("---")
    st.markdown("## 🧠 Query Execution Workflow")

    st.markdown(st.session_state.workflow)


# ------------------------------------------------
# FULL STEP BREAKDOWN
# ------------------------------------------------

if st.session_state.steps:

    st.markdown("---")
    st.markdown("## 📜 Full Execution Breakdown")

    for i, step in enumerate(st.session_state.steps):

        parsed = parse_llm_json(st.session_state.explanations[i])

        with st.expander(f"Step {i+1}: {step}"):

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(parsed["what_happens"])

            with col2:
                st.write(parsed["why_this_step_exists"])

            with col3:
                st.write(parsed["data_effect"])