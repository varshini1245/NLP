import spacy

def perform_ner(text):
    # Load the English NER model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using SpaCy NLP pipeline
    doc = nlp(text)

    # Extract and print named entities
    print("Named Entities:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")

# Example usage
def main():
    text = "Apple Inc. is planning to open a new store in New York City in 2022."

    # Perform Named Entity Recognition
    perform_ner(text)

if __name__ == "__main__":
    main()
