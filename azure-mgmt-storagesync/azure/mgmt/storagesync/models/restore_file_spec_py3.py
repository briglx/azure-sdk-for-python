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


class RestoreFileSpec(Model):
    """Restore file spec.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param path: Restore file spec path
    :type path: str
    :ivar isdir: Restore file spec isdir
    :vartype isdir: bool
    """

    _validation = {
        'isdir': {'readonly': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'isdir': {'key': 'isdir', 'type': 'bool'},
    }

    def __init__(self, *, path: str=None, **kwargs) -> None:
        super(RestoreFileSpec, self).__init__(**kwargs)
        self.path = path
        self.isdir = None
