import streamlit as st

st.set_page_config(page_title="CareerBot AI", page_icon="🤖")

st.title("🤖 CareerBot: AI Career Guidance")
st.write("Answer the questions below to get a tech career suggestion:")

# Input fields
interests = st.text_input("🌟 What are your interests?")
skills = st.text_input("🛠️ What are your main skills?")
subject = st.text_input("📚 What is your favorite subject?")

def suggest_career(interests, skills, subject):
    interests = interests.lower()
    skills = skills.lower()
    subject = subject.lower()

    if "ai" in interests or "machine learning" in interests or "python" in skills:
        return "💡 AI Developer or Machine Learning Engineer"
    if "data" in interests or "analysis" in skills or "math" in subject:
        return "💡 Data Analyst or Data Scientist"
    if "linux" in skills or "infrastructure" in interests:
        return "💡 Linux Systems Engineer or DevOps Specialist"
    if "cloud" in interests or "networking" in skills:
        return "💡 Cloud Engineer or Cloud Solutions Architect"
    if "security" in interests or "ethical hacking" in skills:
        return "💡 Cybersecurity Analyst or Penetration Tester"
    if "apps" in interests or "software" in skills:
        return "💡 Software Developer or Full Stack Engineer"
    if "design" in interests or "creativity" in skills:
        return "💡 UX/UI Designer or Product Designer"
    if "business" in subject or "project management" in skills:
        return "💡 IT Project Manager or Business Analyst"
    return "💡 Explore careers in Tech, AI, Data, or Cloud. Keep learning!"

# Button
if st.button("Get Career Suggestion"):
    if interests and skills and subject:
        suggestion = suggest_career(interests, skills, subject)
        st.success(f"🎯 CareerBot Suggestion: {suggestion}")
    else:
        st.warning("Please fill in all the fields above.")
