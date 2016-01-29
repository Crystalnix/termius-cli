# -*- coding: utf-8 -*-
"""Transformers is like django rest framework transformer."""
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Transformer(object):
    """Base transformer."""

    def __init__(self, storage):
        """Create new Transformer."""
        assert storage
        self.storage = storage

    @abc.abstractmethod
    def to_model(self, payload):
        """Convert REST API payload to Application models."""

    @abc.abstractmethod
    def to_payload(self, model):
        """Convert Application models to REST API payload."""
        pass
