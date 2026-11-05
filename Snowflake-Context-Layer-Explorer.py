import streamlit as st

st.set_page_config(page_title="Snowflake Context Layer Explorer", layout="wide")

st.title("Snowflake Context Layer for AI-Powered BI")
st.caption("Concepts from the session on how context unlocks AI-powered BI (Cortex Sense, Semantic Views, Business Ontology, Horizon Context, etc.)")

st.markdown("""
High-quality analytical + business context is required for agents to answer multi-domain, reasoning-style questions 
(e.g., “Why did revenue drop last quarter?”). Context lives in query history, BI models, dbt, docs, CRM hierarchies, 
and people’s heads. Snowflake’s context layer collects, enriches, and activates it.
""")

# Dataset of concepts/tools
concepts = [
    {
        "name": "Cortex Sense",
        "category": "Always-on Context",
        "description": "Always-on managed context layer. Automatically learns business definitions, metrics, relationships, and rules from query history, metadata, dashboards, and existing semantic views. Serves relevant context to agents (CoWork / CoCo) at runtime. Improves accuracy significantly on complex enterprise questions.",
        "link": "https://www.snowflake.com/en/blog/enterprise-ai-agents-grounded-context/",
        "status": "Private preview / coming to public preview"
    },
    {
        "name": "Semantic Views",
        "category": "Executable Analytical Context",
        "description": "First-party curated, executable context. Schema-level objects that define metrics, dimensions, facts, relationships/joins, and business logic. Deterministic calculations for agents, BI tools, and SQL. The gold standard for governed metric definitions.",
        "link": "https://docs.snowflake.com/en/user-guide/views-semantic/overview",
        "status": "Generally available"
    },
    {
        "name": "Business Ontology",
        "category": "Governed Business Graph",
        "description": "Governed graph of the business: concepts, entities, relationships, rules, constraints, policies, ownership, and approval status. Links business meaning to the semantic views/tables that implement it. Only approved definitions are served to agents.",
        "link": "https://www.snowflake.com/en/blog/business-ontology-context/",
        "status": "Public preview soon (part of Horizon Context)"
    },
    {
        "name": "Horizon Context",
        "category": "Context Layer",
        "description": "Governed context layer inside Horizon Catalog. Collects metadata (schemas, query logs, dashboards, popularity) from Snowflake + external sources, enriches it with business meaning, and activates it for people, BI tools, and AI agents.",
        "link": "https://www.snowflake.com/en/product/features/horizon-context/",
        "status": "Available (connectors in public preview)"
    },
    {
        "name": "Horizon Catalog",
        "category": "Catalog & Governance",
        "description": "Agentic catalog for all data (inside and outside Snowflake). Home of Horizon Context, semantic views, lineage, governance, security, and discovery. Enables one source of trusted context across tools and agents.",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-horizon",
        "status": "Available"
    },
    {
        "name": "Metadata Connectors (First-party)",
        "category": "Ingestion",
        "description": "First-party connectors that pull metadata, query history, dashboard definitions, and usage signals from sources such as query history, dbt, Tableau, Power BI, Sigma, SQL Server, PostgreSQL, and others into the Snowflake context layer.",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-horizon/horizon-context",
        "status": "Public preview (18+ sources)"
    },
    {
        "name": "MCP / External Agent Access",
        "category": "Activation",
        "description": "External agents can consume the context via MCP (Model Context Protocol) or Cortex code plug-ins. Snowflake-managed MCP servers can expose Cortex Agents, Analyst, Search, semantic views, and SQL as tools.",
        "link": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp",
        "status": "Available"
    },
    {
        "name": "Semantic Fuse / Interoperability",
        "category": "BI Interoperability",
        "description": "Query interface and interoperability layer so your favorite BI tools (Spot, Sigma, and others) and declarative experiences use the same governed context/semantic definitions instead of rebuilding them.",
        "link": "https://docs.snowflake.com/en/user-guide/views-semantic/overview",
        "status": "Invested / available via semantic views"
    },
    {
        "name": "CoWork & CoCo",
        "category": "Native Agents",
        "description": "Snowflake-native agent surfaces that consume the context layer. CoWork for knowledge workers; CoCo (formerly Cortex Code) for builders/engineers. Both benefit from Cortex Sense + Ontology + Semantic Views.",
        "link": "https://www.snowflake.com/en/product/features/cortex/",
        "status": "Available"
    }
]

# Filters
col1, col2 = st.columns([2, 1])
with col1:
    search = st.text_input("Search concepts", placeholder="Type to filter by name or description...")
with col2:
    categories = ["All"] + sorted(list(set(c["category"] for c in concepts)))
    category_filter = st.selectbox("Category", categories)

# Filter data
filtered = concepts
if search:
    search_lower = search.lower()
    filtered = [c for c in filtered if search_lower in c["name"].lower() or search_lower in c["description"].lower()]
if category_filter != "All":
    filtered = [c for c in filtered if c["category"] == category_filter]

st.subheader(f"Concepts ({len(filtered)})")

# Display as expandable cards with links
for concept in filtered:
    with st.expander(f"**{concept['name']}** — {concept['category']}", expanded=False):
        st.markdown(f"**Status:** {concept['status']}")
        st.write(concept["description"])
        st.link_button(f"Open {concept['name']}", concept["link"], type="primary")

st.divider()
st.markdown("""
**Why context matters** (from the session):  
Text-to-SQL in a single domain is largely solved. The next frontier is agents that reason across domains, understand business rules (fiscal calendars, pricing changes, renewal logic, account hierarchies), and answer “why” questions. High-quality context collected from query history, BI models, pipelines, docs, and governed definitions is what unlocks reliable AI-powered BI.
""")

st.caption("Links point to official Snowflake documentation and product pages. Statuses are approximate based on public announcements as of late 2026.")
