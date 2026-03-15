import time
import json
import streamlit as st
from visualizer.graph_builder import build_graph


def safe_parse_explanation(explanation):

    try:
        data = json.loads(explanation)

        return {
            "what": data.get("what_happens", ""),
            "why": data.get("why_this_step_exists", ""),
            "effect": data.get("data_effect", "")
        }

    except Exception:

        return {
            "what": explanation,
            "why": "",
            "effect": ""
        }


def animate_steps(steps, explanations):

    progress = st.progress(0)

    graph_placeholder = st.empty()
    info_placeholder = st.empty()

    total = len(steps)

    for i in range(total):

        parsed = safe_parse_explanation(explanations[i])

        graph = build_graph(steps, highlight=i)

        graph_placeholder.graphviz_chart(graph)

        with info_placeholder.container():

            st.markdown("## ⚙ Current Execution Step")

            st.success(steps[i])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### 🔍 What Happens")
                st.write(parsed["what"])

            with col2:
                st.markdown("### 🧠 Why This Step Exists")
                st.write(parsed["why"])

            with col3:
                st.markdown("### 📊 Effect On Data")
                st.write(parsed["effect"])

        progress.progress((i + 1) / total)

        time.sleep(2)