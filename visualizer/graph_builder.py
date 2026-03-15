from graphviz import Digraph


def build_graph(steps, highlight=None):

    dot = Digraph()

    dot.attr(
        rankdir="LR",
        bgcolor="#0e1117",
        nodesep="0.6",
        ranksep="0.7"
    )

    for i, step in enumerate(steps):

        if i == highlight:
            color = "#ffb703"
            font = "white"
        else:
            color = "#219ebc"
            font = "white"

        dot.node(
            str(i),
            step,
            shape="box",
            style="filled,rounded",
            fillcolor=color,
            fontcolor=font,
            fontsize="14",
            width="2"
        )

        if i > 0:

            if highlight == i:
                edge_color = "#ffb703"
                pen = "3"
            else:
                edge_color = "white"
                pen = "1"

            dot.edge(
                str(i-1),
                str(i),
                color=edge_color,
                penwidth=pen
            )

    return dot