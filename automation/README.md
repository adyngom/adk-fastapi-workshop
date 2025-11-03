# 🤖 Workshop Access Automation

> **Purpose**: Automate repository access for workshop attendees as part of the 99 Agents Masterclass lead generation funnel

---

## 🎯 Overview

This automation system manages the complete workshop attendee lifecycle:

1. **Registration** → Collect GitHub usernames
2. **Access Grant** → Add as collaborators (T-24h)
3. **Workshop** → Students use private repo via IDX
4. **Post-Workshop** → 7-day access for exploration
5. **Access Removal** → Remove collaborators (T+7d)
6. **Conversion Tracking** → Workshop → Masterclass enrollment

---

## 🚀 Quick Start

### Prerequisites

1. **GitHub Personal Access Token**
   - Go to: https://github.com/settings/tokens
   - Generate new token (classic)
   - Scopes needed: `repo` (full control)
   - Save token securely

2. **Python Environment**
   ```bash
   pip install requests pandas
   ```

3. **Registration Data**
   - CSV export from your form
   - Must include: github_username column

### Usage

```bash
# Set your GitHub token
export GITHUB_TOKEN="ghp_your_token_here"

# Add collaborators from CSV
python add_collaborators.py add --csv registrations.csv

# List current collaborators
python add_collaborators.py list

# Remove collaborators (post-workshop)
python add_collaborators.py remove --csv registrations.csv
```

---

## 📁 Files in This Directory

### `add_collaborators.py`
Main automation script for GitHub collaborator management

**Features**:
- Add collaborators in bulk from CSV
- Remove collaborators post-workshop
- List current collaborators
- Rate limiting (respects GitHub API limits)
- Error handling and retry logic
- Results logging (JSON output)

### `registrations.example.csv`
Template CSV format for workshop registrations

**Required columns**:
- `name`: Full name
- `email`: Email address
- `github_username`: GitHub username (required!)
- `company`: Company/organization (optional)
- `registered_at`: Registration timestamp

### `email_templates.md`
Complete email sequence for workshop funnel

**7 email templates**:
1. Registration confirmation
2. Pre-workshop checklist (T-48h)
3. Access grant (T-24h)
4. Day-of reminder (T-2h)
5. Post-workshop thank you (T+2h)
6. Access expiring (T+6d)
7. Post-removal follow-up (T+8d)

### `REGISTRATION_FORM_GUIDE.md`
Comprehensive guide for setting up registration form

**Includes**:
- Required fields
- Optional fields for lead qualification
- Form copy examples
- Integration recommendations (TypeForm, Google Forms, Luma)
- GDPR compliance

---

## 🔄 Complete Workflow

### Timeline

```
T-2 weeks: Registration opens
           ↓
T-48 hours: Send pre-workshop checklist (Email 2)
            Collect GitHub usernames
           ↓
T-24 hours: Run add_collaborators.py
            Send access grant emails (Email 3)
            Students test IDX setup
           ↓
T-2 hours: Send day-of reminder (Email 4)
           ↓
Workshop Day: Students use private repo
              Track engagement
           ↓
T+2 hours: Send thank you + survey (Email 5)
           Masterclass promotion begins
           ↓
T+6 days: Send expiring notice (Email 6)
          Final conversion push
           ↓
T+7 days: Run remove_collaborators.py
          Send post-removal (Email 7)
          ↓
Ongoing: Nurture sequence for non-converters
```

### Automation Options

#### Option A: Fully Automated (Zapier/Make)

**Trigger**: TypeForm submission
**Actions**:
1. Add to Google Sheet
2. Call add_collaborators API
3. Send confirmation email
4. Tag in email marketing tool
5. Add to CRM

**Cost**: ~$20-50/month
**Effort**: 2-3 hours setup
**Scalability**: Unlimited

#### Option B: Semi-Automated (Manual CSV)

**Process**:
1. Export registrations daily
2. Run add_collaborators.py manually
3. Manual email sending

**Cost**: Free
**Effort**: 15 min/day
**Scalability**: Up to 100-200 attendees

#### Option C: Hybrid

**Automated**:
- Registration confirmation (Email 1)
- Add to email list

**Manual**:
- Bulk collaborator addition (once, T-24h)
- Access removal (once, T+7d)

**Cost**: Minimal
**Effort**: 30 min total
**Scalability**: 300-500 attendees

---

## 🛠️ Technical Setup

### Step 1: Create GitHub Token

```bash
# Go to GitHub Settings
https://github.com/settings/tokens

# Generate new token (classic)
Name: workshop-automation
Scopes:
  ✅ repo (full control of private repositories)

# Save token securely
# Use environment variable (never commit!)
```

### Step 2: Prepare Registration CSV

**Export from your form** with these columns:
```csv
name,email,github_username,company,registered_at
```

Save as: `registrations_devfest_atlanta_2025.csv`

### Step 3: Test with Small Batch

```bash
# Create test CSV with 2-3 people
echo "name,email,github_username" > test.csv
echo "Test User,test@example.com,your-test-account" >> test.csv

# Dry run (test mode)
export GITHUB_TOKEN="your_token"
python add_collaborators.py add --csv test.csv

# Check results
cat add_results.json

# Verify on GitHub
python add_collaborators.py list
```

### Step 4: Production Run

```bash
# Full batch (day before workshop)
python add_collaborators.py add \
  --csv registrations_devfest_atlanta_2025.csv \
  --permission pull

# Review results
cat add_results.json

# Success emails
# Use add_results.json to send Email 3 to newly added users
```

### Step 5: Post-Workshop Cleanup

```bash
# 7 days after workshop
python add_collaborators.py remove \
  --csv registrations_devfest_atlanta_2025.csv

# Confirm
python add_collaborators.py list
# Should be back to original collaborators only
```

---

## 📊 Tracking & Analytics

### GitHub Insights

**What you can track** (GitHub API):
- Who cloned the repo
- Who starred it
- Which git tags were checked out (via commits to forks)
- Time spent (rough estimate)
- Most viewed files

**Access**:
```bash
# Get repo traffic data
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/adyngom/adk-fastapi-workshop/traffic/clones

# Get referring sites
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/adyngom/adk-fastapi-workshop/traffic/popular/referrers
```

### Email Marketing Metrics

**Track in your email tool**:
- Email 1: Registration confirmation (baseline engagement)
- Email 2: Pre-workshop checklist (commitment level)
- Email 3: Access grant (excitement, did they click IDX?)
- Email 5: Post-workshop thank you (**Masterclass conversion rate**)
- Email 6: Access expiring (**Urgency conversions**)

### Conversion Funnel

```
100 Registrations
  ↓ (85%)
85 Provide GitHub username
  ↓ (95%)
81 Added as collaborators
  ↓ (70%)
57 Actually attend workshop
  ↓ (60%)
34 Access repo in 7-day window
  ↓ (10-15%)
5-8 Convert to 99 Agents Masterclass
```

**Key metrics**:
- Registration → Attendance: 70%
- Attendance → Repo usage: 60%
- Workshop → Masterclass: 10-15%

---

## 🔒 Security Best Practices

### Token Management

❌ **Never**:
- Commit tokens to git
- Share tokens publicly
- Use tokens with more permissions than needed

✅ **Always**:
- Use environment variables
- Rotate tokens every 90 days
- Use read-only permission for collaborators
- Log all actions

### Access Control

**Read-only access** (pull permission):
- ✅ Students can clone
- ✅ Students can use with IDX
- ✅ Students can fork (keep their copy)
- ❌ Students can't push changes
- ❌ Students can't modify original

### Data Privacy

**Comply with**:
- GDPR (EU students)
- CCPA (California students)
- General data protection

**Requirements**:
- Explicit consent for emails
- Right to be forgotten (delete data)
- Data retention policy (how long you keep usernames)

---

## 💡 Pro Tips

### Increase GitHub Username Collection

**In registration form**:
> "No GitHub account? No problem!
> Create one free in 2 minutes: github.com/signup
>
> Why required: You'll get exclusive access to workshop code,
> worth $299 if purchased separately. GitHub account = your key."

**Value prop**:
- Emphasize exclusivity
- Mention dollar value
- Make it seem premium

### Reduce No-Shows

**After access grant**:
- "Test your setup NOW" (Email 3)
- Send calendar invite
- Reminder 2 hours before (Email 4)
- Early access (join 10 min early)

**Typical improvement**: 20% reduction in no-shows

### Maximize Masterclass Conversion

**During workshop**:
- Mention Masterclass 2-3 times
- "This is module 1 of 99 Agents Masterclass"
- Show what else is in Masterclass
- Exclusive discount for attendees

**In emails**:
- Email 5: Soft sell (you just learned basics, want more?)
- Email 6: Urgency (access expiring, discount expiring)
- Email 7: FOMO (others are enrolling, spots filling)

---

## 🎓 Example: Full Automation

### TypeForm → Zapier → GitHub → Email

**Step 1**: TypeForm Submission
- Student fills registration
- Includes GitHub username

**Step 2**: Zapier Trigger
- New TypeForm response
- Zapier catches it

**Step 3**: Actions (in order)
1. Add row to Google Sheets (backup)
2. Webhook to your add_collaborators API
3. Wait for success response
4. Send Email 1 via SendGrid
5. Add to email sequence (Email 2-7)
6. Add to CRM with tag: workshop_attendee

**Result**: Fully hands-off, scales to 1000+

---

## 📞 Support Scripts

### Check Collaborator Status

```bash
# Is specific user a collaborator?
python add_collaborators.py list | grep "johndoe"
```

### Re-Add After Failure

```bash
# Create CSV with failed users
# Run add again (script skips existing)
python add_collaborators.py add --csv failed_users.csv
```

### Manual One-Off Addition

```python
from add_collaborators import CollaboratorManager

manager = CollaboratorManager("adyngom", "adk-fastapi-workshop", "token")
result = manager.add_collaborator("username")
print(result)
```

---

## 🎯 Success Metrics

**Your goals**:
- Workshop signups: Maximized
- Day-of attendance: 70%+
- Repo engagement: 50%+
- Masterclass conversion: 10-15%
- Setup friction: Minimized (< 5 min)

**This automation achieves all of them!** 🚀

---

**Next steps**: Test with small batch, refine, then scale to 100+
