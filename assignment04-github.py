""" Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with the text "Anthony"
    The program should then commit those changes and push the file back to the repository."""
    

from github import Github

# Replace "Andrew" with "Anthony" in a file
def replace_text_in_file(repo, file_path, old_text, new_text):
    content = repo.get_contents(file_path)
    file_data = content.decoded_content.decode('utf-8')
    file_data = file_data.replace(old_text, new_text)
    
    # Commit the modified content to the repository
    repo.update_file(
        file_path,
        "Replace 'Andrew' with 'Anthony'",
        file_data,
        content.sha)
    
    
# GitHub credentials and repository information
github_token = ""
repository_name = ""

#Enter the location of the file that changes are to be made
file_path = 
old_text = "Andrew"
new_text = "Anthony"



g = Github(github_token)

# Access the repository
repo = g.get_repo(repository_name)

# Replace text in the file
replace_text_in_file(repo, file_path, old_text, new_text)

print("Changes committed and pushed successfully.")
