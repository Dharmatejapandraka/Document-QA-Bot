from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

topics = [
    "Artificial Intelligence",
    "Cloud Computing",
    "Cybersecurity",
    "Data Science"
]

for topic in topics:

    prompt = f"""
Generate a very detailed study material about {topic}.

Include:
- Introduction
- History
- Concepts
- Types
- Architecture
- Algorithms
- Advantages
- Disadvantages
- Applications
- Real-world examples
- Interview questions
- FAQs
- Future scope

Generate at least 10000 words.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    filename = topic.lower().replace(" ", "_") + ".txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.choices[0].message.content)

    print(f"Saved {filename}")