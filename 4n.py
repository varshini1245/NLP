class MorphologicalParser:
    def __init__(self):
        self.current_state = "start"

    def apply_rules(self, word):
        plural = None

        for char in reversed(word):
            if self.current_state == "start":
                if char == 's':
                    self.current_state = "state_s"
                elif char == 'y':
                    self.current_state = "state_y"
                else:
                    break
            elif self.current_state == "state_s":
                if char == 'e':
                    plural = 'es'
                else:
                    plural = 's'
                break
            elif self.current_state == "state_y":
                if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                    plural = 's'
                else:
                    plural = 'ies'
                break

        return plural

def generate_plural_forms(nouns):
    parser = MorphologicalParser()

    plural_forms = {}
    for noun in nouns:
        plural = parser.apply_rules(noun)
        if plural:
            plural_forms[noun] = noun + plural

    return plural_forms

def main():
    # Sample English nouns
    english_nouns = ["cat", "dog", "city", "baby", "party", "bus"]

    # Generate plural forms using the finite-state machine
    plural_forms = generate_plural_forms(english_nouns)

    # Display the results
    print("Original Nouns:", english_nouns)
    print("Plural Forms:", plural_forms)

if __name__ == "__main__":
    main()
