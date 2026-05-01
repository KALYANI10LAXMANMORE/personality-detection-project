import streamlit as st
from model import predict_personality
from career import suggest_career

# Page config
st.set_page_config(page_title="Personality Predictor", page_icon="🧠")

# 🎨 CLEAN LIGHT BACKGROUND (Better visibility)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
}

h1, h2, h3 {
    color: #2c3e50;
    text-align: center;
}

p {
    color: #2c3e50;
    font-size: 16px;
}

.stTextArea textarea {
    background-color: white;
    color: black;
    border-radius: 10px;
}

.stButton button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

.stButton button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("## 🧠 Personality Detection & Career Suggestion")
st.write("✨ Write about yourself and discover your personality!")

# Input
user_input = st.text_area("✍️ Enter your text here:")

# Button
if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text!")

    else:
        personality, confidence = predict_personality(user_input)
        careers = suggest_career(personality)

        # Result
        st.subheader("🎯 Result")

        if personality == "extrovert":
            st.success(f"Personality: {personality}")
        else:
            st.info(f"Personality: {personality}")

        # Confidence bar
        st.progress(float(confidence))
        st.write(f"Confidence: {confidence:.2f}")

        # Careers
        st.subheader("💼 Suggested Careers")
        for c in careers:
            st.write("👉", c)

        #st.balloons()