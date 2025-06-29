
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Request the website
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract quote text and authors
quotes = soup.find_all("div", class_="quote")

# Step 3: Store in lists
quote_texts = []
authors = []
tags_list = []

for quote in quotes:
    quote_texts.append(quote.find("span", class_="text").text)
    authors.append(quote.find("small", class_="author").text)
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]
    tags_list.append(", ".join(tags))

# Step 4: Create a DataFrame
df_quotes = pd.DataFrame({
    "Quote": quote_texts,
    "Author": authors,
    "Tags": tags_list
})

# Step 5: Save to CSV
df_quotes.to_csv("quotes.csv", index=False)
print("Web scraping completed and saved to quotes.csv")
