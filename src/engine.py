from exa_py import Exa
from dotenv import load_dotenv
import os

load_dotenv()


exa = Exa(os.getenv("EXA_API_KEY"))
query = input("Search Here: ")


response = exa.search(
    query
)
print(response)

