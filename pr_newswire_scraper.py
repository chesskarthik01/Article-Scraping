from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.prnewswire.com/'


def pr_newswire_scraper():

    all_articles = []

    url = 'news-releases/english-releases/?page=1&pagesize=100'
    res = requests.get(f"{BASE_URL}{url}")
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all(class_='news-release')

    for article in articles:

        article_url = f"{BASE_URL}{article['href']}"
        print(f"Now Scraping {article_url}...")
        res2 = requests.get(article_url)
        res2.encoding = 'utf-8'
        soup2 = BeautifulSoup(res2.text, 'html.parser')

        article_text = soup2.find_all('p')
        article_text = [tag.get_text().strip() for tag in article_text]
        article_text = [s for s in article_text if not '\n' in s]
        article_text = [s for s in article_text if '.' in s]
        article_text = ' '.join(article_text)
        article_text = article_text.replace(
            "Searching for your content... ", "")
        article_text = article_text.replace("/PRNewswire/ ", "")

        all_articles.append({
            'title': article.get_text(),
            'url': article_url,
            'text': article_text
        })
    return all_articles


if __name__ == "__main__":
    pass
