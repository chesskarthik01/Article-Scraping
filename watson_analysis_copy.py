import os
import pandas as pd
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, SentimentOptions
import re
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def nlp():
    authenticator = IAMAuthenticator(
        '<API Key>')
    service = NaturalLanguageUnderstandingV1(
        version='2018-03-16',
        authenticator=authenticator)
    service.set_service_url(
        '<API URL>')

    article_path = os.path.join('datasets', 'articles.json')
    df = pd.read_json(article_path)

    num = 1
    result = []
    file_path = os.path.join('datasets', 'watson_analysis.json')

    for x in df['text']:
        print(f"Now analysing row {num}...")
        response = service.analyze(text=x,
                                   features=Features(
                                       entities=EntitiesOptions(),
                                       sentiment=SentimentOptions()
                                   ), language='en').get_result()
        result.append(response)
        num += 1
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    pass
