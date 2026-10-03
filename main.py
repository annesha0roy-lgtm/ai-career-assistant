print("================================")
print("      AI CAREER ASSISTANT")
print("================================")

name = input("What is your name? ")
interest = input("What area are you interested in? ")

print("\nHello,", name + "!")

if "ai" in interest.lower():
    print("\nCareer suggestions:")
    print("- AI/ML Engineer")
    print("- AI Application Developer")
    print("- Python Developer")

    print("\nRecommended roadmap:")
    print("1. Learn Python")
    print("2. Learn NumPy and Pandas")
    print("3. Learn Machine Learning")
    print("4. Explore LLMs")
    print("5. Build AI projects")

elif "web" in interest.lower():
    print("\nCareer suggestions:")
    print("- Frontend Developer")
    print("- Backend Developer")
    print("- Full Stack Developer")

    print("\nRecommended roadmap:")
    print("1. Learn HTML and CSS")
    print("2. Learn JavaScript")
    print("3. Learn a backend language")
    print("4. Learn databases")
    print("5. Build web projects")

else:
    print("\nCareer suggestions:")
    print("- Software Developer")
    print("- Technical Analyst")
    print("- Data Analyst")

print("\nKeep learning and keep building! 🚀")
