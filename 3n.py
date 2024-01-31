import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def morphological_analysis(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)

    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Perform lemmatization based on part-of-speech tags
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag))
                        for word, pos_tag in pos_tags]

    # Display the original words, part-of-speech tags, and lemmatized words
    print("Original Words:", words)
    print("Part-of-Speech Tags:", pos_tags)
    print("Lemmatized Words:", lemmatized_words)

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN  # Default to noun if not found

def main():
    # Sample text
    text = "The cats are jumping over the fences."

    # Perform morphological analysis
    morphological_analysis(text)

if __name__ == "__main__":
    main()
