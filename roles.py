roles = {
    "AI Engineer": {
        "Python": 30,
        "Statistics & Mathematics": 20,
        "Machine Learning": 30,
        "Deep Learning": 10,
        "Projects": 10,
        "Data Engineering": 10,
        "Generative AI & LLMs": 30,
        "MLOps": 20,
        "Soft Skills": 10
    },

    "Data Scientist": {
        "Python": 25,
        "Statistics & Mathematics": 25,
        "Machine Learning & Artificial Intelligence": 20,
        "SQL": 15,
        "Projects": 15,
        "Data Wrangling & Engineering": 20,
        "Data Visualization & Communication": 20,
        "Business & Soft Skills": 10
    },

    "Data Analyst": {
        "SQL": 30,
        "Excel": 25,
        "Power BI": 25,
        "Python": 20,
        "Statistics": 20,
        "Data Visualization": 20,
        "Projects": 15,
        "Business Communication": 10
    },

    "Software Engineer": {
        "Programming Fundamentals": 20,
        "DSA": 40,
        "OOP": 20,
        "DBMS": 20,
        "Operating Systems": 15,
        "Computer Networks": 15,
        "Git & GitHub": 10,
        "Projects": 20,
        "Problem Solving": 20,
        "Soft Skills": 10
    },

    "Web Developer": {
        "HTML": 15,
        "CSS": 15,
        "JavaScript": 30,
        "React": 25,
        "Node.js": 20,
        "Express.js": 15,
        "MongoDB": 20,
        "Git & GitHub": 10,
        "Projects": 20,
        "Responsive Design": 10,
        "Soft Skills": 10
    }
}

# Generate list of all unique skills
all_skills = sorted({
    skill
    for role_data in roles.values()
    for skill in role_data.keys()
})