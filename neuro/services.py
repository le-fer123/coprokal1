from openai import OpenAI
client = OpenAI(api_key='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')

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Общайся как быдло"},
        {
            "role": "user",
            "content": "Что такое двач"
        }
    ]
)

print(completion.choices[0].message)