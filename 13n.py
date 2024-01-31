import nltk
from nltk import CFG

# Define the context-free grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Define the sentence
sentence = "the dog chased the cat"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Create a chart parser based on the grammar
parser = nltk.ChartParser(grammar)

# Generate the parse tree
for tree in parser.parse(tokens):
    tree.pretty_print()
