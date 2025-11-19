# Medical Authorization Agent

**Step 4 of 9** | **Duration:** 30 minutes | **Difficulty:** Intermediate

## Overview

A 4-agent Sequential workflow for medical pre-authorization processing. Demonstrates compliance workflows with structured data extraction, validation gates, and audit trails.

Final Sequential agent before moving to Parallel patterns - students master complex decision logic and regulatory requirements.

## Learning Objectives

By completing this agent, you will understand:

- ✅ **Structured Data Extraction** - Parsing unstructured requests into validated formats
- ✅ **Decision Gates** - Each stage can approve/deny/request-more-info
- ✅ **Compliance Workflows** - HIPAA, clinical guidelines, insurance rules
- ✅ **Audit Trails** - Documenting every decision for regulatory review
- ✅ **Multi-Criteria Decisions** - Combining eligibility + coverage + medical necessity

## Pattern Demonstrated

**Sequential Workflow with Validation Gates**

```
medical_authorization (SequentialAgent)
├── intake_agent (Agent)
│   └── Role: Extract structured data (patient, provider, procedure)
│   └── Gate: Complete/Incomplete → Stop if incomplete
│
├── verification_agent (Agent)
│   └── Role: Verify eligibility and coverage
│   └── Gate: Approved/Denied → Stop if not eligible
│
├── medical_review_agent (Agent)
│   └── Role: Review medical necessity
│   └── Gate: Approve/Deny/Peer-Review → Stop if denied
│
└── authorization_agent (Agent)
    └── Role: Generate final decision + documentation
    └── Output: Authorization number OR denial + appeal rights
```

**Key Learning:** Decision gates at each stage - workflow can stop early if criteria not met.

## Business Value

Real-world impact:
- **Hours → Minutes** - Authorization decisions in 5-10 minutes vs 2-3 days
- **Consistent compliance** - Every request follows same regulatory guidelines
- **Audit ready** - Complete documentation trail
- **Cost control** - Medical necessity validation prevents inappropriate approvals
- **Patient safety** - Clinical review catches contraindications

Use cases:
- Healthcare pre-authorization
- Insurance claims processing
- Regulatory compliance workflows
- Any process requiring multiple validation stages

## ADK 1.18+ Features

### Callback Management
- **Available:** ✅
- **Usage:** Log each validation gate for audit compliance
  ```python
  def audit_callback(agent_name, result):
      audit_log.append({
          "agent": agent_name,
          "decision": extract_decision(result),
          "timestamp": datetime.now(),
          "reasoning": extract_reasoning(result)
      })
  ```
- **Benefit:** Complete audit trail for regulatory review

## Architecture

### Workflow with Decision Gates

```
User Input: Pre-authorization request (patient, procedure, clinical justification)

    ↓

[INTAKE AGENT]
Extract: patient info, provider, CPT codes, diagnosis, clinical justification
Validate: All required fields present, codes properly formatted
Decision Gate:
  ✅ Complete → Proceed
  ❌ Incomplete → Stop, request missing information

Output: Structured medical data

    ↓

[VERIFICATION AGENT]
Check: Eligibility, active coverage, procedure covered, provider in-network
Decision Gate:
  ✅ Eligible + Covered → Proceed
  ❌ Not eligible → Stop, deny with reason
  ❌ Not covered → Stop, suggest alternatives

Output: Coverage determination

    ↓

[MEDICAL REVIEW AGENT]
Review: Medical necessity, clinical guidelines, evidence quality
Assess: Diagnosis supports procedure, conservative treatment tried, timing appropriate
Decision Gate:
  ✅ Medically necessary → Proceed
  ❌ Not necessary → Stop, deny with clinical rationale
  ⚠️ Complex case → Trigger peer review

Output: Clinical determination

    ↓

[AUTHORIZATION AGENT]
Generate: Final decision (approved/denied/pending)
Document: Authorization number, effective dates, conditions, audit trail
Provide: Appeal rights if denied, pending requirements if more info needed

Output: Official authorization response

    ↓

Provider receives decision with full documentation
```

### Agent Responsibilities

| Agent | Input | Decision Gate | Output |
|-------|-------|---------------|--------|
| **Intake** | Unstructured request | Complete/Incomplete | Structured data |
| **Verification** | Structured data | Eligible/Not eligible | Coverage status |
| **Medical Review** | Data + Coverage | Necessary/Not necessary | Clinical determination |
| **Authorization** | All previous | Approved/Denied/Pending | Final decision |

## Files

```
medical_authorization/
├── agent.py          # 4 sub-agents + SequentialAgent root
├── .env              # API key
├── __init__.py       # Package marker
└── README.md         # This file
```

## Running the Agent

### Example Request

```python
from google.adk import run_debug
from adk_agents.medical_authorization.agent import root_agent

request = """
Patient: John Smith, DOB: 1965-03-15, Member ID: ABC123456
Provider: Dr. Jane Doe, NPI: 1234567890, Cardiology Associates
Procedure: Cardiac catheterization (CPT: 93458)
Diagnosis: Chest pain, suspected coronary artery disease (ICD-10: R07.9, I25.10)
Clinical Justification: Patient presents with persistent chest pain despite medical management.
Stress test shows significant ST-segment depression. Requires diagnostic catheterization to
assess coronary anatomy before determining treatment approach.
Urgency: Urgent (symptoms worsening)
"""

run_debug(root_agent, request)
```

## Example Interactions

### Example 1: Approved Authorization

**Request:**
```
Patient: Sarah Johnson, DOB: 1978-06-20, Member ID: XYZ789012
Provider: Dr. Michael Chen, NPI: 9876543210, Orthopedic Surgery Center
Procedure: Knee arthroscopy (CPT: 29881)
Diagnosis: Meniscal tear, right knee (ICD-10: S83.241A)
Clinical Justification: MRI confirms complex medial meniscus tear. Conservative treatment
(physical therapy, NSAIDs) for 8 weeks without improvement. Persistent pain and locking
episodes affecting daily activities.
Urgency: Routine
```

**Intake Output:**
```json
{
  "completeness_check": {"complete": true, "missing_fields": []},
  "patient": {...},
  "procedure": {
    "cpt_codes": ["29881"],
    "diagnosis_codes": ["ICD-10: S83.241A"],
    "clinical_justification": "MRI-confirmed tear, failed conservative treatment"
  }
}
```

**Verification Output:**
```json
{
  "eligibility": {"active": true},
  "coverage_status": {
    "procedure_covered": true,
    "pre_auth_required": true,
    "provider_in_network": true
  },
  "verification_result": "APPROVED"
}
```

**Medical Review Output:**
```json
{
  "medical_necessity": {
    "necessary": true,
    "criteria_met": ["MRI confirmation", "Failed conservative treatment", "Functional impairment"],
    "guidelines_referenced": ["AAOS Clinical Practice Guidelines"]
  },
  "review_decision": "APPROVE"
}
```

**Final Authorization:**
```json
{
  "authorization_number": "AUTH-20241119-12345",
  "decision": "APPROVED",
  "effective_dates": {"start": "2024-11-25", "end": "2025-02-25"},
  "authorized_procedure": {
    "cpt_codes": ["29881"],
    "description": "Arthroscopy, knee, surgical; with meniscectomy",
    "units_authorized": 1
  },
  "conditions": [
    "Must be performed by in-network orthopedic surgeon",
    "Valid for 90 days from issue date"
  ],
  "financial_estimate": {
    "insurance_pays": "$3,500",
    "patient_responsibility": "$500 (deductible)"
  }
}
```

### Example 2: Denied - Not Medically Necessary

**Request:**
```
Procedure: Cosmetic rhinoplasty (CPT: 30400)
Diagnosis: Deviated septum (ICD-10: J34.2)
Clinical Justification: Patient requests nose reshaping for aesthetic reasons.
```

**Flows through intake → verification → medical review**

**Medical Review Output:**
```json
{
  "medical_necessity": {
    "necessary": false,
    "criteria_met": [],
    "evidence_quality": "weak"
  },
  "clinical_assessment": {
    "diagnosis_supports_procedure": false
  },
  "review_decision": "DENY",
  "clinical_rationale": "Diagnosis (deviated septum) would support functional septoplasty,
   but procedure code is for cosmetic rhinoplasty. No documented functional impairment
   (breathing difficulty, sleep apnea). Cosmetic procedures are not covered benefits."
}
```

**Final Authorization:**
```json
{
  "decision": "DENIED",
  "denial_details": {
    "reason_code": "NOT_MEDICALLY_NECESSARY",
    "reason_description": "Cosmetic procedures are excluded from coverage. If functional
     impairment exists, provider should resubmit with appropriate CPT code (30520 for
     septoplasty) and documentation of breathing difficulty.",
    "appeal_rights": "Appeals can be filed within 180 days...",
    "alternatives_suggested": ["Septoplasty (CPT: 30520) if functional impairment present"]
  }
}
```

### Example 3: Pending - More Information Needed

**Request:** Missing clinical justification

**Intake Output:**
```json
{
  "completeness_check": {
    "complete": false,
    "missing_fields": ["clinical_justification", "supporting_documentation"]
  }
}
```

**Workflow stops here** - Verification doesn't run

**Response:**
```json
{
  "decision": "PENDING",
  "pending_requirements": {
    "required_documents": [
      "Clinical notes documenting symptoms and duration",
      "Results of diagnostic tests (if applicable)",
      "Documentation of conservative treatments attempted"
    ],
    "due_date": "2024-11-26",
    "submission_instructions": "Fax to 555-0123 or upload via provider portal"
  }
}
```

## Common Issues

### Workflow Stops at Verification

**Problem:** Medical review doesn't run

**Solution:**
- This is CORRECT behavior - verification failed (not eligible or not covered)
- Decision gates prevent unnecessary processing
- Check verification output for denial reason

### Missing Medical Codes

**Problem:** Intake agent can't extract CPT or ICD codes

**Solution:**
- Provide codes in request: "Procedure: Knee surgery (CPT: 29881)"
- Or use clear procedure names: "Diagnostic cardiac catheterization"
- Intake agent will ask for missing codes

### Denial Without Clear Reason

**Problem:** Authorization denied but rationale unclear

**Solution:**
- Check medical_review output for clinical_rationale
- Authorization agent should summarize all denial reasons
- If unclear, improve medical_review agent's instruction

## Understanding Compliance Workflows

**Key Concepts:**

1. **Decision Gates**
   - Each agent can stop the workflow
   - Prevents unnecessary processing
   - Saves costs (don't review if not eligible)
   - Example: Why review medical necessity if patient not eligible?

2. **Structured Data**
   - Unstructured request → Structured format
   - Enables automated validation
   - Required for audit trails
   - Standard medical codes (CPT, ICD-10, NPI)

3. **Audit Trails**
   - Every decision documented
   - Timestamps for each stage
   - Reasoning captured
   - Regulatory requirement

4. **Multi-Criteria Decisions**
   - Eligibility AND Coverage AND Medical Necessity
   - All must pass for approval
   - Any failure = denial
   - Clear explanation for each criterion

## Success Criteria

Before moving to Step 5, verify:

- [ ] All 4 agents execute for complete requests
- [ ] Workflow stops early when validation fails
- [ ] Approvals include authorization numbers
- [ ] Denials include clear rationale + appeal rights
- [ ] Pending requests specify missing information
- [ ] Tested with approved, denied, and pending scenarios

## Next Steps

Phase 2 complete! You've mastered Sequential workflows.

**Step 5: Financial Advisor (Parallel Pattern)**

Preview: First parallel agent! Multiple analysts work simultaneously: data analyst, trading strategist, execution planner, risk assessor. Learn when parallel > sequential.

## Debugging Tips

### Test Each Gate

```python
from adk_agents.medical_authorization.agent import (
    intake_agent, verification_agent, medical_review_agent
)

# Test intake with incomplete request
incomplete = "Patient: John Smith. Procedure: Surgery."
run_debug(intake_agent, incomplete)
# Should return: completeness_check.complete = false

# Test verification with non-covered procedure
not_covered = """
Patient: John, Member ID: ABC123 (active)
Procedure: Experimental treatment (CPT: 99999)
"""
# Should deny at verification stage
```

### Monitor Decision Gates

```python
def log_decision_gate(agent_name, result):
    decision = extract_decision_from_result(result)
    print(f"{agent_name}: {decision}")

    if decision in ["DENIED", "INCOMPLETE", "PENDING"]:
        print(f"  ⚠️ Workflow should stop here")
        print(f"  Reason: {extract_reason(result)}")

root_agent.after_agent_callback = log_decision_gate
```

### Validate Medical Codes

- CPT codes: 5 digits (e.g., 99213, 29881)
- ICD-10 codes: 3-7 characters (e.g., I25.10, S83.241A)
- NPI numbers: 10 digits (e.g., 1234567890)

## Comparison with Previous Steps

| Step | Pattern | Decision Logic | Output |
|------|---------|----------------|--------|
| 2 (Customer Service) | Sequential | Always process all 3 agents | Final response |
| 3 (Content Pipeline) | Sequential | Always process all 4 agents | Published content |
| 4 (Medical Auth) | Sequential with Gates | **Can stop at any stage** | Approval/Denial/Pending |

**Key Difference:** Step 4 introduces **conditional execution** - not all agents always run.

## References

- [ADK Documentation - Sequential Agents](https://google.github.io/adk-docs/agents/sequential/)
- [Workshop Progression](../../workshop_progression.yaml)
- [ADK Samples - Medical Pre-Auth](https://github.com/google/adk-samples/tree/main/python/agents/medical-pre-authorization)
- [Step 3 - Content Pipeline](../content_pipeline/README.md) - Previous step

---

**Tags:** `step-4-medical-authorization`, `intermediate`, `sequential-agent`, `compliance-workflow`, `decision-gates`
