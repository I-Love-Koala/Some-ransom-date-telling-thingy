import time
from datetime import date  # Importing the date class from the datetime module
import sys

# Ask the user if they want to know the date
decision = input("Do you want to know the date? (Yes/No): ")

if decision.lower() == "yes":  # Convert the input to lowercase for a case-insensitive comparison
    print("Today's date is:", date.today())  # Print today's date
else:
    print("Goodbye!")  # If the user answers anything other than 'yes', print a message

    SystemExit