from azure.cognitiveservices.search.entitysearch import EntitySearchClient
from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "d8c84aab3fdb4dbcaa7b702f37fe4578"
endpoint_search = "https://bingysearch.cognitiveservices.azure.com"
client_bing = EntitySearchClient(endpoint=endpoint_search, credentials=CognitiveServicesCredentials(subscription_key))
entity_data_bing = client_bing.entities.search(query="Gibralter")

if entity_data_bing.entities.value:

    main_entities = [entity for entity in entity_data_bing.entities.value
                     if entity.entity_presentation_info.entity_scenario == "DominantEntity"]

    if main_entities:
        print(main_entities[0].description)