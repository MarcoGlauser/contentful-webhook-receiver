=============================
Contentful Webhook Receiver
=============================

.. image:: https://badge.fury.io/py/contentful-webhook-receiver.svg
    :target: https://badge.fury.io/py/contentful-webhook-receiver

.. image:: https://github.com/MarcoGlauser/contentful-webhook-receiver/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/MarcoGlauser/contentful-webhook-receiver/actions/workflows/ci.yml

.. image:: https://codecov.io/gh/MarcoGlauser/contentful-webhook-receiver/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/MarcoGlauser/contentful-webhook-receiver

A Django package to receive Webhooks from Contentful as signals

Documentation
-------------

The full documentation is at https://contentful-webhook-receiver.readthedocs.io.

Quickstart
----------

Install Contentful Webhook Receiver::

    pip install contentful-webhook-receiver

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'contentful_webhook_receiver.apps.ContentfulWebhookReceiverConfig',
        ...
    )

Add Contentful Webhook Receiver's URL patterns:

.. code-block:: python

    from contentful_webhook_receiver import urls as contentful_webhook_receiver_urls


    urlpatterns = [
        ...
        path(r'^', include(contentful_webhook_receiver_urls)),
        ...
    ]


Listen for the Contentful Webhook Receiver signal:

.. code-block:: python

    @receiver(contentful_publish_entry)
    def entry_published(sender, instance: WebhookInvocation, **kwargs):
        print(instance.data['sys']['content_type']['id'])

Register a Webhook on Contentful:

The path added to the urlpatterns is `contentful-webhook/`.
If you're adding it to the root url configuration the path will be `https://example.com/contentful-webook/`


Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    poetry run tox


Development commands
---------------------

::

    poetry install --with=dev

Cutting new release
-------

::

    poetry version <patch|minor|major>
    # Update changelog
    git add HISTORY.rst pyproject.toml contentful_webhook_receiver/__init__.py
    NEW_RELEASE=$(poetry version --short)
    git commit -m "Release $NEW_RELEASE"
    git tag $NEW_RELEASE
    git push --tags

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
