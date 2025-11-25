# Concept #1: Pattern Matching (Regular Expressions)

**Recording Template - Your Regex Story**
**Duration:** 8 minutes video + 1000-word post
**Hook:** "The $3.75 transcript formatting mistake"

---

## 🎬 VIDEO RECORDING SCRIPT (8 minutes)

### SEGMENT 1: HOOK (0:00-0:45)

**[Screen recording: Show ChatGPT with huge transcript pasted]**

**SAY:**
"So I had a problem. I had this 3-hour YouTube transcript - 50,000 words - and it needed formatting as markdown.

My first instinct? Paste the whole thing into ChatGPT and ask it to format it properly.

[Show ChatGPT processing]

Big mistake.

First problem: ChatGPT started adding code examples that weren't in the original transcript. It was hallucinating content.

Second problem: Look at the cost. 50,000 input tokens - that's about a dollar fifty. Plus 75,000 output tokens - another two twenty-five. Total: $3.75.

For formatting. A transcript.

And it was wrong.

[Pause]

So I took a step back and actually looked at the transcript.

[Show raw transcript]

And I saw this pattern..."

---

### SEGMENT 2: THE AHA MOMENT (0:45-1:30)

**[Show raw transcript snippet]**

**SAY:**
"Here's what the transcript actually looked like:

```
[00:15:42] The first thing you need to know...
[00:16:03] And then after that...
[00:17:21] This is very important...
```

You see that pattern? Every line starts with a timestamp in brackets.

I didn't need AI to 'figure out' the formatting. The pattern was obvious. I just needed to find all the timestamps and convert them to markdown headers.

So instead of ChatGPT, I used a simple find-and-replace pattern. It's called a regular expression, or regex.

Let me show you what I did..."

---

### SEGMENT 3: THE SOLUTION (1:30-4:00)

**[Screen recording: Text editor with regex]**

**SAY:**
"Okay, so here's the regex pattern I used:

```
Find: \[(.*?)\]
Replace with: ## $1
```

That's it. One line.

What this says in plain English:
- Find anything inside square brackets
- Replace it with markdown header (##) plus what was inside the brackets

Let me run this...

[Show find-and-replace dialog]
[Run it]
[Show transformed text]

There you go. All timestamps are now markdown headers. Perfect formatting. 30 seconds. Cost: $0.

And it's EXACT. No hallucinations. No added content. Just the transformation I wanted.

This is the power of pattern matching."

---

### SEGMENT 4: WHEN TO USE IT (4:00-5:30)

**[Show slide: Code vs ChatGPT Decision]**

**SAY:**
"So when should you use pattern matching instead of AI?

✅ **Use pattern matching when:**
- You have a predictable repeated structure
- You need exact, consistent results
- You're processing multiple items with the same pattern
- The pattern is obvious to you when you look at it

Examples:
- Extracting all email addresses from text
- Converting timestamps to different formats
- Cleaning up phone numbers
- Removing HTML tags
- Finding all URLs

❌ **Don't use pattern matching when:**
- The content needs interpretation
- Patterns vary significantly
- Context changes the meaning
- You actually need reasoning

Example where AI is better: 'Summarize these customer reviews' - that needs understanding, not just pattern matching.

The key question: Is this a pattern or is this understanding?

If it's a pattern, use regex. If it's understanding, use AI.

All right, now let me show you how to actually do this..."

---

### SEGMENT 5: TRY IT YOURSELF (5:30-7:30)

**[Browser-based demo - regex101.com or similar]**

**SAY:**
"Let's try a practical example together. You can do this right now in your browser.

Go to regex101.com - it's a free tool.

Here's the scenario: You have a list of emails that look like this:

```
Contact: john@example.com for sales inquiries
Reach out to jane@example.com for support
Email: bob@example.com for questions
```

You want to extract just the email addresses. Here's the regex pattern:

```
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

Let me break this down...
[Explain each part]

Now paste your text and watch...
[Show emails being highlighted/extracted]

There you go! Three email addresses extracted. No ChatGPT needed.

Compare this to the AI approach:
[Show ChatGPT doing the same thing]
- Cost: ~$0.10-0.15 per request
- Inconsistent (might format differently each time)
- Slower (API roundtrip)

vs regex:
- Cost: $0
- Exact every time
- Instant

When you have a clear pattern, regex beats AI every time."

---

### SEGMENT 6: RECAP & NEXT (7:30-8:00)

**[Back to you on camera or voiceover]**

**SAY:**
"Okay, so that's Concept #1 - Pattern Matching with Regular Expressions.

The key takeaway: Before asking ChatGPT to process text, look for patterns. If you see a repeated structure, regex is faster, cheaper, and more accurate than AI.

This saved me $3.75 on that transcript. But more importantly, it's EXACT. No hallucinations. No surprises.

Next week: Concept #2 - Find and Replace Patterns. We're going to look at template systems and how to personalize 200 emails in 10 seconds instead of asking ChatGPT 200 times.

That's all for Concept #1. Try the exercise at the link below. See you next week!"

**[End screen with links]**

---

## 📝 WRITTEN POST VERSION (1000 words)

### Title: "I Wasted $3.75 Asking ChatGPT to Format a Transcript"

**THE STORY (Opening):**

I had a problem that seemed perfect for AI.

A 3-hour YouTube transcript needed formatting as markdown. 50,000 words of raw text with timestamps like `[00:15:42]` that needed to become proper headers.

My solution? Paste it all into ChatGPT with the prompt: "Format this transcript as markdown."

Cost: $3.75 in API tokens (50k input + 75k output)
Time: 3 minutes
Result: Wrong

ChatGPT decided to add code examples that weren't in the transcript. It hallucinated content. And the formatting was inconsistent.

So I took a step back and actually LOOKED at the transcript...

**THE AHA MOMENT:**

The pattern was obvious:
```
[00:15:42] Some text
[00:16:03] More text
[00:17:21] Even more text
```

Every line: `[timestamp] content`

I didn't need AI to figure this out. I needed find-and-replace.

One regex pattern:
- Find: `\[(.*?)\]`
- Replace: `## $1`

30 seconds. $0. Perfect formatting.

**WHAT PATTERN MATCHING IS:**

Pattern matching (regular expressions, or "regex") finds repeated structures in text.

Think of it like this:
- Find-and-replace on steroids
- Describe the pattern once
- Apply it thousands of times
- Exact results every time

Common patterns:
- Email addresses: `word@word.word`
- Phone numbers: `(123) 456-7890`
- Timestamps: `[00:15:42]`
- URLs: `https://word.word`

Once you see the pattern, regex extracts or transforms it.

**WHEN TO USE IT INSTEAD OF AI:**

✅ **Use regex when:**
1. You have predictable repeated structure
2. You need exact, consistent results
3. You're processing multiple items
4. The pattern is obvious when you look at it

Examples where regex wins:
- Extract all email addresses from 100 documents
- Convert 500 timestamps to different formats
- Clean up messy phone number formatting
- Remove HTML tags from text
- Find all mentions of a product name

❌ **Don't use regex when:**
1. Content needs interpretation
2. Patterns vary significantly
3. Context changes meaning
4. You genuinely need reasoning

Example where AI wins:
"Summarize these 50 customer reviews" - that needs understanding context, not just pattern matching.

**THE DECISION:**

Ask yourself: "Is this a PATTERN or is this UNDERSTANDING?"

Pattern = Regex (exact, fast, free)
Understanding = AI (approximate, slower, costs tokens)

**TRY IT YOURSELF:**

[Embedded CodePen or link to regex101.com]

Exercise: Extract emails from this text:
```
Contact sales at john@company.com
Support: help@company.com
Questions? reach out to info@company.com
```

Regex pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`

Try it. See the emails highlighted instantly.

Compare to ChatGPT:
- Your approach: $0, instant, exact
- ChatGPT approach: $0.10, 2 seconds, might vary

**THE TRANSCRIPT BREAKDOWN:**

My original problem:
- 50,000 words
- ~800 timestamp lines
- Needed: Each timestamp as a header

ChatGPT approach:
- Cost: $3.75
- Time: 3 minutes
- Result: Added unwanted content
- Accuracy: 85% (hallucinations)

Regex approach:
- Cost: $0
- Time: 30 seconds
- Result: Exact transformation
- Accuracy: 100%

**Savings: $3.75 + 2.5 minutes + peace of mind**

**LEVEL UP:**

Once you understand regex, it opens up:

→ Concept #2: Find and Replace Patterns
→ Concept #9: Template Systems
→ Concept #23: Filtering Data
→ Concept #47: APIs and Endpoints

And here's the powerful combination:

1. **Use regex** to extract clean data (emails, names, timestamps)
2. **Use AI** to make it meaningful (personalize messages, categorize, analyze)

Regex gets data CLEAN. AI makes it SMART.

Example:
```
Step 1 (Regex): Extract 500 customer emails from messy text
Step 2 (AI): Generate personalized outreach for each

Cost: $0 for extraction + $20 for AI = $20 total
vs ChatGPT for both: $50+ and still might miss emails
```

**NEXT WEEK:**

Concept #2: Find and Replace Patterns - How to personalize 200 emails in 10 seconds instead of asking ChatGPT 200 times.

---

**YOUR TURN:**

Take a messy text file you have. Look for patterns. Try extracting them with regex.

When you find a pattern ChatGPT was costing you money to handle, share it in the comments!

**RESOURCES:**

- regex101.com (interactive regex tester)
- regexr.com (visual regex builder)
- Your regex cheat sheet (PDF download)

**JOIN THE COMMUNITY:**

Can't wait 50 weeks for all concepts? Get immediate access to all 50 in the [Skool community link].

Plus: Weekly office hours, exercises with solutions, and the complete ADK course for Pro members.

---

**That's Concept #1. See you next Saturday!**

Ady Ngom
[LinkedIn] | [YouTube] | [Skool Community]

---

## 📊 TEMPLATE COMPONENTS

**This template includes:**

✅ **Video script** (8 minutes, your voice)
✅ **Written post** (1000 words, newsletter format)
✅ **Exercise** (browser-based, interactive)
✅ **Hook** (personal story with cost comparison)
✅ **When to use** (decision framework)
✅ **Level up** (connects to other concepts)
✅ **CTA** (Skool community, next concept)

**Replicable for all 50 concepts!**

**Production time per concept:** 3-4 hours
- Video: 1 hour recording
- Written: 1 hour writing
- Exercise: 1 hour creating
- Editing: 30-60 min

**By Dec 31:** 10 concepts ready = 30-40 hours work
**Realistic:** 2 concepts/day in Week 3-4 = achievable!

---

**This is the template. Use for Concepts 2-10!** 🚀
