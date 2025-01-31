import ollama

completions = ollama.chat(
    model="deepseek-r1:latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Why sky is blue?"}
    ],
)
