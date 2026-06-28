import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_cover_letter(cv_text, jd_text):
    prompt = f"""
    ----------------------
    STRUCTURE (in order):
    ----------------------
    --------
    HEADER:
    --------
    - Your contact details (name, email, phone, location extracted from the CV)
    - Recipient details (company name, hiring manager extracted from the job description if present)
    - Date
    - Subject line (job title extracted from the job description)
    Salutation — "Dear [Name]" or "Dear Hiring Committee"

    ------
    BODY:
    ------
    3–4 to the point short paragraphs:
    - Open with which role, why this company specifically 
    - For skills match 2–3 concrete achievements mapped to JD requirements extracted from CV
    - Explain why this company and role is a good fit for you, and how you can contribute to the company
    - Make the entire content relevant to the job description and the company, avoid generic statements
    - Avoid repeating the CV content, instead complement it with examples and facts
    - Make the entire conversation sound like talking to a human, not a machine. Avoid robotic language.
    - Don't use bullet points, write in full prose only. Avoid emotional language, stay formal and professional.
    - End with a closing paragraph that expresses interest in an interview and appreciation for the opportunity to apply.

    -----------
    FOOTER:
    -----------
    Closing: availability for interview, "Regards" or "Sincerely", your name [extracted from the CV]


    --------------------------
    RULES MUST FOLLOW:
    --------------------------
    - Exactly one page, formal business letter format 
    - No bullet points, fully written prose only
    - Mirror language and keywords from the job posting 
    - Complement the CV, never repeat it, use examples and facts instead
    - Short, clear paragraphs, stay formal, avoid emotional language
    - Extract user details from the CV automatically

    --------------------------
    CV:
    --------------------------
    {cv_text}   

    ---------------------------
    JOB DESCRIPTION:
    ---------------------------
    {jd_text}   

    ----------------------------
    Return in JSON format with the following keys:
    ----------------------------
    - "header": the generated cover letter header
    - "body": the generated cover letter body
    - "footer": the generated cover letter footer
    ----------------------------
    
    """
    response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are acting as a German HR who hires people for the German Company based on their cover letter quality. Help in creating an inspiring cover letter."},
        {"role": "user", "content": prompt}
    ]
    )
    return response.choices[0].message.content
   