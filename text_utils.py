#Task 1: Custom Module with Aliases 

#Problem Statement: Create a custom module named `text_utils.py` with functions for 
# string manipulation (e.g., reversing a string, capitalizing). 
# In your main script, import this module using an alias and utilize its functions.

    # Import text_utils using an alias and utilize its functions
# Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, 
#demonstrating an understanding of custom module creation and aliasing.

def make_title(mood):
    title = mood.title()
    print(title)

def make_encoded(mood):
    title = mood.encode()
    print(title)