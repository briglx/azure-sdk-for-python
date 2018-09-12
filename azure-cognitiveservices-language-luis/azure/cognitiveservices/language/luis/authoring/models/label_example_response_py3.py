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


class LabelExampleResponse(Model):
    """Response when adding a labeled example.

    :param utterance_text: The sample's utterance.
    :type utterance_text: str
    :param example_id: The newly created sample ID.
    :type example_id: int
    """

    _attribute_map = {
        'utterance_text': {'key': 'UtteranceText', 'type': 'str'},
        'example_id': {'key': 'ExampleId', 'type': 'int'},
    }

    def __init__(self, *, utterance_text: str=None, example_id: int=None, **kwargs) -> None:
        super(LabelExampleResponse, self).__init__(**kwargs)
        self.utterance_text = utterance_text
        self.example_id = example_id