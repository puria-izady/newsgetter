# tools/rss_tools.py
from typing import List
from server import mcp
from utils.rss_reader import fetch_and_parse

DEFAULT_FEEDS = [
    # Tier 1 — Must-Have (Primary Sources)
    "https://openai.com/blog/rss.xml",                      # GPT announcements
    "https://www.anthropic.com/rss.xml",                    # Claude updates
    "https://blog.google/technology/ai/rss/",               # Gemini, DeepMind
    "https://blog.google/technology/developers/rss/",               # Gemini, DeepMind
    "https://aws.amazon.com/blogs/machine-learning/feed/",  # Bedrock, SageMaker
    "https://huggingface.co/blog/feed.xml",                 # Open source models
    "https://ai.meta.com/blog/rss/",                        # Llama, research
    
    # Tier 2 — Curated Newsletters (via RSS)
    "https://www.deeplearning.ai/the-batch/feed/",         # The Batch (Andrew Ng)
    "https://simonwillison.net/atom/everything/",          # LLM tooling insights
    "https://www.latent.space/feed",                       # AI engineering
    
    # Tier 3 — Community Signals
    "https://hnrss.org/newest?q=AI+OR+LLM+OR+GPT",         # Hacker News (AI)
    "https://www.reddit.com/r/MachineLearning/.rss",       # r/MachineLearning
    "http://export.arxiv.org/rss/cs.AI"                    # ArXiv cs.AI
]

@mcp.tool()
def get_digest(limit: int) -> List[str]:
    """
    Fetch up to `limit` items from your default RSS feeds.
    Returns a list of strings "title: link".
    """
    entries = fetch_and_parse(DEFAULT_FEEDS, limit)
    # Return raw entries; the LLM client will then summarize them.
    return [f"{e.title}: {e.link}" for e in entries]
