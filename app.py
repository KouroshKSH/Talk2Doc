import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader

# sidebar of the website
def func_make_sidebar():
    with st.sidebar:
        st.title("Talk 2 Doc 💬📂")
        st.markdown("""
        ## Info 📝
        This website let's you chat with your documents.
        """)

        add_vertical_space(3)
        
        st.write("""
        ## Made by 💻
        This website is coded by Kourosh Sharifi.
        """)

        add_vertical_space(3)

        st.write("""
        ## Contact 📧
        - [LinkedIn](https://www.linkedin.com/in/kouroshsharifi/)
        - [GitHub](https://github.com/KouroshKSH)
        """)
        

def main():
    func_make_sidebar()

    st.header("""
    Talk to your Document 💭
    """)

    pdf = st.file_uploader("Upload your PDF file here.", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)



if __name__ == "__main__":
    main()