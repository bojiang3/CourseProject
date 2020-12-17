# Course Final Project for CS 410 Text Information Systems

## Sentiment Analysis Tool (Option 5: Free topic)

### Group SN (#196)
Bojiang Li, Yunfei Ma, David Ye


This project aims to help students improve paper-reading and -writing ability by providing sentimental and keyword analysis.

- The source code is provided in the main folder.

### For the specific information, sample text input and output results, please see "*CS 410 Final Project Report*" in the main menu.


## Software installation

First install the azure coginitive services package service.
```
pip3 install azure3
pip3 install cognitiveservices
pip3 install msrest
pip3 install docx2txt
```

Then direct run the file with Python.
- Python3 works

```
python text_analytics_bing_search_key_phase.py 
```

The result will be rendered in *textanalyticresult.docx*


## Discussion & Midway Topic Change

Since during our original planned project implementation - EducationalWeb, we encountered too many unforeseen obstacles, we decided to switch something new - this sentimental analysis project. We have completed the project for giving feedbacks on the sentiment and giving scores for the sentimentals. We may keep working on the frontend later to to improve the user experience.

##  Result and Outcome

- In the rendered, according to every sentence, it will give a score to the phrase.
- Sentimental analysis will be given to each one of sentences.
- The high scores on both positive and negetive will be noticed because it does not follow the require neutral tone of the essay.

050B.docx is the sample file we test for the sentimental analysis.

For grammercheck.py, it is the code for checking the right wording for the whole paper.

Main.py will be the user side code for this project


## Video presentation

https://mediaspace.illinois.edu/media/1_h6ncumvp


## References/Sources

- ![azure grammer](https://docs.microsoft.com/en-us/office/troubleshoot/word/spelling-grammar-checker-underline-color)
- https://docs.microsoft.com/en-us/office/troubleshoot/word/spelling-grammar-checker-underline-color
- ![Use Sentiment Analysis With Python to Classify Movie Reviews](https://realpython.com/sentiment-analysis-python/)
- https://realpython.com/sentiment-analysis-python/
- ![How To Perform Sentiment Analysis in Python 3 Using the Natural Language Toolkit (NLTK)](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)
- https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
- ![nlp sentiment](https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/)
- https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

