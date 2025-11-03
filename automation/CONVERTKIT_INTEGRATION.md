# 🚀 ConvertKit (Kit) Integration Guide

> **Context**: 25 RSVPs in 5 minutes for deep dive! Now let's automate the entire funnel.

---

## 🎯 ConvertKit Setup for Workshop Funnel

### Your Advantage

ConvertKit is **perfect** for your use case:
- ✅ Landing pages built-in
- ✅ Email sequences automated
- ✅ Tag-based segmentation
- ✅ Webhook support (GitHub automation)
- ✅ Visual automation builder

---

## 📋 ConvertKit Structure

### Tags to Create

```
workshop_registered       # Applied on signup
workshop_github_provided  # Has GitHub username
workshop_access_granted   # Added as collaborator
workshop_attended        # Showed up
workshop_completed       # Used repo post-workshop
masterclass_interested   # Clicked Masterclass links
masterclass_enrolled     # Converted! 🎉
```

### Forms to Create

#### 1. Workshop Registration Form

**URL**: kit.com/your-username/adk-workshop-registration

**Fields**:
- Name (required)
- Email (required)
- GitHub Username (required - custom field)
- Company (optional - custom field)
- Role (optional - dropdown custom field)

**Success action**:
- Tag: `workshop_registered`
- Redirect: Thank you page
- Trigger: Email Sequence 1

**Custom CSS** to match your brand:
```css
/* Your 99 Agents brand colors */
```

#### 2. Masterclass Interest Form

**Embedded in** Email 5, Email 6
**Minimal**: Just "Yes, I'm interested" button
**Action**: Tag `masterclass_interested` → Sales sequence

---

## 🔄 Automated Sequences in ConvertKit

### Sequence 1: Pre-Workshop (Starts at registration)

**Email 1**: Immediate - Registration confirmation
- Subject: "✅ You're in! ADK Workshop confirmed"
- Tags applied: `workshop_registered`
- CTA: Join community

**Email 2**: Day 2 - Pre-workshop checklist
- Subject: "🚀 Workshop Prep - 3 Steps (10 min)"
- **Include**: GitHub username collection (if missing)
- **If username provided**: Tag `workshop_github_provided`

**Delay**: 2 days OR T-48 hours (whichever comes first)

**Email 3**: Day before workshop
- Subject: "🎉 Your ADK Workshop Access is Ready!"
- **Conditional**: Only send if tagged `workshop_access_granted`
- Include: "Open in IDX" link

---

### Sequence 2: Post-Workshop (Starts after workshop)

**Email 4**: 2 hours after - Thank you + Masterclass intro
- Subject: "🎉 Thank You + Your Next Steps"
- Include: Survey, resources, Masterclass soft intro
- CTA: "Learn about Masterclass" → tags `masterclass_interested`

**Email 5**: Day 2 - Value reminder
- Subject: "🎓 Your Workshop Materials + Special Offer"
- Showcase Masterclass
- 20% discount code
- **Hard CTA**: Enroll now

**Email 6**: Day 5 - Urgency (access expiring soon)
- Subject: "⏰ Access Expires in 48 Hours"
- Urgency: Access removal + discount expiration
- **Final push**: Enroll or fork

**Email 7**: Day 8 - Final touchpoint
- Subject: "Thanks for Exploring ADK"
- Soft sell: Masterclass still available
- Nurture: Stay connected, next workshop

---

### Sequence 3: Masterclass Nurture (For non-converters)

**For those tagged** `masterclass_interested` but not `masterclass_enrolled`:

**Week 2**: Success stories
**Week 3**: Curriculum deep dive
**Week 4**: Limited-time offer
**Month 2**: Next workshop announcement
**Month 3**: Case study / testimonial

---

## 🔗 Webhook Automation (ConvertKit → GitHub)

### Setup Webhooks in ConvertKit

**Navigate to**: Settings → Webhooks → Create Webhook

**Trigger**: Form submitted (Workshop Registration)
**Endpoint**: Your automation server URL
**Payload**: Sends subscriber data

### Option A: Zapier Integration (Easiest)

**Zapier Flow**:
```
ConvertKit: New Subscriber (workshop_registered tag)
    ↓
Filter: Has github_username field
    ↓
Webhook: POST to add_collaborators API
    ↓
ConvertKit: Add tag (workshop_access_granted)
    ↓
Email: Send Email 3 (access confirmation)
```

**Setup time**: 30 minutes
**Cost**: Zapier Pro ($20/month)

### Option B: Make.com Integration (More powerful)

**Scenario**:
```
1. Watch ConvertKit for new workshop_registered
2. Wait 24 hours
3. Call GitHub API (add collaborator)
4. If success:
   - Tag: workshop_access_granted
   - Trigger Email 3
5. If failure:
   - Tag: workshop_access_failed
   - Send support email
```

**Setup time**: 1 hour
**Cost**: Make Pro ($9/month)

### Option C: Custom Webhook Server (Full control)

**Host simple Flask/FastAPI server**:

```python
# webhook_server.py
from fastapi import FastAPI, Request
from add_collaborators import CollaboratorManager

app = FastAPI()

@app.post("/webhook/convertkit")
async def handle_registration(request: Request):
    data = await request.json()

    # Extract info
    email = data['email']
    name = data['first_name']
    github_username = data['custom_fields']['github_username']

    # Add as collaborator
    manager = CollaboratorManager("adyngom", "adk-fastapi-workshop", TOKEN)
    result = manager.add_collaborator(github_username)

    if result['success']:
        # Tag in ConvertKit
        tag_subscriber(email, 'workshop_access_granted')
        # Trigger Email 3
        send_email_3(email, name)

    return {"status": "success"}
```

**Host on**: Cloud Run, Vercel, Railway
**Cost**: Free tier sufficient

---

## 📊 ConvertKit Custom Fields

### Required Custom Fields

Create in ConvertKit Settings → Custom Fields:

1. **github_username** (text)
   - Used for: Collaborator addition
   - Required: Yes

2. **company** (text)
   - Used for: Segmentation, B2B targeting
   - Required: No

3. **role** (text)
   - Used for: Content personalization
   - Required: No

4. **experience_level** (text)
   - Used for: Follow-up personalization
   - Required: No

5. **workshop_date** (date)
   - Used for: Timing sequences
   - Auto-filled: Yes

6. **attended** (boolean)
   - Used for: Segmentation
   - Updated: Post-workshop (manual or via webhook)

---

## 🎨 Landing Page Strategy (in Kit)

### Landing Page 1: Workshop Registration

**URL**: kit.com/your-page/adk-workshop

**Sections**:
1. **Hero**: "Build Production AI Agents in 2 Hours"
2. **Problem**: "Most AI tutorials are toy examples..."
3. **Solution**: "This workshop shows real production patterns"
4. **What You'll Build**: 3 agents, 3 patterns
5. **Unique Value**: "Only workshop showing ADK + FastAPI"
6. **Social Proof**: "25 seats filled in 5 minutes!"
7. **CTA**: Registration form
8. **FAQ**: Common questions
9. **Instructor Bio**: Your credibility
10. **Teaser**: "Preview of 99 Agents Masterclass"

### Landing Page 2: Masterclass Enrollment

**URL**: kit.com/your-page/99-agents-masterclass

**Targeted to**: Workshop attendees (special discount)

**Sections**:
1. **Hero**: "From Workshop to Mastery"
2. **What You Learned**: Recap workshop (3 agents, 3 patterns)
3. **What's Next**: 99 agents, production deployment, etc.
4. **Workshop Attendee Bonus**: 20% off, exclusive access
5. **Testimonials**: From previous workshops
6. **Curriculum**: Detailed breakdown
7. **CTA**: Enroll now (discount code auto-applied)

---

## 🎯 Automation Workflows in ConvertKit

### Workflow 1: Workshop Funnel

```
Form Submit (Workshop Reg)
    ↓
Tag: workshop_registered
    ↓
Email 1: Confirmation (immediate)
    ↓
Wait: Until T-48 hours
    ↓
Email 2: Pre-workshop checklist
    ↓
If: github_username provided
    ↓
Tag: workshop_github_provided
    ↓
External: Add as collaborator (Zapier)
    ↓
Tag: workshop_access_granted
    ↓
Email 3: Access ready (T-24h)
    ↓
Email 4: Day-of reminder (T-2h)
    ↓
[Workshop happens]
    ↓
Tag: workshop_attended (manual or webhook)
    ↓
Email 5: Thank you + Masterclass intro (T+2h)
    ↓
Wait: 2 days
    ↓
Email 6: Urgency (T+6d)
    ↓
Wait: 2 days
    ↓
Email 7: Final touchpoint (T+8d)
```

### Workflow 2: Masterclass Conversion

```
If: Clicked Masterclass link in Email 5, 6, or 7
    ↓
Tag: masterclass_interested
    ↓
Email: Masterclass details + benefits
    ↓
Wait: 3 days
    ↓
Email: Success stories
    ↓
Wait: 4 days
    ↓
If NOT enrolled:
    Email: Last chance (discount expiring)
    ↓
If STILL not enrolled:
    Move to: Long-term nurture sequence
```

---

## 💰 Revenue Optimization

### Conversion Math

**100 workshop attendees**:
- Masterclass interest: 40% = 40 people
- Email sequence conversion: 10-15% = 10-15 enrollments
- Masterclass price: $397 (discounted from $497)
- **Revenue**: $3,970 - $5,955 per workshop

**Cost**:
- ConvertKit: $29/month
- Zapier/Make: $20/month
- Workshop delivery: 2 hours
- **Profit margin**: Excellent

### Upsells

**During Masterclass enrollment**:
1. One-time offer: Add private coaching ($200)
2. Payment plan: 3 months @ $149/month
3. Team license: 5 seats @ $1,500

---

## 📈 Metrics Dashboard (ConvertKit)

### Key Metrics to Monitor

**Funnel metrics**:
- Registration form conversion (landing page → submit)
- GitHub username collection rate (should be 95%+)
- Email open rates (target: 60%+ average)
- Click-through rates (target: 15%+ for CTAs)
- Workshop attendance (target: 70%+)

**Revenue metrics**:
- Masterclass click rate (Email 5: target 25%+)
- Enrollment conversion (target: 10-15%)
- Revenue per attendee (target: $40-60)
- LTV (if they stay in ecosystem)

### A/B Testing Ideas

**Test these**:
- Subject line variations
- Discount amounts (20% vs 25% vs $100 off)
- Urgency messaging (scarcity vs FOMO)
- CTA button text
- Email send timing

---

## 🎁 Workshop Attendee Incentives

### Immediate Value

**In Email 3** (access grant):
- Private repo access (exclusive!)
- "Open in IDX" one-click setup
- 3 working agent examples
- Git tags for self-paced learning

### Extended Value

**In Email 5** (post-workshop):
- 7 days to explore
- Survey → coffee gift card
- Community access (Discord/Slack)
- Office hours invite (1 time)

### Conversion Incentives

**Workshop → Masterclass**:
- 20% discount (time-limited)
- Early access to new content
- Priority support
- Exclusive community tier
- Certification path

---

## 🔗 Integration Checklist

### ConvertKit Setup

- [ ] Create custom fields (github_username, etc.)
- [ ] Create tags (all 7 from above)
- [ ] Create Form 1 (workshop registration)
- [ ] Create Form 2 (Masterclass interest)
- [ ] Build Sequence 1 (pre-workshop)
- [ ] Build Sequence 2 (post-workshop)
- [ ] Build Sequence 3 (Masterclass nurture)

### Automation Setup

- [ ] Set up Zapier/Make workflow
- [ ] Test GitHub collaborator addition
- [ ] Configure webhooks
- [ ] Test end-to-end flow with test account

### Testing

- [ ] Register with test account
- [ ] Receive all 7 emails
- [ ] GitHub access granted successfully
- [ ] IDX link works
- [ ] Masterclass links track clicks
- [ ] Conversion tags apply correctly

---

## 🚀 Quick Win: Your First Automated Workshop

### This Week

1. **Create ConvertKit form** (30 min)
   - Workshop registration
   - Include GitHub username field

2. **Set up Email 1-2** (30 min)
   - Registration confirmation
   - Pre-workshop checklist

3. **Manual collaborator addition** (15 min)
   - Export CSV from ConvertKit
   - Run add_collaborators.py
   - Send Email 3 manually

### Next Workshop

1. **Add Zapier integration** (1 hour)
   - Auto-add collaborators
   - Auto-tag in ConvertKit

2. **Complete email sequence** (2 hours)
   - Emails 3-7
   - Masterclass conversion messaging

3. **Landing page optimization** (1 hour)
   - A/B test headlines
   - Add social proof
   - Optimize for mobile

---

## 💡 Pro Tips for 99 Agents Funnel

### Positioning

**Workshop = Module 0** (free preview)
**Masterclass = Modules 1-99** (paid deep dive)

"You just experienced module 0. Ready for the other 99?"

### Pricing Psychology

**Anchor high**:
- Regular price: $497
- Workshop discount: $397 (20% off)
- Payment plan: $149/month × 3

**Urgency**:
- Discount expires: 7 days post-workshop
- Spots limited: "Only 20 seats at discounted rate"
- Bonuses expire: "Early enrollees get X"

### Social Proof

**In emails**:
- "25 people registered in 5 minutes!"
- "87% of workshop attendees rate it 5 stars"
- "Students go from beginner to deploying agents in weeks"

**Testimonials**:
- Real workshop feedback
- Before/after stories
- Career advancement examples

---

## 📊 Expected Funnel Performance

### With 100 Workshop Attendees

```
100 Registrations
  ↓ (95%)
95 Provide GitHub username
  ↓ (90%)
86 Access granted
  ↓ (70%)
60 Attend workshop
  ↓ (50%)
30 Use repo post-workshop
  ↓ (25%)
15 Click Masterclass links (Email 5)
  ↓ (60%)
9 Enroll in Masterclass
```

**Conversion rate**: 9% (workshop → Masterclass)
**Revenue**: $3,573 (9 × $397)

**With optimization**: 12-15% conversion = $4,764-$5,955

---

## 🎯 Your Deep Dive Follow-Up

### Immediate Actions

**Since you got 25 RSVPs already**:

1. **Export registrations from Kit** (now)
   - Download as CSV
   - Check for GitHub usernames

2. **Send follow-up email** (tomorrow)
   - Thank for registering
   - Ask for GitHub username (if missing)
   - Set expectations

3. **Plan access grant** (day before deep dive)
   - Run add_collaborators.py
   - Send access confirmation
   - Test with 2-3 early adopters

### For This Deep Dive

**Timeline**:
- Today: 25 registered
- Tomorrow: Send Email 2 (GitHub username collection)
- T-24h: Add collaborators, send Email 3
- Deep dive: Deliver content
- T+2h: Email 5 (Masterclass promotion)

**Goal**: Convert 2-4 to Masterclass (8-16% of 25)

---

## 🔧 Technical Integration

### ConvertKit → GitHub Automation

**Option 1: Zapier** (Recommended for now)

```
Trigger: Tag added (workshop_github_provided)
    ↓
Action 1: HTTP POST to your webhook server
    Body: {email, name, github_username}
    ↓
Your server: Runs add_collaborators.py
    ↓
Action 2: Tag subscriber (workshop_access_granted)
    ↓
Action 3: Send Email 3 (access ready)
```

**Option 2: ConvertKit API** (Full control)

```python
# In your add_collaborators.py success callback
import requests

def tag_in_convertkit(email, tag_name):
    CONVERTKIT_API_KEY = os.environ['CONVERTKIT_API_KEY']

    # Get subscriber
    # Add tag
    # Return success
```

---

## 📧 Email Copywriting for Maximum Conversion

### Email 5 (Key Conversion Email)

**Subject line A/B test**:
- A: "🎉 Thank You + Your Next Steps"
- B: "What's Next After Today's Workshop?"
- C: "Ready to Master All 99 Agent Patterns?"

**Opening** (build on workshop):
> "You just built 3 production agents in 2 hours.
> Imagine what you could build with 99 patterns..."

**Middle** (show what's possible):
> "Masterclass students have built:
> - Voice customer service agents
> - Automated research systems
> - Multi-agent development teams
>
> All in production, serving real users."

**CTA** (clear, actionable):
> [Enroll in 99 Agents Masterclass]
> Workshop attendee exclusive: 20% off
> Code: WORKSHOP2025 (expires in 7 days)

**PS** (create urgency):
> "P.S. Your repo access expires in 7 days.
> Masterclass students get permanent access + weekly updates."

---

## 🎓 Masterclass Enrollment Page

### ConvertKit Product Setup

**Create in ConvertKit**:
- Product name: "99 Agents Masterclass"
- Price: $497
- Discounted: $397 (workshop code)
- Payment: Stripe integration
- Tags on purchase: `masterclass_enrolled`

**Purchase triggers**:
- Welcome sequence
- Access grant to Masterclass materials
- Remove from nurture sequences

---

## 🚀 Scale Plan

### Workshop 1 (Done)

- 30 attendees
- Manual process
- Learn conversion rate

### Deep Dive (Now)

- 25+ attendees
- Semi-automated
- Refine messaging

### Workshop 2 (Next)

- 100+ attendees
- Fully automated (Zapier)
- Optimized emails
- Target: 15% conversion

### Workshop 3+

- Multiple per month
- Self-serve automation
- Segment by source
- A/B test everything
- Scale to 1000+/month

---

**Congratulations on the quick RSVPs!**

With this automation in place, you can scale to unlimited workshops while maximizing Masterclass conversions! 🎯

**Next**: Test the automation with your 25 deep dive attendees!
