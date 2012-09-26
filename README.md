A Flask Application Template
============================

Copying the template
--------------------

Make a copy of the directory and rename every instance of "myapplication"
to the name of your application.

TODO: write a Python script to prompt the user for a new name and do this automatically.

Run the application in debug mode
---------------------------------

Make sure that Flask is installed:

% sudo easy_install Flask

From inside the top level directory, start the app from the command line:

% ./run_myapplication.py

Add new pages
-------------

* Create a new file in the "controller" directory.
* Add the name of the file to the "all" list in controllers/__init__.py
* Add a new template for the page as needed in templates.

The `@app.route('/')` decorator defines the URL. To create a page
at `http://your.domain.com/somePage`, the decorator would be

    @app.route('/somePage')
    
The decorated function immediately below that will typically have the same
name as the page, but it doesn't have to. The decorator just binds the function
to the name that it's given.

Controllers or views?
---------------------

Flask calls the code that takes HTTP requests and returns HTML responses
"views". In the [MVC](http://en.wikipedia.org/wiki/Model–view–controller) design pattern (which Flask clearly follows), these parts of the code are actually called
"controllers". In MVC, the views here are actually the HTML responses, so this is terribly confusing. That is why the folder that contains the Python code is called "controllers". Just so you know.

Typically, there will be one controller file per web page, but this is not required.