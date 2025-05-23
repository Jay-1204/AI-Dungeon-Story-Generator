import streamlit as st
from transformers import pipeline

# 🚨 Set page config first (this must be the first Streamlit command)
st.set_page_config(page_title="AI Dungeon Story Generator", page_icon="📖",layout="centered")

# Load the GPT-2 text generation model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# Streamlit app UI
st.title("🧙‍♂️ AI Dungeon Story Generator")

st.markdown("""
Welcome to the AI Dungeon! Enter a story prompt and let GPT-2 generate the next chapter.
You can choose a genre to guide your adventure.
""")

# Genre options
genre = st.selectbox("Choose a genre:", ["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Random"])
default_prompt = {
    "Fantasy": "In the magical kingdom of Eldoria, a young wizard named Elric discovered...",
    "Sci-Fi": "In the year 3049, Earth had become a barren wasteland and humans lived on Mars...",
    "Mystery": "Detective Clara arrived at the mansion, rain soaking her coat, as she examined the body...",
    "Adventure": "High in the Himalayan mountains, a secret map led them to the lost temple...",
    "Random": "It was a day like any other until..."
}

# Prompt input
user_prompt = st.text_area("Your story prompt:", default_prompt.get(genre, "Once upon a time..."))

# Generation settings
max_length = st.slider("Max length of story:", 100, 500, 200, step=50)
num_outputs = st.slider("Number of versions:", 1, 3, 1)

# Generate button
if st.button("Generate Story"):
    with st.spinner("Weaving your story..."):
        outputs = generator(user_prompt, max_length=max_length, num_return_sequences=num_outputs)
        for i, out in enumerate(outputs):
            st.subheader(f"Story {i+1}")
            st.write(out['generated_text'])
            st.download_button(f"📄 Download Story {i+1}", out['generated_text'], file_name=f"story_{i+1}.txt")
            
