""" Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with the text "Anthony"
    The program should then commit those changes and push the file back to the repository."""
    

import os
import git

# Define a function to replace text in a file
def replace_text_in_file(file_path, old_text, new_text):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        file_data = file.read()