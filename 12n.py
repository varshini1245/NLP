class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, input_string):
        self.chart = [set() for _ in range(len(input_string) + 1)]
        self.predict(0, 'expression', 0)

        for i in range(len(input_string) + 1):
            added_states = set()  # Create a set to store newly added states
            while True:
                added = False
                for state in self.chart[i]:
                    if not state.completed() and state.next_symbol() in self.grammar:
                        added_states |= self.predict(i, state.next_symbol(), state.origin)
                        added = True
                    elif not state.completed() and state.next_symbol() == input_string[i]:
                        added_states |= self.scan(i, state)
                        added = True
                    elif state.completed():
                        added_states |= self.complete(i, state)
                        added = True
                    else:
                        added_states |= self.advance(i, state)
                if not added:
                    break

            # Add the newly added states to the chart
            self.chart[i].update(added_states)

        # Check if the goal symbol is in the last set of the chart
        goal_state = EarleyState('goal', ['expression'], 0, 0)
        return goal_state in self.chart[len(input_string)]

    def predict(self, index, nonterminal, origin):
        new_states = set()
        for production in self.grammar[nonterminal]:
            new_state = EarleyState(nonterminal, production, 0, index)
            new_states.add(new_state)
        return new_states

    def scan(self, index, state):
        new_state = state.advance()
        return {new_state}

    def complete(self, index, state):
        new_states = set()
        for s in self.chart[state.origin]:
            if not s.completed() and s.next_symbol() == state.nonterminal:
                new_state = s.advance()
                new_states.add(new_state)
        return new_states

    def advance(self, index, state):
        next_symbol = state.next_symbol()
        if next_symbol in self.grammar:
            return self.predict(index, next_symbol, state.origin)
        return set()


class EarleyState:
    def __init__(self, nonterminal, production, dot_index, origin):
        self.nonterminal = nonterminal
        self.production = production
        self.dot_index = dot_index
        self.origin = origin

    def __eq__(self, other):
        return (self.nonterminal, self.production, self.dot_index, self.origin) == \
               (other.nonterminal, other.production, other.dot_index, other.origin)

    def __hash__(self):
        return hash((self.nonterminal, tuple(self.production), self.dot_index, self.origin))

    def completed(self):
        return self.dot_index == len(self.production)

    def next_symbol(self):
        if self.dot_index < len(self.production):
            return self.production[self.dot_index]

    def advance(self):
        return EarleyState(self.nonterminal, self.production, self.dot_index + 1, self.origin)


# Example usage
def main():
    # Define a simple context-free grammar for arithmetic expressions
    arithmetic_grammar = {
        'expression': [['term'], ['expression', '+', 'term'], ['expression', '-', 'term']],
        'term': [['factor'], ['term', '*', 'factor'], ['term', '/', 'factor']],
        'factor': [['(', 'expression', ')'], ['number']],
        'number': [['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']],
        'goal': [['expression']]
    }

    parser = EarleyParser(arithmetic_grammar)

    # Test expressions
    expression1 = "3 + 4 * (5 - 2)"
    expression2 = "(7 * 2) / (4 + 1)"

    # Parse expressions
    result1 = parser.parse(expression1)
    result2 = parser.parse(expression2)

    # Display results
    print(f"Result for '{expression1}': {result1}")
    print(f"Result for '{expression2}': {result2}")


if __name__ == "__main__":
    main()
