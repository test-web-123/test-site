import requests
import json
import csv
import os

session = requests.Session()
access_token = os.environ.get('GITHUB_TOKEN')
#access_token = os.environ.get('github')
#access_token = '3681c6ef66b33fa05508f5136254ebafa45c56ec'
session.headers.update({'Authorization': f'Bearer {access_token}'})
org = 'test-web-123'

file = open('output.csv','w', newline='')
writer = csv.writer(file)
writer.writerow(['repository', 'data'])

repoResponse = session.get(f'https://api.github.com/orgs/{org}/repos')
repos = json.loads(repoResponse.content)


for repo in repos:
    repoName = repo['name']
    ownerName = repo['owner']['login']
    collaboratorsResponse = session.get(f'https://api.github.com/repos/{ownerName}/{repoName}/collaborators')
    collaborators = json.loads(collaboratorsResponse.content)
    for collaborator in collaborators:
        print(collaborator)
        userPermission = collaborator['permissions']
        if (userPermission['admin'] == True):
            userResponse = session.get(f"https://api.github.com/users/{collaborator['login']}")
            userName = json.loads(userResponse.content)['name']
            writer.writerow([repoName, [collaborator['login'], userName, collaborator['html_url'], "admin"]])
        elif (userPermission['maintain'] == True):
            userResponse2 = session.get(f"https://api.github.com/users/{collaborator['login']}")
            userName2 = json.loads(userResponse2.content)['name']
            writer.writerow([repoName, [collaborator['login'], userName2, collaborator['html_url'], "maintain"]])
        else: 
            pass

file.close()
