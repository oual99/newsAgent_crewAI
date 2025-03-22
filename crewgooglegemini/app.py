import streamlit as st
import asyncio
import nest_asyncio

# Set up an event loop in the current thread
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Then import your other modules
from crew import crew
import os

# Streamlit App Title
st.title("AI-Powered Tech News Generator")

# Input Field for Topic
topic = st.text_input("Enter a topic for research and writing:", "AI in Healthcare")

# Run the AI Workflow
if st.button("Generate Article"):
    with st.spinner("Generating content... Please wait."):
        # Execute the CrewAI workflow
        result = crew.kickoff(inputs={'topic': topic})
        
        # Display Result
        st.subheader("Generated Article:")
        st.markdown(result)

        # Save to file
        output_file = "new-blog-post.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        st.success(f"Article saved as {output_file}")

# Footer
st.markdown("---")
st.markdown("Powered by CrewAI and Google Gemini AI")