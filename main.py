import streamlit as st
from dotenv import load_dotenv
import openai
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App Title
st.title("TalentScout Hiring Assistant Chatbot")
st.write("Welcome! I'm here to assist with your initial screening.")

# Collect User Information
with st.form("candidate_form"):
    name = st.text_input("Full Name", help="Enter your full name.")
    email = st.text_input("Email Address", help="Enter a valid email address.")
    phone = st.text_input("Phone Number", help="Enter your phone number.")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, help="Enter your total years of experience.")
    desired_position = st.text_input("Desired Position", help="Enter the position you're applying for.")
    current_location = st.text_input("Current Location", help="Enter your current city or location.")

    # Collect Tech Stack
    tech_stack = st.text_area("List your tech stack (e.g., Python, Django, MySQL)", help="Enter the technologies you are proficient in.")

    # Submit Button
    submitted = st.form_submit_button("Submit")

if submitted:
    if name and email and tech_stack:
        st.success(f"Thank you, {name}! Generating questions based on your tech stack...")
    else:
        st.error("Please fill in all required fields.")

# Generate Technical Questions Function
def generate_questions(tech_stack):
    prompt = (
        f"You are an expert technical interviewer. Generate 3-5 detailed technical interview questions "
        f"for a candidate proficient in the following tech stack: {tech_stack}. "
        f"Focus on practical implementation and problem-solving skills."
    )
    try:
        # Updated API call for openai.ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert interviewer skilled in generating technical questions."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if submitted and tech_stack:
    # Generate and display questions
    questions = generate_questions(tech_stack)
    st.write("### Here are your technical interview questions:")
    st.write(questions)

# Optional: Sentiment Analysis for User Feedback
def analyze_sentiment(feedback):
    prompt = f"Analyze the sentiment of the following feedback: '{feedback}'. Provide a summary of the sentiment."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in sentiment analysis."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Collect Feedback
st.write("---")
feedback = st.text_area("Provide your feedback on this chatbot (optional):")
if st.button("Submit Feedback"):
    if feedback:
        sentiment = analyze_sentiment(feedback)
        st.write("### Feedback Sentiment Analysis:")
        st.write(sentiment)
    else:
        st.warning("Please enter some feedback before submitting.")

# Conversation Exit
st.write("---")
end_conversation = st.text_input("Type 'exit' to end the chat")
if end_conversation.lower() == "exit":
    st.write("Thank you for using the Hiring Assistant! Goodbye!")
    st.stop()
