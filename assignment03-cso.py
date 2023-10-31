# Importing the 2 libraries required , request and json
"""
Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

Upload this program to the same repository you used for the XML assignment

Save this assignment as "assignment03-cso.py"

This program should not be a long one

I don't need you to reformat or analyse the data in any way

It should be about 10ish lines long (I have not counted)

You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest 
way to find it is search for it."""


import requests
import json

# Define the URL of the dataset to retrieve. 

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
  # Assuming the data is in JSON format, parse it into a Python data structure
    data = response.json()
    
    # Open a file named "cso.json" in write mode to save the retrieved data
    with open("cso.json", "w") as json_file:
      
      # Write the JSON data to the file with an indentation of 4 spaces for readability
        json.dump(data, json_file, indent=4)
        
    # Print the a success message to show the    
    print("Data successfully retrieved and saved to cso.json.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")