from typing import TypedDict

class State(TypedDict, total=False):
    input: str
    decision: str
    output: str
    result: str

    def __init__(self, input: str, decision: str, output: str, result: str) -> None:
        self.input = input
        self.decision = decision
        self.output = output
        self.result = result