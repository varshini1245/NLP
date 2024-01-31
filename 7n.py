import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag



def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)

    return pos_tags

# Example usage
def main():
    text = "The quick brown fox jumps over the lazy dog."

    # Perform part-of-speech tagging
    pos_tags = pos_tagging(text)

    # Display the result
    print("Original Text:", text)
    print("\nPart-of-Speech Tagging:")
    for word, pos_tag in pos_tags:
        print(f"{word}: {pos_tag}")

if __name__ == "__main__":
    main()
