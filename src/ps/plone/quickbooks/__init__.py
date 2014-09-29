# -*- coding: utf-8 -*-
"""Quickbooks integration for Plone."""

# zope imports
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('ps.plone.quickbooks')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
