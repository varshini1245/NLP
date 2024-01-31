class TopDownParser:
    def __init__(self, input_string):
        self.tokens = input_string.split()
        self.current_token = None

    def parse(self):
        self.current_token = self.tokens.pop(0)
        result = self.parse_expression()
        if not self.tokens:  # Ensure all tokens are consumed
            return result
        else:
            raise SyntaxError("Unexpected tokens in the input.")

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.tokens:
                self.current_token = self.tokens.pop(0)
            else:
                self.current_token = None
        else:
            raise SyntaxError(f"Expected '{expected_token}', found '{self.current_token}'")

    def parse_expression(self):
        result = self.parse_term()
        while self.current_token in ['+', '-']:
            operator = self.current_token
            self.match(operator)
            right_operand = self.parse_term()
            result = (operator, result, right_operand)
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.current_token in ['*', '/']:
            operator = self.current_token
            self.match(operator)
            right_operand = self.parse_factor()
            result = (operator, result, right_operand)
        return result

    def parse_factor(self):
        if self.current_token.isdigit():
            result = int(self.current_token)
            self.match(self.current_token)
            return result
        elif self.current_token == '(':
            self.match('(')
            result = self.parse_expression()
            self.match(')')
            return result
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

# Example usage
def main():
    input_string = "3 + 4 * (5 - 2)"

    parser = TopDownParser(input_string)

    try:
        parsed_expression = parser.parse()
        print(f"Input string '{input_string}' is valid.")
        print("Parsed Expression:", parsed_expression)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")

if __name__ == "__main__":
    main()
