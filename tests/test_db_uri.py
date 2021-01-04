import unittest
from yaml_pyconf import FlaskConfig
import os


class TestSQLiteURI(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["FLASK_ENV"] = "development"

    def tearDown(self):
        os.environ.pop("FLASK_ENV")

    def test_env(self):
        self.assertEqual(os.getenv("FLASK_ENV"), "development")

    def test_sqlite_uri(self):
        conf = FlaskConfig("sample", "sample")
        self.assertEqual(
            conf.SQLALCHEMY_DATABASE_URI,
            "sqlite:////Users/test/projects/project-top-dir/app.db"
        )


class TestPostgreSQLURI(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["FLASK_ENV"] = "testing"

    def tearDown(self):
        os.environ.pop("FLASK_ENV")

    def test_postgresql_uri(self):
        conf = FlaskConfig("sample", "sample")
        self.assertEqual(
            conf.SQLALCHEMY_DATABASE_URI,
            "postgresql://test_username:test_password@test_server:5432/test_db_name"
        )


class TestSQLiteRelative(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["FLASK_ENV"] = "development"
        os.environ["SQLITE_PROJECT_DIRECTORY"] = ""

    def tearDown(self):
        os.environ.pop("FLASK_ENV")
        os.environ.pop("SQLITE_PROJECT_DIRECTORY")

    def test_sqlite_relative_path(self):
        conf = FlaskConfig("sample", "sample")
        conf.SQLALCHEMY_DATABASE_URI  # This sets the directory being tested below
        self.assertEqual(
            conf.SQLITE_PROJECT_DIRECTORY,
            os.path.abspath(os.curdir)
        )