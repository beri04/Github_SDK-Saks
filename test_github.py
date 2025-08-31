
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

# def test_get_issue():
#     sdk = GitHub()
#     data = sdk.get_issue("octocat","Hello-World",4268)
#     print(data)

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code 

    def json(self):
        return self._json
        

def test_get_repo(monkeypatch):
    def mock(*args, **kwargs):
        return DummyResponse({
            'name': 'Hello-World',
            'owner': {'login': 'octocat'},
            'description': "your first repo",
            'stargazers_count': 1200,
            'open_issues_count': 100,
            'forks_count': 500,
            'license': {'name': 'MIT License'} 
        })
    monkeypatch.setattr('requests.get', mock)

    sdk = GitHub()
    data = sdk.get_repo('octocat', 'Hello-World')

    #Assertions for get_repo
    assert data["name"] == "Hello-World"
    assert data["owner"] == "octocat"
    assert data["stars"] == 1200
    assert data["forks"] == 500
    assert data["open_issues"] == 100
    assert data["license"] == "MIT License"

def test_get_issues(monkeypatch):
    def mock(*args, **kwargs):
        return DummyResponse({
            'number': 1347,
            'title': 'bug fix',
            'state': 'open',
            'user': {'login': 'octocat'},
            'created_at': "2025-09-01 15:00:00",
            'html_url': "https://github.com/octocat/Hello-World/issues/1347"
        })
    monkeypatch.setattr('requests.get', mock)

    sdk = GitHub()
    data = sdk.get_issue('octocat', 'Hello-World', 1347)

    #Assertions for get_issues
    assert data['id'] == 1347
    assert data["title"] == "bug fix"
    assert data["state"] == "open"
    assert data["author"] == "octocat"
    assert "2025-09-01" in data["created_at"]
    assert "issues/1347" in data["url"]

def test_list_issues(monkeypatch):
    def mock(*args,**kwargs):
        return DummyResponse([
            {
                'number':1,
                'title':'bug fix',
                'state':'open',
                'user':{'login':'bob'}
            },
            {
                'number':2,
                'title':"fixed pages",
                'state':'closed',
                'user':{'login':'john'}
            }
        ])
    monkeypatch.setattr('requests.get',mock)
    sdk = GitHub()
    data = sdk.list_issues('octocat','Hello-world')

    #Assertions for first issue
    assert data[0]['id'] == 1
    assert data[0]['title'] == 'bug fix'
    assert data[0]['state'] == 'open'
    assert data[0]['author'] == 'bob'

    # Assertions for second issue
    assert data[1]['id'] == 2
    assert data[1]['title'] == 'fixed pages'
    assert data[1]['state'] == 'closed'
    assert data[1]['author'] == 'john' 
