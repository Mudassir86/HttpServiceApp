from src.version_service import VersionService
import unittest
import responses


class VersionServiceTestCase(unittest.TestCase):
    @responses.activate
    def test_verionz_success(self):
        sut = VersionService()
        responses.add(responses.GET, 'https://api.github.com/repos/Mudassir86/HttpServiceApp', json={'name': 'bla bal'},
                      status=200)
        responses.add(responses.GET, 'https://api.github.com/repos/Mudassir86/HttpServiceApp/commits/master',
                      json={'sha': 'my sha'}, status=200)

        result = sut.versionz()

        expected = {"name": "bla bal", "last_commit_hash": "my sha"}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
