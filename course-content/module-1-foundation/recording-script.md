# Module 1: The Modern AI Agent Stack - Recording Script

**Duration:** 90 minutes content
**Recording Time:** 3-4 hours (with retakes)
**Energy Level:** Moderate, welcoming
**Focus:** Theory and setup (no coding yet)

---

## 🎬 SEGMENT 1: HOOK (30 seconds)

**[On camera or voice over title slide]**

**SAY:**
"Hello, and welcome to the Ultimate AI Agents Masterclass. My name is Ady Ngom, and I'm a Google Developer Expert for AI and Machine Learning.

Okay, so today we're starting with Module 1 - The Modern AI Agent Stack. And by the end of this module, you'll understand what AI agents are, how they're different from regular chatbots, and you'll have your development environment completely set up and ready to build.

Let's get into it."

**[Transition to screen recording]**

---

## 🎬 SEGMENT 2: OVERVIEW (2-3 minutes)

**[Show slide: Module 1 Overview]**

**SAY:**
"All right, so here's what we're covering in this module. First, I'm going to show you what an AI agent actually is - and how it's different from just a language model or a chatbot. A lot of people get confused about this, so we're going to make it very clear.

Then we're going to look at the Google AI ecosystem - Gemini API versus Vertex AI, and when you'd use which one.

After that, I'm going to show you a comparison of different agent frameworks - ADK versus LangChain versus CrewAI - so you can understand when to use each one and why we're focusing on ADK for this course.

And finally, we're going to get your development environment set up. So we're going to install Python, set up ADK, get your API key, and verify everything works.

This is going to be fun."

**[Show slide: Learning Objectives]**

**SAY:**
"By the end of this module, you'll be able to:
- Explain what an AI agent is and how it differs from an LLM or chatbot
- Understand the Google AI ecosystem
- Choose the right framework for your use case
- Have ADK installed and ready to go

Okay, so let's start with the most fundamental question: What is an AI agent?"

---

## 🎬 SEGMENT 3: What is an AI Agent? (15 minutes)

**[Show slide: LLM vs Chatbot vs Agent]**

**SAY:**
"So let me show you the difference between an LLM, a chatbot, and an AI agent. This is very important because people use these terms interchangeably, but they're actually quite different.

**AN LLM - Large Language Model** - is the base capability. Think of it like the engine. It's just the model that can understand and generate text. Gemini, GPT-4, Claude - these are LLMs. They're powerful, but they're just sitting there waiting for input.

**A CHATBOT** is an LLM plus conversation memory. So now it can remember what you said earlier in the conversation. ChatGPT is a chatbot - it uses an LLM (GPT-4) plus conversation history. But it's still limited to just conversation.

**AN AI AGENT** - this is where it gets interesting - is an LLM plus tools plus reasoning plus autonomy.

Let me break that down:
- **Tools**: The agent can DO things - search Google, query databases, send emails, create calendar events
- **Reasoning**: The agent can think through problems, make plans, decide which tools to use
- **Autonomy**: The agent can work on tasks without constant human input

So the difference: A chatbot answers questions. An agent completes tasks."

**[Show slide: Chatbot vs Agent Example]**

**SAY:**
"Here's a real example. Let's say you want to research a topic and write a blog post about it.

**With a chatbot:**
- You: 'Research AI agents for me'
- Chatbot: [Writes research summary from training data]
- You: 'Now write a blog post'
- Chatbot: [Writes blog post]
- You: 'Optimize it for SEO'
- Chatbot: [Optimizes]

You're doing all the orchestration. You're the project manager telling it what to do at each step.

**With an AI agent:**
- You: 'Write a blog post about AI agents'
- Agent thinks: 'I need to research first. I'll use Google Search tool. Then I'll write a draft. Then I'll optimize it.'
- Agent: [Uses Google Search tool, researches current info, writes draft, optimizes, returns final post]

You see the difference? The agent figures out the steps and uses the right tools autonomously. That's what we're building in this course."

**[Pause for absorption]**

**SAY:**
"Okay, so that's the fundamental difference. Now let's talk about Google's ecosystem for building these agents."

---

## 🎬 SEGMENT 4: The Google AI Ecosystem (20 minutes)

**[Show slide: Gemini API vs Vertex AI]**

**SAY:**
"All right, so Google gives you two ways to access Gemini models: Gemini API and Vertex AI. Let me show you when to use which one.

**GEMINI API** - This is the simple, fast way to get started. You go to Google AI Studio, get an API key, and you're coding in 5 minutes. It's perfect for:
- Development and prototyping
- Personal projects
- Learning and experimentation
- When you just want to build something quickly

The pricing is super affordable - like 10 cents per million tokens for Gemini 2.0 Flash. That's insanely cheap.

**VERTEX AI** - This is Google Cloud's enterprise platform for AI. It's more complex to set up, but it gives you:
- Enterprise-grade security and compliance
- Integration with other Google Cloud services
- Fine-tuning capabilities
- Team collaboration features
- SLA guarantees

So when do you use Vertex AI? When you're building production systems for companies. When you need SOC 2 compliance, or you're handling sensitive data, or you need to integrate with BigQuery and Cloud Storage.

For this course, we're using Gemini API because we want to move fast. But everything we build works with Vertex AI too - you just change the authentication method."

**[Show slide: ADK Overview]**

**SAY:**
"Now, ADK - the Agent Development Kit - this is Google's framework for building AI agents. And this is what we're focusing on in this entire course.

ADK gives you:
- Built-in agent patterns (Sequential, Parallel, Loops)
- Session and memory management
- Tool integration (Google Search, code execution, databases)
- Production-ready architecture
- Integration with Google Cloud

The beautiful thing about ADK is it's opinionated. It tells you: 'Here's the right way to build agents.' You're not starting from scratch trying to figure out patterns. Google has done the hard work."

**[Pause]**

**SAY:**
"Okay, so that's the Google ecosystem. Now let's compare ADK to other frameworks you might have heard about."

---

## 🎬 SEGMENT 5: Framework Comparison (25 minutes)

**[Show slide: ADK vs LangChain vs CrewAI vs AutoGen]**

**SAY:**
"So you might be wondering: Why ADK? There are other frameworks out there - LangChain, CrewAI, AutoGen. Let me show you when to use each one and why we're using ADK for this course.

**LANGCHAIN** - This is probably the most popular framework. It's been around longer. The thing about LangChain is it's very flexible - you can do almost anything with it. But that flexibility comes with complexity. You have to make a lot of decisions. It's like getting a box of LEGO pieces - you can build anything, but you need to figure out the architecture yourself.

When to use LangChain:
- You need maximum flexibility
- You're integrating with lots of different services
- You want access to their huge ecosystem of tools
- You're comfortable figuring out patterns yourself

**CREWAI** - This is opinionated in a different way. It's all about role-based agents working as a team. It's like having a company of AI workers - you have a CEO agent, a researcher agent, a writer agent.

When to use CrewAI:
- Your use case maps to 'roles' well (marketing team, dev team, etc.)
- You like the 'crew' metaphor
- You want simpler code than LangChain

**AUTOGEN** - This is Microsoft's framework. It's focused on multi-agent conversations. Agents can talk to each other back and forth.

When to use AutoGen:
- You need agents debating or collaborating
- You're in the Microsoft ecosystem
- You want agents that converse with each other

**ADK - Agent Development Kit** - This is Google's opinionated framework. And here's why we're using it for this course:

✅ **Google-native** - Works seamlessly with Gemini, Vertex AI, Google Cloud
✅ **Production-ready** - Built for enterprise from day one
✅ **Clear patterns** - Sequential, Parallel, Loops - Google tells you the best practices
✅ **Performance** - Optimized for Gemini models specifically
✅ **Built-in tools** - Google Search, code execution, BigQuery - just work
✅ **Latest features** - Voice input, multimodal, everything new from Google

The thing I really like about ADK - and you'll see this as we build - it's designed for production. Not just prototypes. When we build something in this course, you can deploy it to real business use cases."

**[Show slide: Decision Matrix]**

**SAY:**
"So here's my recommendation: Use ADK when you're building production systems with Google Cloud, especially if you're using Gemini models. Use LangChain when you need maximum flexibility and ecosystem. Use CrewAI when you're building role-based teams. Use AutoGen when agents need to converse.

For most business use cases with Gemini, ADK is the right choice. And that's what we're mastering in this course.

All right, so that's the landscape. Now let's get your environment set up so you can start building."

---

## 🎬 SEGMENT 6: Environment Setup (30 minutes)

**[Switch to terminal/screen recording]**

**SAY:**
"Okay, so let's get your development environment ready. We need three things: Python 3.11 or higher, a virtual environment, and ADK installed. Let me walk you through this step by step.

First, let's check if you have Python installed. Open your terminal and type:
[Type: python --version]

You should see Python 3.11 or higher. If you see 3.10 or lower, you'll need to upgrade. I'm on 3.11 here, so we're good.

Perfect."

**[Show slide: Virtual Environment - Why?]**

**SAY:**
"All right, real quick - why virtual environments? Because each Python project has different dependencies. If you install everything globally, you're going to have version conflicts. So we create an isolated environment for this course.

Let me show you how to do this."

**[Back to terminal]**

**SAY:**
"So I'm just going to create a new directory for our course. Let's call it:
[Type: mkdir adk-course]
[Type: cd adk-course]

There you go. Now we're in our project folder.

Now let's create a virtual environment:
[Type: python -m venv .venv]

This creates a .venv folder with an isolated Python environment. You see that? Perfect.

Now we need to activate it. On Mac or Linux, you do:
[Type: source .venv/bin/activate]

On Windows, it's:
.venv\\Scripts\\activate

You'll see (.venv) appear in your prompt. There you go - that means you're in the virtual environment now."

**[Show terminal with (.venv) prefix]**

**SAY:**
"Okay, so now we're ready to install ADK. This is very important - make sure you're in the virtual environment before installing.

Let's install ADK:
[Type: pip install google-adk]

This will take about 30-60 seconds. It's installing ADK and all its dependencies.

[Wait for installation to complete]

There you go. All right, now let's verify it installed correctly:
[Type: adk --version]

You should see version 1.18 or higher. Perfect - we're ready."

**[Show slide: Get Your API Key]**

**SAY:**
"Now we need a Gemini API key. This is free, and it takes about 1 minute to get. Let me show you how.

Open your browser and go to:
https://aistudio.google.com/apikey

[Open the site on screen]

You'll see this page. If you're not signed into Google, sign in. Then click 'Create API key'.

[Click the button]

There you go - it generates a key that starts with 'AIza'. This is your key - keep it private, don't share it publicly.

Click the copy button.

[Copy the key]

Perfect. Now let's save this in our project. We're going to create a .env file:
[Type: touch .env]

Now open it in your editor:
[Open .env file]

And add your key:
[Type: GOOGLE_API_KEY=your_key_here]
[Paste the actual key]

There you go. Save that.

This is very important - the .env file is where ADK looks for your API key. Make sure the variable name is exactly GOOGLE_API_KEY."

**[Pause for emphasis]**

**SAY:**
"All right, one more thing. Let's verify everything works. Let's create a quick test. Create a file called test.py:
[Type: touch test.py]

And let's put in some simple code:
[Type in test.py:
```python
from google.adk.agents import Agent

test_agent = Agent(
    name='test',
    model='gemini-2.0-flash-exp',
    instruction='You are a helpful assistant.'
)

print('ADK is installed and working!')
```
]

Save that. Command S.

Now let's run it:
[Type: python test.py]

If you see 'ADK is installed and working!' - you're ready. There you go. Perfect."

---

## 🎬 SEGMENT 7: ADK Web Introduction (10 minutes)

**[Show slide: ADK Web - Your Development UI]**

**SAY:**
"Okay, so ADK comes with a built-in development UI called ADK Web. This is very cool - it's like a playground for testing your agents. Let me show you how to use it.

First, we need an agent to test. Let's create a simple one. Create a folder structure like this:
[Type: mkdir -p greeting_agent]
[Type: cd greeting_agent]

Now create three files:
[Type: touch __init__.py agent.py .env]

In the __init__.py, just put:
[Type in __init__.py:
```python
from .agent import root_agent
```
]

This tells Python we have an agent in this folder.

In the .env file, copy your API key:
[Type: GOOGLE_API_KEY=your_key_here]

And in agent.py, let's create a super simple agent:
[Type in agent.py:
```python
from google.adk.agents import Agent

root_agent = Agent(
    name='greeting_agent',
    model='gemini-2.0-flash-exp',
    description='A friendly assistant',
    instruction='You are a helpful and friendly assistant. Keep responses concise.'
)
```
]

There you go. Save that.

Now, this is the cool part. Go back to your terminal and type:
[Type: cd ..]  (back to parent directory with greeting_agent folder)
[Type: adk web]

ADK Web starts up and you'll see a URL - usually localhost:3002.

[Open browser to localhost:3002]

There you go! This is ADK Web. You see greeting_agent in the dropdown? That's our agent.

Let's test it. Type: 'Hello, how are you?'

[Send message]

And you get a response! Perfect.

Now, this is very important - see these tabs? Events, State, Artifacts.

The **Events tab** shows you everything the agent does. Every tool call, every decision.
The **State tab** shows conversation history.
The **Artifacts tab** is for files the agent creates.

We're going to use ADK Web throughout the course for testing. It's your best friend for debugging."

**[Close browser]**

**SAY:**
"All right, so that's ADK Web. Very powerful for development. Okay, let's keep going."

---

## 🎬 SEGMENT 8: EXERCISE INTRO (5 minutes)

**[Show slide: Exercise 1]**

**SAY:**
"Okay, so now it's your turn. Here's what I want you to do:

**Exercise: Verify Your Setup**

1. Make sure Python 3.11+ is installed (python --version)
2. Create a virtual environment (.venv)
3. Activate the environment
4. Install google-adk (pip install google-adk)
5. Get your API key from aistudio.google.com
6. Create the greeting_agent folder structure
7. Test with ADK Web

Take your time with this. Pause the video if you need to. The exercise files are in the module-1 folder with detailed instructions.

When you're ready, let's go through common issues you might hit."

---

## 🎬 SEGMENT 9: SOLUTION / TROUBLESHOOTING (10 minutes)

**[Screen recording - terminal]**

**SAY:**
"All right, let's walk through common issues you might encounter.

**Issue 1: Python version too old**

If you see Python 3.9 or 3.10, you need to upgrade. Go to python.org and download the latest version. On Mac, you can use Homebrew:
[Type: brew install python@3.11]

**Issue 2: 'adk: command not found'**

This usually means you're not in the virtual environment. Make sure you see (.venv) in your terminal prompt. If not, activate it:
[Type: source .venv/bin/activate]

**Issue 3: 'API key not found'**

Make sure your .env file has exactly this:
GOOGLE_API_KEY=your_actual_key_here

No quotes, no spaces. And make sure the .env file is in the same folder as agent.py.

**Issue 4: ADK Web shows 'No agents found'**

This means the folder structure isn't right. Make sure:
- Folder name matches agent name in agent.py
- You have __init__.py with: from .agent import root_agent
- The variable is called 'root_agent' (not just 'agent')

Most issues come from folder structure or .env file problems. So double-check those first."

**[Pause]**

**SAY:**
"If you're stuck, there's a troubleshooting guide in the course materials. And you can always re-watch this module - that's what it's here for."

---

## 🎬 SEGMENT 10: RECAP & NEXT (3 minutes)

**[Show slide: Module 1 Summary]**

**SAY:**
"Okay, so let's recap what we learned in Module 1:

**First**, we understand what an AI agent is - it's an LLM plus tools plus reasoning plus autonomy. It can complete tasks, not just answer questions.

**Second**, we know the Google ecosystem - Gemini API for fast development, Vertex AI for enterprise production.

**Third**, we can compare frameworks - ADK for Google-native production, LangChain for flexibility, CrewAI for role-based, AutoGen for conversations.

And **fourth**, you have ADK installed and working. You tested it with ADK Web and verified your setup.

That's a solid foundation."

**[Show slide: Coming Up in Module 2]**

**SAY:**
"In Module 2, we're going to dive into the Python skills you need for building production agents. We're going to cover async/await - this is where a lot of people get stuck, so we're going to make it very clear. We'll also cover Pydantic models for structured output, type hints, and error handling.

This is going to get more hands-on. We're going to start writing code.

That's all for Module 1. See you in Module 2!"

**[Fade out]**

---

## 📝 RECORDING NOTES

**Energy Level:** Moderate, welcoming (first module, set tone)
**Pace:** Slow and clear (foundation, don't rush)
**Key Moments:**
- LLM vs Chatbot vs Agent explanation (critical concept)
- API key creation (show the actual process)
- ADK Web demo (show it working live)

**Common Phrases to Use:**
- "Let me show you..." (frequent)
- "This is very important" (2-3 times for key concepts)
- "There you go" (after each success)
- "Perfect" (validation)
- "Okay, so..." (transitions)

**If You Make Mistakes:**
- Say "Let me redo that"
- Pause 3 seconds
- Redo the section
- Editor will cut it

**Total Segments:** 10
**Total Recording Time:** 90 min content = ~3 hours with retakes

---

## ✅ PRE-RECORDING CHECKLIST

**Before recording Module 1:**

**Slides Needed:**
- [ ] Title slide (Module 1: Foundation)
- [ ] LLM vs Chatbot vs Agent diagram
- [ ] Gemini API vs Vertex AI comparison
- [ ] Framework comparison matrix (ADK/LangChain/CrewAI/AutoGen)
- [ ] ADK Web screenshot
- [ ] Exercise slide
- [ ] Module summary slide
- [ ] Module 2 preview slide

**Demos Ready:**
- [ ] Terminal ready for Python install check
- [ ] Can access aistudio.google.com (API key page)
- [ ] greeting_agent test folder created
- [ ] ADK Web can launch

**Environment:**
- [ ] Quiet space (no interruptions)
- [ ] Good audio (microphone tested)
- [ ] Screen recording software ready
- [ ] Water/coffee nearby

---

**This script is ready to record! Just follow along and speak naturally.**
