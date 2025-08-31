# 🗳️ GITHUB SDK 

[![Run tests](https://github.com/beri04/Github_SDK-Saks/actions/workflows/test.yml/badge.svg)](https://github.com/beri04/Github_SDK-Saks/actions/workflows/test.yml)

This SDK file has been created to :-
- get the **details** of repo.
- get the **issues** of repo.
- get the **information about issue** by putting the id of the issue.

# ⬇️Installation 
```bash 

git clone https://github.com/beri04/Github_SDK-Saks.git
cd Github_SDK_Saks
pip install -r requirements.txt



```python
sdk = GitHub()

#TO print the repo details
print(sdk.get_repo("octocat","Hello-world"))

#To print the lists of issues
print(sdk.list_issues("octocat","Hello-world"))

#To print the details of issue
print(sdk.get_issues("octocat","Hello-world",1347))