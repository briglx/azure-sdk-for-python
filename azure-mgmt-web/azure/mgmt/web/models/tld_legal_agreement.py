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


class TldLegalAgreement(Model):
    """Legal agreement for a top level domain.

    All required parameters must be populated in order to send to Azure.

    :param agreement_key: Required. Unique identifier for the agreement.
    :type agreement_key: str
    :param title: Required. Agreement title.
    :type title: str
    :param content: Required. Agreement details.
    :type content: str
    :param url: URL where a copy of the agreement details is hosted.
    :type url: str
    """

    _validation = {
        'agreement_key': {'required': True},
        'title': {'required': True},
        'content': {'required': True},
    }

    _attribute_map = {
        'agreement_key': {'key': 'agreementKey', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TldLegalAgreement, self).__init__(**kwargs)
        self.agreement_key = kwargs.get('agreement_key', None)
        self.title = kwargs.get('title', None)
        self.content = kwargs.get('content', None)
        self.url = kwargs.get('url', None)
