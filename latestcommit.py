import requests

# Replace these with your own values
github_username = "Mahi2k"
github_token = "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"
repository_owner = "Mahi2k"
repository_name = "cicdpipeline"

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
    print(latest_commit_id)
    
    previousCommitId = readCommitId()
    print("Prev",previousCommitId)
    print("First", firstCommit)
    if(previousCommitId != latest_commit_id):
       writeCommitId(latest_commit_id) 
else:
    print("Request failed with status code:", response.status_code)