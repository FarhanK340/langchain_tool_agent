import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from datetime import datetime


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

@tool
def get_current_datetime(tool_input: str = "") -> str:
    '''
    Return Current Date and Time as a string
    '''
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0)
    
    llm_with_tool = llm.bind_tools([get_current_datetime])
    
    queries = ['What is the current time and date?', 'Tell me a joke']
   
    for query in queries:
        print(f"User: {query}")
        response = llm_with_tool.invoke(query)
        tool_calls = response.additional_kwargs.get("tool_calls", [])

        if tool_calls:
            for call in tool_calls:
                tool_name = call.get("function", {}).get("name")
                raw_args = call.get("function", {}).get("arguments", "{}")
                args = json.loads(raw_args) if raw_args else {}

                print(f"LLM requested tool: {tool_name}")

                if tool_name == "get_current_datetime":
                    result = get_current_datetime.invoke("")
                    print(f"Tool Output: {result}")
                else:
                    print("Unknown tool requested.")
        else:
            # Regular response without tool use
            print(f"LLM: {response.content}")

if __name__ == "__main__":
    main()