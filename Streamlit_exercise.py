import streamlit as st
st.title("Austin Li - Interactive Resume")
st.write("If you can see this, the app is running.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Austin Li - Interactive Resume")

st.header("About Me")
st.write("""
Finance and analytics professional with experience in private equity, equity research,
and financial modeling. Passed CFA Level II and experienced in credit analysis,
financial statement modeling, and investment research.
""")

# ---------------------------
# Interactive Widgets
# ---------------------------

experience = st.selectbox(
    "Select experience to view:",
    ["SPM Private Equity", "CITICS Securities"]
)

show_skills = st.checkbox("Show Technical Skills")

years_slider = st.slider(
    "Select years of experience to visualize",
    0, 5, 2
)

# ---------------------------
# Experience Section
# ---------------------------

st.header("Professional Experience")

if experience == "SPM Private Equity":
    st.write("""
    - Built integrated three-statement financial models
    - Conducted due diligence on 20+ private placement transactions
    - Created investment committee memorandums
    """)
    
elif experience == "CITICS Securities":
    st.write("""
    - Contributed to equity research reports
    - Prepared client presentation materials
    - Translated quantitative analysis into investment insights
    """)

# ---------------------------
# Skills Table
# ---------------------------

if show_skills:

    skills_data = {
        "Skill": ["Excel", "Financial Modeling", "Python", "Valuation", "Credit Analysis"],
        "Proficiency": ["Advanced", "Advanced", "Intermediate", "Advanced", "Advanced"]
    }

    skills_df = pd.DataFrame(skills_data)

    st.header("Skills")
    st.table(skills_df)

# ---------------------------
# Chart Example
# ---------------------------

st.header("Experience Timeline")

years = ["2021", "2022", "2023", "2024"]
experience_level = [1, 2, 3, years_slider]

fig, ax = plt.subplots()
ax.bar(years, experience_level)

ax.set_ylabel("Experience Level")
ax.set_title("Growth in Finance & Analytics Experience")

st.pyplot(fig)