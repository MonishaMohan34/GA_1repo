
# from fastapi import FastAPI, Form, UploadFile, File, HTTPException
# import openai

# app = FastAPI()

# # OpenAI API Setup
# OPENAI_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjMwMDIwOTFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.COZ_4kVMSwz0jqlAlTFV9wWqiYtOGiai4Qu3wqZW1gA"
# openai.api_key = OPENAI_API_KEY

# SYSTEM_PROMPT = """You are an AI assistant for the IIT Madras Online Degree in Data Science course.
# Answer graded assignment questions accurately.

# Question: {question}

# If the question asks for a command’s output, return only the exact output.
# If the question refers to a file (e.g., ZIP, CSV, PDF), extract and analyze it.
# If the question contains code, execute it and return the result.

# Provide only the final answer in this format:  
# { "answer": "<your response here>" }"""

# @app.post("/api/")
# async def answer_question(question: str = Form(...)):
#     try:
#         print(f"Received question: {question}")  # Debug log

#         # Call GPT-4o-mini with custom system prompt
#         response = openai.ChatCompletion.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT.replace("{question}", question)},
#                 {"role": "user", "content": question}
#             ]
#         )

#         # Extract the answer from response
#         answer = response["choices"][0]["message"]["content"].strip()
#         return {"answer": answer}

#     except Exception as e:
#         print(f"Error: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")



from fastapi import FastAPI, Form, HTTPException
import openai
import os

app = FastAPI()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjMwMDIwOTFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.COZ_4kVMSwz0jqlAlTFV9wWqiYtOGiai4Qu3wqZW1gA")
import openai

client = openai.OpenAI(
    api_key="eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjMwMDIwOTFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.COZ_4kVMSwz0jqlAlTFV9wWqiYtOGiai4Qu3wqZW1gA",
    base_url="http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"  # Replace with actual AI Proxy base URL
)  # Correctly initialize client

# System Prompt
SYSTEM_PROMPT = """You are an AI assistant for the IIT Madras Online Degree in Data Science course.
Answer graded assignment questions accurately.

Question: {question}

If the question asks for a command’s output, return only the exact output.
If the question refers to a file (e.g., ZIP, CSV, PDF), extract and analyze it.
If the question contains code, execute it and return the result.

Provide only the final answer in this format:  
{ "answer": "<your response here>" }"""

@app.post("/api/")
async def answer_question(question: str = Form(...)):
    try:
        print(f"Received question: {question}")  # Debug log

        # Call GPT-4o-mini with the correct API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.replace("{question}", question)},
                {"role": "user", "content": question}
            ]
        )

        # Extract answer
        answer = response.choices[0].message.content.strip()
        return {"answer": answer}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
