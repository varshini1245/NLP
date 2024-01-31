import random
from collections import defaultdict

def build_bigram_model(text):
    bigram_model = defaultdict(list)

    # Tokenize the text into words
    words = text.split()

    # Build the bigram model
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        bigram_model[current_word].append(next_word)

    return bigram_model

def generate_text(bigram_model, starting_word, max_length=50):
    generated_text = [starting_word]

    for _ in range(max_length - 1):
        current_word = generated_text[-1]

        if current_word in bigram_model:
            next_word_options = bigram_model[current_word]
            next_word = random.choice(next_word_options)
            generated_text.append(next_word)
        else:
            break  # Stop if the current word has no following words in the model

    return ' '.join(generated_text)

# Example usage
def main():
    # Example text
    input_text = "This is a simple example of a bigram model for text generation. It uses a basic approach to build the model and generate new text."

    # Build bigram model
    bigram_model = build_bigram_model(input_text)

    # Generate text using a starting word
    starting_word = "This"
    generated_text = generate_text(bigram_model, starting_word)

    # Display the generated text
    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
