key = "9809f16410bf43fd9271836d3dde4f30"
endpoint = "https://bojiangli.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.cognitiveservices.search.entitysearch import EntitySearchClient
from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.search.websearch import WebSearchClient


import docx2txt

#setup for entity search
subscription_key = "9809f16410bf43fd9271836d3dde4f30"
endpoint_search = "https://bojiangli.cognitiveservices.azure.com/"
client_bing = WebSearchClient(endpoint="https://bojiangli.cognitiveservices.azure.com/",credentials=CognitiveServicesCredentials(subscription_key))

my_text = docx2txt.process("050B.docx")

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()


def sentiment_analysis_example(client):
    document = [my_text]
    response = client.analyze_sentiment(documents=document)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("[Length: {}]".format(sentence.grapheme_length))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))


sentiment_analysis_example(client)

def entity_recognition_example(client):

    try:
        document = [my_text]
        result = client.recognize_entities(documents= document)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("Text: ", entity.text)#, "Category: ", entity.category, "SubCategory: ", entity.subcategory,
                      #"Offset: ", entity.offset, "Length: ", entity.offset,
                      #"Confidence Score: ", round(entity.score, 3)

    except Exception as err:
        print("Encountered exception. {}".format(err))

entity_recognition_example(client)


def key_phrase_extraction_example(client):
    try:
        document = [my_text]

        response = client.extract_key_phrases(documents=document)[0]

        if not response.is_error:
            print("Key Phrases:")
            for phrase in response.key_phrases:
                print(phrase)
                try:
                    web_data = client_bing.web.search(query=str(phrase))

                    if hasattr(web_data.web_pages, 'value'):

                        print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

                        first_web_page = web_data.web_pages.value[0]
                        print("First web page name: {} ".format(first_web_page.name))
                        print("First web page URL: {} ".format(first_web_page.url))

                    else:
                        print("Didn't find any web pages...")

                    if hasattr(web_data.news, 'value'):

                        print("\r\nNews Results#{}".format(len(web_data.news.value)))

                        first_news = web_data.news.value[0]
                        print("First News name: {} ".format(first_news.name))
                        print("First News URL: {} ".format(first_news.url))

                    else:
                        print("Didn't find any news...")

                except Exception as err:
                    print("Encountered exception. {}".format(err))
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


key_phrase_extraction_example(client)

