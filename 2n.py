class State:
    def __init__(self, name, accepting=False):
        self.name = name
        self.accepting = accepting
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

class Automaton:
    def __init__(self):
        # Define states
        self.q0 = State("q0")
        self.q1 = State("q1")
        self.q2 = State("q2", accepting=True)

        # Set initial state
        self.current_state = self.q0

        # Define transitions
        self.q0.add_transition('a', self.q0)
        self.q0.add_transition('b', self.q1)

        self.q1.add_transition('a', self.q0)
        self.q1.add_transition('b', self.q2)

    def process_input(self, input_string):
        for symbol in input_string:
            if symbol in self.current_state.transitions:
                self.current_state = self.current_state.transitions[symbol]
            else:
                print(f"Invalid input: {symbol} is not allowed in state {self.current_state.name}")
                return

        if self.current_state.accepting:
            print(f"Accepted: '{input_string}' ends with 'ab'")
        else:
            print(f"Rejected: '{input_string}' does not end with 'ab'")


def main():
    # Create automaton
    automaton = Automaton()

    # Test strings
    test_strings = ["aab", "abab", "xyzab", "abb", "ab"]

    # Process each test string
    for test_string in test_strings:
        print("\nProcessing:", test_string)
        automaton.process_input(test_string)


if __name__ == "__main__":
    main()
