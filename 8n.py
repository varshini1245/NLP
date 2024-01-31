import nltk
from nltk.tokenize import word_tokenize
from nltk import FreqDist


def train_pos_tagger(train_text):
    # Tokenize the training text into words
    words = word_tokenize(train_text)

    # Create a frequency distribution of words
    freq_dist = FreqDist(words)

    # Create a basic probabilistic model based on word frequencies
    pos_tagger = {}

    for word, freq in freq_dist.items():
        # Assume common nouns
        pos_tagger[word] = 'NN'

    return pos_tagger

def stochastic_pos_tagging(text, pos_tagger):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Assign POS tags based on the probabilistic model
    pos_tags = [pos_tagger.get(word, 'NN') for word in words]

    return pos_tags

# Example usage
def main():
    # Training text for building the probabilistic model
    train_text = "The quick brown fox jumps over the lazy dog. The lazy dog barks loudly."

    # Test text for POS tagging
    test_text = "A quick brown cat meows loudly."

    # Train the POS tagger
    pos_tagger = train_pos_tagger(train_text)

    # Perform stochastic POS tagging on the test text
    pos_tags = stochastic_pos_tagging(test_text, pos_tagger)

    # Display the result
    print("Original Text:", test_text)
    print("\nStochastic Part-of-Speech Tagging:")
    for word, pos_tag in zip(word_tokenize(test_text), pos_tags):
        print(f"{word}: {pos_tag}")

if __name__ == "__main__":
    main()
