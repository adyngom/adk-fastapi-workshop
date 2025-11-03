# 📝 Registration Form Setup Guide

Configure your registration form to collect the right data for access automation and lead tracking.

---

## 🎯 Required Fields

### 1. Name (Required)
**Field Type**: Text input
**Label**: "Full Name"
**Purpose**: Personalization, email addressing
**Validation**: Required

### 2. Email (Required)
**Field Type**: Email input
**Label**: "Email Address"
**Purpose**: Communication, CRM, email automation
**Validation**: Required, valid email format
**Note**: Primary identifier

### 3. GitHub Username (Required)
**Field Type**: Text input
**Label**: "GitHub Username"
**Help text**: "Required for workshop repository access. Don't have one? Create free at github.com/signup"
**Purpose**: Repository collaborator addition
**Validation**: Required, alphanumeric + hyphens only
**Example**: "johndoe" (not full URL)

---

## 📊 Recommended Fields

### 4. Company/Organization (Optional but valuable)
**Field Type**: Text input
**Label**: "Company or Organization"
**Purpose**: Lead qualification, segmentation
**Use for**: B2B targeting, enterprise conversions

### 5. Role/Title (Optional)
**Field Type**: Dropdown
**Options**:
- Software Developer
- Data Scientist
- ML Engineer
- DevOps Engineer
- Engineering Manager
- Student
- Other

**Purpose**: Content personalization, lead scoring

### 6. Experience Level (Optional)
**Field Type**: Dropdown
**Label**: "Python Experience"
**Options**:
- Beginner (< 1 year)
- Intermediate (1-3 years)
- Advanced (3+ years)
- Expert (5+ years)

**Purpose**: Workshop pacing, segmentation for follow-up

### 7. Primary Interest (Optional)
**Field Type**: Multiple choice
**Label**: "What brings you to this workshop?" (select all that apply)
**Options**:
- [ ] Learning ADK fundamentals
- [ ] Building production agents
- [ ] FastAPI integration
- [ ] Career advancement
- [ ] Specific project in mind
- [ ] Interested in 99 Agents Masterclass

**Purpose**: Lead intent scoring

---

## 🎁 Lead Magnet Fields

### 8. Referral Source (Optional)
**Field Type**: Dropdown
**Label**: "How did you hear about this workshop?"
**Options**:
- DevFest website
- Social media (Twitter/LinkedIn)
- Friend/colleague referral
- Google search
- YouTube
- Email newsletter
- Other

**Purpose**: Marketing attribution

### 9. Interested in Masterclass? (Optional)
**Field Type**: Yes/No
**Label**: "Interested in learning about our 99 Agents Masterclass?"
**Purpose**: Hot lead identification, pre-qualification

---

## 🔐 Consent & Legal

### 10. Terms Agreement (Required)
**Field Type**: Checkbox
**Label**: "I agree to the workshop terms and code of conduct"
**Link**: [Your terms page]

### 11. Email Consent (Required for GDPR)
**Field Type**: Checkbox
**Label**: "I consent to receive workshop-related emails and occasional updates about 99 Agents"
**Note**: Required in EU, good practice everywhere

---

## 💾 Data Export Format

### CSV Export Configuration

**Filename**: `workshop_registrations_{date}.csv`

**Columns** (in order):
```csv
timestamp,name,email,github_username,company,role,experience,interests,referral_source,masterclass_interest,terms_agreed,email_consent
```

**Example row**:
```csv
2025-10-15 14:30:00,John Doe,john@example.com,johndoe,Acme Corp,Software Developer,Intermediate,"Learning ADK;Production agents",DevFest website,Yes,true,true
```

---

## 🔗 Integration Recommendations

### TypeForm (Recommended)

**Why**:
- Beautiful UX
- Conditional logic (if no GitHub username → show instructions)
- Webhook support
- CSV export
- Email integration

**Setup**:
1. Create form with fields above
2. Add logic: "No GitHub username? Here's how to create one"
3. Webhook → trigger add_collaborators.py
4. Export → email automation tool

### Google Forms (Free alternative)

**Why**:
- Free
- Easy setup
- Google Sheets integration
- Familiar to attendees

**Limitations**:
- Less beautiful
- Manual export
- No webhooks (use Zapier/Make)

### Luma (Event-first)

**Why**:
- Event management built-in
- Calendar invites
- Reminder emails
- Attendee tracking

**Setup**:
- Create event
- Custom registration questions
- Export attendees
- Manual process to add collaborators

---

## 🤖 Automation Workflow

### Recommended: Zapier/Make Integration

**Trigger**: New registration (TypeForm/Google Forms)
**Actions**:
1. Add row to Google Sheet (backup)
2. Add to email list (Mailchimp/ConvertKit)
3. HTTP request to add_collaborators API endpoint (if you host it)
4. Send confirmation email (Email 1)
5. Tag in CRM (HubSpot/Salesforce)

### Manual Process (Small workshops)

**Every 24 hours**:
1. Export registrations to CSV
2. Run: `python add_collaborators.py add --csv registrations.csv`
3. Send Email 3 to new adds
4. Update tracking spreadsheet

---

## 📊 Registration Form Examples

### Minimal (Fast signup)

**Fields**: Name, Email, GitHub Username
**Time**: < 1 minute
**Conversion**: High (90%+)
**Use when**: Quick workshop signups, repeat attendees

### Comprehensive (Lead qualification)

**Fields**: All 11 fields above
**Time**: 3-5 minutes
**Conversion**: Lower (70-80%)
**Use when**: Masterclass funnel, enterprise targeting

### Recommended Balance

**Required**: Name, Email, GitHub Username (3 fields)
**Optional**: Company, Role, Masterclass Interest (3 fields)
**Total time**: 2 minutes
**Conversion**: ~85%

---

## 🎯 Form Copy Examples

### Opening

**Good**:
> "Join 100+ developers learning to build production AI agents with Google ADK.
> Free 2-hour hands-on workshop. Limited spots!"

**With urgency**:
> "Only 50 spots left! DevFest Atlanta ADK Workshop.
> Learn to build AI agents like the pros. Registration closes {date}."

### GitHub Username Field

**Clear instructions**:
> GitHub Username (required for repo access)
>
> Don't have one? Create free: github.com/signup
> Example: johndoe (just username, not full URL)
>
> Why needed: You'll get private access to workshop materials

### Submit Button

**Standard**: "Register for Workshop"
**Better**: "Save My Spot" or "Get Workshop Access"

---

## ✅ Registration Form Checklist

Before launching:

- [ ] All required fields present
- [ ] GitHub username field has clear instructions
- [ ] Help text explains why each field needed
- [ ] Terms & consent checkboxes (legal compliance)
- [ ] Mobile-responsive design
- [ ] Thank you page with next steps
- [ ] Confirmation email auto-sends
- [ ] CSV export configured
- [ ] Zapier/Make integration tested (if using)
- [ ] Tested on multiple devices

---

## 📈 Post-Launch Monitoring

**Track these metrics**:
- Registration conversion rate (landing page → submit)
- GitHub username collection rate (should be 95%+)
- Email open rates (pre-workshop communications)
- Workshop attendance rate (registered → attended)
- Repository access usage (GitHub API insights)
- Masterclass conversion rate (workshop → paid)

**Optimize based on**:
- Where people drop off
- Which fields slow them down
- What messaging resonates

---

**Result**: Streamlined registration that feeds your entire lead generation funnel! 🎯
