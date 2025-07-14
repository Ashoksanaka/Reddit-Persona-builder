from scraper import fetch_user_data
from persona_generator import generate_persona
import json

def process_user(username):
    print(f"\nProcessing user: {username}")
    data = fetch_user_data(username)
    posts = data['posts'][:5]
    comments = data['comments'][:5]
    with open(f"output/{username}_data.json", "w") as f:
        json.dump(data, f, indent=2)
    persona = generate_persona(posts, comments)
    with open(f"output/{username}_persona.txt", "w") as f:
        f.write(persona)

    print(f"✅ Persona saved to: output/{username}_persona.txt")

if __name__ == "__main__":
    for user in ["kojied", "Hungry-Move-6603"]:
        process_user(user)
