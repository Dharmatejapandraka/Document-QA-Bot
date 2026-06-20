import streamlit as st

from utils.rag import ask_question

st.set_page_config(
    page_title="AI Document Q&A Bot",
    page_icon="📚"
)

st.title("📚 AI Document Q&A Bot")

question = st.text_input(
    "Ask a question from your documents"
)

if st.button("Get Answer"):

    if question:

        with st.spinner("Searching documents..."):

            answer, citations = ask_question(question)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        for source in citations:
            st.write("•", source)