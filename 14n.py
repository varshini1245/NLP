import nltk
from nltk import CFG

def check_subject_verb_agreement(sentence):
    # Define a context-free grammar for subject-verb agreement
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N
        VP -> V
        Det -> 'the'
        N -> 'cat' | 'cats'
        V -> 'chases' | 'chase'
    """)

    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Create a parser based on the grammar
    parser = nltk.ChartParser(grammar)

    # Check subject-verb agreement
    for tree in parser.parse(tokens):
        if check_tree_subject_verb_agreement(tree):
            print("Subject-Verb Agreement: The sentence is grammatically correct.")
        else:
            print("Subject-Verb Agreement Error: The sentence does not have proper agreement.")

def check_tree_subject_verb_agreement(tree):
    # Traverse the parse tree to check subject-verb agreement
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            # Check for a singular noun followed by a singular verb
            if subtree[1].label() == 'N' and tree[1].label() == 'V' and subtree[1][0] != 'cats':
                return False
            # Check for a plural noun followed by a plural verb
            elif subtree[1].label() == 'N' and tree[1].label() == 'V' and subtree[1][0] == 'cats':
                return False
    return True

# Example usage
def main():
    sentence1 = "the cat chases"
    sentence2 = "the cats chase"
    sentence3 = "the cats chases"

    check_subject_verb_agreement(sentence1)
    check_subject_verb_agreement(sentence2)
    check_subject_verb_agreement(sentence3)

if __name__ == "__main__":
    main()
