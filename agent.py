from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from graph.graph import build_graph

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.7
)


app = build_graph(llm)

user_input = input("user : ")

result = app.invoke({"input" : user_input})
print("Decision:", result["decision"])
print("Result:", result.get("result"))