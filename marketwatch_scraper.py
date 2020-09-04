from bs4 import BeautifulSoup
import requests
import re

BASE_URL = 'https://www.marketwatch.com/'


def marketwatch_scraper():

    all_articles = []
    pattern = re.compile(r'([\S]+)')

    res = requests.get(BASE_URL)
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all(class_='article__headline')

    for article in articles:

        article_url = f"{article.find('a')['href']}"
        try:
            res2 = requests.get(article_url)
            print(f"Now scraping {article_url}...")
            res2.encoding = 'utf-8'
            soup2 = BeautifulSoup(res2.text, 'html.parser')

            article_text = soup2.find_all('p')
            article_text = [tag.get_text().strip() for tag in article_text]
            article_text = [s for s in article_text if not '\n' in s]
            article_text = [s for s in article_text if '.' in s]
            article_text = ' '.join(article_text)
        except:
            pass
        if article:
            all_articles.append({
                'title': " ".join(pattern.findall(article.get_text())),
                'url': article_url,
                'text': article_text
            })
        else:
            pass
    return all_articles


if __name__ == "__main__":
    pass
