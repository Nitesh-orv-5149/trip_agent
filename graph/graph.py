from langgraph.graph import StateGraph, END
from nodes.judges import judge_function, judge_node
from nodes.tools import flight_tool, train_tool
from graph.state import State


def build_graph(llm):
    
    graph = StateGraph(State)

    # nodes
    graph.add_node("judge", lambda state : judge_node(llm, state))
    graph.add_node("flight", flight_tool)
    graph.add_node("train", train_tool)

    graph.set_entry_point("judge")

    # edges
    graph.add_conditional_edges(
        "judge",
        judge_function,
        {
            "train" : "train", 
            "flight" : "flight"
        },
    )
    graph.add_edge("train", END)
    graph.add_edge("flight", END)

    return graph.compile()