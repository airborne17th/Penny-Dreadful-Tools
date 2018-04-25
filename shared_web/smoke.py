from flask import Flask


class SmokeTester:
    def __init__(self, app: Flask) -> None:
        self.test_client = app.test_client()
        # Propagate the exceptions to the test client
        self.test_client.testing = True

    def base_tests(self) -> None:
        self.response_test('/', 200)
        self.response_test('/doesnotexist', 404)

    def data_test(self, path: str, expected: str) -> None:
        result = self.test_client.get(path)
        assert expected in result.data.decode('utf-8')

    def response_test(self, path: str, expected_code: int) -> None:
        result = self.test_client.get(path)
        assert result.status_code == expected_code
