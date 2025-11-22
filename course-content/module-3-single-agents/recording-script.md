# Module 3: Single Agents with Custom Tools - Recording Script

**Duration:** 90 minutes
**Focus:** First hands-on agent build
**Energy:** Excited (this is where it gets fun!)

---

## 🎬 HOOK (30 sec)

**SAY:**
"Hello and welcome to Module 3. Okay, so this is where it gets fun - we're going to build your first AI agent from scratch.

By the end of this module, you'll have a working agent that can call custom Python tools and respond to questions. And you'll understand exactly how agents work under the hood.

Let's build this thing!"

---

## 🎬 OVERVIEW (3 min)

**SAY:**
"All right, here's what we're doing today. We're going to build the greeting agent - a friendly assistant with custom tools.

First, I'll show you the agent class structure - the five components every agent needs.
Then we'll build it together from scratch - I'm going to code it live, you follow along.
We'll add two custom tools - one that returns company info, one that returns the current time.
Then we'll test it with ADK Web and see it working.

This is hands-on. You're going to build this with me.

Okay, so let's start. What does an agent actually look like in code?"

---

## 🎬 AGENT STRUCTURE (20 min)

**[Show slide: Agent Class Anatomy]**

**SAY:**
"So let me show you the five components every ADK agent has. This is the structure you'll use over and over.

[Show code on screen - greeting_agent/agent.py example]

**Component 1: name**
The name is the identifier. When you have multiple agents, this is how you tell them apart. Very straightforward.

**Component 2: model**
This is which Gemini model to use. We're using 'gemini-2.0-flash-exp' - it's fast, cheap, and supports voice input. You could also use 'gemini-2.5-pro' for more complex reasoning, but it costs more.

**Component 3: description**
This is a short summary of what the agent does. It becomes important when you have multi-agent systems - agents use descriptions to decide who to delegate work to. For a single agent, it's just documentation.

**Component 4: instruction**
This is the most important one. The instruction is the agent's personality and behavior. It's like the job description. This is where you shape what the agent does and how it does it.

**Component 5: tools**
Tools are Python functions the agent can call. This is what makes it an AGENT instead of just a chatbot. The agent can DO things - search, calculate, query databases, whatever tools you give it.

All right, so those are the five components. Now let's build an agent together using these."

---

## 🎬 BUILDING GREETING AGENT (30 min)

**[Fresh VS Code window]**

**SAY:**
"Okay, so let's build this from scratch. I'm going to create a new directory:
[Type: mkdir greeting_agent]
[Type: cd greeting_agent]

Perfect. Now we need three files. Let me create them:
[Type: touch __init__.py agent.py tools.py .env]

There you go.

Let's start with the __init__.py. This is very simple:
[Open __init__.py]
[Type:
```python
'''Greeting Agent - Your first ADK agent'''
from .agent import root_agent
```
]

This just tells Python we have an agent in this folder. Command S.

All right, now the .env file. Open it:
[Open .env]
[Type: GOOGLE_API_KEY=your_key_here]

Paste your actual API key there. Save it.

Perfect. Now the fun part - let's build the agent itself.

[Open agent.py]

So I'm just going to start typing:
[Type:
```python
'''
Greeting Agent - Demonstrates basic agent with custom tools
'''
from google.adk.agents import Agent
from .tools import get_company_info, get_current_time
```
]

There you go - we're importing Agent class and our tools. We haven't created the tools yet, but we will in a second.

Now let's create the agent:
[Type:
```python

root_agent = Agent(
    name='greeting_agent',
```
]

Okay, so the name is 'greeting_agent'. This is very important - it must match the folder name. If your folder is greeting_agent, the name here must be greeting_agent. ADK is strict about this.

[Continue typing:
```python
    model='gemini-2.0-flash-exp',
```
]

We're using the flash model - it's fast and supports voice input.

[Continue:
```python
    description='A friendly assistant that provides company info and time',
```
]

Just a simple description.

[Continue:
```python
    instruction='''You are a helpful and friendly assistant.

You have access to tools that provide:
- Company information (get_company_info)
- Current time (get_current_time)

When users ask about the company or time, use these tools.
Keep responses concise and friendly.
''',
```
]

There's our instruction. You see that? I'm telling it what tools it has and when to use them. This guides the agent's behavior.

[Finish:
```python
    tools=[get_company_info, get_current_time]
)
```
]

And we list the tools. Perfect. Command S.

All right, so that's the agent structure. Now we need to create those tools."

**[Open tools.py]**

**SAY:**
"Okay, so let's create the tools. Tools are just Python functions. Let me show you:

[Type:
```python
'''
Custom tools for greeting_agent
'''
from datetime import datetime

def get_company_info() -> dict:
    '''Get information about the company.

    Returns information about the organization.

    Returns:
        dict: Company information
    '''
    return {
        'company_name': 'Acme Corporation',
        'industry': 'Technology',
        'location': 'San Francisco',
        'use_cases': [
            'Customer service automation',
            'Content creation',
        ]
    }
```
]

There you go. Very simple function. The important parts:
- Type hint (-> dict) so ADK knows what it returns
- Docstring explaining what it does - ADK uses this!
- Returns a dictionary with structured data

Let's add the second tool:
[Type:
```python

def get_current_time() -> dict:
    '''Get the current time.

    Returns:
        dict: Current time information
    '''
    from datetime import timezone, timedelta

    eastern = timezone(timedelta(hours=-5))
    now = datetime.now(eastern)

    return {
        'current_time': now.strftime('%I:%M %p'),
        'date': now.strftime('%B %d, %Y'),
        'timezone': 'EST'
    }
```
]

Perfect. Command S.

And like that, we have our tools. All right, now let's test this agent."

---

## 🎬 TESTING (15 min)

**[Terminal]**

**SAY:**
"So from the parent directory (one level above greeting_agent folder), let's launch ADK Web:
[Type: adk web]

There you go - it's starting up...

[Browser opens to localhost:3002]

Perfect! You see greeting_agent in the dropdown? Let's select it.

Now let's test. I'm going to ask: 'What time is it?'

[Type and send]

Watch what happens...

[Agent calls get_current_time tool, returns time]

There you go! You see that? In the Events tab, you can see it called the get_current_time tool. This is very cool - you can see exactly what the agent does.

Let's try the other tool: 'Tell me about the company'

[Send]

[Agent calls get_company_info]

Perfect - it called get_company_info and returned the company details.

This is your first working agent!"

**[Show voice input]**

**SAY:**
"Real quick - see the microphone icon? That's voice input, new in ADK 1.18. Let's try it:
[Click microphone, speak: 'What time is it?']

[Agent responds with voice]

There you go - voice input works! This only works with simple agents using Gemini 2.0 models. Sequential and Parallel agents don't support voice because they don't have a model at the root level.

All right, so that's testing. Now you try."

---

## 🎬 EXERCISE (5 min)

**SAY:**
"Okay, here's your exercise:

1. Customize get_company_info() with YOUR company information
2. Add a new tool called get_team_members() that returns your team
3. Update the agent to use all three tools
4. Test it in ADK Web

The starter code is in module-3/exercises/. Take 15-20 minutes. Pause the video.

Solution walkthrough is next when you're ready."

---

## 🎬 SOLUTION (10 min)

**SAY:**
"All right, let's walk through the solution. So first, customizing company_info - you just change the values:
[Show solution]

For the new tool, here's the pattern:
[Show get_team_members() complete solution]

And update the imports and tools list:
[Show complete agent.py]

There you go - three tools working. Perfect."

---

## 🎬 RECAP (2 min)

**SAY:**
"Okay, so Module 3 complete. You built your first AI agent from scratch.

You know the five components: name, model, description, instruction, tools.
You created custom Python function tools.
You tested with ADK Web and voice input.

In Module 4, we're going to build multi-agent workflows where agents work together in sequence. This is where agents become really powerful.

See you in Module 4!"

---
