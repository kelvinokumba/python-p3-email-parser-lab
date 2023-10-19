# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Split the email_string based on spaces or commas using regular expressions
        addresses = re.split(r'[ ,]+', self.email_string)

        # Remove empty strings (if any)
        addresses = [address.strip() for address in addresses if address.strip()]

        # Use a set to store unique email addresses and then convert to a sorted list
        unique_addresses = sorted(set(addresses))

        return unique_addresses
