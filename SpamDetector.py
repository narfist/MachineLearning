#Pandas importieren
import pandas as pd
import string
#Die Daten laden und in eine Liste mit den Spaltennamen "label" und "sms_message" abspeichern
df = pd.read_table('smsspamcollection/SMSSpamCollection',
                   sep='\t', 
                   header=None, 
                   names=['label', 'sms_message'])
#Die ersten 10 Elemente ausgeben
print(df.head())

#Die Werte spam und ham auf 0 oder 1 mappen, da der weitere Algorithmus nur Zahlen verarbeiten kann
df['label'] = df.label.map({'ham':0, 'spam':1})

#Die Form der Liste ausgeben
print(df.shape)

#Erneut die ersten 10 (nun modifizierten) Elemente ausgeben
print(df.head())

#Uebung - convert to lower case
print("Convert to lower case")
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']
print(documents)
lower_case_documents = []
for i in documents:
    lower_case_documents.append(i.lower())
print(lower_case_documents)

#Satzzeichen entfernen
print("Satzzeichen entfernen")
without_punktation = []
for i in lower_case_documents:
	without_punktation.append(i.translate(str.maketrans('', '', string.punctuation)))
print(without_punktation)

#In einzelne Woerter aufsplitten
print("In einzelne Woerter aufsplitten")
words = []
for i in without_punktation:
	words.append(i.split(' '))
print(words)

gezaehlte_Liste = []
import pprint
from collections import Counter
for i in words:
	counts = Counter(i)
	gezaehlte_Liste.append(counts)
pprint.pprint(gezaehlte_Liste)
