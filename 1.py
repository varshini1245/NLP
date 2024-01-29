import re

def main():
    # Sample text
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Email addresses: user@example.com, admin@email.com
    Phone numbers: 123-456-7890, 9876543210
    """

    # Define regular expressions for email addresses and phone numbers
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

    # Use re.findall to find all matches for the patterns in the text
    email_matches = re.findall(email_pattern, text)
    phone_matches = re.findall(phone_pattern, text)

    # Print the matches
    print("Email addresses found:", email_matches)
    print("Phone numbers found:", phone_matches)

    # Use re.search to find the first match for a pattern in the text
    first_email_match = re.search(email_pattern, text)
    if first_email_match:
        print("\nFirst email address found:", first_email_match.group())

if __name__ == "__main__":
    main()
