import streamlit as st
from exa_py import Exa
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Exa client
exa = Exa(os.getenv("EXA_API_KEY"))

def search(query, num_results=10):
    try:
        response = exa.search(query=query, num_results=num_results)
        return response.results
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit app
st.title("Exa Search Engine")

# Search input
query = st.text_input("Enter your search query:")

# Search button
if st.button("Search"):
    if query:
        with st.spinner("Searching..."):
            results = search(query)
        
        if results:
            for result in results:
                st.subheader(result.title)
                st.write(result.url)
                st.write(result.snippet)
                st.markdown("---")
        else:
            st.info("No results found.")
    else:
        st.warning("Please enter a search query.")

# Add some information about the app
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple search engine app using the Exa API. "
    "Enter your query in the search box and click 'Search' to get results."
)

# Add a footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: #FAFAFA;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Powered by Exa API | Created with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)