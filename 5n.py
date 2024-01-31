import nltk
from nltk.stem import PorterStemmer

def apply_porter_stemmer(words):
    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()

    # Apply the Porter Stemmer to each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    return stemmed_words

def main():
    # Sample words
    words = ["running", "flies", "happily", "jumped", "beautifully"]

    # Apply Porter Stemmer
    stemmed_words = apply_porter_stemmer(words)

    # Display the results
    print("Original Words:", words)
    print("Stemmed Words:", stemmed_words)

if __name__ == "__main__":
    main()
