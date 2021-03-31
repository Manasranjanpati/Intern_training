# Introduction
### Virtual Environment (The Saviour)
The best time to learn about virtual environment is when you are a beginner in learning python/django as it will be very much helpful.

### What is virtual environment ?

A virtual environment is a way for you to have multiple versions of python on your machine without them clashing with each other, each version can be considered as a development environment and you can have different versions of python libraries and modules all isolated from one another. For more information visit virtualenv

### Importance of virtual environment.

Say, if you’re working on an open source project that uses django 1.7 but locally, you installed django 2.0 for other project. It’s almost impossible for you to contribute to open source because you’ll get a lot of errors due to the difference in django versions. If you decide to downgrade to django 1.7 then you can’t work on your project anymore because that depend on django 2.0. Virtual environment lets you handle this situation by creating a separate virtual(development) environments that are not tied together and can be activated/deactivated easily whenever you want.

### How does virtual environment work ?
```bash
$ virtualenv venv
$ source venv/Scripts/activate
(venv)$                 // The current shell starts using the virtual environment.
(venv)$ deactivate      // virtual environment deactivated.
```

## Downloading and Installing
```python
Option 1
$ pip install Django==2.0.3
Option 2

$ git clone https://github.com/django/django.git // latest version of django
```

# What is Django?
Django is a free open-source web framework, written in Python, which follows the model-view-template(MVT) architectural pattern. It is maintained by Django Software Foundation(DSF). Django’s primary goal is to ease the creation of complex, database-driven websites.
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

# Django Features:
1. Fast
2. Code Reusability
3. Security
4. Scalable
5. Versatile
6. Documentation
7. Community
8. Inside Django
9. Django Philosophy
10. The web framework for perfectionists with deadlines.

# Inside Django 
* Django Architecture
    Django follows the MVC pattern closely, however it does use its own logic in the implementation. Because the “C” is handled by the framework itself and most of the excitement in Django happens in models, templates and views, Django is often referred to as an MTV framework.

* Django ORM
    ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.

* DRY principle
    To help developers adhere to the DRY principle, Django forces users to use the MVC code structure. Django forces users to use this format by initially creating a views.py, models.py, and template files. By keeping the controller code separate from the views, it allows multiple controllers to use the same view.

* Loose coupling
    A fundamental goal of Django’s stack is loose coupling and tight cohesion. The various layers of the framework shouldn’t “know” about each other unless absolutely necessary.

    For example, the template system knows nothing about Web requests, the database layer knows nothing about data display and the view system doesn’t care which template system a programmer uses.

* Request-Response cycle
    Django uses request and response objects to pass state through the system.

    When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

* Middleware
    Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.

* Template tags
    Django’s template language comes with a wide variety of built-in tags and filters designed to address the presentation logic needs of your application.


