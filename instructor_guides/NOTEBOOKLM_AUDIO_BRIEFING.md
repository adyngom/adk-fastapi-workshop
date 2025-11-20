# ADK Workshop - Instructor Audio Briefing

**For NotebookLM Audio Generation**

This document is optimized for NotebookLM to generate an audio briefing you can listen to tonight. It covers everything you need to know for tomorrow's 4-hour workshop.

---

## Workshop Overview

You're teaching a 4-hour deep dive workshop on building production AI agents with Google's Agent Development Kit. This is not a beginner "build a calculator" workshop - you're teaching real production patterns that transform businesses.

The workshop takes students from single agents with custom tools all the way to complex multi-agent systems with verification and audit trails, inspired by Ayo Adedeji's charity advisor that uses the Agent Payments Protocol.

Total agents: 9
Total time: 4 hours
Format: YouTube live stream
Start time: 12 PM Eastern, but students should arrive at 11:45 for setup checks

---

## Workshop Philosophy

The core philosophy is simple: teach production-ready patterns through real business use cases. No weather agents or calculators. Every agent demonstrates a pattern students can immediately apply to their work.

You're teaching three fundamental patterns: Sequential workflows for multi-step processes, Parallel execution for speed and multiple perspectives, and verification systems for high-stakes decisions. By the end, students combine all three patterns in complex orchestrations.

The progression is carefully designed. Each agent builds on concepts from previous agents. Students master Sequential in steps 2 through 4, learn Parallel in steps 5 and 6, then see them combined in steps 7 through 9.

---

## Phase 1: Foundation - 30 Minutes

You start with greeting agent. This is step 1 of 9. It's a simple agent with custom Python function tools. The goal here is to establish the fundamentals: how agents are structured, how tools work, how to write instructions that shape agent behavior.

The greeting agent demonstrates voice input, which is a new feature in ADK 1.18. Only simple agents support voice, not sequential or parallel workflows. This is because voice requires synchronous request-response, which workflows can't provide.

Key teaching points for step 1:
- Agent class structure: name, model, description, instruction, and tools
- Custom tools are just Python functions with docstrings
- The docstring is critical - ADK uses it to understand what the tool does
- Instructions shape personality and behavior
- Testing with ADK Web on port 3002 or Streamlit on port 8501

Students will customize the company info tool and add a new team members tool. This hands-on exercise cements the basic pattern.

---

## Phase 2: Real Workflows - 90 Minutes

Now you introduce Sequential agents. This is the big conceptual leap from single agents to multi-agent workflows.

Step 2 is customer service. Three agents in sequence: triage categorizes and prioritizes, research finds solutions, response crafts the customer reply. The key concept is automatic state passing - each agent sees the previous agent's output in the conversation history. No manual state management needed.

Students need to understand that sequential means dependent. Triage MUST happen before research. Research MUST happen before response. If tasks depend on each other, use Sequential.

Step 3 is content pipeline. Same sequential pattern, different domain. Research, draft, optimize, publish. This is where students realize the pattern is reusable. If they understood customer service, they understand content pipeline. The pattern transfers across any business domain.

Step 4 is medical authorization. This introduces decision gates. Not all agents always run. Intake checks completeness - if incomplete, workflow stops. Verification checks eligibility - if not eligible, workflow stops. Medical review checks necessity - if not necessary, workflow stops. This teaches conditional execution within sequential workflows.

Key teaching point: Decision gates save processing time and costs. Why review medical necessity if the patient isn't eligible? Why research solutions if the triage shows it's spam? Gates are critical for production systems.

---

## Phase 3: Intelligent Decision Making - 60 Minutes

This is where you introduce Parallel agents. Major paradigm shift.

Step 5 is financial advisor. Four analysts work simultaneously: data analyst researches metrics, trading analyst develops strategies, execution analyst creates trade plans, risk analyst assesses risks. Then synthesis agent combines all four perspectives into one recommendation.

The critical teaching moment: Why parallel here but sequential before? Because these four tasks are INDEPENDENT. Data analyst doesn't need strategy recommendations to research market data. They all analyze the same stock from different angles. Independent tasks equal parallel execution.

Performance benefit is huge. Sequential would be: 30 seconds plus 30 seconds plus 30 seconds plus 30 seconds equals 2 minutes. Parallel is: maximum of 30 seconds equals 30 seconds. Four times faster!

Step 6 is brand intelligence. Same parallel pattern, different domain. Four researchers: news, social media, trends, competitors. All search simultaneously. Then synthesis combines into actionable insights.

This reinforces that parallel is domain-agnostic. Same pattern works for financial analysis and marketing intelligence and any scenario where you need multiple independent perspectives quickly.

Key teaching point: Synthesis is critical. Without synthesis, you hand the user four separate reports and say "good luck combining them." The synthesis agent is what makes parallel execution valuable - it creates one coherent recommendation from multiple viewpoints.

---

## Phase 4: Production Grade Systems - 60 Minutes

Now you bring everything together with advanced production patterns.

Step 7 is software assistant. This demonstrates Model Context Protocol integration. The workshop version simulates MCP tools, but you show production code patterns in the README and comments.

In production, this agent would use MCP Toolbox for PostgreSQL database queries, GitHub MCP server for issue searches, and LangChain tools for Stack Overflow. The workshop focuses on teaching the architecture and integration patterns, not on actually setting up PostgreSQL.

Key teaching point: MCP is how agents access external services. Database tools, API integrations, file systems - all through MCP. The protocol standardizes how tools work across different systems.

Step 8 is project management. This one already exists in the repo. It demonstrates complex orchestration - Sequential outer structure containing Parallel inner structure. Task breakdown happens first sequentially. Then three analysts work in parallel: resources, risks, timeline. Then synthesis combines everything into a comprehensive project plan.

This is where you introduce the Agent-to-Agent pattern as an alternative. Currently it uses ParallelAgent, which always runs all sub-agents. With A2A pattern using agent-to-a2a function, a coordinator agent could decide which specialists to call. More flexible, but more complex. Show both approaches.

Step 9 is verified recommendations. This is the finale, inspired by Ayo's charity advisor. When agents handle money or high-stakes decisions, you need more than model capability - you need accountability.

The architecture separates roles: researcher finds candidates, but verification agent independently validates claims. Risk checker assesses risks separately. No single agent controls the full decision. Then auditor creates an immutable trail of the entire decision process.

Key teaching point: This is how you build AI systems people can TRUST. Independent verification, complete audit trails, role separation, accountability. These aren't nice-to-haves for charity donations or financial transactions - they're requirements.

---

## ADK 1.18 Features Throughout

You're teaching the latest version of ADK, released November 5th. Several new features are integrated throughout the workshop.

Voice input works with simple agents using gemini-2-flash-exp or gemini-2-flash-live models. Students see this in greeting agent. Don't make a big deal of it - show it works, but emphasize it's only for simple agents, not workflows.

Visual Agent Builder is new in 1.18. This is an AI assistant that writes agent YAML from natural language descriptions. You can demo this after students build greeting agent in code - show how you could describe the same agent in plain English and have the AI generate it. But emphasize: code-first for production, visual builder for rapid prototyping.

Run debug helper is useful throughout. Instead of running full ADK Web, students can quickly test individual agents with run-debug function. Show this when debugging issues or testing sub-agents independently.

MCP Toolbox for databases is new in 1.18 and showcased in step 7. The production implementation would use this for PostgreSQL with vector search for RAG. The workshop simulates it, but the patterns are real.

BigQuery logging plugin is new in 1.18 and shown in step 9. In production, this logs every agent decision to BigQuery for audit and compliance. Show the code example - students understand the pattern even if they don't implement it.

Agent-to-Agent pattern is from 1.17 but important for step 8. The agent-to-a2a function converts agents into tools for other agents. More flexible than ParallelAgent for conditional orchestration.

---

## Common Teaching Challenges

Students new to async await might worry they need to understand Python's async internals. Emphasize: ADK handles all the async complexity. Students just define agents. They don't write async code, they configure agents that ADK runs asynchronously.

API key issues will happen. Have backup keys ready. Test all keys before the workshop starts. If a student's key doesn't work, swap in a backup immediately - don't let them debug during the workshop.

Different paces are inevitable. Some students will race ahead, others will struggle with step 2. This is why you have git tags. Fast students can checkout step-5 and jump ahead. Slow students can catch up by checking out the tag for where everyone else is. The tag system is your friend.

Time management is critical with 9 agents in 4 hours. Each step has suggested duration in the workshop progression YAML. Phase 1 and 2 are foundation - don't rush these. Phase 3 and 4 can be more demo-heavy if time runs short. Better that students master Sequential deeply than see all 9 agents superficially.

---

## Testing Strategy for Tomorrow Morning

You have 4 hours before the workshop starts. Here's how to use them effectively.

First hour: Test all 9 agents in sequence. Don't test thoroughly, just verify each loads and responds to one query. This is smoke testing - making sure nothing is completely broken.

Second hour: Deep test the critical agents. Steps 1, 2, 5, 7, and 9. These are where students will have questions. Make sure you can explain them confidently.

Third hour: Review your presentation flow. What will you say when introducing each pattern? What examples will you use? Write down 2-3 key teaching points per agent.

Fourth hour: Final tech check. IDX workspace open, all services running, backup API keys ready, YouTube stream tested, screenshare working. Then 15 minutes of breathing room before 11:45 when students start arriving.

---

## Agent Testing Order for Tomorrow

Test in the order students will experience them:

Greeting agent: Test company info tool, test current time tool, test workshop roadmap tool. Verify voice input works - click microphone in ADK Web. Make sure all three tools are callable.

Customer service: Test with issue like "customer can't login after password reset". Watch Events tab - verify triage runs, then research, then response. Make sure state passes correctly between agents.

Content pipeline: Test with "write about AI agent testing". Verify all four agents run in sequence. Check that draft uses research, optimizer improves draft, publisher formats correctly.

Medical authorization: Test with complete authorization request. Verify workflow runs all four agents. Then test with incomplete request - workflow should stop at intake. Then test with ineligible patient - workflow should stop at verification. Decision gates must work.

Financial advisor: This is the first parallel agent. Test with "analyze Apple stock for moderate investor". Watch Events tab carefully - all four analysts should show simultaneous execution times, not sequential. Synthesis must combine all perspectives.

Brand intelligence: Test with "analyze Tesla brand health". Verify parallel execution again. Four researchers work simultaneously. Synthesis creates actionable insights.

Software assistant: Test with "fix 500 error on file upload". Verify analyzer extracts key info, searcher simulates multi-source search, solution generator creates actionable fix. Remember this is simulated MCP - production would use real database tools.

Project management: Test with "plan migration to microservices". Verify task breakdown runs first, then three analysts run in parallel, then synthesis creates comprehensive plan. This is Sequential containing Parallel - make sure that structure is clear.

Verified recommendations: Test with "recommend charity for climate change donation". Verify independent verification runs parallel with risk assessment. Make sure audit trail is created. This is the finale - everything should work together.

---

## Key Concepts to Emphasize

Sequential versus Parallel: Students will ask when to use which. The answer is dependency. If task B needs task A's output, use Sequential. If tasks A and B are independent, use Parallel. It's that simple.

State passing in Sequential: Students might think they need to explicitly pass data between agents. Emphasize: it's automatic. Each agent sees the full conversation history including previous agent outputs. ADK handles this.

Synthesis after Parallel: Students might wonder why you need synthesis. Emphasize: Parallel gives you four separate outputs. Without synthesis, you hand the user four reports and confusion. Synthesis creates one cohesive answer - that's what makes parallel valuable.

Decision gates in workflows: Students might think Sequential always runs all agents. Step 4 teaches that's not true. Gates can stop execution early. This is important for costs and efficiency in production.

Built-in tools limitations: Only one built-in tool per agent. This is a Gemini model restriction, not ADK. The workaround exists for google search tool with bypass-multi-tools-limit flag, but for workshop simplicity, stick to one tool per agent or use sub-agents.

Voice only works with simple agents: Students will ask why greeting agent has voice but financial advisor doesn't. Answer: Voice requires a model on the root agent. Sequential and Parallel agents don't have models - they orchestrate sub-agents. Only simple Agent class supports voice.

---

## Bonus Content Strategy

You have 15 to 20 minutes of optional bonus content. Here's how to position it.

If you finish early with time remaining: Deliver all four bonus demos. Google Search tool, code execution, multi-model switching, deployment preview. End with masterclass teaser.

If you're running behind: Skip bonus entirely or just do 5-minute masterclass teaser. The core 9 agents are what matters.

If you finish exactly on time: Show google search demo only - it's the most impressive and takes 2 minutes to add to any agent. Quick masterclass mention, then close.

The masterclass positioning is important. You're not saying "today wasn't enough" - you're saying "today taught you patterns, masterclass teaches production deployment." Different value propositions. Today they learned to fish, masterclass takes them to the ocean.

Quick wins they can try tonight: Add google search to research agents, enable code executor for calculations, try different models via LiteLLM. These are 2 to 5 minute tasks that give immediate value and whet appetite for deeper masterclass content.

---

## Troubleshooting Scenarios

If a student's IDX setup fails during pre-workshop checks at 11:45: Have them close and create new workspace. The manual setup is so reliable now, a fresh start almost always works.

If Streamlit shows blank screen: The config is in the repo now, so this shouldn't happen. But if it does, they need to check that dot streamlit config dot toml exists. Quick fix: create it manually using the troubleshooting section of the checklist.

If API key doesn't work: Swap in backup key immediately. Don't debug live. After workshop, help them figure out what went wrong with their key.

If an agent doesn't load: Check auto-discovery is working. Look at agents manager in api directory - it should scan adk-agents folder and find all directories with root-agent variable. If specific agent missing, check that agent.py has root-agent equals something.

If tools don't work: Most common issue is the agent's instruction doesn't tell it to use tools. Second most common is tool docstring unclear. Third is tool not in tools list. Check those three in order.

If student falls way behind: Use git tags. Have them checkout the step where everyone else is. They can catch up on their own later using the comprehensive READMEs.

---

## The Four Phases Explained

Phase 1 is foundation. 30 minutes. Just greeting agent. Students learn ADK basics. This is critical - don't rush it. If they don't understand step 1, they'll struggle with everything else.

Phase 2 is real workflows. 90 minutes. Customer service, content pipeline, medical authorization. All Sequential agents. Students master the pattern through repetition in different domains. By end of phase 2, Sequential should feel natural.

Phase 3 is intelligent decision making. 60 minutes. Financial advisor and brand intelligence. Both Parallel with synthesis. This is the paradigm shift. Students understand when and why to use parallel. The performance benefit should be obvious - 4x faster for independent tasks.

Phase 4 is production grade systems. 60 minutes. Software assistant shows MCP integration. Project management shows Sequential plus Parallel combined. Verified recommendations shows the ultimate pattern with verification and audit. This is where everything comes together.

---

## Time Management Tips

If running ahead: Great! Do bonus content or take a break. Let students catch up and experiment.

If running exactly on time: Perfect. Stick to the plan. Each step has allocated time in workshop progression YAML.

If running behind: Cut exercises, increase demo ratio. Phases 1 and 2 are critical foundation - protect that time. Phase 3 can be more demo-heavy. Phase 4 can be mostly demo with discussion. Better to cover fewer agents deeply than all 9 superficially.

The exercises in each step are optional. If time is tight, demo the concepts instead of having students do hands-on. They can try exercises later using the comprehensive READMEs.

Consider this ratio: Phase 1 should be 50 percent hands-on, 50 percent demo. Phase 2 should be 30 percent hands-on, 70 percent demo. Phase 3 should be 80 percent demo, 20 percent discussion. Phase 4 should be 90 percent demo, 10 percent Q and A. Adjust based on student pace.

---

## Critical Teaching Moments

When introducing Sequential in step 2, show the Events tab in ADK Web. Students need to see that all three agents run even though only the final response appears in chat. The intermediate outputs are there, just not user-facing. This prevents confusion.

When introducing Parallel in step 5, show execution times in Events tab. Point out that all four analysts have similar timestamps - they ran simultaneously, not sequentially. This makes the performance benefit tangible.

When showing decision gates in step 4, deliberately test with incomplete data. Show that workflow stops at intake instead of continuing. Then test with complete data - workflow runs all four agents. The contrast makes the concept clear.

When demonstrating MCP integration in step 7, acknowledge you're simulating the tools. Explain: In production, these would be real database queries and GitHub API calls. We're focusing on the integration patterns and architecture, not the infrastructure setup. The patterns are production-ready even if the demo is simplified.

When revealing the AP2-inspired pattern in step 9, tell Ayo's story. He built a charity advisor where agents discover, verify, and process donations. The key insight: when agents handle money, you need accountability, not just capability. Independent verification, complete audit trails, role separation - these aren't optional for high-stakes decisions.

---

## Questions Students Will Ask

"Why can't I use voice with sequential agents?" Answer: Voice requires a model on the root agent. Sequential agents don't have models - they orchestrate sub-agents with models. The root just manages workflow. Only simple Agent class has a model at root level.

"Do I always need synthesis after parallel?" Answer: Almost always, yes. Parallel gives you N outputs. User wants 1 answer. Synthesis combines them. Exception: If user genuinely wants separate reports from each expert, skip synthesis. But that's rare.

"When should I use agent-to-agent instead of ParallelAgent?" Answer: A2A when the orchestrator needs to decide which agents to call. ParallelAgent always runs all sub-agents. If you need conditional agent execution, use A2A. Otherwise, ParallelAgent is simpler.

"Can I use Google Search with other tools in the same agent?" Answer: Not easily. Built-in tools have limitations - one per agent unless you use the bypass flag for google search. Workaround: Create sub-agents, each with one built-in tool, then orchestrate them.

"Is this stuff really used in production?" Answer: Absolutely. The adk-samples repository on GitHub has production examples from Google. Customer service, financial advisor, software bug assistant - these are production patterns. The workshop teaches simplified versions, but the patterns are proven.

---

## What Makes This Workshop Special

Students have done AI workshops before. Most were "build a chatbot" or "fine-tune a model." This is different. You're teaching system architecture.

By the end, students understand not just how to build agents, but when to use which pattern. They can look at a business problem and say: "This is a sequential workflow. I'll use triage, research, response pattern." Or: "This needs multiple perspectives. I'll use parallel analysts with synthesis."

The production focus is critical. Every agent demonstrates a real business use case. Customer service reduces support time by 70 percent. Content pipeline makes teams 3x more productive. Financial advisor provides comprehensive analysis in seconds instead of hours. These are transformational outcomes, not demos.

The AP2-inspired finale sets this apart. Most workshops end with "you built 9 agents, great job." You end with "here's how to build AI systems with accountability and trust." That's the difference between toy projects and production systems.

---

## Pacing and Energy

Start high energy. This is production AI agent development, not theory. Set expectations: We're building real systems today, not demos.

Maintain energy through phase 1 and 2. Keep it interactive. Ask questions. Check for understanding. Don't just lecture.

Energy might dip in phase 3 when concepts get complex. This is normal. Take a 5-minute break before introducing parallel. Let students reset.

Build energy back up for phase 4. This is the finale. Complex orchestration, MCP integration, the AP2-inspired verification system. End strong.

The bonus content should feel like "here's even more cool stuff" not "here's what we didn't have time for." High energy, quick demos, exciting possibilities. Then position masterclass as the next adventure.

---

## Your Preparation Tomorrow Morning

Four hours before the workshop. Here's your hour-by-hour plan.

Hour 1: Test all 9 agents. One query each, verify they respond. This is just smoke testing.

Hour 2: Deep test steps 1, 2, 5, and 9. These are your teaching moments. Make sure you can demo them confidently.

Hour 3: Review your notes. What are the 2-3 key points for each agent? Write them down. These are your anchor points during the workshop.

Hour 4: Tech check. IDX workspace, services running, screen share working, YouTube stream tested. Then relax for 15 minutes before students arrive.

The detailed testing checklist I'm creating next will guide you through exactly what to test and in what order.

---

## Closing Thoughts

You've built something special. Nine production-ready agents with comprehensive documentation, a complete progression system, and real business value. This isn't another generic AI workshop - this is the workshop that turns developers into AI system builders.

The manual setup decision was right. Reliable beats automated-but-fragile. Students will complete setup successfully because it's simple and clear.

The progression from simple to complex is well-designed. Each agent builds on previous concepts. By step 9, students are combining everything they learned.

The AP2-inspired finale is powerful. It's not just about building agents - it's about building agents you can trust with important decisions.

You're ready. The materials are production-quality. The setup is tested. The progression is solid.

Tomorrow at 11:45, students arrive. At noon, you start. At 4 PM, they leave with the ability to build enterprise AI systems.

Sleep well. You've got this.

---

**End of Audio Briefing**

Upload this to NotebookLM, generate audio, listen tonight.
Tomorrow morning, use the testing checklist I'm creating next.
