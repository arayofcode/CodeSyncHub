# import github
# from github import Github, Auth
# from github.GithubException import UnknownObjectException

# github.enable_console_debug_logging()

# def create_file(repo, path, commit_message, content, branch="main"):
#     try:
#         contents = repo.get_contents(path)
#         print("File present already. Updating it...")
#         results = repo.update_file(path, commit_message, content, sha=contents.sha, branch=branch)
#     except UnknownObjectException as e:
#         results = repo.create_file(path, commit_message, content, branch)
#     return results


# def delete_file(repo, path, commit_message, branch="main"):
#     results = None
#     try:
#         contents = repo.get_contents(path, branch)
#         results = repo.delete_file(contents.path, commit_message, sha=contents.sha, branch=branch)
#     except UnknownObjectException as e:
#         print("File not present. Nothing to delete.")
#     return results


# auth = Auth.Token("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")

# g = Github(auth=auth)

# repo = g.get_repo("arayofcode/LeetCode")
# # create_file(repo, "test/test1.txt", "This is the commit message", "This is the content of the file")
# delete_file(repo, "test/test1.txt", "Deleting message")

# g.close()



# Usage
token = "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"
repo_name = "arayofcode/LeetCode"
githubSync = GitHubClient(token, repo_name)

# Example of creating a file
# githubSync.create_file("test/test1.txt", "This is the commit message", "This is the content of the file")

# Example of deleting a file
# githubSync.delete_file("test/test1.txt", "Deleting message")

# Close the Github session when done
githubSync.close()
