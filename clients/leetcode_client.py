from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

class LeetCodeClient:
    def __init__(self, cookie):
        self.transport = RequestsHTTPTransport(
            url='https://leetcode.com/graphql',
            headers={
                "Content-Type": "application/json",
                "Cookie": cookie,
            },
            use_json=True,
            retries=3,
        )
        self.client = Client(transport=self.transport, fetch_schema_from_transport=False)

    def get_submission_details(self, submission_id):
        query = gql("""
        query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                runtimeDisplay
                runtimePercentile
                memoryDisplay
                memoryPercentile
                code
                lang {
                    name
                    verboseName
                }
                question {
                    questionId
                    questionTitleSlug
                }
                notes
                topicTags {
                    tagId
                    slug
                    name
                }
            }
        }
        """)
        try:
            with self.client as client:
                result = client.execute(query, variable_values={"submissionId": submission_id})
                return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None