import os
import requests

from github import Github, GithubIntegration, Auth

app_id = "999142"
# Read the bot certificate
with open("./buildbot34.2024-09-16.private-key.pem", "r") as cert_file:
    app_key = cert_file.read()

# Create an GitHub integration instance
git_integration = GithubIntegration(app_id, app_key)

# Comment on the pull request
installation_id = 54917174
access_token = git_integration.get_access_token(installation_id).token
# git_connection = Github(
#     login_or_token=git_integration.get_access_token(installation_id).token
# )
# repo = git_connection.get_repo("tanmoysrt/test2")
# issue = repo.get_issue(number=1)
# issue.create_comment("Hello world") # comment

# comment = issue.get_comment(2352582520)
# comment.create_reaction("rocket") # reaction

# comment = issue.get_comment(2352582520)
# comment.delete() # delete

# comment = issue.get_comment(2352614952)
# comment.edit("Hello world [updated]") # edit


def post_comment(
    token: str, comment: str, owner: str, repo: str, issue_number: int
) -> bool:
    try:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}",
        }
        data = {
            "body": comment,
        }
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
        response = requests.post(url, headers=headers, json=data)
        return response.status_code == 201
    except Exception as e:
        print(e)
        return False


def update_comment(
    token: str, comment_id: int, comment: str, owner: str, repo: str
) -> bool:
    try:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}",
        }
        data = {
            "body": comment,
        }
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}"
        )
        response = requests.patch(url, headers=headers, json=data)
        return response.status_code == 200
    except Exception as e:
        print(e)
        return False


def delete_comment(token: str, comment_id: int, owner: str, repo: str) -> bool:
    try:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}",
        }
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}"
        )
        response = requests.delete(url, headers=headers)
        return response.status_code == 204
    except Exception as e:
        print(e)
        return False


def add_reaction(token: str, comment_id: int, owner: str, repo: str, reaction: str) -> bool:
    try:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {token}",
        }
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions"
        response = requests.post(url, headers=headers, json={"content": reaction})
        return response.status_code == 201
    except Exception as e:
        print(e)
        return False


# post_comment(
#     token=access_token,
#     comment="Hello world",
#     owner="tanmoysrt",
#     repo="test2",
#     issue_number=1,
# )
# update_comment(
#     token=access_token,
#     comment_id=2352614952,
#     comment="Hello world [updated again]",
#     owner="tanmoysrt",
#     repo="test2"
# )
# delete_comment(
#     token=access_token, comment_id=2352676024, owner="tanmoysrt", repo="test2"
# )
add_reaction(
    token=access_token, comment_id=2352614952, owner="tanmoysrt", repo="test2", reaction="rocket"
)
