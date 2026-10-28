import streamlit as st

from genai import generate_insight


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GenAI Subscriber Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* =======================================================
       GLOBAL THEME
    ======================================================= */

    :root {
        color-scheme: light dark;
    }

    .stApp {
        background-color: light-dark(
            #f5f7fb,
            #0f141c
        );

        color: light-dark(
            #172033,
            #e8edf5
        );
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }


    /* =======================================================
       HEADER
    ======================================================= */

    .main-title {
        font-size: 40px;
        font-weight: 800;

        color: light-dark(
            #102a43,
            #f3f6fb
        );

        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }

    .subtitle {
        font-size: 16px;

        color: light-dark(
            #64748b,
            #aeb9c8
        );

        margin-bottom: 25px;
    }


    /* =======================================================
       SIDEBAR
    ======================================================= */

    section[data-testid="stSidebar"] {
        background-color: light-dark(
            #eef2f7,
            #1a1f2b
        );

        border-right: 1px solid light-dark(
            #dbe2ea,
            #2c3442
        );
    }

    section[data-testid="stSidebar"] * {
        color: light-dark(
            #1f2937,
            #f2f5f9
        );
    }

    section[data-testid="stSidebar"] code {
        color: light-dark(
            #0f7a50,
            #58d68d
        );
    }


    /* =======================================================
       CHAT MESSAGE CONTAINER
    ======================================================= */

    div[data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 10px 14px;
        margin-bottom: 10px;

        border: 1px solid light-dark(
            #e5eaf0,
            #303746
        );

        box-shadow: 0 3px 12px
            light-dark(
                rgba(15, 39, 71, 0.04),
                rgba(0, 0, 0, 0.30)
            );
    }


    /* =======================================================
       USER MESSAGE
    ======================================================= */

    div[data-testid="stChatMessage"]:has(
        div[data-testid="stChatMessageAvatarUser"]
    ) {
        background-color: light-dark(
            #eef3f9,
            #2a2f39
        );
    }


    /* =======================================================
       ASSISTANT MESSAGE
    ======================================================= */

    div[data-testid="stChatMessage"]:has(
        div[data-testid="stChatMessageAvatarAssistant"]
    ) {
        background-color: light-dark(
            #ffffff,
            #171c24
        );
    }


    /* =======================================================
       CHAT TEXT
    ======================================================= */

    div[data-testid="stChatMessage"] p,
    div[data-testid="stChatMessage"] li,
    div[data-testid="stChatMessage"] span,
    div[data-testid="stChatMessage"] div {
        color: light-dark(
            #1d2939,
            #f1f5f9
        ) !important;
    }


    /* =======================================================
       CHAT INPUT AREA
    ======================================================= */

    div[data-testid="stChatInput"] {
        background-color: light-dark(
            #ffffff,
            #161b22
        );
    }

    div[data-testid="stChatInput"] textarea {
        background-color: light-dark(
            #f8fafc,
            #222834
        ) !important;

        color: light-dark(
            #172033,
            #f1f5f9
        ) !important;

        border: 1px solid light-dark(
            #d9e0e8,
            #3a4252
        ) !important;

        border-radius: 12px !important;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: light-dark(
            #8a98aa,
            #8f9bad
        ) !important;
    }


    /* =======================================================
       CHAT SEND BUTTON
    ======================================================= */

    div[data-testid="stChatInput"] button {
        background-color: light-dark(
            #e9eef5,
            #2b3240
        ) !important;

        color: light-dark(
            #102a43,
            #f1f5f9
        ) !important;

        border-radius: 10px !important;
    }


    /* =======================================================
       BUTTONS
    ======================================================= */

    .stButton > button {
        background-color: light-dark(
            #ffffff,
            #222834
        );

        color: light-dark(
            #172033,
            #f1f5f9
        );

        border: 1px solid light-dark(
            #d6dde6,
            #3a4252
        );

        border-radius: 10px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: light-dark(
            #edf2f7,
            #2d3442
        );

        border-color: light-dark(
            #b9c4d0,
            #4b5568
        );
    }


    /* =======================================================
       GENERAL TEXT
    ======================================================= */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    p,
    label {
        color: light-dark(
            #172033,
            #f1f5f9
        );
    }


    /* =======================================================
       DIVIDERS
    ======================================================= */

    hr {
        border-color: light-dark(
            #dde4ec,
            #303746
        );
    }


    /* =======================================================
       CODE
    ======================================================= */

    code {
        background-color: light-dark(
            #eef2f7,
            #212733
        );

        color: light-dark(
            #0f7a50,
            #67e8a5
        );

        border-radius: 5px;
        padding: 2px 5px;
    }


    /* =======================================================
       SPINNER / STATUS TEXT
    ======================================================= */

    div[data-testid="stSpinner"] {
        color: light-dark(
            #475569,
            #d0d7e2
        );
    }


    /* =======================================================
       SCROLLBAR
    ======================================================= */

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: light-dark(
            #f1f5f9,
            #161b22
        );
    }

    ::-webkit-scrollbar-thumb {
        background: light-dark(
            #c1cad6,
            #3b4555
        );

        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: light-dark(
            #9eabba,
            #526072
        );
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        GenAI Subscriber Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Ask natural-language questions about subscriber performance,
        churn, spending, plans, and regions.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🤖 GenAI Subscriber Assistant"
    )

    st.write(
        "A GenAI-powered analytics assistant that combines "
        "subscriber data analysis with natural-language insights."
    )

    st.divider()

    st.markdown(
        "### 🎯 Project Capabilities"
    )

    st.write(
        "• Query subscriber data using natural language"
    )

    st.write(
        "• Analyze subscriber counts by region and plan"
    )

    st.write(
        "• Calculate average subscriber spending"
    )

    st.write(
        "• Measure churn and retention performance"
    )

    st.write(
        "• Analyze average subscriber tenure"
    )

    st.write(
        "• Compare active and churned subscribers"
    )

    st.write(
        "• Generate business-friendly insights using OpenAI"
    )

    st.write(
        "• Ground GenAI responses using verified Pandas metrics"
    )

    st.divider()

    st.markdown(
        "### ⚙️ How It Works"
    )

    st.caption(
        "Natural-language query → Query Parser → "
        "Pandas Analytics → Verified Metrics → "
        "OpenAI → Business Insight"
    )

    st.divider()

    st.markdown(
        "### 💬 Sample Prompt"
    )

    st.info(
        "Tell me about Premium subscribers in the South region."
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# INITIALIZE CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask about your subscriber data..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # SAVE USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # --------------------------------------------------------
    # DISPLAY USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message(
        "user"
    ):

        st.markdown(
            question
        )

    # --------------------------------------------------------
    # GENERATE AI RESPONSE
    # --------------------------------------------------------

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Analyzing subscriber data..."
        ):

            try:

                response = generate_insight(
                    question
                )

                st.markdown(
                    response
                )

            except Exception as error:

                response = (
                    "An error occurred while generating "
                    "the subscriber insight."
                )

                st.error(
                    response
                )

                st.caption(
                    str(error)
                )

    # --------------------------------------------------------
    # SAVE ASSISTANT RESPONSE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
