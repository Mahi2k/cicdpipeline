import requests, os
from dotenv import load_dotenv

load_dotenv()

# Replace these with your own values
github_username = os.getenv('github_username')
github_token = os.getenv('github_token')
repository_owner = os.getenv('repository_owner')
repository_name = os.getenv('repository_name')

print("github_token",github_token)

# URL to the GitHub API endpoint for commits
url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/commits"

# Set up authentication headers
headers = {
    "Authorization": f"Bearer {github_token}",
    "User-Agent": "Python GitHub API Client"
}

old_commitId = ""

def writeCommitId(id):
    f_object = open('latest-commit.txt', 'w')
    f_object.write(id)
    f_object.close()

def readCommitId():
    f_object = open('latest-commit.txt', 'r')
    commitId = f_object.read()
    f_object.close()
    return commitId

# Make a GET request to the API
response = requests.get(url, headers=headers)
# Check if the request was successful
if response.status_code == 200:
    commits = response.json()  # Parse JSON from the response
    # for commit in commits:
    firstCommit = commits[0]
    latest_commit_id = firstCommit["sha"]
    
    previousCommitId = readCommitId()
    print("OLD: ",previousCommitId)
    print("LATEST: ",latest_commit_id)
    if(previousCommitId != latest_commit_id):
       writeCommitId(latest_commit_id)
    
else:
    print("Request failed with status code:", response.status_code)