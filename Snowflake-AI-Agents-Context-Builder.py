import streamlit as st

st.set_page_config(page_title="Snowflake AI Agents & Context Builder", page_icon="❄️", layout="wide")

# Sidebar navigation
st.sidebar.title("❄️ Snowflake AI Builder")
section = st.sidebar.radio(
    "Navigate",
    [
        "Overview & Problems Solved",
        "Horizon Catalog & Context Layers",
        "Cortex AI Gateway (Trust Boundary)",
        "Adaptive Compute & Cost Control",
        "Build Trusted Agents & Apps",
        "Interactive Checklist & Resources"
    ]
)

# ========== OVERVIEW ==========
if section == "Overview & Problems Solved":
    st.title("Snowflake AI: From Access to Trusted, Contextual, Cost-Controlled Agents")
    st.markdown("""
    **Core insight from the notes:** Models need access to your data, but *access ≠ context*.  
    LLMs do not know your products, customers, vendors, business rules, or how your company runs.  
    Agents are moving from answering questions to taking actions across ERP, partners, vendors, Salesforce, Workday, ServiceNow, etc.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Problems")
        st.markdown("""
        - Data spread across Snowflake accounts, regions, ERPs, pipelines, partners
        - Schemas ≠ business rules → confident wrong answers
        - Agents can leak data or take unauthorized actions
        - Fixed compute sized for peak → pay for idle
        - Governance is often onerous or fragmented
        - Cost spirals from pilot to production
        """)
    with col2:
        st.subheader("Snowflake Solution")
        st.markdown("""
        - **One governed view** via Horizon Catalog (zero-copy, open with Iceberg/Polaris)
        - **Context layers**: Cortex Sense + Business Ontology + Semantic Views
        - **One trust boundary**: Cortex AI Gateway (identity, policy, tools, models, data)
        - **Adaptive Compute** that tracks demand
        - Budgets, per-user quotas, model routing, abuse detection
        - Fresh data + lineage + observability
        """)

    st.info("Result: AI that understands business meaning, acts safely under existing RBAC, and scales without runaway cost.")

# ========== CONTEXT LAYERS ==========
elif section == "Horizon Catalog & Context Layers":
    st.title("Horizon Catalog + Context Layers")
    st.markdown("""
    **Horizon Catalog** is the universal agent catalog. It provides one governed foundation for data and AI assets (inside and outside Snowflake), with zero-copy sharing (Apache Polaris / Iceberg), lineage, and consistent policies.
    
    Three complementary context layers ensure every agent gets the same trusted answer:
    """)

    tab1, tab2, tab3 = st.tabs(["Cortex Sense", "Business Ontology", "Semantic Views"])

    with tab1:
        st.subheader("Cortex Sense")
        st.markdown("""
        Always-on inferred context. Automatically discovers metadata, query patterns, usage history, joins, and definitions across your estate (including external sources via connectors).
        - Value on day one without manual building
        - Surfaces entities, metrics, relationships, and conflicts
        - Promote useful findings into the ontology
        """)
        st.link_button("Learn more", "https://www.snowflake.com/en/product/features/horizon-context/")

    with tab2:
        st.subheader("Business Ontology")
        st.markdown("""
        Governed official meaning of business terms, entities, relationships, and metrics.  
        Defines *what* something means, who owns it, and approved definitions.  
        Independent of any single data model. Agents receive only approved definitions.
        """)
        st.image("https://www.snowflake.com/content/dam/snowflake-site/blog/2026/11/expedition-business-ontology.png", use_container_width=True)
        st.link_button("Business Ontology blog", "https://www.snowflake.com/en/blog/business-ontology-context/")

    with tab3:
        st.subheader("Semantic Views")
        st.markdown("""
        Executable definitions. Package tables, relationships, dimensions, facts, and metrics into a native Snowflake object.  
        Agents, BI tools, and SQL all query the same governed logic (no guessing joins or calculations).
        """)
        st.code("""
CREATE OR REPLACE SEMANTIC VIEW sales_analytics
TABLES (
    orders PRIMARY KEY (order_id),
    customers PRIMARY KEY (customer_id),
    products PRIMARY KEY (product_id)
)
RELATIONSHIPS (
    orders (customer_id) REFERENCES customers,
    order_lines (product_id) REFERENCES products
)
DIMENSIONS (
    orders.order_date,
    customers.region,
    products.category
)
METRICS (
    total_revenue AS SUM(order_lines.amount),
    avg_order_value AS AVG(orders.total)
);
        """, language="sql")
        st.markdown("[Semantic Views docs](https://docs.snowflake.com/en/user-guide/views-semantic/overview)")

    st.success("Together: Sense (discover) → Ontology (govern meaning) → Semantic Views (execute consistently).")

# ========== AI GATEWAY ==========
elif section == "Cortex AI Gateway (Trust Boundary)":
    st.title("Cortex AI Gateway: One Trust Boundary")
    st.markdown("""
    Every request from any agent (Cortex Agents, CoCo, CoWork, external agents, MCP tools, third-party models) flows through one control plane.
    
    **Controls how agents access models, tools, and data.**
    """)

    st.subheader("Key Capabilities")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**Observability**\n- Centralized agent traces (OpenTelemetry)\n- Session & conversation grouping\n- Full lifecycle visibility")
    with cols[1]:
        st.markdown("**Security & Guardrails**\n- AI rails (prompt injection, jailbreaks)\n- Agent abuse detection (trajectories)\n- MCP tool governance (auth, rate limits, RBAC)")
    with cols[2]:
        st.markdown("**Cost & Routing**\n- Dynamic model routing\n- Per-user / team budgets & quotas\n- Attribution by user, role, agent, app")

    st.markdown("""
    **Cortex Sandboxes**: Secure private space for agents to run custom code alongside governed data (inherits user permissions).  
    **Integrations**: Native MCP support (100+ servers: Salesforce, ServiceNow, Slack, SAP, etc.) with policy enforcement.
    """)

    st.link_button("Cortex AI Gateway docs", "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-gateway")
    st.link_button("Gateway blog & architecture", "https://www.snowflake.com/en/blog/cortex-ai-gateway-control-plane-enterprise-ai/")

# ========== COST & COMPUTE ==========
elif section == "Adaptive Compute & Cost Control":
    st.title("Scale Without Surprise Bills")
    st.markdown("""
    Fixed capacity sized for peak means you pay for idle. Adaptive Compute tracks demand.
    """)

    st.subheader("Adaptive Compute (Adaptive Warehouses)")
    st.markdown("""
    - Workload-aware: right-sizes per query automatically
    - Shared pool of compute (no reserved idle capacity)
    - Up to 2.4× better throughput on analytics, up to 5.2× faster on DML-heavy work (cost similar to Gen2)
    - Set performance goals; Snowflake handles the rest
    """)
    st.link_button("Adaptive Compute docs", "https://docs.snowflake.com/en/user-guide/warehouses-adaptive")
    st.link_button("Product page", "https://www.snowflake.com/en/product/features/adaptive-compute/")

    st.subheader("AI Cost Governance")
    st.markdown("""
    - Visibility: who spent what (down to query tags, user, agent)
    - Budgets + alerts
    - Per-user quotas (daily/weekly/monthly) with hard blocking
    - Anomaly detection + AI-powered explanations
    - Model routing for better efficiency
    """)

    # Simple interactive estimator
    st.markdown("---")
    st.subheader("Rough Cost Planner")
    users = st.slider("Number of active users / agents", 1, 200, 20)
    daily_credits = st.number_input("Estimated daily credits per user", min_value=0.1, value=5.0, step=0.5)
    monthly = users * daily_credits * 22  # rough business days
    st.metric("Estimated monthly credits", f"{monthly:,.0f}")
    st.caption("Use actual ACCOUNT_USAGE views and AI_GATEWAY_USAGE_HISTORY for real numbers. Set quotas early.")

# ========== BUILDER GUIDE ==========
elif section == "Build Trusted Agents & Apps":
    st.title("Build Apps Start-to-Finish")
    st.markdown("Follow these steps to create governed, contextual, cost-controlled agentic applications.")

    steps = [
        ("1. Unify & Govern Data", "Bring data into Snowflake (or federate). Use Horizon Catalog. Enable automatic sensitive data classification, tags, masking, and data movement policies."),
        ("2. Add Context", "Create Semantic Views for key metrics. Define Business Ontology terms. Let Cortex Sense discover additional context."),
        ("3. Establish Trust Boundary", "Route all agents/models/tools through Cortex AI Gateway. Set model allowlists, AI rails, and MCP policies."),
        ("4. Control Cost", "Create Adaptive Warehouses. Set per-user quotas and team budgets on the gateway and AI features."),
        ("5. Build Agents", "Use CoCo (coding agent) or CoWork. Create Cortex Agents with semantic views, skills, and sandboxes. Schedule automations."),
        ("6. Deploy & Observe", "Expose via MCP, Streamlit in Snowflake, or external apps. Monitor traces, abuse detection, and spend in the Trust Center / AI Gateway.")
    ]

    for title, desc in steps:
        with st.expander(title, expanded=False):
            st.write(desc)

    st.subheader("Sample Agent Patterns")
    st.markdown("""
    - **Analytics agent**: Semantic view + Cortex Analyst / CoWork for “why did revenue drop?”
    - **Action agent**: MCP tools (Salesforce, ServiceNow) + Gateway policies + Sandbox for custom logic
    - **Background automation**: CoCo Automations that check data quality or generate reports on a schedule
    - **Hybrid lookup**: Hybrid tables for fast operational lookups + analytical data
    """)

    st.info("All actions inherit existing Snowflake roles and policies. No separate agent identity model required.")

# ========== CHECKLIST & RESOURCES ==========
elif section == "Interactive Checklist & Resources":
    st.title("Governance Checklist & Resources")

    if "checks" not in st.session_state:
        st.session_state.checks = {
            "horizon": False, "ontology": False, "semantic": False,
            "gateway": False, "quotas": False, "adaptive": False,
            "classification": False, "observability": False
        }

    st.subheader("Setup Checklist")
    c1, c2 = st.columns(2)
    with c1:
        st.session_state.checks["horizon"] = st.checkbox("Horizon Catalog active with connectors", st.session_state.checks["horizon"])
        st.session_state.checks["semantic"] = st.checkbox("Key Semantic Views created", st.session_state.checks["semantic"])
        st.session_state.checks["ontology"] = st.checkbox("Business Ontology terms approved", st.session_state.checks["ontology"])
        st.session_state.checks["classification"] = st.checkbox("Sensitive data classified & tagged", st.session_state.checks["classification"])
    with c2:
        st.session_state.checks["gateway"] = st.checkbox("All agents routed through AI Gateway", st.session_state.checks["gateway"])
        st.session_state.checks["quotas"] = st.checkbox("Per-user quotas & budgets set", st.session_state.checks["quotas"])
        st.session_state.checks["adaptive"] = st.checkbox("Adaptive Warehouses in use for variable workloads", st.session_state.checks["adaptive"])
        st.session_state.checks["observability"] = st.checkbox("Traces & abuse detection reviewed", st.session_state.checks["observability"])

    done = sum(st.session_state.checks.values())
    st.progress(done / 8)
    st.caption(f"{done}/8 items complete")

    st.subheader("Official Resources")
    resources = {
        "Horizon Catalog": "https://www.snowflake.com/en/product/features/horizon/",
        "Horizon Context": "https://www.snowflake.com/en/product/features/horizon-context/",
        "Business Ontology": "https://www.snowflake.com/en/blog/business-ontology-context/",
        "Semantic Views": "https://docs.snowflake.com/en/user-guide/views-semantic/overview",
        "Cortex AI Gateway": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-gateway",
        "Adaptive Compute": "https://docs.snowflake.com/en/user-guide/warehouses-adaptive",
        "CoCo & Automations": "https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-automations",
        "Cortex Agents": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents",
        "Expedition 2026 announcements": "https://www.snowflake.com/en/news/press-releases/expedition-2026-business-ontology-ai-gateway/"
    }
    for name, url in resources.items():
        st.link_button(name, url)

st.sidebar.markdown("---")
st.sidebar.caption("Built from Snowflake Expedition 2026 concepts. Always verify current GA/preview status in official docs.")
