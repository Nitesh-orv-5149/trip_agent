from graph.state import State


# judge function
def judge_function(state: State):
    return state["decision"].strip().lower()

# node-1 node to judge
def judge_node(llm, state: State):
    response = llm.invoke(
         f"User asked: {state['input']}.\n"
        "Decide which tool to use: 'train' or 'flight'. Respond with only one word."
    )
    return {"decision" : response.content}
