from roles import roles, all_skills
import streamlit as st


def find_missing_skills(user_skills, required_skills):

    missing = []

    for skill in required_skills:

        if skill.lower() not in [
            s.strip().lower()
            for s in user_skills
        ]:
            missing.append(skill)

    return missing


st.title("🚀 AI Career Mentor Agent")
st.markdown(
    "Analyze your skills, identify gaps, and get a personalized roadmap."
)

year = st.selectbox(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "Final Year"]
)


user_skills = st.multiselect(
    "Select Your Current Skills",
    all_skills,
    placeholder="Choose your skills..."
)
if not user_skills:
    st.warning("Please select at least one skill.")
    st.stop()

role = st.selectbox(
    "Target Role",
    [
        "AI Engineer",
        "Data Scientist",
        "Data Analyst",
        "Software Engineer",
        "Web Developer"
    ]
)

st.caption("Enter realistic study hours available each day")

hours = st.slider(
    "Study Hours Per Day",
    min_value=1,
    max_value=24,
    value=3
)

if st.button("Submit"):

    required_skills = roles[role].keys()

    missing_skills = find_missing_skills(
        user_skills,
        required_skills
    )

    st.write("Year:", year)
    st.write("Skills:", user_skills)
    st.write("Role:", role)
    st.write("Hours:", hours)

    total_skills = len(required_skills)
    matched_skills = total_skills - len(missing_skills)

    score = (matched_skills / total_skills) * 100

    st.subheader("📊 Match Score")
    st.metric("Career Match", f"{score:.1f}%")
    st.progress(int(score))

    st.subheader("❌ Skill Gap Analysis")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"• {skill}")
    else:
        st.success("No Skill Gaps Found!")

    st.subheader("📚 Recommended Study Plan")

    for skill in missing_skills:

        required_hours = roles[role][skill]

        days = max(
            1,
            round(required_hours / hours)
        )

        st.write(
            f"📚 {skill}: {required_hours} hours (~{days} days at {hours} hrs/day)"
        )

    if score >= 80:
        st.success("🚀 Job Ready")
    elif score >= 50:
        st.warning("⚡ Almost Ready")
    else:
        st.error("📖 Need More Skills")

    st.subheader("🗺️ Learning Roadmap")

    for i, skill in enumerate(missing_skills):
        st.write(
            f"Week {i+1}: Focus on {skill}"
        )