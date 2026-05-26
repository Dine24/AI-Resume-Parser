from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_summary(resume_text, jd_text):

    prompt = f"""
    Generate a concise professional summary
    based on this resume and job description.

    Resume:
    {resume_text[:3000]}

    Job Description:
    {jd_text[:2000]}
    """

    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
