import os
import streamlit as st
import fitz 
import openai

def extract_text_from_pdf(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def query_llm(prompt, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

def summarize_text(text, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": f"Summarize the following text concisely:\n\n{text}"}],
        max_tokens=500,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

def main():
    st.title("PDF Chatbot with LLM")

    pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
    
    if pdf_file:
        with st.spinner('Extracting text from PDF...'):
            extracted_text = extract_text_from_pdf(pdf_file)
        
        st.success("PDF loaded and text extracted successfully!")

        if st.checkbox("Show extracted text"):
            st.text_area("Extracted Text", extracted_text, height=300)
        
        if len(extracted_text) > 10000:  
            with st.spinner('Summarizing extracted text...'):
                extracted_text = summarize_text(extracted_text)
                st.info("Text was too long and has been summarized.")

        user_query = st.text_input("Ask a question based on the PDF content:")
        
        if user_query:
            with st.spinner('Generating response...'):
                prompt = f"Based on this document: {extracted_text}\nAnswer this question: {user_query}"
                try:
                    response = query_llm(prompt)
                    st.write("Response:")
                    st.write(response)
                except openai.error.OpenAIError as e:
                    st.error(f"An error occurred: {e}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
