import spacy
nlp = spacy.load('en_core_web_sm')
def show_ents(docs):
    doc = nlp(docs)
    if doc.ents:
        for ent in doc.ents:
            print(ent.text +
                 ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print('No named entities found')
doc1 = nlp("Leonardo DaVinci went to Florence and painted the Mona Lisa")


from spacy.tokens import Span
doc = nlp(u"Bostards is not cool")
ORG = doc.vocab.strings[u'ORG']
new_ent = Span(doc,0,1, label = ORG)
doc.ents = list(doc.ents) + [new_ent]
doc.ents