import nltk
from nltk.tag import BrillTaggerTrainer
from nltk.tag import UnigramTagger
from nltk.corpus import treebank



train_data = treebank.tagged_sents()[:3000]
baseline_tagger = UnigramTagger(train_data)


template = nltk.tag.brill.fntbl37()

# Create a BrillTaggerTrainer with the baseline tagger and template
brill_trainer = BrillTaggerTrainer(baseline_tagger, template)

# Train the Brill tagger
brill_tagger = brill_trainer.train(train_data)

# Example usage
def main():
    # Test sentence
    test_sentence = "The cat is sitting on a mat."

    # Tokenize the test sentence
    words = nltk.word_tokenize(test_sentence)

    # Tag the words using the Brill tagger
    tagged_words = brill_tagger.tag(words)

    # Display the result
    print("Original Sentence:", test_sentence)
    print("\nTransformation-Based Tagging:")
    for word, pos_tag in tagged_words:
        print(f"{word}: {pos_tag}")

if __name__ == "__main__":
    main()
