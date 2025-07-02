import streamlit as st
import cohere

# 👉 Paste your API key directly here 
co = cohere.Client("YOUR-API-KEY")

# 🎯 Motivation generation logic
def generate_motivation(mood: str) -> str:
    prompt = (
        f"You are a friendly motivational coach. The user is feeling {mood}. "
        "Provide a short (2–3 sentence) uplifting motivational message tailored to that mood."
    )
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=60,
            temperature=0.8,
            k=0,
            p=0.75,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating message: {e}"

# 🧪 Streamlit App UI
st.set_page_config(page_title="Daily Motivation Generator", layout="centered", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center;'>🌟 Daily Motivation Generator</h1>", unsafe_allow_html=True)

st.markdown("Choose your current vibe, and let the AI give you a push!")

# 🎭 Emoji Mood Selector
moods = {
    "😊 Happy": "Happy",
    "😓 Stressed": "Stressed",
    "😴 Tired": "Tired",
    "😰 Anxious": "Anxious",
    "🤩 Excited": "Excited",
    "🎨 Creative Block": "Creative Block",
    "😔 Sad": "Sad",
    "🔥 Motivated": "Motivated",
    "🧠 Curious": "Curious",
    "😵 Overwhelmed": "Overwhelmed"
}

selected_emoji = st.selectbox("I'm feeling:", list(moods.keys()))
selected_mood = moods[selected_emoji]

# 🚀 Generate Button
if st.button("✨ Generate Motivation"):
    with st.spinner("Creating your spark..."):
        message = generate_motivation(selected_mood)
        st.success(message)

        # 📋 Copy to Clipboard
        st.code(message, language="markdown")

        # 💾 Download
        st.download_button(
            label="💾 Download as .txt",
            data=message,
            file_name="motivation.txt",
            mime="text/plain"
        )

        # 🔁 Generate Again
        st.markdown("---")
        if st.button("🔁 Generate Another"):
            st.experimental_rerun()

