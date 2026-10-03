
print("=" * 40)
print("       AI CAREER ASSISTANT")
print("=" * 40)

name = input("Enter your name: ")

print("\nChoose your area of interest:")
print("1. Artificial Intelligence")
print("2. Web Development")
print("3. Data Analytics")
print("4. Software Development")

choice = input("\nEnter your choice (1-4): ")

careers = {
    "1": {
        "roles": ["AI/ML Intern", "Python Developer", "AI Application Developer"],
        "skills": ["Python", "NumPy", "Pandas", "Machine Learning", "LLMs"]
    },
    "2": {
        "roles": ["Frontend Developer", "Backend Developer", "Full Stack Developer"],
        "skills": ["HTML", "CSS", "JavaScript", "APIs", "Databases"]
    },
    "3": {
        "roles": ["Data Analyst", "Business Analyst", "Junior Data Scientist"],
        "skills": ["Python", "SQL", "Excel", "Pandas", "Data Visualization"]
    },
    "4": {
        "roles": ["Software Developer", "Application Developer", "Backend Engineer"],
        "skills": ["Python", "Data Structures", "Algorithms", "Git", "APIs"]
    }
}

if choice in careers:
    result = careers[choice]

    print(f"\nHello, {name}!")
    print("\nSuggested career paths:")

    for role in result["roles"]:
        print("-", role)

    print("\nRecommended skills to learn:")

    for skill in result["skills"]:
        print("-", skill)

    print("\nYour learning roadmap:")
    print("1. Learn the fundamentals")
    print("2. Practice through small exercises")
    print("3. Build practical projects")
    print("4. Create a portfolio")
    print("5. Apply for internships")

else:
    print("\nInvalid choice. Please restart and select 1-4.")

print("\nKeep learning and building!")

