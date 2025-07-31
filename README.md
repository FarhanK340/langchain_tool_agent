# LangChain Tool Calling Agent

This project demonstrates how to build an LLM-powered agent using LangChain that can call custom tools when required. In this case, we provide the LLM with a tool for fetching the current system date and time.

## Features

- Integrates an LLM (via Groq API) with LangChain.
- Defines a custom tool (get_current_datetime) using the @tool decorator.
- Allows the LLM to decide when to call the tool based on user queries.
- Executes the tool and returns the real system time.

### Project Structure

```gaphql
langchain_tool_agent/
│
├── requirements.txt   # Dependencies
├── .env               # Environment variables (Groq API key)
├── tool_agent_app.py  # Main agent script
└── README.md          # Documentation
```

### Installation

Clone the repository or create a new folder:

```bash
mkdir langchain_tool_agent
cd langchain_tool_agent
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Create a requirements.txt file with the following:

```bash
langchain
langchain-core
langchain-groq
python-dotenv
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file in the project root:

```bash
GROQ_API_KEY=groq_api_key
```

### Running the Agent

Run the Python script:

```bash
python tool_agent_app.py
```

Example Output

```bash
User: What is the current time and date?
LLM requested tool: get_current_datetime
Tool Output: 2025-07-31 23:41:43
User: Tell me a joke
LLM: Here's one: What do you call a fake noodle? An impasta.
```

### Tool Explanation

```code
@tool
def get_current_datetime(tool_input: str = "") -> str:
    """
    Returns the current date and time as a string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Decorated with @tool so LangChain can register it.

The docstring becomes the tool description for the LLM.

Uses .invoke() to avoid deprecation warnings.

### Observations

- When the query required the tool (e.g., “What is the current time and date?”), the LLM generated a structured tool_call for get_current_datetime. The script executed the tool and displayed the real system time.

- When the query did not require the tool (e.g., “Tell me a joke.”), the LLM simply produced a natural-language text response without invoking any tool.

- How the LLM decides: The LLM looks at the tool descriptions (provided via @tool docstrings) and matches them against the intent of the user query. If the query clearly asks for something only a tool can provide (like real-time data), it triggers the tool call; otherwise, it responds directly.

### Benefits of Tool-Enabled LLMS

- Overcomes LLM training cutoffs by connecting to tools that provide current information.

- Allows integration with APIs, databases, and system functions (e.g., time, weather, calculators).

- Tools make LLMs more reliable for tasks that require precision or live data.

- The LLM can dynamically choose between generating language-only answers and invoking tools, depending on the query.
  