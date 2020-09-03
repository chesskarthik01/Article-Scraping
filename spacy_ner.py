import os
import spacy
import json
import pandas as pd


def ner_extractor():
    article_path = os.path.join('datasets', 'articles.json')
    df = pd.read_json(article_path)
    spacy.prefer_gpu()
    nlp = spacy.load('en_core_web_lg')

    ents = []
    num = 1
    for x in df['text']:
        doc = nlp(x)
        for ent in doc.ents:
            ents.append(ent)
        print(f"Extracting row {num}")
        num += 1

    file_path = os.path.join('datasets', 'spacy_ner.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        ents = [str(x) for x in ents]
        json.dump(ents, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    pass
