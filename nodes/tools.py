from graph.state import State

# --- Tool A: Train Booking ---
def train_tool(state: State):
    return {"result": f"✅ Train ticket booked for input: {state['input']}"}

# --- Tool B: Flight Booking ---
def flight_tool(state: State):
    return {"result": f"✅ Flight ticket booked for input: {state['input']}"}