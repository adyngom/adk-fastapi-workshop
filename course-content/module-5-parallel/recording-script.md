# Module 5: Parallel Execution & Synthesis - Recording Script

**Duration:** 120 minutes
**Recording Time:** 4 hours
**Energy:** HIGH (paradigm shift + magic problem setup!)
**Focus:** Parallel patterns + THE $175 PROBLEM

---

## 🎬 HOOK (30 sec)

**SAY:**
"Hello and welcome to Module 5. This is the paradigm shift.

In Module 4, we learned Sequential - agents running one after another. Today, we're learning Parallel - agents running all at the same time. 4x faster.

By the end, you'll know when to use Parallel instead of Sequential, and you'll have built a financial advisory system with four analysts working simultaneously.

This is going to be exciting. Let's go!"

---

## 🎬 THE PARADIGM SHIFT (15 min)

**[Show slide: Sequential vs Parallel]**

**SAY:**
"Okay, so let me show you the fundamental difference between Sequential and Parallel.

**Sequential workflows** (Module 4):
- Tasks depend on each other
- A must finish before B starts
- Example: Triage THEN Research THEN Respond
- Time: Agent1 (30 sec) + Agent2 (30 sec) + Agent3 (30 sec) = 90 seconds total

**Parallel workflows** (this module):
- Tasks are independent
- All agents can work on the same input simultaneously
- Example: 4 analysts all analyze the same stock at once
- Time: All agents run together = 30 seconds total (the slowest one)

[Show timing diagram]

You see that? 4x faster because they're not waiting for each other!

So when do you use Parallel? When tasks are INDEPENDENT. Let me give you examples:

**Use Parallel for:**
- Financial analysis: 4 analysts (data, strategy, execution, risk) all analyze same stock
- Due diligence: Legal team, finance team, tech team all review same company
- Product launch: Marketing, Engineering, Sales all plan simultaneously
- Brand intelligence: News, social media, trends, competitors all research same brand

**Use Sequential for:**
- Customer support: Must triage BEFORE researching
- Content creation: Must research BEFORE writing
- Any workflow where output of step 1 is needed by step 2

The decision matrix is simple: Independent tasks = Parallel. Dependent tasks = Sequential.

All right, so that's the paradigm shift. Now let's build a Parallel workflow - financial advisor with 4 analysts."

---

## 🎬 BUILDING FINANCIAL_ADVISOR (40 min)

**[Fresh VS Code]**

**SAY:**
"Okay, let's build a financial advisory system. Four analysts working in parallel: data analyst, trading strategist, execution planner, and risk assessor. Then a synthesis agent combines their perspectives.

Let me create the folder:
[Type: mkdir financial_advisor]
[Type: cd financial_advisor]
[Type: touch __init__.py agent.py .env]

Perfect.

[Open agent.py]

Imports first:
[Type:
```python
'''
Financial Advisor - Parallel analysts + Synthesis
'''
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
```
]

We need all three this time. ParallelAgent for the analysts, and we'll wrap that in SequentialAgent with synthesis. You'll see why in a second.

All right, let's build the first analyst - data analyst:

[Type:
```python

# Data Analyst - Researches market data
data_analyst = Agent(
    name='data_analyst',
    model='gemini-2.0-flash-exp',
    description='Analyzes market data and financial metrics',
    instruction='''You are a financial data analyst.

Analyze the given stock ticker. Research:
- Current price and market cap
- P/E ratio, EPS, dividend yield
- Recent news and sentiment
- Analyst consensus

Provide objective data analysis.

Output format:
{
    "ticker": "...",
    "current_price": "$X",
    "key_metrics": {...},
    "recent_news": [...],
    "analyst_consensus": "X% Buy, Y% Hold, Z% Sell"
}'''
)
```
]

There you go. Now trading analyst:

[Type:
```python

# Trading Analyst - Develops strategies
trading_analyst = Agent(
    name='trading_analyst',
    model='gemini-2.0-flash-exp',
    description='Develops trading strategies based on risk profile',
    instruction='''You are a trading strategy specialist.

Develop 3-5 trading strategies for the stock.
Consider user's risk profile and timeframe.

Each strategy should include:
- Entry points
- Target prices
- Stop-loss levels
- Rationale

Output recommended strategies.'''
)
```
]

Perfect. Execution analyst:

[Type:
```python

# Execution Analyst - Creates trade plans
execution_analyst = Agent(
    name='execution_analyst',
    model='gemini-2.0-flash-exp',
    description='Creates execution plans for strategies',
    instruction='''You are a trade execution specialist.

Create detailed execution plan:
- Order types (market, limit, stop-loss)
- Position sizing
- Timing considerations
- Cost analysis

Be specific with numbers.'''
)
```
]

And finally, risk analyst:

[Type:
```python

# Risk Analyst - Assesses risks
risk_analyst = Agent(
    name='risk_analyst',
    model='gemini-2.0-flash-exp',
    description='Evaluates risks and mitigation strategies',
    instruction='''You are a risk assessment specialist.

Identify risks:
- Market risk
- Company-specific risk
- Execution risk

Provide mitigation strategies and risk/reward assessment.'''
)
```
]

There you go - four independent analysts. Now here's the key - we wrap them in a ParallelAgent:

[Type:
```python

# Parallel Execution - All 4 run simultaneously
parallel_analysts = ParallelAgent(
    name='parallel_analysts',
    description='4 analysts working simultaneously',
    sub_agents=[
        data_analyst,
        trading_analyst,
        execution_analyst,
        risk_analyst
    ]
)
```
]

Perfect. So ParallelAgent runs all four at the same time. But we have a problem - we get 4 separate outputs. The user wants ONE recommendation, not four reports.

This is where synthesis comes in:

[Type:
```python

# Synthesis Agent - Combines all perspectives
synthesis_agent = Agent(
    name='synthesis_agent',
    model='gemini-2.0-flash-exp',
    description='Synthesizes all analyst recommendations',
    instruction='''You receive outputs from 4 analysts:
1. Data Analyst - market data
2. Trading Analyst - strategies
3. Execution Analyst - execution plan
4. Risk Analyst - risk assessment

Combine into one cohesive recommendation.

Reference all 4 perspectives in your synthesis.'''
)
```
]

And finally, we need to run parallel THEN synthesis. That's Sequential at the top level:

[Type:
```python

# Root Agent: Parallel analysts, then synthesis
root_agent = SequentialAgent(
    name='financial_advisor',
    description='Multi-analyst team with parallel execution',
    sub_agents=[
        parallel_analysts,  # ← 4 analysts run in parallel
        synthesis_agent     # ← Then synthesis combines them
    ]
)
```
]

There you go! Command S.

Let me explain the structure:
- Top level: SequentialAgent (parallel THEN synthesis)
- Middle: ParallelAgent (4 analysts simultaneously)
- Bottom: 4 individual Agents + 1 synthesis Agent

All right, now let's test it. And this is where you're going to see something interesting..."

---

## 🎬 THE $175 PROBLEM (10 min) ⚠️ CRITICAL SETUP FOR MODULE 7!

**[ADK Web]**

**SAY:**
"So let's test the financial advisor. I'm going to ask for stock analysis:
[Type: 'Analyze AAPL stock for a moderate risk, long-term investor']

[Send]

Now watch the Events tab...

[Show all 4 analysts executing with similar timestamps]

You see that? Look at the timestamps - all four analysts started around the same time. They're running in parallel, not sequential.

[Wait for completion]

There you go. And here's the final recommendation...

[Read the synthesis output]

Perfect. But wait - let me check something. What did it say the Apple stock price is?

[Look at data_analyst output in Events]

It says... $175.23.

[Open new tab, search 'AAPL stock price']

[Show real price: ~$273]

Okay, so here's a problem. The agent says Apple is $175. But the real price today is $273. That's almost a $100 difference!

[Pause for effect]

So what's going on here? This is very important.

The problem is: LLMs have training cutoffs. Gemini's training data is from months ago. Back then, Apple was around $175. Today it's $273. But the LLM doesn't know that - it only knows what it was trained on.

So if you're making investment decisions based on this, you're using stale data. Not good for production!

Now, here's the cool part. There's a fix. And it's literally two lines of code. But I'm going to save that for Module 7 when we cover production tools.

In Module 7, I'm going to show you how to add the Google Search tool to the data_analyst. And when we do that, instead of using training data, it will search Google for the current price. $175 becomes $273. Real-time data.

For now, just know: The Parallel pattern works perfectly. The agent architecture is solid. The only issue is data freshness - and we'll fix that in Module 7.

All right, let's keep going. Let me show you the same Parallel pattern in a different domain."

---

## 🎬 BRAND_INTELLIGENCE (25 min)

**SAY:**
"So the same Parallel pattern works for brand and competitive intelligence. Let me show you:

[Open brand_intelligence/agent.py]

Four researchers: news, social media, trends, competitors. All searching different sources simultaneously.

[Show the parallel_researchers structure]

Same pattern as financial_advisor:
- 4 independent tasks (news research, social analysis, trend tracking, competitor monitoring)
- All run in parallel
- Synthesis combines into brand intelligence report

Let's test it:
[ADK Web, select brand_intelligence]
[Type: 'Analyze Tesla brand perception']

[Show Events tab - parallel execution]

There you go - all four researchers working at the same time. News finds recent articles, social analyzes sentiment, trends checks search volume, competitors looks at market position.

Then synthesis creates one cohesive report.

Same pattern. Different domain. This is the power of Parallel workflows.

Perfect. Now let's talk about synthesis."

---

## 🎬 SYNTHESIS PATTERNS (20 min)

**[Show slide: Why Synthesis Matters]**

**SAY:**
"All right, so synthesis. This is critical for Parallel workflows.

Without synthesis:
- You have 4 separate outputs
- User gets 4 different reports
- Confusing and overwhelming
- 'Which one do I listen to?'

With synthesis:
- Synthesis agent reads all 4 outputs
- Combines perspectives
- Resolves conflicts
- Creates ONE coherent recommendation

Let me show you a synthesis example:
[Show synthesis_agent from financial_advisor]

Look at the instruction - it says 'You receive outputs from 4 analysts...' and 'Combine into one cohesive recommendation.'

When analysts disagree (data says buy, but risk says concerns), synthesis acknowledges both:
'Data shows strong fundamentals, but risk analysis indicates caution due to high valuation. Recommended approach: Dollar-cost averaging to balance growth potential with risk management.'

You see that? It doesn't ignore the disagreement. It creates a balanced recommendation considering both viewpoints.

This is what makes Parallel valuable - not just speed, but comprehensive analysis from multiple perspectives, synthesized into actionable guidance.

Okay, let's wrap up Module 5."

---

## 🎬 EXERCISE (5 min)

**SAY:**
"Your exercise: Add a fifth analyst to the financial_advisor.

Create a sentiment_analyst that analyzes social media and news sentiment about the stock. Add it to the parallel_analysts. Make sure synthesis incorporates the sentiment perspective.

Exercise files in module-5/exercises/. Take 20 minutes. Solution next."

---

## 🎬 SOLUTION (10 min)

**SAY:**
"All right, solution walkthrough:

[Show sentiment_analyst creation]
[Show adding to parallel_analysts list]
[Show updated synthesis instruction]

There you go - five analysts now. Test it, and all five run in parallel. Perfect."

---

## 🎬 RECAP (3 min)

**SAY:**
"Module 5 complete - the paradigm shift.

You understand Parallel execution - for independent tasks, 4x faster.
You built financial_advisor with 4 parallel analysts.
You learned synthesis - combining multiple perspectives.
And you discovered a problem - the $175 stock price. We'll fix that in Module 7!

Next up: Module 6 - Memory and RAG. We're going to make agents remember past conversations and search through documents. Production-grade context management.

See you in Module 6!"

---

## 📝 RECORDING NOTES

**CRITICAL:** Set up the $175 problem clearly for Module 7 payoff!
**Energy:** High for paradigm shift, performance demo
**Demo:** Show Events tab timestamps (parallel proof)
