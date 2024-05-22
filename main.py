import requests
from bs4 import BeautifulSoup

def fetch_hacker_news_topics():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('a', class_='storylink')
    topics = []

    for title in titles:
        print(title)
        if "language model" in title.text.lower() or "llm" in title.text.lower() or "gpt" in title.text.lower():
            topics.append({
                'title': title.text,
                'link': title['href']
            })

    return topics

if __name__ == "__main__":
    topics = fetch_hacker_news_topics()
    if topics:
        print("Topics related to Large Language Models on Hacker News:")
        for topic in topics:
            print(f"Title: {topic['title']}\nLink: {topic['link']}\n")
    else:
        print("No topics related to Large Language Models found.")
