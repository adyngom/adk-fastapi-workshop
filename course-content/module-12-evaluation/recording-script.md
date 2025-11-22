# Module 12: Agent Evaluation & Testing - Recording Script

**Duration:** 120 min
**Focus:** Quality assurance for AI agents

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 12. Okay, so today we're talking about testing AI agents.

Traditional unit tests don't work for agents - they're probabilistic, not deterministic. You can't just assert 'output equals X'. So we need a different approach.

By the end, you'll know how to build evaluation datasets, use LLM-as-judge patterns, and test your agents' quality. Production confidence.

Let's build this!"

---

## 🎬 CONTENT STRUCTURE

**1. Why Traditional Tests Fail** (15 min)
- Probabilistic vs deterministic
- "Same input, different output"
- What to test instead (quality, trajectory, correctness)

**2. Building Eval Datasets** (25 min)
- Create test cases for customer_service
- Expected behaviors vs exact outputs
- Edge cases and failure modes

**3. LLM-as-Judge Pattern** (30 min)
- Using another LLM to evaluate agent output
- Scoring criteria (accuracy, helpfulness, format)
- Demo: Evaluate customer_service responses

**4. Trajectory Evaluation** (25 min)
- Not just output - HOW the agent got there
- Did it use the right tools?
- Did it follow the intended workflow?

**5. Regression Testing** (15 min)
- Catch quality degradation
- Automated evaluation in CI/CD
- Build: Eval suite that runs on every deploy

**6. Exercise & Recap** (10 min)

**Key moment:** "This investment pays off quickly - confidence in production"

---
