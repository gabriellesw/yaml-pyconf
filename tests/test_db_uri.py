import unittest
from yaml_pyconf import FlaskConfig
import os


class TestSQLiteURI(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["ENVIRONMENT"] = "development"

    def tearDown(self):
        os.environ.pop("ENVIRONMENT")

    def test_env(self):
        self.assertEqual(os.getenv("ENVIRONMENT"), "development")

    def test_sqlite_uri(self):
        conf = FlaskConfig()
        self.assertEqual(
            conf.SQLALCHEMY_DATABASE_URI,
            "sqlite:////Users/test/projects/project-top-dir/app.db"
        )


class TestPostgreSQLURI(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["ENVIRONMENT"] = "testing"

    def tearDown(self):
        os.environ.pop("ENVIRONMENT")

    def test_postgresql_uri(self):
        conf = FlaskConfig()
        self.assertEqual(
            conf.SQLALCHEMY_DATABASE_URI,
            "postgresql://test_username:test_password@test_server:5432/test_db_name"
        )
