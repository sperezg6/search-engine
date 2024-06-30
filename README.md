# Exa Search Engine Streamlit App

## Overview

This Streamlit app provides a user-friendly interface for searching the web using the Exa API. It features a clean, visually appealing design with a dark mode color scheme inspired by the Nord palette.

## Features

- Web search functionality powered by the Exa API
- Clean and intuitive user interface
- Visually appealing dark mode design
- Display of search results including title, URL, published date, and extract
- Error handling for API requests

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An Exa API key (sign up at [https://exa.ai](https://exa.ai) if you don't have one)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/sperezg6/search-engine
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Exa API key:
   ```
   EXA_API_KEY=your_api_key_here
   ```

## Usage

To run the Streamlit app:

```
streamlit run app.py
```

Then, open your web browser and go to `http://localhost:8501`.

To use the search engine:
1. Enter your search query in the text input field.
2. Click the "Search" button or press Enter.
3. View the search results displayed below.

## Customization

You can customize the app's appearance by modifying the CSS in the `st.markdown()` function at the beginning of the script. The current color scheme is based on the Nord palette, but you can adjust it to your liking.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the web app framework
- [Exa](https://exa.ai) for the search API
- [Nord](https://www.nordtheme.com/) for color palette inspiration

## Contact

If you have any questions or feedback, please open an issue on this repository.