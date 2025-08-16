import requests

BASE_URL = "http://localhost:8000"

def safe_post(endpoint, payload):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload)
    print(f"\n>>> Calling {url}")
    print("STATUS:", response.status_code)
    print("RAW:", response.text)  # debug
    try:
        return response.json()
    except Exception:
        return {"error": response.text}

def get_essay(topic):
    return safe_post("/essay/invoke", {"input": {"topic": topic}})

def get_poem(topic):
    return safe_post("/poem/invoke", {"input": {"topic": topic}})

def get_groq(message):
    return safe_post("/groqai/invoke", {"input": message})

if __name__ == "__main__":
    print("Essay:", get_essay("Artificial Intelligence"))
    print("Poem:", get_poem("Nature"))
    print("Groq:", get_groq("Explain quantum computing in simple terms"))
