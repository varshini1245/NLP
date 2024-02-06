
import nltk

# Download the 'punkt' resource
nltk.download('punkt')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.wsd import lesk
def lesk_algorithm(sentence, target_word):
    # Tokenize the sentence and remove stopwords
    tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]

    # Apply Lesk algorithm
    sense = lesk(tokens, target_word)

    return sense.definition() if sense else None

# Example usage
sentence = "I went to the bank to deposit money."
target_word = "bank"

result = lesk_algorithm(sentence, target_word)
if result:
    print(f"Sense for '{target_word}': {result}")
else:
    print(f"No sense found for '{target_word}' in the given context.")
