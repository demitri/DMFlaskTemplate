
## Unit Testing

All test files in this directory should have the prefix `test_`;
this will make them autodiscoverable by `pytest`.

## Useful References

#### Links

* [Testing JSON responses in Flask](https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html)
* [Testing a Flask Application using pytest](http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)
* [Delightful testing with pytest and Flask-SQLAlchemy](http://alexmic.net/flask-sqlalchemy-pytest/) (We're not using the SQLAlchemy extension.)

#### pytest-flask

It's possible that we can omit this extension as a dependency if we
define `config` in `conftest.py` (code in file, but commented out).
But things work now.

* [pytest-flask on GitHub](https://github.com/pytest-dev/pytest-flask)
* [pytest-flask Documentation](https://pytest-flask.readthedocs.io/en/latest/)
* [Example pytest-flask usage pattern](https://github.com/pytest-dev/pytest-flask/issues/7)
