import os
import json
from marketwatch_scraper import marketwatch_scraper
from pr_newswire_scraper import pr_newswire_scraper
from watson_analysis import nlp
from spacy_ner import ner_extractor


def master_scraper():
    set1 = marketwatch_scraper()
    set2 = pr_newswire_scraper()
    all_articles = [*set1, *set2]
    return all_articles


def write_articles(articles):
    file_path = os.path.join("datasets")
    os.makedirs(file_path, exist_ok=True)
    json_path = os.path.join(file_path, 'articles.json')
    num = 1
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for x in articles:
            if x not in data:
                data.append(x)
                print(f"Adding article {num}...")
                num += 1
            else:
                pass
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


articles = master_scraper()
write_articles(articles)
ner_extractor()
nlp()
