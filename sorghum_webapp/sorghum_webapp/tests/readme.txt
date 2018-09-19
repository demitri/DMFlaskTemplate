
## Unit Testing

All test files in this directory should have the prefix `test_`;
this will make them autodiscoverable by `pytest`.

### Useful Flags

Add these flags to `py.test` on the command line.

* `-s` : allow print statements to appear inline (STDOUT not captured and placed at end)
* `-v` : verbose output of tests
* `--fixtures` : list all available fixtures

### Links

* [Testing JSON responses in Flask](https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html)
* [Testing a Flask Application using pytest](http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)
* [Delightful testing with pytest and Flask-SQLAlchemy](http://alexmic.net/flask-sqlalchemy-pytest/) (We're not using the SQLAlchemy extension.)

### pytest-flask

It's possible that we can omit this extension as a dependency if we
define `config` in `conftest.py` (code in file, but commented out).
But things work now.

* [pytest-flask on GitHub](https://github.com/pytest-dev/pytest-flask)
* [pytest-flask Documentation](https://pytest-flask.readthedocs.io/en/latest/)
* [Example pytest-flask usage pattern](https://github.com/pytest-dev/pytest-flask/issues/7)

### Produce a Summary Report

```
py.test -r<x>
```

where `<x>` is one or more of:

Ref: <https://docs.pytest.org/en/latest/usage.html#detailed-summary-report>

 * `f` - failed
 * `E` - error
 * `s` - skipped
 * `x` - xfailed
 * `X` - xpassed
 * `p` - passed
 * `P` - passed with output
 * `a` - all except pP

