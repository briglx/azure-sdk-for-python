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


class LegalHold(Model):
    """The LegalHold property of a blob container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar has_legal_hold: The hasLegalHold public property is set to true by
     SRP if there are at least one existing tag. The hasLegalHold public
     property is set to false by SRP if all existing legal hold tags are
     cleared out. There can be a maximum of 1000 blob containers with
     hasLegalHold=true for a given account.
    :vartype has_legal_hold: bool
    :param tags: Required. Each tag should be 3 to 23 alphanumeric characters
     and is normalized to lower case at SRP.
    :type tags: list[str]
    """

    _validation = {
        'has_legal_hold': {'readonly': True},
        'tags': {'required': True},
    }

    _attribute_map = {
        'has_legal_hold': {'key': 'hasLegalHold', 'type': 'bool'},
        'tags': {'key': 'tags', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(LegalHold, self).__init__(**kwargs)
        self.has_legal_hold = None
        self.tags = kwargs.get('tags', None)