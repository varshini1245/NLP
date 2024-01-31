import nltk
from nltk import PCFG

# Define a Probabilistic Context-Free Grammar
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.4] | 'John' [0.6]
    VP -> V NP [0.7] | 'eats' [0.3]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'apple' [0.5] | 'banana' [0.5]
    V -> 'eats' [1.0]
""")

# Define a sentence
sentence = "John eats the apple"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Create a PCFG parser
parser = nltk.ChartParser(pcfg_grammar)

# Parse the sentence and display the most likely parse tree
parse_trees = parser.parse(tokens)
best_parse_tree = next(parse_trees)

print("Best Parse Tree (highest probability):")
best_parse_tree.pretty_print()
