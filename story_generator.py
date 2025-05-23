from transformers import pipeline
import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = st.text_area("Enter your story prompt:", "Once upon a time in a distant kingdom...")
story = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']


st.title("🧙 AI Dungeon Story Generator")

genre = st.selectbox("Choose a genre", ["Fantasy", "Sci-Fi", "Mystery", "Adventure"])
prompt = st.text_area("Enter your story prompt:", f"In a {genre.lower()} world...")

if st.button("Generate Story"):
    generator = pipeline("text-generation", model="gpt2")
    story = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
    st.markdown("### ✨ Your Story:")
    st.write(story)
    st.download_button("Download Story", story, file_name="ai_story.txt")
