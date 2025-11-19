"""
Brand Intelligence Agent - Step 6 of 9
Demonstrates Parallel data gathering from multiple sources + Synthesis
"""
from google.adk.agents import Agent, ParallelAgent, SequentialAgent


# ============================================================================
# PARALLEL RESEARCHERS - All search simultaneously
# ============================================================================

news_researcher = Agent(
    name="news_researcher",
    model="gemini-2.0-flash-exp",
    description="Searches recent news mentions and media coverage",
    instruction="""You are a news research specialist.

Your role: Find recent news coverage about the given brand/company.

Search for:
1. Recent news articles (last 30 days)
2. Press releases
3. Media mentions
4. Industry publications
5. Sentiment (positive/negative/neutral)

Output format:
{
    "brand": "...",
    "news_coverage": [
        {
            "headline": "...",
            "source": "...",
            "date": "YYYY-MM-DD",
            "sentiment": "positive/negative/neutral",
            "summary": "Key points from article"
        }
    ],
    "overall_sentiment": "Mostly positive/mixed/mostly negative",
    "trending_topics": ["topic1", "topic2"],
    "media_reach": "High/Medium/Low coverage"
}

Focus on recent, credible sources."""
)

social_analyzer = Agent(
    name="social_analyzer",
    model="gemini-2.0-flash-exp",
    description="Analyzes social media presence and engagement",
    instruction="""You are a social media intelligence specialist.

Your role: Analyze brand's social media presence and conversations.

Analyze:
1. Social media mentions (Twitter, LinkedIn, Reddit, etc.)
2. Engagement levels (likes, shares, comments)
3. Influencer discussions
4. Customer sentiment in comments
5. Viral moments or crises

Output format:
{
    "social_presence": {
        "platforms": ["Twitter", "LinkedIn", "Instagram"],
        "follower_estimates": "X million total",
        "engagement_rate": "High/Medium/Low"
    },
    "conversation_themes": [
        "Product quality discussions",
        "Customer service experiences",
        "Innovation and features"
    ],
    "sentiment_breakdown": {
        "positive": "60%",
        "neutral": "30%",
        "negative": "10%"
    },
    "notable_mentions": [
        {"influencer": "...", "reach": "...", "sentiment": "..."}
    ],
    "trending_hashtags": ["#hashtag1", "#hashtag2"]
}

Look for authentic customer voices."""
)

trend_tracker = Agent(
    name="trend_tracker",
    model="gemini-2.0-flash-exp",
    description="Tracks search trends and SEO positioning",
    instruction="""You are a search trend analyst.

Your role: Analyze brand search trends and online visibility.

Research:
1. Search volume trends (Google Trends)
2. Keyword rankings
3. Brand vs competitors in search
4. Seasonal patterns
5. Geographic interest

Output format:
{
    "search_trends": {
        "trend_direction": "rising/stable/declining",
        "search_volume": "High/Medium/Low",
        "seasonal_patterns": "Q4 spike, summer dip",
        "peak_periods": ["December", "Back-to-school"]
    },
    "keyword_rankings": {
        "brand_terms": "Ranking #1 for 'brand name'",
        "product_terms": "Top 3 for 'product category'",
        "competitor_comparison": "Outranking 2 of 3 main competitors"
    },
    "geographic_interest": {
        "strongest_regions": ["California", "New York"],
        "emerging_markets": ["Texas", "Florida"]
    },
    "related_queries": ["query1", "query2"]
}

Identify momentum and opportunities."""
)

competitor_monitor = Agent(
    name="competitor_monitor",
    model="gemini-2.0-flash-exp",
    description="Monitors competitive positioning and market share",
    instruction="""You are a competitive intelligence specialist.

Your role: Analyze brand position vs competitors.

Research:
1. Main competitors identified
2. Market share estimates
3. Competitor recent moves
4. Differentiation points
5. Competitive advantages/weaknesses

Output format:
{
    "competitive_landscape": {
        "main_competitors": ["Competitor A", "Competitor B", "Competitor C"],
        "market_position": "#2 in category",
        "estimated_market_share": "22%"
    },
    "competitor_activity": [
        {
            "competitor": "...",
            "recent_move": "Launched new product line",
            "impact": "Moderate threat to mid-tier segment"
        }
    ],
    "differentiation": {
        "our_strengths": ["Premium quality", "Customer service"],
        "competitor_strengths": ["Lower prices", "Wider distribution"]
    },
    "market_gaps": [
        "Opportunity in eco-friendly segment",
        "Underserved price point at $X"
    ]
}

Objective competitive analysis."""
)


# ============================================================================
# PARALLEL EXECUTION
# ============================================================================

parallel_researchers = ParallelAgent(
    name="parallel_researchers",
    description="4 intelligence sources searched simultaneously",
    sub_agents=[
        news_researcher,
        social_analyzer,
        trend_tracker,
        competitor_monitor
    ]
)


# ============================================================================
# SYNTHESIS AGENT
# ============================================================================

intelligence_synthesizer = Agent(
    name="intelligence_synthesizer",
    model="gemini-2.0-flash-exp",
    description="Synthesizes multi-source intelligence into actionable insights",
    instruction="""You are a brand intelligence synthesis specialist.

You receive outputs from 4 simultaneous researchers:
1. News Researcher - recent media coverage
2. Social Analyzer - social media sentiment
3. Trend Tracker - search trends & SEO
4. Competitor Monitor - competitive positioning

Your role: Combine into actionable brand intelligence report.

Output format:
{
    "executive_summary": {
        "brand_health_score": "Strong/Good/Fair/Weak",
        "key_finding": "1-2 sentence highlight",
        "overall_sentiment": "Positive/Mixed/Negative",
        "momentum": "Rising/Stable/Declining"
    },
    "integrated_insights": {
        "what_news_shows": "Media coverage summary",
        "what_social_shows": "Customer sentiment summary",
        "what_trends_show": "Search interest summary",
        "what_competitors_show": "Market position summary"
    },
    "opportunities_identified": [
        {
            "opportunity": "...",
            "source": "From social analyzer + trend tracker",
            "action": "Recommended next step"
        }
    ],
    "threats_identified": [
        {
            "threat": "...",
            "source": "From competitor monitor + news",
            "mitigation": "Suggested response"
        }
    ],
    "recommended_actions": {
        "immediate": ["Action 1", "Action 2"],
        "short_term": ["Action 3"],
        "long_term": ["Action 4"]
    },
    "monitoring_priorities": [
        "Watch competitor X's new product launch",
        "Track social sentiment on issue Y"
    ]
}

Provide strategic, actionable synthesis."""
)


# ============================================================================
# ROOT AGENT
# ============================================================================

root_agent = SequentialAgent(
    name="brand_intelligence",
    description="Multi-source brand intelligence gathering with parallel research + synthesis",
    sub_agents=[
        parallel_researchers,  # 4 sources searched simultaneously
        intelligence_synthesizer  # Then combine into insights
    ]
)
