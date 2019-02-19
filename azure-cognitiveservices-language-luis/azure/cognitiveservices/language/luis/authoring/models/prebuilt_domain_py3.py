# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrebuiltDomain(Model):
    """Prebuilt Domain.

    :param name:
    :type name: str
    :param culture:
    :type culture: str
    :param description:
    :type description: str
    :param examples:
    :type examples: str
    :param intents:
    :type intents:
     list[~azure.cognitiveservices.language.luis.authoring.models.PrebuiltDomainItem]
    :param entities:
    :type entities:
     list[~azure.cognitiveservices.language.luis.authoring.models.PrebuiltDomainItem]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'culture': {'key': 'culture', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'examples': {'key': 'examples', 'type': 'str'},
        'intents': {'key': 'intents', 'type': '[PrebuiltDomainItem]'},
        'entities': {'key': 'entities', 'type': '[PrebuiltDomainItem]'},
    }

    def __init__(self, *, name: str=None, culture: str=None, description: str=None, examples: str=None, intents=None, entities=None, **kwargs) -> None:
        super(PrebuiltDomain, self).__init__(**kwargs)
        self.name = name
        self.culture = culture
        self.description = description
        self.examples = examples
        self.intents = intents
        self.entities = entities
