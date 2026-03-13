# LLM Prompt Router for Intent Classification

## Project Overview

This project implements an **LLM-powered prompt routing system** that intelligently detects a user's intent and routes the request to a specialized AI persona for generating high-quality responses.

Instead of using a single large prompt to handle every type of request, the system follows a **two-stage architecture**:

1. **Intent Classification** – Detect the user’s intent using a lightweight LLM call.
2. **Prompt Routing** – Route the message to a specialized expert prompt that generates the final response.

This architecture improves response quality, modularity, and scalability in real-world AI systems.

---

## System Architecture

```
User Input
   ↓
Intent Classifier (LLM Call)
   ↓
Intent JSON Output
{ "intent": "...", "confidence": ... }
   ↓
Prompt Router
   ↓
Expert Persona System Prompt
   ↓
Final LLM Response
   ↓
Logging (route_log.jsonl)
```

The system uses **Groq LLM APIs** to perform both the classification and response generation.

---

## Key Features

* Intent classification using a lightweight LLM call
* Prompt routing to specialized expert personas
* Modular prompt design
* JSON structured responses
* Confidence score for classification
* Logging of all requests and responses
* Handling of unclear or ambiguous user inputs

---

## Expert Personas

The system defines four expert AI personas, each specialized for a different type of task.

### 1. Code Expert

Provides production-quality code and technical explanations.
Responses prioritize correctness, best practices, and proper error handling.

### 2. Data Analyst

Analyzes datasets or numerical information.
Explains statistical concepts such as patterns, correlations, distributions, and anomalies.

### 3. Writing Coach

Helps users improve writing clarity and structure.
Provides feedback on grammar, tone, passive voice, and wordiness without rewriting the text.

### 4. Career Advisor

Offers actionable career guidance.
Asks clarifying questions and provides realistic, practical advice for professional development.

---

## Project Structure

```
prompt-router-project
│
├── main.py
├── classifier.py
├── router.py
├── prompts.py
├── logger.py
├── route_log.jsonl
├── requirements.txt
└── README.md
```

### File Descriptions

**main.py**
Entry point of the application. Handles user interaction and orchestrates the routing workflow.

**classifier.py**
Implements the `classify_intent()` function that calls the LLM to detect user intent.

**router.py**
Implements `route_and_respond()` which selects the correct expert persona prompt and generates the final response.

**prompts.py**
Stores all expert system prompts in a dictionary for modular design.

**logger.py**
Logs requests and responses into a JSON Lines file for observability and debugging.

**route_log.jsonl**
Stores logs of every interaction including intent classification, confidence score, user message, and final response.

---

## Installation

### 1. Clone or Download the Project

```
git clone <repository-url>
cd prompt-router-project
```

### 2. Install Dependencies

```
pip install groq python-dotenv
```

Or install using the requirements file:

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

You can obtain an API key from the Groq console.

---

## Running the Application

Start the system using:

```
python main.py
```

Example interaction:

```
User: how do I sort a list in python?

Detected Intent:
{ "intent": "code", "confidence": 0.91 }

Assistant:
Use Python's built-in sorted() function...
```

---

## Logging System

Each interaction is logged into `route_log.jsonl` in JSON Lines format.

Example log entry:

```
{
 "intent": "code",
 "confidence": 0.92,
 "message": "how do I sort a list in python",
 "response": "Use the sorted() function..."
}
```

This allows developers to monitor system behavior and improve routing performance.

---

## Test Inputs

The system can be tested using a variety of messages:

```
how do i sort a list of objects in python?
explain this sql query
this paragraph sounds awkward
i need job interview tips
what is a pivot table
fix this bug: for i in range(10) print(i)
hey
can you write a poem about clouds
```

These tests ensure the router correctly identifies different intents.

---

## Handling Unclear Inputs

If the classifier returns the intent **"unclear"**, the system will ask the user for clarification instead of routing to an incorrect persona.

Example:

```
User: hey

Assistant:
Could you clarify what you need help with?
```

---

## Possible Improvements

Future enhancements could include:

* Confidence threshold for routing decisions
* Manual intent override using prefixes such as `@code`
* Web-based user interface
* Advanced evaluation metrics
* Multi-model routing strategies

---

## Conclusion

This project demonstrates how **prompt routing architectures** can improve the quality and organization of LLM-based applications.
By separating intent classification from response generation, the system provides more focused and reliable outputs while remaining scalable and maintainable.
