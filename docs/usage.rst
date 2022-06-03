=====
Usage
=====

To use Contentful Webhook Receiver in a project, add it to your `INSTALLED_APPS`:

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
