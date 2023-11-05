from dotenv import load_dotenv
import os
from clients import GitHubClient, LeetCodeClient

extensions = {
    "golang" : "go",
    "java": "java",
    "python3": "py",
    "python": "py",
    "cpp": "cpp",
    "c": "c",
    "dart": "dart",
    "kotlin": "kt",
    "swift": "swift",
    "php": "php",
    "typescript": "ts",
    "javascript": "js",
    "csharp": "cs",
    "elixir": "ex",
    "erlang": "erl",
    "racket": "rkt",
    "rust": "rs",
    "scala": "sc",
    "ruby": "rb"
}

def sync_submission(github_client: GitHubClient, leetcode_client: LeetCodeClient, submission_id: int):
    # filename: questionId-questionTitleSlug
    # commit message: Time: runTimeDisplay (percentile), Space: memoryDisplay (memoryPercentile)
    submission_details = leetcode_client.get_submission_details(submission_id)["submissionDetails"]
    directory_name = f"{submission_details['question']['questionId']}-{submission_details['question']['questionTitleSlug']}"
    filename = f"{directory_name}/{directory_name}.{extensions[submission_details['lang']['name']]}"
    code = submission_details["code"]


def main():
    load_dotenv()
    
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('REPO_NAME')
    leetcode_cookie = os.getenv('LEETCODE_COOKIE')

    github_client = GitHubClient(token=github_token, repo_name=repo_name)
    print("GitHub client created.")
    
    leetcode_client = LeetCodeClient(cookie=leetcode_cookie)
    print("LeetCode client created.")
    
    sync_submission(github_client, leetcode_client, 1084043098)
    # print(leetcode_client.get_submission_details(1084043098))

    github_client.close()

if __name__ == "__main__":
    main()