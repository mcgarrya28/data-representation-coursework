""" Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with the text "Anthony"
    The program should then commit those changes and push the file back to the repository."""
    

from github import Github

# Replace "Andrew" with "Anthony" in a file
def replace_text_in_file(repo, file_path, old_text, new_text):
    content = repo.get_contents(file_path)
    file_data = content.decoded_content.decode('utf-8')
    file_data = file_data.replace(old_text, new_text)
    
apikey = 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