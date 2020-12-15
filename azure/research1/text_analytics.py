key = "8d4febee8bf849a2b9a97797b422223e"
endpoint = "https://azuretext1.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
from azure.cognitiveservices.search.entitysearch import EntitySearchClient
from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
from msrest.authentication import CognitiveServicesCredentials

import docx2txt

#setup for entity search
subscription_key = "d8c84aab3fdb4dbcaa7b702f37fe4578"
endpoint_search = "https://bingysearch.cognitiveservices.azure.com"
client_bing = EntitySearchClient(endpoint=endpoint_search, credentials=CognitiveServicesCredentials(subscription_key))

my_text = docx2txt.process("050B.docx")

def authenticate_client():
    ta_credential = TextAnalyticsApiKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()


def sentiment_analysis_example(client):
    document = [my_text]
    response = client.analyze_sentiment(inputs=document)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        response.sentiment_scores.positive,
        response.sentiment_scores.neutral,
        response.sentiment_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("[Offset: {}, Length: {}]".format(sentence.offset, sentence.length))
        print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.3f}\nNeutral={1:.3f}\nNegative={2:.3f}\n".format(
            sentence.sentiment_scores.positive,
            sentence.sentiment_scores.neutral,
            sentence.sentiment_scores.negative,
        ))


sentiment_analysis_example(client)

def entity_recognition_example(client):

    try:
        document = [my_text]
        result = client.recognize_entities(inputs= document)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("Text: ", entity.text)#, "Category: ", entity.category, "SubCategory: ", entity.subcategory,
                      #"Offset: ", entity.offset, "Length: ", entity.offset,
                      #"Confidence Score: ", round(entity.score, 3)
            try:
                s=str(entity.text)
                ss=str(s)
                entity_data_bing = client_bing.entities.search(query=ss)

                if entity_data_bing.places.value:
                    main_entities = [entity for entity in entity_data_bing.entities.value
                                    if entity.entity_presentation_info.entity_scenario == "DominantEntity"]
                    if main_entities:
                        print(main_entities[0].description)
            except Exception as err:
                print("Encountered exception. {}".format(err))

    except Exception as err:
        print("Encountered exception. {}".format(err))
entity_recognition_example(client)


def key_phrase_extraction_example(client):
    try:
        document = [my_text]

        response = client.extract_key_phrases(inputs=document)[0]

        if not response.is_error:
            print("Key Phrases:")
            for phrase in response.key_phrases:
                print(phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


key_phrase_extraction_example(client)

