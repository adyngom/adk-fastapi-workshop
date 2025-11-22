# Module 8: Complex Orchestration - Recording Script

**Duration:** 120 min
**Energy:** HIGH (bringing it all together!)
**Focus:** Sequential + Parallel combined + AP2 story

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 8. This is where everything comes together.

We've learned Sequential workflows. We've learned Parallel execution. Today we're combining them into complex orchestrations. Plus, I'm going to tell you a story about a developer who built a charity donation agent that handles real money - and why that required a completely different architecture.

By the end, you'll build systems with verification, audit trails, and accountability. Production-grade AI.

Let's go!"

---

## 🎬 SEQUENTIAL + PARALLEL COMBINED (50 min)

**SAY:**
"Okay, so let me show you project_management - this combines Sequential and Parallel.

[Open project_management/agent.py]

The structure:
1. Task breakdown agent (Sequential step 1)
2. Three parallel analysts (Sequential step 2, contains Parallel!)
   - Resource allocator
   - Risk assessor
   - Timeline estimator
3. Synthesis agent (Sequential step 3)

[Show the code structure]

You see that? Sequential outer layer, Parallel middle layer. Task breakdown MUST happen first. Then three analysts can work simultaneously. Then synthesis combines them.

[Demo with project planning query]

[Show Events tab - task breakdown, then 3 parallel, then synthesis]

There you go - complex orchestration. Real-world workflows combine patterns based on actual dependencies.

Perfect. Now let me tell you about Ayo Adedeji's charity advisor."

---

## 🎬 AYO'S AP2 CHARITY ADVISOR STORY (30 min)

**[Show slide: When Agents Handle Money]**

**SAY:**
"So there's a developer named Ayo Adedeji who built something really interesting - a charity donation agent using the Agent Payments Protocol, AP2.

The agent helps people donate to charities. It discovers high-impact charities, verifies their legitimacy, and processes donations.

But here's the thing: When agents handle money, you need more than just capability. You need accountability.

Ayo's insight: The agent needs role separation. Let me show you why:

**BAD architecture:**
- One agent discovers charities
- Same agent verifies them
- Same agent recommends AND executes donation
- Problem: Can cut corners, no checks and balances

**GOOD architecture (AP2-inspired):**
- Researcher agent: Finds candidate charities
- Verification agent: Independently validates (doesn't know which researcher prefers!)
- Risk agent: Assesses risks (also independent)
- Recommendation agent: Only recommends verified + low-risk options
- Auditor agent: Creates complete audit trail

Role separation. Independent verification. Complete audit trails.

Why? Because when you can replay the exact decision process - 'Why did you recommend this charity?' - you have accountability.

Let me show you how we built this pattern:

[Open verified_recommendations/agent.py]

[Walk through the 5-agent structure with narration]

[Demo query: 'Recommend charity for climate change, $10k donation']

[Show verification happening independently, audit trail created]

There you go. Every decision documented. Every verification independent. Complete accountability.

This is how you build AI systems companies can TRUST with high-stakes decisions.

Perfect. Let's wrap up Module 8."

---

## 🎬 RECAP

**SAY:**
"Module 8 complete. You learned complex orchestration - Sequential + Parallel combined. You learned the AP2-inspired pattern - verification and audit for high-stakes decisions. You understand accountability in AI systems.

Module 9 is the finale: Cloud deployment. We're taking everything we built and deploying it to Google Cloud Run. Production-ready.

See you in Module 9!"

---
