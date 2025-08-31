
from github_sdk.github import GitHub
import pytest
# def test_get_repo():
#     sdk = GitHub()
#     data = sdk.get_repo("octocat","Hello-world")
    
#     print("Name:", data["name"])
#     print("Owner:", data["owner"])
#     print("Stars:", data["stars"])
#     print("Forks:", data["forks"])
#     print("Open Issues:", data["open_issues"])
    
    # assert 'name' in data
# def test_list_issues():
#     sdk = GitHub()
#     data = sdk.list_issues("octocat","Hello-World")
#     print(data[0]['title'])
#     print(data[0]['state'])
#     print(data[0]['id'])

def test_get_issue():
    sdk = GitHub()
    data = sdk.get_issue("octocat","Hello-World",4268)
    print(data)