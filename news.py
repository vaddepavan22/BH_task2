import requests
from bs4 import BeautifulSoup

# Function to scrape news headlines from Hacker News
def scrape_hacker_news(url):
    print(f"Fetching headlines from {url}...")
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # On Hacker News, headlines are in <span> tags with the class 'titleline'
    headlines = []
    for title_span in soup.find_all('span', class_='titleline'):
        # The headline text is inside an <a> tag within the span
        headline_tag = title_span.find('a')
        if headline_tag:
            headlines.append(headline_tag.get_text(strip=True))
    
    print(f"Found {len(headlines)} headlines.")
    return headlines

# --- Main part of the script ---
if __name__ == "__main__":
    news_url = "https://news.ycombinator.com/"
    
    scraped_headlines = scrape_hacker_news(news_url)
    
    if scraped_headlines:
        # Save the headlines to a .txt file
        with open('headlines.txt', 'w', encoding='utf-8') as f:
            for headline in scraped_headlines:
                f.write(f"{headline}\n")
        print("Headlines saved to headlines.txt")
