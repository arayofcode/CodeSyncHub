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

def sync_submission(github_client: GitHubClient, leetcode_client: LeetCodeClient, submission_id: int, question_data: dict):
    submission_details = leetcode_client.get_submission_details(submission_id)
    
    questionID = question_data["questionId"]
    difficulty = question_data["difficulty"]
    title = question_data["title"]
    title_slug = question_data["titleSlug"]
    questionContent = question_data["content"]

    directory_name = f"{questionID}-{title_slug}"
    filename = f"{directory_name}/{directory_name}.{extensions[submission_details['lang']['name']]}"
    code = submission_details["code"]
    notes = submission_details["notes"]
    commit_message = f"Time: {submission_details['runtimeDisplay']} (Beats {submission_details['runtimePercentile']:.2f}%), Space: {submission_details['memoryDisplay']} (Beats {submission_details['memoryPercentile']:.2f}%)"
    README = f"# [{questionID}. {title}](https://leetcode.com/problems/{title_slug})\n\n**Difficulty:** {difficulty}\n\n---\n\n{questionContent}\n```"

    github_client.create_file(f"{directory_name}/README.md", commit_message, README)
    github_client.create_file(f"{directory_name}/NOTES.md", commit_message, notes)
    github_client.create_file(filename, commit_message, code)

def main():
    load_dotenv()
    
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('REPO_NAME')
    leetcode_cookie = os.getenv('LEETCODE_COOKIE')

    github_client = GitHubClient(token=github_token, repo_name=repo_name)
    print("GitHub client created.")
    
    leetcode_client = LeetCodeClient(cookie=leetcode_cookie)
    print("LeetCode client created.")
    
    questions = leetcode_client.get_solved_questions()
    print(f"Found {len(questions)} questions.")
    for question in questions:
        accepted_submission_ids = leetcode_client.get_accepted_submissionID(question["titleSlug"])
        for submission_id in accepted_submission_ids:
            sync_submission(github_client, leetcode_client, submission_id, question)

    github_client.close()

if __name__ == "__main__":
    main()