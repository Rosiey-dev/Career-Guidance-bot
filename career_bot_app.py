import streamlit as st

st.set_page_config(page_title="CareerBot AI", page_icon="🤖")

st.title("🤖 CareerBot: AI Career Guidance")
st.write("Answer the questions below to get a career suggestion:")

# Input fields
interests = st.text_input("🌟 What are your interests?")
skills = st.text_input("🛠️ What are your main skills?")
subject = st.text_input("📚 What is your favorite subject?")

def suggest_career(interests, skills, subject):
    interests = interests.lower()
    skills = skills.lower()
    subject = subject.lower()

    if "ai" in interests or "artificial intelligence" in interests or "machine learning" in interests or "deep learning" in interests or "neural networks" in interests:
        return "💡 AI Engineer or ML Researcher"
    if "math" in interests or "calculation" in interests or "analysis" in interests or "statistics" in interests:
        return "💡 Data Analyst"
    if "biology" in interests or "medicine" in interests or "health" in interests or "nursing" in interests or "care" in interests or "anatomy" in interests:
        return "💡 Doctor or Nurse"
    if "physics" in interests or "engineering" in interests or "mechanics" in interests or "construction" in interests:
        return "💡 Mechanical Engineer"
    if "chemistry" in interests or "pharmacy" in interests or "labs" in interests or "drugs" in interests or "research" in interests:
        return "💡 Pharmacist or Chemist"
    if "computers" in interests or "technology" in interests or "software" in interests or "programming" in interests or "coding" in interests:
        return "💡 Software Developer"
    if "business" in interests or "economics" in interests or "finance" in interests or "accounting" in interests:
        return "💡 Business Analyst or Accountant"
    if "education" in interests or "teaching" in interests or "learning" in interests or "pedagogy" in interests:
        return "💡 Teacher or Education Specialist"
    if "art" in interests or "design" in interests or "creativity" in interests or "drawing" in interests or "illustration" in interests:
        return "💡 Graphic Designer or Illustrator"
    if "writing" in interests or "english" in interests or "language" in interests or "journalism" in interests or "communication" in interests:
        return "💡 Content Writer or Journalist"
    if "law" in interests or "justice" in interests or "politics" in interests or "debate" in interests:
        return "💡 Lawyer or Legal Advisor"
    if "finance" in interests or "investment" in interests or "banking" in interests or "money" in interests or "markets" in interests:
        return "💡 Financial Advisor or Banker"
    if "environment" in interests or "nature" in interests or "geography" in interests or "earth" in interests:
        return "💡 Environmental Scientist"
    if "history" in interests or "social science" in interests or "archaeology" in interests:
        return "💡 Historian or Anthropologist"
    if "psychology" in interests or "mental health" in interests or "behavior" in interests:
        return "💡 Psychologist or Counselor"
    if "sports" in interests or "fitness" in interests or "coaching" in interests:
        return "💡 Fitness Trainer or Sports Coach"
    if "music" in interests or "instruments" in interests or "singing" in interests or "composition" in interests:
        return "💡 Musician or Music Producer"
    if "drama" in interests or "acting" in interests or "film" in interests or "stage" in interests:
        return "💡 Actor or Director"
    if "marketing" in interests or "sales" in interests or "advertising" in interests or "promotion" in interests:
        return "💡 Marketing Specialist"
    if "leadership" in interests or "organization" in interests or "management" in interests:
        return "💡 Project Manager or Entrepreneur"

    return "💡 Explore careers in your areas of interest — education, healthcare, business, design, tech, or more!"


# Button
if st.button("Get Career Suggestion"):
    if interests and skills and subject:
        suggestion = suggest_career(interests, skills, subject)
        st.success(f"🎯 CareerBot Suggestion: {suggestion}")
    else:
        st.warning("Please fill in all the fields above.")
