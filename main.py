# CareerPath AI
# AI Career Exploration Assistant for College Students

print("=" * 60)
print("                 CAREERPATH AI")
print("        AI Career Exploration Assistant")
print("=" * 60)

print("\nWelcome! Let's explore a career path that fits you.")
print("Answer a few questions and we'll create a practical career roadmap.\n")

# -----------------------------
# STUDENT INFORMATION
# -----------------------------

name = input("What's your name? ")

degree = input("What are you studying? (Example: BCA, B.Tech, BBA): ")

year = input("Which year/semester are you currently in? ")

print("\nWhat area interests you the most?")
print("1. Artificial Intelligence / Machine Learning")
print("2. Software Development")
print("3. Data Analytics")
print("4. Cybersecurity")
print("5. Business + Technology")
print("6. UI/UX & Product Design")

interest = input("\nEnter the number of your choice: ")

print("\nWhich skill do you currently know best?")
print("1. Python")
print("2. Java / C / C++")
print("3. HTML / CSS / JavaScript")
print("4. Data / Excel")
print("5. Communication / Business")
print("6. I'm still a beginner")

skill = input("\nEnter the number of your choice: ")

print("\nWhat is your main career goal?")
print("1. Get a job in a good tech company")
print("2. Become an AI/ML professional")
print("3. Become a software developer")
print("4. Work in data/analytics")
print("5. Build my own product/startup")
print("6. I'm still exploring")

goal = input("\nEnter the number of your choice: ")


# -----------------------------
# CAREER RECOMMENDATION ENGINE
# -----------------------------

career = ""
description = ""
skills = []
roadmap = []
projects = []

if interest == "1":
    career = "AI / Machine Learning Engineer"
    description = (
        "You seem interested in building intelligent systems and working "
        "with modern AI technologies."
    )

    skills = [
        "Python",
        "Data Structures & Algorithms",
        "Statistics & Mathematics",
        "Machine Learning",
        "Deep Learning",
        "LLMs and Generative AI",
        "Git & GitHub"
    ]

    roadmap = [
        "Month 1: Strengthen Python fundamentals",
        "Month 2: Learn DSA and problem solving",
        "Month 3: Learn NumPy, Pandas and ML fundamentals",
        "Month 4: Build your first Machine Learning project",
        "Month 5: Learn LLMs, APIs and AI applications",
        "Month 6: Build and deploy a real-world AI project"
    ]

    projects = [
        "AI Career Recommendation Assistant",
        "AI Resume Analyzer",
        "Student Study Assistant",
        "College FAQ Chatbot"
    ]

elif interest == "2":
    career = "Software Developer"
    description = (
        "Your interests point toward building applications, websites "
        "and software products."
    )

    skills = [
        "Programming Fundamentals",
        "Data Structures & Algorithms",
        "Git & GitHub",
        "Backend Development",
        "APIs",
        "Databases",
        "System Design Basics"
    ]

    roadmap = [
        "Month 1: Strengthen programming fundamentals",
        "Month 2: Learn DSA",
        "Month 3: Learn backend development",
        "Month 4: Learn APIs and databases",
        "Month 5: Build a full-stack project",
        "Month 6: Deploy your project and prepare for interviews"
    ]

    projects = [
        "Student Management System",
        "College Event Platform",
        "Job Application Tracker",
        "Personal Finance Dashboard"
    ]

elif interest == "3":
    career = "Data Analyst"
    description = (
        "You may enjoy working with data, finding patterns and "
        "turning information into useful decisions."
    )

    skills = [
        "Excel",
        "SQL",
        "Python",
        "Pandas",
        "Data Visualization",
        "Statistics",
        "Power BI / Tableau"
    ]

    roadmap = [
        "Month 1: Excel and data fundamentals",
        "Month 2: Learn SQL",
        "Month 3: Learn Python for data analysis",
        "Month 4: Learn Pandas and visualization",
        "Month 5: Build analytics projects",
        "Month 6: Create a portfolio and prepare for interviews"
    ]

    projects = [
        "Student Performance Dashboard",
        "Sales Analytics Dashboard",
        "College Placement Analysis",
        "Student Attendance Analytics"
    ]

elif interest == "4":
    career = "Cybersecurity Professional"
    description = (
        "You may enjoy understanding systems, networks and how "
        "digital information can be protected."
    )

    skills = [
        "Computer Networks",
        "Linux",
        "Python",
        "Cybersecurity Fundamentals",
        "Web Security",
        "Ethical Hacking Concepts",
        "Security Tools"
    ]

    roadmap = [
        "Month 1: Computer fundamentals",
        "Month 2: Networking fundamentals",
        "Month 3: Linux",
        "Month 4: Cybersecurity fundamentals",
        "Month 5: Practice security labs",
        "Month 6: Build security projects and portfolio"
    ]

    projects = [
        "Password Strength Analyzer",
        "Network Monitoring Dashboard",
        "Phishing Awareness Tool",
        "Basic Security Log Analyzer"
    ]

elif interest == "5":
    career = "Technology & Product Professional"
    description = (
        "Your interests combine technology with business, making "
        "product management, technology consulting and entrepreneurship "
        "potential career directions."
    )

    skills = [
        "Technology Fundamentals",
        "Product Management",
        "Business Communication",
        "Data Analysis",
        "Market Research",
        "AI Tools",
        "Leadership"
    ]

    roadmap = [
        "Month 1: Strengthen technology fundamentals",
        "Month 2: Learn product management basics",
        "Month 3: Learn data and market research",
        "Month 4: Study real technology products",
        "Month 5: Create a product case study",
        "Month 6: Build and present your own product idea"
    ]

    projects = [
        "AI Career Guidance Platform",
        "Student Productivity App",
        "Campus Marketplace",
        "AI-Powered Student Assistant"
    ]

elif interest == "6":
    career = "UI/UX & Product Designer"
    description = (
        "You may enjoy understanding users and designing simple, "
        "useful digital experiences."
    )

    skills = [
        "UI Design",
        "UX Research",
        "Figma",
        "Wireframing",
        "Prototyping",
        "Product Thinking",
        "User Research"
    ]

    roadmap = [
        "Month 1: Learn UI/UX fundamentals",
        "Month 2: Learn Figma",
        "Month 3: Practice wireframes",
        "Month 4: Conduct user research",
        "Month 5: Design a complete product",
        "Month 6: Build a professional portfolio"
    ]

    projects = [
        "College Student App",
        "Career Exploration Platform",
        "Campus Event Application",
        "Student Productivity Dashboard"
    ]

else:
    career = "Technology Explorer"
    description = (
        "You're still exploring your options, which is completely normal. "
        "Start by experimenting with different technology areas."
    )

    skills = [
        "Programming Fundamentals",
        "Python",
        "Git & GitHub",
        "Communication",
        "Problem Solving",
        "Basic AI Concepts"
    ]

    roadmap = [
        "Month 1: Learn programming fundamentals",
        "Month 2: Try Python",
        "Month 3: Explore web development",
        "Month 4: Explore AI and data",
        "Month 5: Build a small project",
        "Month 6: Choose your strongest career direction"
    ]

    projects = [
        "Personal Portfolio Website",
        "Student Management System",
        "AI Chatbot",
        "Career Exploration Tool"
    ]


# -----------------------------
# PERSONALIZED REPORT
# -----------------------------

print("\n\n" + "=" * 60)
print("                 YOUR CAREER REPORT")
print("=" * 60)

print(f"\nHello, {name}! 👋")

print(f"\nEducation: {degree}")
print(f"Current Level: {year}")

print("\n🎯 RECOMMENDED CAREER")
print("-" * 60)
print(career)

print("\nWhy this could be a good direction:")
print(description)

print("\n📚 SKILLS TO DEVELOP")
print("-" * 60)

for i, item in enumerate(skills, 1):
    print(f"{i}. {item}")

print("\n🗺️ 6-MONTH ROADMAP")
print("-" * 60)

for step in roadmap:
    print("• " + step)

print("\n💡 PROJECT IDEAS")
print("-" * 60)

for i, project in enumerate(projects, 1):
    print(f"{i}. {project}")

print("\n🚀 YOUR NEXT STEP")
print("-" * 60)

if skill == "6":
    print(
        "Start with the fundamentals. Don't try to learn everything "
        "at once. Pick one skill and practice consistently."
    )
else:
    print(
        "Use your existing skill as a starting point and gradually "
        "add the skills listed in your roadmap."
    )

print("\nRemember:")
print(
    "A career is not decided by one test. Explore, build projects, "
    "gain experience and adjust your direction as you learn."
)

print("\n" + "=" * 60)
print("             CAREERPATH AI • Explore. Learn. Build.")
print("=" * 60)





