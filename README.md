TalentScout Hiring Assistant Chatbot
The TalentScout Hiring Assistant Chatbot is a user-friendly web application that streamlines the initial stages of technical hiring. Built using Streamlit and integrated with OpenAI’s GPT models, it allows recruiters to collect candidate details and generate personalized technical interview questions based on their tech stack.

#Features

1. Collects essential candidate details such as name, email, phone, experience, desired position, and location.
2. Generates 3–5 technical interview questions tailored to the candidate's specified tech stack.
3. User-friendly interface built with Streamlit.
4. Multilingual support (optional enhancement).
5. Optional sentiment analysis for evaluating candidate responses.


#Tech Stack

1. Python
2. Streamlit for the user interface
3. OpenAI GPT-3.5/4 for generating interview questions
4. dotenv for environment variable management


#Prerequisites

1. Python 3.8 or above installed on your system.
2. OpenAI API key.
3. Streamlit installed.


#Installation and Setup

1. Clone the repository:

git clone https://github.com/your-repo/talentscout-chatbot.git
cd talentscout-chatbot

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install the dependencies:

pip install -r requirements.txt

4. Add your OpenAI API key:

Create a .env file in the project root and add the following:
OPENAI_API_KEY=sk-xxxxxx
Alternatively, if using st.secrets, edit secrets.toml:
[default]
OPENAI_API_KEY = "sk-xxxxxx"

5. Run the application:

streamlit run main.py 


#Usage

1. Open the web app in your browser at http://localhost:8501.
2. Fill in the required candidate details:
Full Name
Email Address
Phone Number
Years of Experience
Desired Position 
Current Location
Tech Stack
3. Click Submit to generate technical interview questions.
4. View and copy the generated questions.


#File Structure

├── main.py                # Main application code
├── requirements.txt       # Python dependencies
├── .env                   # API key (not included in version control)
├── secrets.toml           # Optional: Streamlit secrets configuration
├── README.md              # Project documentation
└── .gitignore             # Ignored files/folders


#Requirements

The following packages are required and listed in requirements.txt:

streamlit
openai
python-dotenv

Install them with:

pip install -r requirements.txt


#Troubleshooting

Error: You tried to access openai.ChatCompletion, but this is no longer supported
Ensure you have upgraded the OpenAI package to the latest version:
pip install --upgrade openai
Ensure you are using openai.ChatCompletion.create for interacting with GPT models.

#Common Issues

Environment variable not found: Verify the .env file or st.secrets configuration.
Streamlit app not starting: Ensure all dependencies are installed, and you're using the correct Python version.


#Future Enhancements

Add sentiment analysis for evaluating candidate responses.
Integrate multilingual support for global hiring.
Store candidate details and responses in a database.


#License

This project is licensed under the MIT License.

#Contact

For queries or contributions, feel free to reach out to Aditya Jain.

