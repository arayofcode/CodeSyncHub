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

    def get_solved_questions(self):
        query = gql("""
        query problemsetQuestionList(
                $categorySlug: String,
                $limit: Int,
                $skip: Int,
                $filters: QuestionListFilterInput
        ) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
                questions: data {
                    questionId
                    title
                    titleSlug
                    difficulty
                    content
                    topicTags {
                        name
                        id
                        slug
                    }
                }
            }
        }
        """)
        try:
            with self.client as client:
                result = client.execute(query, variable_values={
                                        "categorySlug": "", "skip": 0, "limit": 50, "filters": {"status": "AC"}})
                return result["problemsetQuestionList"]["questions"]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_accepted_submissionID(self, question_slug):
        query = gql("""
        query submissionList(
            $offset: Int!,
            $limit: Int!,
            $lastKey: String,
            $questionSlug: String!,
            $lang: Int,
            $status: Int
        ) {
            questionSubmissionList(
                offset: $offset
                limit: $limit
                lastKey: $lastKey
                questionSlug: $questionSlug
                lang: $lang
                status: $status
            ) {
                submissions {
                    id
                }
            }
        }
        """)
        try:
            with self.client as client:
                # Status 10 means accepted
                result = client.execute(query, variable_values={
                                        "questionSlug": question_slug,
                                        "offset": 0,
                                        "limit": 20,
                                        "lastKey": None,
                                        "status": 10}
                                        )
                ids = result["questionSubmissionList"]["submissions"]
                return [id["id"] for id in ids]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

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
                    content
                }
                notes
            }
        }
        """)
        try:
            with self.client as client:
                result = client.execute(query, variable_values={"submissionId": submission_id})
                return result["submissionDetails"]
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
