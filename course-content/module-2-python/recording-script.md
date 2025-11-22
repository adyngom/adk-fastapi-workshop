# Module 2: Python for Production Agents - Recording Script

**Duration:** 90 minutes content
**Recording Time:** 3-4 hours
**Energy Level:** Moderate, practical
**Focus:** Hands-on Python skills

---

## 🎬 HOOK (30 seconds)

**SAY:**
"Hello and welcome to Module 2. Okay, so today we're going to cover the Python skills you need for building production AI agents.

Now, a lot of people know basic Python, but when it comes to agents, there are three things that trip people up: async/await, Pydantic models, and type hints. So we're going to make all three very clear in this module.

By the end, you'll be able to write production-ready Python code for agents. Let's get into it."

---

## 🎬 OVERVIEW (2-3 min)

**SAY:**
"All right, here's what we're covering today. First, async/await - this is the big one. Agents need to run asynchronously, and if you don't understand async, you're going to hit errors. So we're spending 30 minutes just on this.

Then we're going to look at Pydantic models. These are for getting structured output from your agents. Instead of just text, you get validated JSON. Very powerful.

After that, type hints - why they matter in production, and how they help your IDE help you.

And finally, error handling patterns - because production agents need to handle failures gracefully.

By the end, you'll have the Python foundation for everything we build in this course. Okay, so let's start with async/await."

---

## 🎬 ASYNC/AWAIT EXPLAINED (30 min)

**[Show slide: Sync vs Async]**

**SAY:**
"So let me show you why agents need async. The problem with regular synchronous Python is it blocks. Let me demonstrate what I mean.

[Open VS Code, create sync_example.py]

Say you have a function that makes an API call:
[Type:
```python
import time

def fetch_data():
    print('Fetching data...')
    time.sleep(3)  # Simulates API call
    print('Data received!')
    return {'result': 'success'}

def process_data():
    print('Processing...')
    time.sleep(2)
    print('Done processing!')

# Call them
fetch_data()
process_data()
```
]

Let's run this:
[Type: python sync_example.py]

You see that? It takes 5 seconds total. Fetch takes 3, process takes 2. They run one after another - blocking.

[Watch output]

There you go. Now, the problem: What if you have 4 agents that each need 2 seconds? Synchronous = 8 seconds total.

But these tasks don't depend on each other. Why wait?"

**[Show slide: Async = Concurrent]**

**SAY:**
"All right, so here's where async comes in. Async lets Python do multiple things at the same time. Let me show you the same example with async:

[Create async_example.py]

[Type:
```python
import asyncio

async def fetch_data():
    print('Fetching data...')
    await asyncio.sleep(3)  # Async wait
    print('Data received!')
    return {'result': 'success'}

async def process_data():
    print('Processing...')
    await asyncio.sleep(2)
    print('Done processing!')

# Run them concurrently
async def main():
    await asyncio.gather(
        fetch_data(),
        process_data()
    )

asyncio.run(main())
```
]

Now let's run this:
[Type: python async_example.py]

Watch what happens...

[Both print statements appear at same time, finishes in 3 seconds!]

There you go! Both started at the same time. Total time: 3 seconds (not 5). That's the power of async."

**[Pause for effect]**

**SAY:**
"This is very important for agents. When you have multiple agents working in parallel - like our financial advisor with 4 analysts - async lets them all run at the same time. Without async, they'd wait for each other.

Now, let me show you the syntax you need to know."

**[Show slide: Async/Await Syntax]**

**SAY:**
"Three simple rules:

**Rule 1:** If a function needs to wait for something (API call, database, etc.), make it async:
```python
async def my_function():  # ← async keyword
    result = await some_async_operation()  # ← await keyword
    return result
```

**Rule 2:** You can only use 'await' inside async functions. Can't mix.

**Rule 3:** To run async functions, use asyncio.run() or await them from another async function.

That's it. That's async in 3 rules."

**[Back to code]**

**SAY:**
"Okay, so let me show you one more practical example. Real quick, let's create an async function that makes multiple API calls:

[Create parallel_example.py]

[Type:
```python
import asyncio
import time

async def call_api(api_name, delay):
    print(f'Starting {api_name}')
    await asyncio.sleep(delay)
    print(f'{api_name} complete!')
    return f'{api_name} result'

async def main():
    start = time.time()

    # Run 3 API calls in parallel
    results = await asyncio.gather(
        call_api('Google Search', 2),
        call_api('Database Query', 3),
        call_api('Weather API', 1)
    )

    elapsed = time.time() - start
    print(f'Total time: {elapsed:.1f} seconds')
    print(f'Results: {results}')

asyncio.run(main())
```
]

Let's run this:
[Run it]

You see that? All three started at the same time. Total time: 3 seconds (the slowest one). If this was sync, it would be 6 seconds.

Perfect. This is how ADK runs parallel agents - using async under the hood."

**SAY:**
"All right, one last thing about async - common mistakes.

**Mistake 1:** Forgetting 'await'
[Type bad example]
If you just call an async function without await, it returns a coroutine object, not the result. Confusing error.

**Mistake 2:** Using 'await' outside async function
[Type bad example]
Python will yell at you. Can only use await inside async functions.

**Mistake 3:** Blocking the event loop
[Type example with time.sleep instead of asyncio.sleep]
If you use time.sleep() in async code, it blocks everything. Use asyncio.sleep() instead.

Those are the three main gotchas. Now you know async/await. Let's move on to Pydantic."

---

## 🎬 PYDANTIC MODELS (25 min)

**[Show slide: Pydantic - Structured Output]**

**SAY:**
"Okay, so now let's talk about Pydantic. This is how you get structured, validated data from your agents.

The problem: LLMs return text. Sometimes you want JSON. But text is unpredictable - the LLM might return invalid JSON, or forget fields, or use wrong types.

Pydantic solves this. Let me show you how.

[Create pydantic_example.py]

Say you're building a customer support agent. You want it to output a support ticket with specific fields. Here's how you do it with Pydantic:

[Type:
```python
from pydantic import BaseModel, Field
from typing import Literal

class SupportTicket(BaseModel):
    title: str = Field(description='Short summary of the issue')
    category: Literal['technical', 'billing', 'product', 'other']
    priority: Literal['P0', 'P1', 'P2', 'P3']
    description: str
    customer_email: str

# Example usage
ticket = SupportTicket(
    title='Login not working',
    category='technical',
    priority='P1',
    description='Customer cannot login after password reset',
    customer_email='customer@example.com'
)

print(ticket)
print(ticket.model_dump())  # Get as dict
```
]

Let's run this:
[Run it]

There you go. Perfect. You see that? We get a validated ticket object.

Now, what happens if we give it bad data? Let me show you:
[Type:
```python
bad_ticket = SupportTicket(
    title='Issue',
    category='wrong_category',  # ← This isn't in the Literal types
    priority='P1',
    description='Problem',
    customer_email='not_an_email'  # ← This should fail validation
)
```
]

Run it:
[Run - shows validation errors]

You see that? Pydantic caught both errors - wrong category and invalid email. This is very important because it prevents bad data from getting into your system."

**[Show slide: Pydantic with Agents]**

**SAY:**
"All right, so how do you use this with ADK agents? Here's the pattern:

[Type:
```python
from google.adk.agents import Agent
from pydantic import BaseModel

class TicketOutput(BaseModel):
    title: str
    category: str
    priority: str

triage_agent = Agent(
    name='triage',
    model='gemini-2.0-flash-exp',
    instruction='''
    Analyze the support request and output a structured ticket.

    Output format:
    {
        \"title\": \"Short summary\",
        \"category\": \"technical/billing/product\",
        \"priority\": \"P0/P1/P2/P3\"
    }
    '''
)

# When agent responds, parse with Pydantic
response = triage_agent.run('Customer cant login')
ticket = TicketOutput.model_validate_json(response)
```
]

You give the agent the structure in the instruction, and Pydantic validates the output. Beautiful.

Okay, let's keep going to type hints."

---

## 🎬 TYPE HINTS (20 min)

**[Show slide: Type Hints - Why They Matter]**

**SAY:**
"So type hints. A lot of Python developers skip these because Python doesn't enforce them. But for production agents, type hints are critical. Let me show you why.

[Create type_hints_example.py]

Without type hints:
[Type:
```python
def create_agent(name, model, instruction):
    # What types are these? Who knows!
    return Agent(name=name, model=model, instruction=instruction)
```
]

Your IDE has no idea what types these are. No autocomplete. No error checking. You're coding blind.

With type hints:
[Type:
```python
from google.adk.agents import Agent

def create_agent(
    name: str,
    model: str,
    instruction: str
) -> Agent:  # ← Returns an Agent object
    return Agent(name=name, model=model, instruction=instruction)
```
]

Now your IDE knows exactly what types to expect. You get autocomplete, error checking, everything.

Let me show you the IDE benefits:
[Type: create_agent(]
[Show autocomplete suggesting parameters]

There you go - see how it suggests the parameters? That's because of type hints.

And if I try to pass the wrong type:
[Type: create_agent(name=123, ...]
[Show IDE warning]

The IDE catches it before you even run the code. Perfect."

**SAY:**
"This is especially important for agent tools. ADK uses type hints to understand your tools. Let me show you:

[Type:
```python
def get_weather(city: str, units: str = 'celsius') -> dict:
    '''Get weather for a city.

    Args:
        city: Name of the city
        units: Temperature units (celsius or fahrenheit)

    Returns:
        Weather data dictionary
    '''
    # ADK reads these type hints!
    return {'temp': 22, 'condition': 'sunny'}
```
]

ADK looks at the type hints and automatically generates the tool schema for the LLM. You don't have to manually describe the parameters - type hints do it for you.

All right, so always use type hints in production code. Your future self will thank you. Okay, let's cover error handling real quick."

---

## 🎬 ERROR HANDLING (15 min)

**[Show slide: Error Handling Patterns]**

**SAY:**
"So error handling. Production agents need to fail gracefully. Let me show you the pattern.

[Create error_handling.py]

Bad error handling:
[Type:
```python
def risky_function():
    result = call_external_api()  # What if this fails?
    return result  # App crashes!
```
]

If the API is down, your whole agent crashes. Not good.

Good error handling:
[Type:
```python
def safe_function():
    try:
        result = call_external_api()
        return result
    except ConnectionError:
        return {'error': 'API unavailable', 'fallback': 'cached_data'}
    except TimeoutError:
        return {'error': 'Request timeout', 'retry': True}
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        return {'error': 'Unknown error occurred'}
```
]

Now if something fails, the agent returns a useful error message instead of crashing. Perfect.

For agent tools, here's the pattern I use:
[Type:
```python
def get_customer_data(customer_id: str) -> dict:
    '''Get customer information from database.'''
    try:
        # Database query
        customer = db.query(customer_id)
        return customer

    except CustomerNotFound:
        # User-friendly error for agent to handle
        return {
            'error': 'Customer not found',
            'suggestion': 'Please verify the customer ID'
        }

    except DatabaseError as e:
        # Log technical error, return simple message
        logger.error(f'Database error: {e}')
        return {
            'error': 'System temporarily unavailable',
            'retry_in': '5 minutes'
        }
```
]

You see that? The agent gets a clear error message it can communicate to the user. It doesn't just crash.

This is very important for production - errors will happen, handle them gracefully."

---

## 🎬 EXERCISE & RECAP (15 min)

**SAY:**
"Okay, so that's the Python foundation. Let's do a quick exercise.

**Exercise:** Build an async function that validates customer data with Pydantic

[Show requirements]

Take 10 minutes, pause the video. Solution is in the module-2/solutions/ folder.

[Pause]

All right, here's the solution:
[Walk through complete solution]

And like that, you have production-ready Python skills.

**Recap:**
- Async/await for concurrent execution (4x faster for parallel tasks)
- Pydantic for structured, validated output
- Type hints for IDE support and documentation
- Error handling for graceful failures

In Module 3, we use all of this to build your first AI agent. That's where it gets fun.

See you in Module 3!"

---

**[End Module 2]**

## 📝 RECORDING NOTES

**Energy:** Practical, code-focused
**Pace:** Moderate (students need to understand async)
**Key Moment:** Async demo showing time difference
**Code to Create Before Recording:** async_examples.py, pydantic_customer.py

---
