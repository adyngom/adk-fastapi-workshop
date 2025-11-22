# Module 9: Cloud Deployment & Operations - Recording Script

**Duration:** 120 min
**Prep Required:** Deployment configs (2 hours)
**Energy:** HIGH (finale!)
**Focus:** LIVE production deployment

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 9 - the final module.

We've built 9 different agent patterns. Today we're deploying them to production. And I'm going to do it live - we're actually going to deploy an agent to Google Cloud Run right now and watch it handle real production traffic.

By the end, you'll know how to containerize agents, deploy to Cloud, set up monitoring, and implement CI/CD pipelines.

This is the finale. Let's deploy this thing!"

---

## 🎬 DOCKER CONTAINERIZATION (30 min)

**SAY:**
"Okay, so first step: Docker. We need to package our agent into a container.

[Show Dockerfile from workshop]

Let me walk you through this Dockerfile:

[Explain multi-stage build with narration]

This is a multi-stage build - very important for production. Stage 1 installs dependencies, Stage 2 copies only what's needed. Result: Smaller image, faster deployments.

[Build Docker image live]

[Type: docker build -t customer-service .]

[Show build process]

There you go. Image built. Now let's test it locally:

[Type: docker run -p 8000:8000 customer-service]

[Test the agent]

Perfect - works in Docker. Now let's deploy to Cloud Run."

---

## 🎬 CLOUD RUN DEPLOYMENT (35 min) - LIVE!

**SAY:**
"All right, so this is it - we're deploying to Google Cloud Run for real.

[Show deployment script]

This script:
1. Builds the container
2. Pushes to Google Container Registry
3. Deploys to Cloud Run

Let me run it:

[Type: ./deploy.sh]

Okay, it's building the container... this takes about 2 minutes...

[Wait, show progress]

Pushing to registry... deploying to Cloud Run...

[Wait for deployment]

There you go! You see that URL? That's your agent LIVE in production!

[Copy the Cloud Run URL]

Let's test it:

[Open URL in browser]

[Send query to the live agent]

[Agent responds]

And like that, we are live! Your agent is handling real production traffic on Google Cloud.

[Pause for effect]

This is production AI. Not localhost. Not demos. Real production deployment.

Perfect. Now let me show you monitoring."

---

## 🎬 MONITORING & OBSERVABILITY (25 min)

**SAY:**
"Okay, so in production, you need to know what your agents are doing. Let me show you Cloud Logging and Monitoring.

[Open Google Cloud Console]

[Navigate to Cloud Logging]

Here you can see every request to your agent. Every tool call. Every error.

[Show live logs from the agent we just deployed]

You see that? Real-time logs. Very powerful for debugging.

[Navigate to Cloud Monitoring]

Here you can create dashboards - request counts, latency, error rates, cost tracking.

[Show example dashboard]

For production, monitoring is not optional. You need to know when things break."

---

## 🎬 COST OPTIMIZATION (15 min)

**SAY:**
"Real quick - cost optimization. Production agents can get expensive. Here's how to control costs:

**1. Model selection:** Use Flash for simple tasks ($0.10/M tokens), Pro for complex ($5/M tokens)
**2. Semantic caching:** Repeat queries are 90% cheaper
**3. Token limits:** Set max_output_tokens
**4. Apigee AI Gateway:** Enterprise governance with rate limiting

[Show quick examples of each]

These strategies can reduce costs 70-90%. Very important at scale."

---

## 🎬 CI/CD PIPELINE (10 min)

**SAY:**
"Last thing: CI/CD. Automate your deployments with GitHub Actions.

[Show .github/workflows/deploy.yml]

Every push to main triggers:
1. Run tests
2. Build container
3. Deploy to Cloud Run

[Show the workflow file]

Set it up once, deployments are automatic. Perfect."

---

## 🎬 COURSE COMPLETE! (10 min)

**[Show slide: What You've Learned]**

**SAY:**
"Okay, so that's Module 9. And that's the entire course!

Let's recap what you've built:

**Module 1:** Understood the AI agent landscape
**Module 2:** Mastered Python for production agents
**Module 3:** Built your first single agent
**Module 4:** Built Sequential workflows for business processes
**Module 5:** Built Parallel execution for 4x speed
**Module 6:** Added memory and RAG for knowledge retention
**Module 7:** Integrated production tools for real-time data
**Module 8:** Combined patterns with verification and audit
**Module 9:** Deployed to production with monitoring

You went from beginner to building enterprise AI agent systems.

These aren't demos. These are production patterns. You can deploy these to your company today.

[Pause]

That's all I have for you in this course. Thank you for learning with me. Now go build amazing AI systems.

And please don't forget to subscribe and share this course if you found it valuable.

See you next time. Take care!"

**[Fade out]**

---

## 📝 FINALE NOTES

**Energy:** Start moderate, build to high for live deployment
**Key Moment:** The live Cloud Run deployment URL working
**Emotion:** Pride in what students accomplished
**Closing:** Warm, encouraging, actionable
