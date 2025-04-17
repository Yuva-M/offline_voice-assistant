import subprocess

DEFAULT_PROMPT = (
    "You are an AI assistant that engages in human-like conversation. "
    "Your responses should be simple, concise, and written in plain language, "
    "using short paragraphs and avoiding overly complex words."
    "use very short paragraph to explain the answers."
)

def query_llm(prompt):
    """
    Queries the Ollama LLM (llama3.2) using subprocess.
    It concatenates the default prompt with the user's prompt,
    and returns the model's output.
    """
    full_prompt = f"{DEFAULT_PROMPT}\n\nUser: {prompt}"
    
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2", full_prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",    # Specify UTF-8 encoding
            errors="replace",    # Replace characters that fail to decode
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error querying LLM: {e.stderr}"

def main():
    print("Welcome to your AI assistant powered by Ollama and Llama3.2!")
    print("This assistant responds in a human-like, concise, and simple manner.")
    print("Type 'exit' or 'quit' to end the session.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting assistant. Goodbye!")
            break
        
        result = query_llm(user_input)
        print("Assistant:", result, "\n")

if __name__ == "__main__":
    main()
