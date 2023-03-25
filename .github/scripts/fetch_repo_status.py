import requests
import json

projects_url = 'https://raw.githubusercontent.com/OWASP/owasp.github.io/main/_data/projects.json'
response = requests.get(projects_url)
projects = response.json()

repo_statuses = []

for project in projects:
    code_urls = project.get('codeurl', '').split()
    for code_url in code_urls:
        if 'github.com' in code_url:
            repo_name = '/'.join(code_url.split('/')[-2:])
            try:
                repo_api_url = f'https://api.github.com/repos/{repo_name}'
                repo_response = requests.get(repo_api_url)
                repo_info = repo_response.json()

                repo_statuses.append({
                    'name': project['name'],
                    'url': project['url'],
                    'created': project['created'],
                    'updated': project['updated'],
                    'build': project['build'],
                    'codeurl': code_url,
                    'title': project['title'],
                    'level': project['level'],
                    'type': project['type'],
                    'region': project['region'],
                    'pitch': project['pitch'],
                    'meetup-group': project['meetup-group'],
                    'github_status': repo_info.get('message', 'success')
                })
            except Exception as e:
                print(f"Error fetching status for {code_url}: {e}")

with open('repo_status.json', 'w') as outfile:
    json.dump(repo_statuses, outfile, indent=2)
