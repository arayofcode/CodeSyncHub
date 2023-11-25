from github import Github, Auth
from github.GithubException import UnknownObjectException

class GitHubClient:
    def __init__(self, token, repo_name):
        self.auth = Auth.Token(token)
        self.g = Github(auth=self.auth)
        self.repo = self.g.get_repo(repo_name)

    def create_file(self, path, commit_message, content, branch="main"):
        try:
            contents = self.repo.get_contents(path, ref=branch)
            print(f"File present already. Updating it. Check here: https://github.com/arayofcode/LeetCode/tree/{branch}/{path}")
            results = self.repo.update_file(path, commit_message, content, sha=contents.sha, branch=branch)
        except UnknownObjectException:
            results = self.repo.create_file(path, commit_message, content, branch=branch)
            print(f"Created file {path}. Check here: https://github.com/arayofcode/LeetCode/tree/{branch}/{path}")
        return results

    def delete_file(self, path, commit_message, branch="main"):
        try:
            contents = self.repo.get_contents(path, ref=branch)
            self.repo.delete_file(contents.path, commit_message, sha=contents.sha, branch=branch)
            print(f"File {path} deleted.")
        except UnknownObjectException:
            print("File not present. Nothing to delete.")

    def close(self):
        self.g.close()