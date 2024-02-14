import os
import sys
from github import Github

def create_github_repo(org_name, repo_name, github_token):
    try:
        g = Github(github_token)
        org = g.get_organization(org_name)
        org.create_repo(repo_name)
        print(f"Repository '{repo_name}' created successfully in the '{org_name}' organization on GitHub.")
    except Exception as e:
        print(f"An error occurred while creating the repository: {e}")
        sys.exit(1)

def push_to_github(repo_name, github_username, github_token):
    try:
        os.system("git init")
        os.system("git add .")
        os.system("git commit -m 'Initial commit'")
        os.system(f"git remote add origin https://github.com/{github_username}/{repo_name}.git")
        os.system("git push -u origin master")
        print("Code pushed to GitHub successfully!")
    except Exception as e:
        print(f"An error occurred while pushing code to GitHub: {e}")
        sys.exit(1)


def trigger_codeql_analysis(repo_name, github_username, github_token):
    try:
        # Initialize PyGithub client
        g = Github(github_token)

        # Get the repository
        repo = g.get_user(github_username).get_repo(repo_name)

        # Trigger GitHub Actions workflow
        workflow_dispatch_event = {
            "event_type": "trigger_codeql_analysis"
        }
        repo.create_repository_dispatch("workflows/codeql_analysis.yml", workflow_dispatch_event)

        print("CodeQL analysis triggered successfully!")
    except Exception as e:
        print(f"An error occurred while triggering CodeQL analysis: {e}")


if __name__ == "__main__":
    org_name = "Shadow-organ"
    repo_name = "demo2"
    github_username = "raviteja1830"
    github_token = "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"

    create_github_repo(org_name, repo_name, github_token)
    push_to_github(repo_name, github_username, github_token)
    trigger_codeql_analysis(repo_name, github_username, github_token)



# from github import Github


# if __name__ == "__main__":
#     repo_name = input("Enter the name of your GitHub repository: ")
#     github_username = input("Enter your GitHub username: ")
#     github_token = input("Enter your GitHub access token: ")

    
