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

# Make a GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    commits = response.json()  # Parse JSON from the response
    for commit in commits:
        commit_id = commit['sha']
        print(commit_id)
else:
    print("Request failed with status code:", response.status_code)