🌟 Daily Motivation Generator

This is a fun and friendly AI-powered web app that gives you short motivational messages based on your mood. Built using Streamlit and powered by the Cohere Command model, it’s perfect for daily inspiration.

✨ Features
- 🔁 "Generate Again" button  
- 💾 Download motivational message as .txt  
- 📋 Copy to clipboard with built‑in Streamlit UI  
- 🎭 Emoji mood picker  
- 🖤 Dark mode compatible

🚀 Setup Instructions

1. Clone the Repository
   git clone https://github.com/ayush126Kashyap/Daily-Motivation-Generator.git
   cd daily-motivation-generator

2. Install Dependencies
   pip install -r requirements.txt

3. Set Up Your API Key
   Recommended (Secure):
     • Create a .env file in the root directory containing:
       COHERE_API_KEY=your-cohere-api-key-here
     • At the top of project.py, add:
       from dotenv import load_dotenv
       load_dotenv()
       import os
       import cohere
       co = cohere.Client(os.getenv("COHERE_API_KEY"))
     • Install python‑dotenv if needed:
       pip install python-dotenv

   OR (Quick test only):
     Hardcode your key in project.py (not recommended for GitHub):
       co = cohere.Client("your-api-key-here")

4. Run the App
   streamlit run code.py
   Then open http://localhost:8501 in your browser.

🧠 Powered By
- Cohere Command Model (https://cohere.com/)
- Streamlit (https://streamlit.io/)
- Python (https://www.python.org/)

📂 File Structure
daily-motivation-generator/

├── code.py         # Streamlit app
├── requirements.txt   # Python dependencies      
└── README.md          # This file

🙌 Contributing
Feel free to fork the repo, open issues, or submit pull requests!

📜 License
MIT License — use it however you want, just give credit. 😄

👨‍💻 Made by
Ayush Kashyap ✨
