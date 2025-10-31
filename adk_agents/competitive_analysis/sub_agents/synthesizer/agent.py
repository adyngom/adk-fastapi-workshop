"""Synthesis Agent - Compares and analyzes competitive data"""
from google.adk.agents import Agent

root_agent = Agent(
    name="synthesizer",
    description="Compares and analyzes data from multiple competitors",
    model="gemini-2.0-flash",
    instruction="""Analyze and compare the competitive data:

- Competitor A (Google): {competitor_a_data}
- Competitor B (Microsoft): {competitor_b_data}
- Competitor C (Amazon): {competitor_c_data}

Provide a comparative analysis with:
1. Key strengths of each competitor
2. Market positioning differences
3. Strategic insights
4. Recommendations

Format as a clear, structured report.""",
    output_key="competitive_analysis"
)
