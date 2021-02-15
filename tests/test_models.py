#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_contentful-webhook-receiver
------------

Tests for `contentful-webhook-receiver` models module.
"""
from unittest import mock

from django.test import TestCase
from rest_framework.test import APIClient

from contentful_webhook_receiver.models import WebhookInvocation
from contentful_webhook_receiver.views import WebHookReceiverView
from tests import webhook_test_data


class TestContentfulWebhookReceiver(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def djangoify_headers(self, headers:{}):
        return {f'HTTP_{key.upper().replace("-", "_")}':value for key, value in headers.items()}

    @mock.patch('contentful_webhook_receiver.signals.contentful_publish_entry.send')
    def test_entry_publish_dispatch(self, signal_mock):
        contentful_headers = {
            "X-Contentful-Topic": "ContentManagement.Entry.publish",
            "X-Contentful-Webhook-Name": "Django Staging",
            "Content-Type": "application/json"
        }
        data = webhook_test_data.homepage_publish_event
        headers = self.djangoify_headers(contentful_headers)
        response = self.client.post('/hook/', data=data, format='json', **headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, WebhookInvocation.objects.count())
        expected_instance = WebhookInvocation.objects.first()
        signal_mock.assert_called_once_with(WebHookReceiverView, instance=expected_instance)

