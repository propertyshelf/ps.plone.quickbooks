# -*- coding: utf-8 -*-
"""Miscellaneous behaviors for ps.plone.quickbooks content types."""

# zope imports
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import alsoProvides

# local imports
from ps.plone.quickbooks import _


QUICKBOOKS_FIELDS = (
    'quickbooks_id',
)


class IQuickbooks(model.Schema):
    """Quickbooks details behavior."""

    fieldset(
        'quickbooks',
        label=_(u'Quickbooks'),
        fields=QUICKBOOKS_FIELDS,
    )

    quickbooks_id = schema.TextLine(
        required=False,
        title=_(u'Quickbooks Customer ID'),
    )

alsoProvides(IQuickbooks, IFormFieldProvider)
