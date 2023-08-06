==================
DjangoAuthProxyApp
==================

AuthProxyApp is a Django app containing a single User Proxy model, which is shared between multiple
Django instances.

The purpose of this Proxy model is to access a single shared "Users" database between Django
applications, with no explicit foreign relations.

It currently operates with a modified User implementation featuring a UUID as a PK, you can easily
implement this by creating your own AbstractUser implementation, and storing all users and permissions
in a single "Users" database.

Quick start
-----------

1. Add "auth_proxy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'auth_proxy'
    ]

2. Run ``python manage.py migrate`` to create the auth_proxy model.

3. To use the proxy, use ``auth_proxy.models.UserProxy`` on foreign relations (like OneToOne, ManyToMany, ManyToOne), instead of ``django.contrib.auth.models.User``. Remember that you're responsible of creating these proxies, unless you use the optional middlewares.

Optional:

4. If you wish to use the Middlewares, include them in settings like this::

    MIDDLEWARE_CLASSES = (
        ...
        'auth_proxy.middleware.GenerateUserProxy',
        'auth_proxy.middleware.AddUserProxyToRequest'
    )

GenerateUserProxy will create the UserProxy on user login, and AddUserProxyToRequest will add the UserProxy to the request, where it can be obtained like this: request.user_proxy.

5. An user router is included. It will route the following labels::

    "admin",
    "auth",
    "profiles",
    "sessions",
    "oauth2_provider",
    "contenttypes"

To a database called ``users``, which you should define in settings (refer to https://docs.djangoproject.com/en/4.0/topics/db/multi-db/ for more instructions). To use this router,
define the following in settings::

    DATABASE_ROUTERS = [
        ...
        'auth_proxy.routers.UsersRouter'
    ]

Note that upper-most routers will have more importance to Django. If you wish to ensure the router will do its intended purpose, insert it in the first position.

Requirements
____________

This UserProxy is intended to be a shared local reference to a User object found in a separate database. This architecture allows multiple Django instances to share the same Users,
and permissions, while retaining the ability to reference User models.

Hence, a shared database is needed, and it should be declared as "users" in all django instances. And a custom User model should be declared, with UUID as primary key.

TODO
----

- REST endpoints to manage UserProxy instances
- Erase UserProxy instances when Users are deleted

Building
--------

Run ``python -m build``