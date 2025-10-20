import ollama

def query_ollama(prompt="Why is the sky blue?"):
    """
    Sends a prompt to the 'my-gemma' model using Ollama and prints the response.
    """
    try:
        response = ollama.chat(
            model='my-gemma',
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ],
        )
        print(response['message']['content'])
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure that the 'ollama' library is installed (`pip install ollama`) and that the Ollama service is running.")
        print("Also, make sure you have the 'my-gemma' model installed (`ollama run my-gemma`).")

