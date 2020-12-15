import spacy
from spacy_grammar.grammar import Grammar

nlp = spacy.load('en_core_web_sm')
grammar = Grammar(nlp)
nlp.add_pipe(grammar)
doc = nlp('I can haz cheeseburger.')
doc._.has_grammar_error  # True

# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Dr Alex Smith chaired first board meeting of Acme Corp Inc.")
# print([(ent.text, ent.label_) for ent in doc.ents])