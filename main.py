from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.cognitiveservices.search.entitysearch import EntitySearchClient
from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.search.websearch import WebSearchClient
from flask import Flask, render_template,request,redirect, url_for
from grammarcheck import grammar_check
from werkzeug.utils import secure_filename
import docx2txt

subscription_key = "d8c84aab3fdb4dbcaa7b702f37fe4578"
endpoint_search = "https://bingysearch.cognitiveservices.azure.com"
client_bing = WebSearchClient(endpoint="https://bingysearch.cognitiveservices.azure.com",credentials=CognitiveServicesCredentials(subscription_key))
key = "8d4febee8bf849a2b9a97797b422223e"
endpoint = "https://azuretext1.cognitiveservices.azure.com/"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("first.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/check")
def check():
    return render_template("check.html")

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

output=[]
@app.route('/uploader', methods = ['GET', 'POST'])
def checkupload():
    #emotion score
   if request.method == 'POST':
      f = request.files['file']

      my_text = docx2txt.process(f)
      document = [my_text]
      response = client.analyze_sentiment(documents=document)[0]
      output.append("Document Sentiment: {}".format(response.sentiment))
      output.append("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
          response.confidence_scores.positive,
          response.confidence_scores.neutral,
          response.confidence_scores.negative,
      ))
      output.append(" ")
      for idx, sentence in enumerate(response.sentences):
          output.append("[Length: {}]".format(sentence.grapheme_length))
          output.append("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
          output.append("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
              sentence.confidence_scores.positive,
              sentence.confidence_scores.neutral,
              sentence.confidence_scores.negative,
          ))

    #key phrase
      output.append(" ")
      output.append(" ")
      output.append(" ")
      try:
          document = [my_text]

          response = client.extract_key_phrases(documents=document)[0]

          if not response.is_error:
              output.append("Key Phrases:")
              for phrase in response.key_phrases:
                  output.append(phrase)
                  try:
                      web_data = client_bing.web.search(query=str(phrase))

                      if hasattr(web_data.web_pages, 'value'):

                          output.append("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

                          first_web_page = web_data.web_pages.value[0]
                          output.append("First web page name: {} ".format(first_web_page.name))
                          output.append("First web page URL: {} ".format(first_web_page.url))

                      else:
                          output.append("Didn't find any web pages...")

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
      return render_template("result.html",info=output)



@app.route("/result",methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        message = request.form['message']
        old_text,new_text = grammar_check(message)
        
        
    return render_template("result.html",info = [new_text])

if __name__ == "__main__":
    app.run(debug=True)

