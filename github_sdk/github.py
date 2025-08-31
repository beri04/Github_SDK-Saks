import requests
import json
class GitHub:
    Base_URL = "https://api.github.com"
    def get_repo(self,owner: str, repo :str,)-> dict:
        url = f"{self.Base_URL}/repos/{owner}/{repo}"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error":f"Something Goes wrong❌ {response.status_code}"}
        
        data = response.json()

        return{
            "name":data.get("name"),
            "owner":data.get('owner',{}).get("login"),
            'description':data.get('description'),
            'stars':data.get('stargazers_count'),
            'license':data.get('license',{}).get('name') if data.get('license') else "No licenses is found",
            'forks':data.get('forks_count'),
            'open_issues':data.get('open_issues_count')
        }
    def list_issues(self,owner:str,repo:str)-> dict:
        url = f"{self.Base_URL}/repos/{owner}/{repo}/issues"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error":f"Something went wrong{response.status_code}"}
        data = response.json()
        issues = []
        for issue in data:
            issues.append(
                {
                    'id':issue.get('number'),
                    'title':issue.get('title'),
                    'state':issue.get('state'),
                    'author':issue.get('user',{}).get("login")
                }
            )
        return issues
    
    def get_issue(self,owner:str,repo:str,issue_no:int)->dict:
        url = f"{self.Base_URL}/repos/{owner}/{repo}/issues/{issue_no}"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error":f"Something went wrong{response.status_code}"}
        
        data = response.json()

        return {
            'id':data.get('number'),
            'title':data.get('title'),
            'state':data.get('state'),
            'author':data.get('user',{}).get('login'),
            'created_at':data.get('created_at'),
            'url':data.get('html_url')
        }
