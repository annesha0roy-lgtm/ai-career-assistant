




print("========================================")
print("      AI CAREER & PLACEMENT ASSISTANT")
print("========================================")

print("\nLet's find some career options for you!\n")

name = input("Enter your name: ")
education = input("What are you studying? (e.g., BCA, BTech, BBA): ")
skills = input("What skills do you have? (e.g., Python, SQL, Java): ").lower()
interests = input("What are you interested in? (e.g., AI, business, web development): ").lower()
experience = input("Do you have any internship/project experience? (yes/no): ").lower()

print("\n----------------------------------------")
print("Career Analysis for", name)
print("----------------------------------------")

careers = []

# AI / ML
if "python" in skills and ("ai" in interests or "machine learning" in interests or "ml" in interests):
    careers.append("AI/ML Engineer")

# Data
if ("python" in skills or "sql" in skills) and ("data" in interests or "analytics" in interests):
    careers.append("Data Analyst")

# Python development
if "python" in skills and ("development" in interests or "backend" in interests or "software" in interests):
    careers.append("Python Developer")

# Web development
if ("html" in skills or "javascript" in skills or "js" in skills) and "web" in interests:
    careers.append("Web Developer")

# Business / Management
if "business" in interests or "management" in interests:
    careers.append("Business / Product Management")

# If nothing matches
if len(careers) == 0:
    careers.append("Software Developer")
    careers.append("Data Analyst")

print("\nRecommended Career Paths:")

for career in careers:
    print("•", career)

print("\n----------------------------------------")
print("Recommended Skills to Learn")
print("----------------------------------------")

print("• Python")
print("• SQL")
print("• Data Structures & Algorithms")
print("• Git & GitHub")
print("• Communication Skills")

if "ai" in interests or "machine learning" in interests or "ml" in interests:
    print("• Machine Learning")
    print("• Large Language Models (LLMs)")

if "web" in interests:
    print("• HTML, CSS and JavaScript")

print("\n----------------------------------------")
print("Experience")
print("----------------------------------------")

if experience == "yes":
    print("Great! Your internship/project experience can strengthen your resume.")
else:
    print("Try building 2-3 projects and completing an internship.")

print("\n========================================")
print("        CAREER PLAN COMPLETE!")
print("========================================")
