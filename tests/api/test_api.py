import unittest

from api.app import app
from api.schemas.response import error_response, success_response


class CompassApiSmokeTest(unittest.TestCase):
    def test_api_app_starts(self):
        self.assertEqual(app.title, "Compass API")
        self.assertEqual(app.version, "v1")

    def test_api_routes_are_registered(self):
        paths = set(app.openapi()["paths"].keys())
        expected_paths = {
            "/api/v1/health",
            "/api/v1/companies",
            "/api/v1/companies/{ticker}",
            "/api/v1/discovery",
            "/api/v1/discovery/top",
            "/api/v1/scores",
            "/api/v1/scores/{ticker}",
            "/api/v1/market",
            "/api/v1/market/sectors",
            "/api/v1/validation",
            "/api/v1/validation/{ticker}",
            "/api/v1/proposals",
            "/api/v1/learning",
            "/api/v1/notifications",
        }
        self.assertTrue(expected_paths.issubset(paths))

    def test_openapi_generation(self):
        schema = app.openapi()
        self.assertEqual(schema["info"]["title"], "Compass API")
        self.assertIn("/api/v1/companies", schema["paths"])
        self.assertIn("/api/v1/discovery/top", schema["paths"])

    def test_unified_response_helpers(self):
        success = success_response({"status": "ok"}).model_dump()
        self.assertTrue(success["success"])
        self.assertEqual(success["version"], "v1")
        self.assertEqual(success["data"]["status"], "ok")

        error = error_response(404, "Not found").model_dump()
        self.assertFalse(error["success"])
        self.assertIsNone(error["data"])
        self.assertEqual(error["error"]["code"], 404)


if __name__ == "__main__":
    unittest.main()
