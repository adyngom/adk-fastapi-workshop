# Financial Advisor Agent

**Step 5 of 9** | **Duration:** 30 minutes | **Difficulty:** Advanced

## Overview

🎯 **MAJOR PATTERN SHIFT!** First Parallel agent in the workshop.

A multi-analyst financial advisory team where 4 specialists work **simultaneously**, then a synthesis agent combines their insights. Demonstrates when and why to use parallel execution over sequential.

## Learning Objectives

By completing this agent, you will understand:

- ✅ **ParallelAgent Pattern** - Multiple agents executing simultaneously
- ✅ **When Parallel > Sequential** - Speed + multiple perspectives
- ✅ **Synthesis After Parallel** - Combining concurrent outputs
- ✅ **Performance Optimization** - 4x faster than sequential for independent tasks
- ✅ **Multi-Perspective Analysis** - Data + Strategy + Execution + Risk analyzed together

## Pattern Demonstrated

**Parallel Execution + Synthesis**

```
financial_advisor (SequentialAgent)
├── parallel_analysts (ParallelAgent) ← ALL RUN AT SAME TIME
│   ├── data_analyst (Agent)
│   │   └── Role: Market data & metrics
│   ├── trading_analyst (Agent)
│   │   └── Role: Strategy recommendations
│   ├── execution_analyst (Agent)
│   │   └── Role: How to execute trades
│   └── risk_analyst (Agent)
│       └── Role: Risk assessment
│
└── synthesis_agent (Agent) ← RUNS AFTER ALL PARALLEL COMPLETE
    └── Role: Combine all perspectives → unified recommendation
```

**Key Difference from Steps 2-4:**

| Pattern | Execution | Time | Use When |
|---------|-----------|------|----------|
| **Sequential** (Steps 2-4) | One after another | 4x time | Tasks depend on previous output |
| **Parallel** (Step 5) | All at once | 1x time | Tasks are independent |

**Example:**
- Sequential: Research THEN Draft THEN Optimize (each needs previous)
- Parallel: Data + Strategy + Execution + Risk (all independent of each other)

## Business Value

Real-world impact:
- **4x faster** - Analysts work simultaneously instead of waiting
- **Comprehensive** - Multiple expert perspectives in one recommendation
- **Balanced** - Data + Strategy + Execution + Risk all considered
- **Quality** - No single point of failure (if one analyst misses something, others catch it)

Use cases:
- Investment analysis
- Product launch decisions (market + tech + finance + risk teams)
- M&A due diligence (legal + financial + technical + cultural)
- Any decision requiring multiple expert viewpoints

## ADK 1.18+ Features

### Agent-to-Agent (A2A) - Preview
- **Available:** 1.17+ (not used here, introduced in Step 8)
- **Preview:** In Step 8, we'll use `agent_to_a2a()` to turn agents into tools
- **This step:** Uses ParallelAgent (built-in ADK pattern)

## Architecture

### Parallel Execution Flow

```
User Input: "Analyze AAPL stock for a moderate-risk, long-term investor"

    ↓

[PARALLEL ANALYSTS] - All execute simultaneously
│
├─ [DATA ANALYST]           ├─ [TRADING ANALYST]       ├─ [EXECUTION ANALYST]     ├─ [RISK ANALYST]
│  Research market data     │  Develop 3-5 strategies  │  Create execution plan   │  Assess risks
│  Current price: $175      │  Strategy 1: Buy & Hold  │  Use limit orders        │  Market risk: Med
│  P/E: 28.5               │  Entry: $170-175         │  Position: 5-10%         │  Company risk: Low
│  Sector: Tech +12% YTD    │  Target: $220            │  Stop-loss: $160         │  Mitigation: Stops
│  Analyst consensus: Buy   │  Timeframe: 12-18mo      │  Cost: Minimal           │  Risk/Reward: 2.5:1
│                          │                          │                          │
│  (30 seconds)            │  (30 seconds)            │  (30 seconds)            │  (30 seconds)
└────────────────────────────┴──────────────────────────┴──────────────────────────┴──────────────────

Total time: ~30 seconds (parallel) vs ~120 seconds (sequential)

    ↓

[SYNTHESIS AGENT]
Combines all 4 perspectives:
- Data: "Strong fundamentals, sector leadership"
- Strategy: "Long-term growth best for this risk profile"
- Execution: "Use limit orders, 5-10% position"
- Risk: "Favorable risk/reward with proper stops"

Final Output: Unified recommendation with action plan

    ↓

User receives comprehensive, multi-perspective advice
```

## Why Parallel Here?

**These tasks are INDEPENDENT:**

✅ Data analyst doesn't need strategy recommendations to research market data
✅ Trading analyst can develop strategies while data is being gathered
✅ Execution analyst can plan order types independently
✅ Risk analyst can assess risks without waiting for execution plan

**They all analyze THE SAME THING (the stock) from different angles.**

Then synthesis combines them.

**Contrast with Sequential (Steps 2-4):**
- Customer service: Triage MUST happen before research
- Content: Research MUST happen before draft
- Medical: Intake MUST happen before verification

Those are DEPENDENT tasks → Sequential
These are INDEPENDENT tasks → Parallel

## Files

```
financial_advisor/
├── agent.py          # 4 parallel analysts + synthesis
├── .env              # API key
├── __init__.py       # Package marker
└── README.md         # This file
```

## Running the Agent

### Example Request

```python
from google.adk import run_debug
from adk_agents.financial_advisor.agent import root_agent

request = """
Stock: AAPL (Apple Inc.)
Risk Profile: Moderate
Investment Timeframe: Long-term (12-18 months)
Portfolio Size: $50,000
Goal: Growth with reasonable safety
"""

run_debug(root_agent, request)
```

**Watch the "Events" tab in ADK Web:**
You'll see all 4 analysts execute simultaneously, then synthesis runs.

## Example Interaction

**User:**
```
I'm thinking about investing in NVDA. I'm a moderate-risk investor with a
long-term horizon (2-3 years). I have $100k to invest. What do you recommend?
```

**Parallel Analysts Execute (simultaneously):**

**Data Analyst Output:**
```json
{
  "ticker": "NVDA",
  "current_price": "$485",
  "market_cap": "$1.2T",
  "key_metrics": {
    "pe_ratio": "62",
    "growth_rate": "High",
    "sector": "Semiconductors (AI chips)"
  },
  "recent_news": [
    "Data center revenue up 200% YoY",
    "New AI chip architecture announced"
  ],
  "analyst_consensus": "85% Buy, 15% Hold"
}
```

**Trading Analyst Output:**
```json
{
  "strategies": [
    {
      "name": "Long-term AI Growth",
      "entry_point": "$480-$500",
      "target_price": "$650-$700 (18-24mo)",
      "stop_loss": "$430",
      "rationale": "AI demand acceleration, data center dominance"
    },
    {
      "name": "Dollar-Cost Averaging",
      "type": "phased-entry",
      "approach": "Invest 25% every quarter over 1 year"
    }
  ],
  "recommended_strategy": "DCA for moderate risk profile"
}
```

**Execution Analyst Output:**
```json
{
  "execution_plan": {
    "initial_entry": {
      "order_type": "Limit order at $485",
      "quantity": "50 shares ($24,250 = 24.25% of portfolio)",
      "timing": "Place during normal trading hours"
    },
    "DCA_schedule": {
      "Q1": "Invest $25k (50 shares at ~$500)",
      "Q2": "Invest $25k (check price then)",
      "Q3": "Invest $25k",
      "Q4": "Invest $25k"
    },
    "stop_loss_setup": "Trailing stop at 10% below purchase price"
  }
}
```

**Risk Analyst Output:**
```json
{
  "risk_assessment": {
    "overall_risk_level": "Moderate-High",
    "key_risks": [
      {
        "category": "Valuation Risk",
        "description": "High P/E ratio (62) means vulnerable to corrections",
        "mitigation": "DCA approach reduces timing risk"
      },
      {
        "category": "Concentration Risk",
        "description": "Single stock = no diversification",
        "mitigation": "Keep under 25% of total portfolio"
      }
    ]
  },
  "risk_reward_ratio": "3:1 (potential 50% upside vs 15% managed downside)"
}
```

**Synthesis Agent Output:**
```json
{
  "recommendation_summary": {
    "ticker": "NVDA",
    "overall_recommendation": "BUY (with DCA approach)",
    "confidence_level": "Medium-High",
    "rationale": "Strong AI growth drivers and data center dominance support
     long-term growth. High valuation warrants dollar-cost averaging to
     reduce timing risk. Moderate risk profile aligns with phased entry."
  },
  "suggested_action_plan": {
    "immediate_steps": [
      "1. Allocate $100k for NVDA investment over 12 months",
      "2. Month 1: Buy $25k worth (~50 shares) with limit order at $485",
      "3. Set trailing stop-loss at 10% below entry",
      "4. Calendar reminders for Months 4, 7, 10 for additional $25k purchases"
    ],
    "monitoring": "Review quarterly before each DCA purchase"
  },
  "key_insights": {
    "from_data_analyst": "85% analyst consensus Buy - strong fundamentals",
    "from_trading_analyst": "DCA reduces timing risk given high valuation",
    "from_execution_analyst": "Limit orders and trailing stops minimize costs/risk",
    "from_risk_analyst": "Keep position under 25% of portfolio, use stops"
  },
  "important_disclaimers": [
    "This is educational, not personalized financial advice",
    "Consult licensed financial advisor before investing",
    "Only invest money you can afford to lose"
  ]
}
```

## Common Issues

### Synthesis Ignoring One Analyst

**Problem:** Final recommendation doesn't reference all 4 analysts

**Solution:**
- Synthesis agent's instruction explicitly says "combine ALL perspectives"
- Check Events tab - did all 4 parallel agents complete?
- Synthesis should acknowledge each analyst's key point

### Parallel Agents Taking Too Long

**Problem:** Parallel execution not actually faster

**Solution:**
- Check if agents are truly running in parallel (Events tab)
- ParallelAgent waits for ALL to complete (slowest determines total time)
- If one agent has complex research, it slows everyone

### Conflicting Recommendations

**Problem:** Trading says "BUY" but Risk says "too risky"

**Solution:**
- This is GOOD! Multiple perspectives should sometimes disagree
- Synthesis agent's job: Acknowledge both and explain tradeoff
- "Trading sees opportunity, Risk urges caution → Recommend DCA for balance"

## Understanding Parallel Patterns

**Key Concepts:**

1. **Independence is Required**
   - All parallel agents must be able to work with same input
   - They shouldn't need each other's outputs
   - If Agent B needs Agent A's output → Use Sequential, not Parallel

2. **Synthesis is Critical**
   - Parallel gives you multiple outputs
   - Synthesis combines them into ONE recommendation
   - Without synthesis, user gets 4 separate reports (confusing!)

3. **Performance Gains**
   - Sequential: T1 + T2 + T3 + T4 = Total Time
   - Parallel: max(T1, T2, T3, T4) = Total Time
   - Example: 4 agents × 30 sec each
     - Sequential: 120 seconds
     - Parallel: 30 seconds (4x faster!)

4. **When to Use Parallel**
   - Multiple expert perspectives needed
   - Tasks are independent
   - Speed matters
   - Examples: Due diligence, product launch analysis, investment research

## Success Criteria

Before moving to Step 6, verify:

- [ ] All 4 analysts execute simultaneously (check Events tab timing)
- [ ] Synthesis combines all perspectives
- [ ] Recommendations are balanced (acknowledge tradeoffs)
- [ ] Faster than sequential would be
- [ ] Tested with at least 2 different stocks

## Next Steps

**Step 6: Brand Intelligence (Parallel + Synthesis)**

Preview: Same Parallel pattern, different domain. Multi-source intelligence gathering (news + social + trends + competitors) all searched simultaneously, then synthesized. Reinforces when to use Parallel.

## Debugging Tips

### Measure Parallel Performance

```python
import time
from google.adk import run_debug
from adk_agents.financial_advisor.agent import root_agent, parallel_analysts

# Time the parallel execution
start = time.time()
result = run_debug(root_agent, "Analyze TSLA for moderate investor")
parallel_time = time.time() - start

print(f"Parallel execution: {parallel_time:.1f} seconds")
# Compare to what sequential would take (estimate 4x longer)
```

### Check All Analysts Contributed

```python
def verify_synthesis(synthesis_output):
    # Synthesis should reference all 4 analysts
    required = ["data_analyst", "trading_analyst", "execution_analyst", "risk_analyst"]
    for analyst in required:
        assert analyst in synthesis_output.lower(), f"Missing {analyst} perspective!"
```

## Comparison with Previous Steps

| Step | Pattern | Agents | Execution | Use Case |
|------|---------|--------|-----------|----------|
| 2-4 | Sequential | 3-4 | One after another | Dependent tasks |
| **5** | **Parallel + Synthesis** | **4 + 1** | **Simultaneous** | **Independent analysis** |

**The Big Shift:** Steps 2-4 taught Sequential. Step 5 teaches Parallel. Both are essential patterns!

## References

- [ADK Documentation - Parallel Agents](https://google.github.io/adk-docs/agents/parallel/)
- [Workshop Progression](../../workshop_progression.yaml)
- [ADK Samples - Financial Advisor](https://github.com/google/adk-samples/tree/main/python/agents/financial-advisor)
- [Step 4 - Medical Auth](../medical_authorization/README.md) - Last Sequential

---

**Tags:** `step-5-financial-advisor`, `advanced`, `parallel-agent`, `synthesis`, `multi-perspective-analysis`
