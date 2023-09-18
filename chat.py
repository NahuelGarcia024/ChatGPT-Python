import openai
import sys

openai.api_key = "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"

chat_history = []

while True:
    prompt = input(">>> ")
    if prompt == "exit":
        break
    else:
        
        chat_history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True,
            max_tokens=150,
            )
    collected_messages = []

    for chunk in response:
        chunk_messages = chunk["choices"][0]["delta"] ##messages
        collected_messages.append(chunk_messages)
        fully_reply_content = "".join([m.get("content","")for m in collected_messages])
        print(fully_reply_content)
        print("\033-[H\033[J", end="") ##clear screen on mac linux windows
    
    chat_history.append({"role": "assistant", "content": fully_reply_content})
    print(fully_reply_content)