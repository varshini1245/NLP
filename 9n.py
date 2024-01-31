import re

def rule_based_pos_tagging(text):
    tagged_tokens = []

    # Define rules using regular expressions
    rules = [
        (r'\b(?:he|she|it)\b', 'PRP'),
        (r'\b(?:I|you|we|they)\b', 'PRP'),
        (r'\b(?:am|is|are)\b', 'VB'),
        (r'\b(?:was|were)\b', 'VBD'),
        (r'\b(?:do|does|did)\b', 'VBP'),
        (r'\b(?:will|shall)\b', 'MD'),
        (r'\b(?:the|a|an)\b', 'DT'),
        (r'\b(?:quick|brown|lazy)\b', 'JJ'),
        (r'\b(?:fox|dog|cat)\b', 'NN'),
        (r'\b(?:jumps|meows)\b', 'VBZ'),
        (r'\b(?:over)\b', 'IN'),
        (r'\b(?:loudly)\b', 'RB'),
        (r'\b(?:\d+)\b', 'CD')  # Match digits as Cardinal Numbers
    ]

    # Apply rules to the text
    for word, pos in rules:
        pattern = re.compile(word, re.IGNORECASE)
        matches = pattern.finditer(text)
        for match in matches:
            tagged_tokens.append((match.group(), pos))

    return tagged_tokens

# Example usage
def main():
    text = "The quick brown fox jumps over the lazy dog. I was running. Cats meow loudly."

    # Perform rule-based POS tagging
    tagged_tokens = rule_based_pos_tagging(text)

    # Display the result
    print("Original Text:", text)
    print("\nRule-Based Part-of-Speech Tagging:")
    for token, pos_tag in tagged_tokens:
        print(f"{token}: {pos_tag}")

if __name__ == "__main__":
    main()
