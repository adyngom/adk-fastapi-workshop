"""
Verified Recommendations Agent - Step 9 of 9
Demonstrates verification, validation, audit trails, and accountability patterns
Inspired by Ayo Adedeji's Charity Advisor using AP2 Protocol
"""
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from datetime import datetime


# ============================================================================
# SUB-AGENT 1: Analyzer Agent
# ============================================================================

analyzer_agent = Agent(
    name="analyzer_agent",
    model="gemini-2.0-flash-exp",
    description="Understands user intent and requirements for high-stakes recommendations",
    instruction="""You are a requirements analysis specialist for high-stakes decisions.

Your role:
1. Understand what user wants to do (donate, invest, purchase, authorize)
2. Extract requirements and constraints:
   - Amount involved (money, resources)
   - Criteria (impact, efficiency, trustworthiness)
   - Risk tolerance
   - Timeline

3. Identify verification needs based on stakes:
   - High stakes ($10k+): Deep verification required
   - Medium stakes ($1k-$10k): Standard verification
   - Low stakes (<$1k): Basic verification

Output format:
{
    "request_type": "charity_donation/investment/authorization/purchase",
    "parameters": {
        "amount": "$X",
        "criteria": ["high_impact", "transparent", "efficient"],
        "constraints": ["must_be_registered_501c3", "low_overhead"],
        "timeline": "Immediate/within_30_days/flexible"
    },
    "verification_level": "deep/standard/basic",
    "stakes_assessment": {
        "financial_risk": "High/Medium/Low",
        "reputational_risk": "High/Medium/Low",
        "reversibility": "Can/cannot reverse decision"
    },
    "audit_requirements": {
        "full_trail_required": true/false,
        "approval_gates_needed": true/false,
        "third_party_verification": true/false
    }
}

Be thorough. High-stakes decisions require careful analysis."""
)


# ============================================================================
# SUB-AGENT 2: Researcher Agent
# ============================================================================

researcher_agent = Agent(
    name="researcher_agent",
    model="gemini-2.0-flash-exp",
    description="Finds potential recommendations matching user criteria",
    instruction="""You are a research specialist for high-stakes recommendations.

You receive requirements from analyzer. Your role:

Find 3-5 potential options that match criteria:
- For charity donations: Research registered charities with proven impact
- For investments: Find assets matching risk/return profile
- For vendors: Identify qualified service providers

Research each option:
1. Basic information (name, location, established date)
2. Track record (history, outcomes, performance)
3. Ratings/reviews (third-party assessments)
4. Financial health (for organizations)
5. Red flags (controversies, complaints)

Output format:
{
    "candidates": [
        {
            "candidate_id": "CAND-001",
            "name": "Example Charity Foundation",
            "type": "501(c)(3) Non-profit",
            "established": "2010",
            "track_record": {
                "years_active": "14 years",
                "projects_completed": "150+",
                "beneficiaries_served": "50,000+",
                "transparency_rating": "A+ (CharityNavigator)"
            },
            "financials": {
                "annual_budget": "$5M",
                "overhead_percentage": "12%",
                "program_spending": "88%"
            },
            "initial_assessment": "Strong candidate",
            "verification_needed": [
                "Confirm 501(c)(3) status",
                "Verify recent financial audit",
                "Check for complaints or controversies"
            ]
        },
        // ... 2-4 more candidates
    ],
    "search_quality": "High - found diverse options",
    "all_meet_basic_criteria": true
}

Find quality options. Verification happens next."""
)


# ============================================================================
# PARALLEL VERIFICATION - Independent validators work simultaneously
# ============================================================================

verification_agent = Agent(
    name="verification_agent",
    model="gemini-2.0-flash-exp",
    description="Independently verifies legitimacy and credentials of recommendations",
    instruction="""You are an independent verification specialist.

CRITICAL: You work independently from the researcher. Your job is to VERIFY, not advocate.

For each candidate, verify:
1. **Legitimacy**
   - Legal registration (501(c)(3), business license, etc.)
   - Physical address and contact info
   - Leadership team credentials
   - Years in operation

2. **Credentials & Certifications**
   - Industry certifications
   - Third-party ratings (CharityNavigator, BBB, etc.)
   - Awards or recognitions
   - Accreditations

3. **Track Record Validation**
   - Can you confirm claimed accomplishments?
   - Independent reviews or assessments
   - Public records of impact
   - References or testimonials

4. **Red Flags Check**
   - Legal issues or lawsuits
   - Complaints or negative reviews
   - Leadership controversies
   - Financial irregularities

Output format:
{
    "candidate_id": "CAND-001",
    "verification_results": {
        "legitimacy_verified": true/false,
        "credentials_confirmed": true/false,
        "track_record_validated": true/false,
        "no_red_flags": true/false
    },
    "verification_details": {
        "501c3_status": "Confirmed via IRS database",
        "charity_navigator_rating": "4/4 stars (verified directly)",
        "financial_audit": "2023 audit on file, clean opinion",
        "complaints": "Zero formal complaints found"
    },
    "verification_score": 0-100,
    "confidence_level": "High/Medium/Low",
    "concerns_identified": [
        "Concern 1 (if any)",
        "Concern 2 (if any)"
    ],
    "verification_timestamp": "2024-11-19T23:45:00Z",
    "sources_checked": ["IRS database", "CharityNavigator", "BBB", "News search"]
}

Be skeptical. Your independence protects the user.
"""
)

risk_checker_agent = Agent(
    name="risk_checker",
    model="gemini-2.0-flash-exp",
    description="Assesses risks and potential issues with each recommendation",
    instruction="""You are a risk assessment specialist.

Working independently (parallel with verification), assess risks:

1. **Financial Risks**
   - Funding stability
   - Overhead creep
   - Dependence on single donor
   - Investment volatility (if applicable)

2. **Operational Risks**
   - Leadership turnover
   - Geographic/political instability
   - Scalability issues
   - Execution capability

3. **Reputational Risks**
   - Association risks
   - Controversy potential
   - Mission drift
   - Transparency issues

4. **Impact Risks**
   - Will the desired outcome actually happen?
   - Measurement and accountability
   - Unintended consequences

Output format:
{
    "candidate_id": "CAND-001",
    "risk_assessment": {
        "overall_risk_level": "Low/Medium/High",
        "risk_score": 0-100,
        "primary_risks": [
            {
                "risk": "Geographic instability",
                "likelihood": "Medium",
                "impact": "High",
                "mitigation": "Diversify across multiple regions"
            }
        ]
    },
    "red_flags": ["flag1", "flag2"] or [],
    "risk_mitigation_recommendations": [
        "Start with small test donation",
        "Request quarterly impact reports"
    ],
    "comparative_risk": "Lower risk than 2 other candidates, higher than 1"
}

Identify risks others might miss."""
)

# Parallel verification
parallel_verifiers = ParallelAgent(
    name="parallel_verifiers",
    description="Independent verification and risk assessment simultaneously",
    sub_agents=[
        verification_agent,
        risk_checker_agent
    ]
)


# ============================================================================
# SUB-AGENT 4: Recommendation Agent
# ============================================================================

recommendation_agent = Agent(
    name="recommendation_agent",
    model="gemini-2.0-flash-exp",
    description="Generates ranked recommendations based on research and verification",
    instruction="""You are a recommendation specialist.

You receive:
- User requirements (from analyzer)
- Candidate research (from researcher)
- Verification results (from verification agent)
- Risk assessment (from risk checker)

Your role: Generate ranked, justified recommendations.

Decision criteria:
1. Must pass verification (legitimacy, credentials, track record)
2. Acceptable risk level for user's risk tolerance
3. Best match for user's criteria
4. Transparent and accountable

Output format:
{
    "top_recommendations": [
        {
            "rank": 1,
            "candidate_id": "CAND-001",
            "name": "...",
            "recommendation_strength": "Strong/Moderate/Weak",
            "why_recommended": {
                "meets_criteria": ["criterion1", "criterion2"],
                "verification_passed": true,
                "risk_level": "Low-Medium (acceptable)",
                "unique_strengths": ["strength1", "strength2"]
            },
            "considerations": [
                "Consider starting with smaller amount to test",
                "Request impact report after 6 months"
            ],
            "next_steps": ["Step 1", "Step 2"]
        },
        // Rank 2-3...
    ],
    "not_recommended": [
        {
            "candidate_id": "CAND-004",
            "name": "...",
            "why_not": "Failed verification - 501(c)(3) status unclear",
            "verification_score": 45
        }
    ],
    "overall_confidence": "High - top recommendation strongly verified"
}

Only recommend what you'd trust yourself."""
)


# ============================================================================
# SUB-AGENT 5: Auditor Agent
# ============================================================================

auditor_agent = Agent(
    name="auditor_agent",
    model="gemini-2.0-flash-exp",
    description="Creates comprehensive audit trail of decision-making process",
    instruction="""You are an audit and accountability specialist.

You receive ALL previous agent outputs. Your role:

Create a complete, immutable audit trail of the decision:

1. **Decision Timeline**
   - When each agent ran
   - What inputs each received
   - What outputs each produced
   - Total processing time

2. **Decision Reasoning**
   - Why these candidates were selected
   - What verification checks passed/failed
   - How risks were assessed
   - Why final ranking was chosen

3. **Accountability Record**
   - Which agent made which determination
   - Confidence levels at each stage
   - Sources cited for each claim
   - Human approval points (if any)

4. **Audit Log Structure** (for compliance/legal review)

Output format:
{
    "audit_id": "AUDIT-20241119-XXXXX",
    "audit_timestamp": "2024-11-19T23:45:00Z",
    "decision_trail": [
        {
            "stage": "Analysis",
            "agent": "analyzer_agent",
            "timestamp": "...",
            "input": "User request summary",
            "output": "Requirements extracted",
            "key_decisions": ["Classified as high-stakes"]
        },
        {
            "stage": "Research",
            "agent": "researcher_agent",
            "timestamp": "...",
            "candidates_found": 5,
            "search_quality": "High"
        },
        {
            "stage": "Verification",
            "agent": "verification_agent",
            "timestamp": "...",
            "candidates_verified": 5,
            "verification_scores": [95, 87, 82, 65, 45],
            "sources_checked": ["IRS", "CharityNavigator", "BBB"]
        },
        {
            "stage": "Risk Assessment",
            "agent": "risk_checker",
            "timestamp": "...",
            "risks_identified": 12,
            "high_risk_items": 2
        },
        {
            "stage": "Recommendation",
            "agent": "recommendation_agent",
            "timestamp": "...",
            "final_ranking": ["CAND-001", "CAND-002", "CAND-003"]
        }
    ],
    "verification_summary": {
        "total_candidates_researched": 5,
        "passed_verification": 3,
        "failed_verification": 2,
        "verification_criteria_used": ["legitimacy", "credentials", "track_record", "red_flags"]
    },
    "decision_accountability": {
        "primary_decision_maker": "recommendation_agent",
        "verification_performed_by": "verification_agent (independent)",
        "risk_assessed_by": "risk_checker (independent)",
        "human_approval_required": "For amounts >$10k",
        "decision_reversible": false,
        "appeal_process": "Contact audit team within 30 days"
    },
    "cryptographic_hash": "sha256_hash_of_entire_decision_trail",
    "audit_log_stored": "BigQuery: agent_audit_logs.verified_recommendations",
    "compliance_checklist": {
        "independent_verification": true,
        "risk_assessment_completed": true,
        "decision_reasoning_documented": true,
        "sources_cited": true,
        "timeline_recorded": true
    }
}

This audit trail can be used for:
- Legal compliance review
- Internal audits
- Dispute resolution
- Process improvement
- Regulatory reporting

CRITICAL: This must be immutable and complete. Once created, it cannot be altered.
"""
)


# ============================================================================
# ROOT AGENT: Complete Verified Recommendation Workflow
# ============================================================================

root_agent = SequentialAgent(
    name="verified_recommendations",
    description="High-stakes recommendation system with verification, risk assessment, and audit trails",
    sub_agents=[
        analyzer_agent,           # Step 1: Understand requirements
        researcher_agent,         # Step 2: Find candidates
        parallel_verifiers,       # Step 3: Verify + Assess Risk (simultaneously)
        recommendation_agent,     # Step 4: Generate recommendations
        auditor_agent            # Step 5: Create audit trail
    ]
)


# ============================================================================
# AP2 (Agent Payments Protocol) INSPIRATION
# ============================================================================
"""
This agent is inspired by Ayo Adedeji's charity advisor using AP2 Protocol.

Key Insight: "When agents handle money, you need more than model capability -
you need accountability."

AP2 Principles Applied:
1. Role Separation
   - Discovery (researcher) ≠ Verification ≠ Execution
   - No single agent controls the entire decision

2. Independent Verification
   - Verification agent works independently from researcher
   - Risk checker provides independent risk assessment
   - Parallel execution ensures no collusion

3. Complete Audit Trail
   - Every decision logged with timestamp
   - Every agent's reasoning captured
   - Sources cited for every claim
   - Immutable record (blockchain-style hash)

4. Accountability
   - Can replay exactly how decision was made
   - Can identify which agent made which determination
   - Can verify no shortcuts were taken
   - Human approval gates for critical thresholds

Production Enhancements:
- Store audit trail in BigQuery (queryable for compliance)
- Cryptographic hashing for immutability
- Session rewind capability (ADK 1.17+)
- Verifiable credentials integration
- Transaction logging to blockchain

See: https://www.linkedin.com/posts/ayo-adedeji_charity-advisor-with-ap2-protocol
"""


# ============================================================================
# PRODUCTION AUDIT LOGGING (ADK 1.18)
# ============================================================================
"""
In production, integrate BigQuery logging:

from google.adk.observability import BigQueryLoggingPlugin

logging_plugin = BigQueryLoggingPlugin(
    project_id="my-project",
    dataset="agent_audit_logs",
    table="verified_recommendations"
)

# Every agent execution logged to BigQuery
# Queryable for: compliance audits, dispute resolution, process analysis

Example query:
SELECT
    audit_id,
    decision_trail,
    verification_summary,
    final_recommendation
FROM agent_audit_logs.verified_recommendations
WHERE amount > 10000
AND decision = 'APPROVED'
ORDER BY timestamp DESC
"""
