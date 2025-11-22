# Module 6: Memory & Context Management - Recording Script

**Duration:** 120 min
**Prep Required:** ChromaDB examples (2-3 hours before recording)

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 6. Okay, so today we're making agents that remember.

Up until now, our agents forget everything after the conversation ends. Today we're adding memory - both short-term session memory and long-term semantic memory with vector databases.

By the end, you'll have agents that remember past conversations and can search through thousands of documents instantly. Let's build this!"

---

## 🎬 OVERVIEW

**SAY:**
"All right, here's what we're covering: Session memory with Redis - this is what the workshop used. Then long-term memory with ChromaDB - vector databases for semantic search. Then RAG - Retrieval-Augmented Generation, the pattern for giving agents access to your company's knowledge. And finally, context management - token limits and what to remember vs forget. This is production-grade memory. Let's start with session memory."

---

## 🎬 SESSION MEMORY WITH REDIS (25 min)

**[Show code from workshop]**

**SAY:**
"So let me show you session memory. The workshop already uses Redis for this. Redis stores conversation history - what the user said, what the agent said, tool calls, everything.

[Demo Redis session management from workshop code]

This is short-term memory. It lasts for the session. When the session ends, memory is gone (unless you persist it - we'll cover that).

Perfect for: Conversations that last minutes to hours.
Not good for: Remembering things across days or searching thousands of documents.

That's where vector databases come in. Let me show you."

---

## 🎬 VECTOR DATABASES (40 min)

**[Show ChromaDB setup]**

**SAY:**
"Okay, so vector databases. This is how you give agents long-term semantic memory.

The concept: Instead of exact text matching, vector databases do semantic search. 'Login problem' matches 'authentication failure' even though words are different.

Let me show you how to set this up with ChromaDB:

[Create customer_service_with_memory example]

[Live coding with full narration - installing ChromaDB, creating collection, storing documents, querying]

[Demo semantic search - query for 'login issue', finds 'authentication problem']

There you go - it found relevant past tickets even though the words are different. This is semantic search.

For production customer service, this is huge. Every ticket you solve gets stored. Future similar tickets are resolved instantly using past solutions.

Perfect. Now let's build a RAG pipeline."

---

## 🎬 RAG DEEP DIVE (30 min)

**SAY:**
"RAG - Retrieval-Augmented Generation. This is the pattern for giving agents access to your documents.

The flow: Query → Retrieve relevant docs → Generate answer using those docs.

[Build rag_pipeline example with narration]

[Demo: Ingest ADK documentation, query 'How do I build Sequential agent?', agent retrieves relevant docs and answers]

And like that, the agent can answer questions about your company docs, policies, technical documentation - anything you feed it.

This is production AI - agents with your company's knowledge."

---

## 🎬 EXERCISE, SOLUTION, RECAP (25 min)

**Exercise:** Add ChromaDB to customer_service (stores past tickets)
**Solution:** Complete walkthrough
**Recap:** Memory types, when to use each, RAG for knowledge access

**SAY closing:**
"In Module 7, we're fixing the $175 stock price problem with production tools. This is going to be fun. See you there!"

---
