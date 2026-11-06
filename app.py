"""
CSIT 349 - Autobiography and Portfolio App
Gia Meggie Quijano | CSIT349 G01
Run with:  streamlit run app.py
"""
from pathlib import Path

import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# PAGE SETUP
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Gia Meggie Quijano | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

NAME = "Gia Meggie Quijano"
SECTION = "CSIT349 G01"
EMAIL = "giameggie.quijano@cit.edu"
GITHUB = "https://github.com/chonkychonkin"
LOCATION = "Cebu City, Philippines"
SUCCESS_MSG = (
    "Thank you for reaching out! Your message has been sent successfully. "
    "I'll get back to you soon!"
)

# ----------------------------------------------------------------------------
# STYLE: Soft Pink Minimalist (Poppins headings, Inter body, rounded cards)
# ----------------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');

:root {
  --rose: #FB6F92;
  --pink: #FF8FAB;
  --petal: #FFB3C6;
  --blush: #FFC2D1;
  --mist: #FFE5EC;
  --ink: #4A2B36;
}

html, body, [class*="css"], .stApp, p, li, label, span, div {
  font-family: 'Inter', sans-serif;
}
h1, h2, h3, h4, h5 {
  font-family: 'Poppins', sans-serif !important;
  color: var(--ink);
  letter-spacing: -0.01em;
}
h1 { color: var(--rose) !important; font-weight: 700 !important; }

.stApp { background: #FFF5F8; }
.block-container { padding-top: 2.2rem; max-width: 1150px; }

/* Sidebar */
section[data-testid="stSidebar"] {
  background: var(--mist);
  border-right: 1px solid var(--blush);
}

/* Rounded cards (bordered containers) */
div[data-testid="stVerticalBlockBorderWrapper"] {
  border-radius: 22px !important;
  border-color: var(--blush) !important;
  background: #FFFFFF;
  box-shadow: 0 6px 20px rgba(251, 111, 146, 0.08);
}

/* Metrics */
div[data-testid="stMetric"] {
  background: #FFFFFF;
  border: 1px solid var(--blush);
  border-radius: 20px;
  padding: 14px 18px;
  box-shadow: 0 4px 14px rgba(251, 111, 146, 0.08);
}
div[data-testid="stMetricValue"] { color: var(--rose); font-family: 'Poppins', sans-serif; }

/* Buttons */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button,
a[data-testid="stLinkButton"], div[data-testid="stLinkButton"] a {
  border-radius: 999px !important;
  border: 1px solid var(--pink) !important;
  background: var(--rose) !important;
  color: #fff !important;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  padding: 0.45rem 1.4rem;
  transition: all .15s ease-in-out;
}
.stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover {
  background: var(--pink) !important;
  transform: translateY(-1px);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 6px; }
.stTabs [data-baseweb="tab"] {
  border-radius: 999px;
  padding: 8px 18px;
  background: var(--mist);
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
}
.stTabs [aria-selected="true"] { background: var(--rose) !important; color: #fff !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

/* Images, expanders, inputs */
img { border-radius: 24px; }
div[data-testid="stExpander"] { border-radius: 16px; border-color: var(--blush); background: #fff; }
.stTextInput input, .stTextArea textarea { border-radius: 14px !important; }

/* Small pill label */
.pill {
  display: inline-block; padding: 3px 12px; margin: 2px 4px 2px 0;
  border-radius: 999px; background: var(--mist); color: var(--rose);
  border: 1px solid var(--blush); font-size: 0.82rem; font-weight: 500;
}
.eyebrow {
  color: var(--pink); font-family: 'Poppins', sans-serif; font-weight: 600;
  letter-spacing: .12em; text-transform: uppercase; font-size: .8rem; margin-bottom: 0;
}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# DATA
# ----------------------------------------------------------------------------
BASE = Path(__file__).parent


def find_photo() -> str:
    """Use profile.jpg/png if you add one, otherwise the labeled placeholder."""
    for name in ("profile.jpg", "profile.jpeg", "profile.png"):
        for folder in (BASE, BASE / "assets"):
            if (folder / name).exists():
                return str(folder / name)
    return str(BASE / "assets" / "profile_placeholder.png")


PHOTO = find_photo()


@st.cache_data
def load_skills() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Skill": [
                "HTML & CSS", "Java", "C Programming", "JavaScript",
                "React.js", "Python", "UI/UX Design", "Office & Google Workspace",
            ],
            "Rating": [8, 7, 7, 6, 6, 6, 8, 9],
            "Category": [
                "Web", "Programming", "Programming", "Web",
                "Web", "Programming", "Design", "Productivity",
            ],
        }
    )


@st.cache_data
def load_milestones() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Year": [2022, 2023, 2024, 2025, 2026],
            "Milestone": [
                "Began exploring programming and information technology",
                "Started pursuing a Bachelor of Science in Information Technology",
                "Developed foundational skills in programming, web development, and database concepts",
                "Worked on academic software projects involving web development and application design",
                "Expanded interests toward UI/UX design, data science, and practical software solutions",
            ],
        }
    )


PROJECTS = [
    {
        "title": "Zomato Restaurant Insights",
        "type": "Data Science",
        "emoji": "📊",
        "role": "Group member: dataset selection, data cleaning, and K-means clustering",
        "tools": ["Python", "pandas", "scikit-learn", "K-means", "Random Forest"],
        "outcome": (
            "Explored the Zomato restaurant dataset (India) with K-means clustering, "
            "a Random Forest classifier, and cuisine association rules. Presented the "
            "findings in a recorded group presentation and submitted the midterm project."
        ),
    },
    {
        "title": "TeknoTrack Test Suite",
        "type": "Software QA",
        "emoji": "🧪",
        "role": "Test analyst (paired activity): requirement analysis and test case writing",
        "tools": ["Excel", "Test Clarification Document", "FSD analysis"],
        "outcome": (
            "Analyzed the TeknoTrack Ticket Management functional specification, logged "
            "open questions in a Test Clarification Document, and wrote a test suite with "
            "up to five test cases per requirement, including cases awaiting clarification."
        ),
    },
    {
        "title": "Student Org Attendance Tracking",
        "type": "Research",
        "emoji": "📝",
        "role": "Individual researcher: problem exploration and literature review",
        "tools": ["Related literature review", "Problem analysis", "Google Workspace"],
        "outcome": (
            "Studied inefficient management of student organization activities and "
            "narrowed the problem down to attendance tracking as the pain point to solve."
        ),
    },
]

QUICK_FACTS = [
    "I was born and raised in Cebu City. 🌴",
    "I went to Southwestern University from elementary all the way to senior high school.",
    "I love both gaming and art. 🎮🎨",
    "My programming journey started in 2022.",
    "Lately I am drawn to UI/UX design and data science.",
]

skills_df = load_skills()
milestones_df = load_milestones()

# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
st.session_state.setdefault("fact_idx", 0)
st.session_state.setdefault("messages", [])

# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    st.image(PHOTO, width=150)
    st.markdown(f"### {NAME}")
    st.caption(f"BSIT, 4th Year  ·  {SECTION}")
    st.markdown(f"📍 {LOCATION}")
    st.link_button("GitHub", GITHUB)
    st.markdown(f"✉️ [{EMAIL}](mailto:{EMAIL})")

    st.divider()
    st.markdown("#### 🎛️ Skill explorer")
    st.caption("These controls filter the Skills tab.")
    min_rating = st.slider("Minimum rating", 1, 10, 1)
    categories = st.multiselect(
        "Categories",
        sorted(skills_df["Category"].unique()),
        default=sorted(skills_df["Category"].unique()),
    )
    show_table = st.checkbox("Show data table", value=True)
    sort_choice = st.radio("Sort by", ["Rating (high to low)", "Name (A to Z)"])

    st.divider()
    st.metric("Messages sent this session", len(st.session_state["messages"]))

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
hero_img, hero_text = st.columns([1, 2.2], gap="large", vertical_alignment="center")

with hero_img:
    st.image(PHOTO, caption="Photo placeholder: swap in profile.jpg" if "placeholder" in PHOTO else None)

with hero_text:
    st.markdown('<p class="eyebrow">Portfolio · Autobiography</p>', unsafe_allow_html=True)
    st.title(NAME)
    st.subheader("4th Year BS Information Technology Student")
    st.write(
        "A quiet yet curious individual who enjoys gaming, exploring new interests, "
        "and continuously learning new things. I strive to grow both personally and "
        "professionally while keeping an open mind to new opportunities and experiences."
    )
    st.markdown(
        '<span class="pill">UI/UX</span><span class="pill">Web Development</span>'
        '<span class="pill">Data Science</span><span class="pill">Gaming</span>'
        '<span class="pill">Art</span>',
        unsafe_allow_html=True,
    )

st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Year level", "4th")
m2.metric("Projects", len(PROJECTS))
m3.metric("Skills tracked", len(skills_df))
m4.metric("Average skill rating", f"{skills_df['Rating'].mean():.1f}/10")

st.write("")

# ----------------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------------
tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["🌸 About Me", "📖 Autobiography", "✨ Skills", "💼 Projects", "💌 Contact"]
)

# ---- ABOUT ------------------------------------------------------------------
with tab_about:
    left, right = st.columns([1.4, 1], gap="large")

    with left:
        with st.container(border=True):
            st.header("Hello, I am Gia 👋")
            st.markdown(
                """
I am a **4th year BSIT student** from **Cebu City**. I describe myself as quiet but
curious: I like to observe, learn how things work, and then try them out myself.

Outside of class you will usually find me **gaming** or making **art**. Both keep me
creative, and both quietly shaped my interest in **UI/UX design**, where visuals
and problem solving meet.
"""
            )
            st.caption("Name and section: Gia Meggie Quijano · CSIT349 G01")

    with right:
        with st.container(border=True):
            st.subheader("🎲 Get to know me")
            st.write(QUICK_FACTS[st.session_state["fact_idx"]])
            if st.button("Show another fact"):
                st.session_state["fact_idx"] = (st.session_state["fact_idx"] + 1) % len(QUICK_FACTS)
                st.rerun()
            st.caption(f"Fact {st.session_state['fact_idx'] + 1} of {len(QUICK_FACTS)}")

# ---- AUTOBIOGRAPHY ----------------------------------------------------------
with tab_story:
    c1, c2 = st.columns(2, gap="large")

    with c1:
        with st.container(border=True):
            st.subheader("🏡 Background")
            st.write(
                "I was born and raised in Cebu City, Philippines. Growing up here "
                "gave me a love for learning and a calm, observant personality."
            )
        st.write("")
        with st.container(border=True):
            st.subheader("🎓 Education")
            st.markdown(
                """
- **Southwestern University**: elementary up to senior high school
- **Bachelor of Science in Information Technology**: 2023 to present (4th year)
"""
            )

    with c2:
        with st.container(border=True):
            st.subheader("🎮 Interests")
            interests = st.selectbox(
                "Pick an interest to read about",
                ["Gaming", "Art", "Learning new things"],
            )
            if interests == "Gaming":
                st.write("Gaming is how I unwind and stay curious about interactive design.")
            elif interests == "Art":
                st.write("Art lets me express ideas visually and feeds my love of UI/UX.")
            else:
                st.write("I enjoy picking up new topics and keeping an open mind to new experiences.")

    st.write("")
    st.subheader("🗓️ Milestones")
    expand_all = st.checkbox("Expand all milestones", value=False)
    for i, row in milestones_df.iterrows():
        with st.expander(f"{row['Year']}", expanded=expand_all or i == len(milestones_df) - 1):
            st.write(row["Milestone"])

    st.write("")
    summary_txt = (
        f"{NAME} ({SECTION})\n\nBSIT, 4th year. Cebu City.\n\nMilestones:\n"
        + "\n".join(f"{y}: {m}" for y, m in zip(milestones_df["Year"], milestones_df["Milestone"]))
    )
    st.download_button(
        "⬇️ Download my timeline (.txt)",
        summary_txt,
        file_name="gia_timeline.txt",
        mime="text/plain",
    )

# ---- SKILLS -----------------------------------------------------------------
with tab_skills:
    st.header("My skills")
    st.write(
        "My strongest areas are **Office & Google Workspace (9/10)**, **HTML & CSS (8/10)**, "
        "and **UI/UX Design (8/10)**. I am still growing in JavaScript, React.js, and Python, "
        "and I am actively practicing them through school projects."
    )

    filtered = skills_df[
        (skills_df["Rating"] >= min_rating) & (skills_df["Category"].isin(categories))
    ]
    if sort_choice.startswith("Rating"):
        filtered = filtered.sort_values("Rating", ascending=False)
    else:
        filtered = filtered.sort_values("Skill")

    if filtered.empty:
        st.info("No skills match the current filters in the sidebar.")
    else:
        ch_col, tb_col = st.columns([1.3, 1], gap="large")
        with ch_col:
            with st.container(border=True):
                st.subheader("Rating by skill")
                st.bar_chart(filtered, x="Skill", y="Rating", color="#FB6F92", horizontal=True)
        with tb_col:
            with st.container(border=True):
                st.subheader("Average by category")
                cat_avg = filtered.groupby("Category", as_index=False)["Rating"].mean()
                st.bar_chart(cat_avg, x="Category", y="Rating", color="#FF8FAB")

        if show_table:
            st.dataframe(
                filtered,
                hide_index=True,
                column_config={
                    "Rating": st.column_config.ProgressColumn(
                        "Rating", min_value=0, max_value=10, format="%d/10"
                    )
                },
            )

        st.subheader("Progress bars")
        pb1, pb2 = st.columns(2)
        for n, (_, r) in enumerate(filtered.iterrows()):
            with (pb1 if n % 2 == 0 else pb2):
                st.write(f"**{r['Skill']}** · {r['Rating']}/10")
                st.progress(int(r["Rating"]) / 10)

        st.download_button(
            "⬇️ Download skills (.csv)",
            filtered.to_csv(index=False),
            file_name="gia_skills.csv",
            mime="text/csv",
        )

# ---- PROJECTS ---------------------------------------------------------------
with tab_projects:
    st.header("Projects")
    f1, f2 = st.columns(2)
    with f1:
        type_filter = st.selectbox("Filter by type", ["All", "Data Science", "Software QA", "Research"])
    with f2:
        view = st.radio("View as", ["Cards", "Table"], horizontal=True)

    shown = [p for p in PROJECTS if type_filter == "All" or p["type"] == type_filter]

    if view == "Cards":
        cols = st.columns(3, gap="medium")
        for col, p in zip(cols, shown):
            with col:
                with st.container(border=True):
                    st.markdown(f"### {p['emoji']} {p['title']}")
                    st.markdown(f'<span class="pill">{p["type"]}</span>', unsafe_allow_html=True)
                    st.markdown(f"**My role:** {p['role']}")
                    st.markdown(
                        "**Tools:** " + " ".join(f'<span class="pill">{t}</span>' for t in p["tools"]),
                        unsafe_allow_html=True,
                    )
                    with st.expander("Outcome"):
                        st.write(p["outcome"])
    else:
        st.dataframe(
            pd.DataFrame(
                [
                    {
                        "Project": p["title"],
                        "Type": p["type"],
                        "Role": p["role"],
                        "Tools": ", ".join(p["tools"]),
                        "Outcome": p["outcome"],
                    }
                    for p in shown
                ]
            ),
            hide_index=True,
        )

    if not shown:
        st.info("No projects match that filter.")

# ---- CONTACT ----------------------------------------------------------------
with tab_contact:
    st.header("Let us connect")
    form_col, info_col = st.columns([1.6, 1], gap="large")

    with form_col:
        with st.container(border=True):
            with st.form("contact_form", clear_on_submit=True):
                name = st.text_input("Your name")
                email = st.text_input("Your email")
                topic = st.selectbox("Topic", ["Say hello", "Feedback on this site", "Collaboration", "Other"])
                rating = st.select_slider(
                    "How do you like the site?", options=["😐", "🙂", "😊", "😍", "🤩"], value="😊"
                )
                reply_pref = st.radio("Preferred reply", ["Email", "GitHub"], horizontal=True)
                message = st.text_area("Message", height=140)
                copy_me = st.checkbox("Send me a copy")
                submitted = st.form_submit_button("Send message")

            if submitted:
                if not name.strip() or "@" not in email or not message.strip():
                    st.error("Please enter your name, a valid email, and a message.")
                else:
                    st.session_state["messages"].append(
                        {"name": name, "topic": topic, "rating": rating}
                    )
                    st.success(SUCCESS_MSG)
                    st.toast("Message sent! 💌")
                    st.balloons()

    with info_col:
        with st.container(border=True):
            st.subheader("Find me")
            st.markdown(f"✉️ **Email**  \n{EMAIL}")
            st.markdown(f"🐙 **GitHub**  \n[{GITHUB.replace('https://', '')}]({GITHUB})")
            st.markdown(f"📍 **Location**  \n{LOCATION}")

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.divider()
st.caption(f"Built with Streamlit 🌸  ·  {NAME}  ·  {SECTION}")
