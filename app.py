import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Career Roadmap & Skill Gap Finder",
    page_icon="🚀",
    layout="wide"
)

# App Header
st.title("🚀 AI Career Roadmap & Skill Gap Finder")
st.markdown("Compare your current skills with your target tech role, identify skill gaps, and follow a personalized 8-week learning plan.")

# Role Definitions Database
ROLES_DB = {
    "Data Scientist": {
        "required_skills": ["Advanced Python", "NumPy & Pandas", "SQL", "Statistics & Math", "Scikit-Learn", "Git & GitHub"],
        "phases": [
            ("Weeks 1-2: Advanced Python & NumPy", "Master Python data structures, functions, OOP, and NumPy for numerical computing."),
            ("Weeks 3-4: Pandas & Data Visualization", "Learn Pandas DataFrames, data cleaning, and plotting with Matplotlib and Seaborn."),
            ("Weeks 5-6: SQL & Exploratory Data Analysis (EDA)", "Connect databases, write SQL JOINs, and execute structured EDA workflows."),
            ("Weeks 7-8: Machine Learning Foundations", "Build supervised learning models using Scikit-Learn and evaluate performance metrics.")
        ],
        "projects": [
            ("Exploratory Data Analysis Dashboard", "Analyze public datasets using Pandas and Seaborn to uncover hidden trends."),
            ("SQL-Powered Business Intelligence Report", "Populate a SQL database and write complex queries to answer business questions."),
            ("Predictive Housing Price Model", "Build a Scikit-Learn model to predict housing prices or customer churn.")
        ]
    },
    "AI/ML Engineer": {
        "required_skills": ["Advanced Python", "NumPy & Pandas", "Deep Learning / PyTorch", "Scikit-Learn", "Git & GitHub", "Node.js / APIs"],
        "phases": [
            ("Weeks 1-2: Python OOP & Linear Algebra", "Master advanced Python features and mathematical foundations for ML."),
            ("Weeks 3-4: Classical ML with Scikit-Learn", "Implement regression, classification, and model evaluation techniques."),
            ("Weeks 5-6: Neural Networks & PyTorch", "Build multi-layer perceptrons and train deep learning models using PyTorch."),
            ("Weeks 7-8: Model Deployment & APIs", "Wrap models into REST APIs using FastAPI or Flask and deploy them.")
        ],
        "projects": [
            ("Custom Image Classifier with PyTorch", "Train a convolutional neural network to classify custom image categories."),
            ("Real-time Sentiment Analysis API", "Deploy a transformer-based text classification model behind a REST API."),
            ("End-to-End Recommendation Engine", "Build a collaborative filtering recommendation system for e-commerce.")
        ]
    },
    "Frontend Web Developer": {
        "required_skills": ["HTML/CSS", "JavaScript", "React", "Git & GitHub", "Node.js / APIs"],
        "phases": [
            ("Weeks 1-2: Modern JavaScript ES6+", "Master modern JS syntax, arrow functions, async/await, and DOM manipulation."),
            ("Weeks 3-4: Responsive Layouts & CSS", "Build mobile-first layouts using CSS Grid, Flexbox, and Tailwind CSS."),
            ("Weeks 5-6: React Components & Hooks", "Learn state management, useEffect, custom hooks, and component architecture."),
            ("Weeks 7-8: API Integration & Performance", "Connect REST APIs, handle loading states, and optimize app performance.")
        ],
        "projects": [
            ("Interactive Weather Dashboard", "Build a weather app fetching live data from third-party APIs with search history."),
            ("Task Management Kanban Board", "Create a Trello-style drag-and-drop task tracker with local storage."),
            ("E-Commerce Product Storefront", "Design a responsive store with filtering, sorting, and shopping cart state.")
        ]
    },
    "Full Stack Developer": {
        "required_skills": ["HTML/CSS", "JavaScript", "React", "Node.js / APIs", "SQL", "Git & GitHub"],
        "phases": [
            ("Weeks 1-2: JavaScript & Frontend Basics", "Solidify core JavaScript and DOM manipulation fundamentals."),
            ("Weeks 3-4: React UI Architecture", "Build reusable component libraries and manage complex application state."),
            ("Weeks 5-6: Node.js & Express APIs", "Build backend servers, middleware, authentication, and REST endpoints."),
            ("Weeks 7-8: Databases & Deployment", "Integrate SQL databases, connect frontend to backend, and deploy full-stack apps.")
        ],
        "projects": [
            ("Personal Finance Tracker", "Full-stack app with user auth, expense categorization, and SQL storage."),
            ("Real-Time Markdown Notes App", "Build a markdown editor with live preview and cloud database sync."),
            ("Event Booking Platform", "Create an event registration platform with seat booking and confirmation emails.")
        ]
    }
}

ALL_SKILLS = [
    "C", "Basic Python", "Advanced Python", "HTML/CSS", "JavaScript", 
    "React", "SQL", "NumPy & Pandas", "Statistics & Math", 
    "Scikit-Learn", "Deep Learning / PyTorch", "Git & GitHub", "Node.js / APIs"
]

# Sidebar Controls
st.sidebar.header("🎯 Configuration")
target_role = st.sidebar.selectbox("Select Target Job Role", list(ROLES_DB.keys()))
study_hours = st.sidebar.slider("Weekly Study Hours", min_value=4, max_value=25, value=10, step=1)

st.sidebar.subheader("Select Your Current Skills")
user_skills = []
for skill in ALL_SKILLS:
    if st.sidebar.checkbox(skill, value= skill in ["C", "Basic Python", "HTML/CSS"]):
        user_skills.append(skill)

# Main Analysis
role_data = ROLES_DB[target_role]
required_skills = role_data["required_skills"]

have_skills = [s for s in required_skills if s in user_skills]
missing_skills = [s for s in required_skills if s not in user_skills]

st.markdown("---")
st.subheader("📊 Skill Gap Analysis")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### ✅ Skills You Already Have")
    if have_skills:
        for s in have_skills:
            st.success(f"• {s}")
    else:
        st.info("None of the core required skills selected yet.")

with col2:
    st.markdown("### 🛠️ Skills to Learn")
    if missing_skills:
        for s in missing_skills:
            st.warning(f"• {s}")
    else:
        st.balloons()
        st.success("🎉 You already have all the core required skills for this role!")

# 8-Week Roadmap
st.markdown("---")
st.subheader(f"📅 Your Personalized 8-Week Roadmap ({study_hours} hrs/week)")

for i, (phase_title, phase_desc) in enumerate(role_data["phases"]):
    with st.expander(f"Week {(i*2)+1}-{(i*2)+2}: {phase_title}", expanded=(i==0)):
        st.markdown(f"**Focus:** {phase_desc}")
        st.markdown(f"*{max(4, study_hours // 2)} hours per week allocated to theory & coding practice.*")

# Portfolio Projects
st.markdown("---")
st.subheader("💡 3 Recommended Portfolio Projects")

proj_cols = st.columns(3)
for idx, (p_title, p_desc) in enumerate(role_data["projects"]):
    with proj_cols[idx]:
        st.markdown(f"### Project {idx+1}")
        st.markdown(f"**{p_title}**")
        st.write(p_desc)
