import streamlit as st
from exa_py import Exa
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Exa client
api_key = os.getenv("EXA_API_KEY")
if not api_key:
    st.error("EXA_API_KEY not found in environment variables. Please set it and restart the app.")
    st.stop()

exa = Exa(api_key)

def search(query, num_results=10):
    try:
        response = exa.search(query=query, num_results=num_results)
        return response.results
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #2E3440;
        color: #D8DEE9;
    }
    .big-font {
        font-size:50px !important;
        color: #88C0D0;
    }
    .subheader {
        font-size:30px !important;
        color: #81A1C1;
    }
    .stTextInput > div > div > input {
        background-color: #3B4252;
        color: #D8DEE9;
    }
    .stButton > button {
        background-color: #88C0D0;
        color: #2E3440;
    }
    .stButton > button:hover {
        background-color: #81A1C1;
        color: #D8DEE9;
    }
    .result-card {
        background-color: #3B4252;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .result-title {
        color: #EBCB8B;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .result-url {
        color: #88C0D0;
        font-style: italic;
        margin-bottom: 10px;
    }
    .result-date {
        color: #81A1C1;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .result-extract {
        color: #D8DEE9;
    }
    .sidebar .sidebar-content {
        background-color: #3B4252;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Search Engine</p>', unsafe_allow_html=True)
# Welcome message and description
st.markdown('''
<div class="welcome-section">
    <p class="subheader">Welcome to the Search Engine!</p>
    <p class="description">
        Discover the power of intelligent web search. Our engine, powered by the Exa API, 
        provides you with accurate and relevant results from across the internet. 
        Whether you're researching, exploring, or just curious, start your journey here!
    </p>
</div>
''', unsafe_allow_html=True)



# Search input
query = st.text_input("Enter your search query:")

# Search button
if st.button("Search"):
    if query:
        with st.spinner("Searching..."):
            results = search(query)
        
        if results:
            for result in results:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">{result.title}</div>
                    <div class="result-url">{result.url}</div>
                    <div class="result-date">{result.published_date}</div>
                    <div class="result-extract">{result.text}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No results found.")
    else:
        st.warning("Please enter a search query.")

# Add information about the app in the sidebar
st.sidebar.title("About")
st.sidebar.markdown("""
    ### Exa Search Engine
    
    This app uses the Exa API to provide powerful web search capabilities.
    
    #### How to Use:
    1. Enter your search query in the text box.
    2. Click the 'Search' button or press Enter.
    3. View the results displayed below the search bar.
    4. Each result shows:
       - Title (clickable link)
       - URL
       - Published date (if available)
       - A brief extract from the page
    
    #### Tips:
    - Be specific in your search queries for better results.
    - Use quotation marks for exact phrase searches.
    - Explore multiple results to find the most relevant information.
    
""")


# Add a footer
st.markdown(
    """
    <div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: #3B4252; color: #D8DEE9; text-align: center; padding: 10px;">
        Powered by Exa API | Created with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)