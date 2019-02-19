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


class Dimension(Model):
    """Specifications of the Dimension of metrics.

    :param name: The public facing name of the dimension.
    :type name: str
    :param display_name: Localized friendly display name of the dimension.
    :type display_name: str
    :param internal_name: Name of the dimension as it appears in MDM.
    :type internal_name: str
    :param to_be_exported_for_shoebox: A Boolean flag indicating whether this
     dimension should be included for the shoebox export scenario.
    :type to_be_exported_for_shoebox: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'internal_name': {'key': 'internalName', 'type': 'str'},
        'to_be_exported_for_shoebox': {'key': 'toBeExportedForShoebox', 'type': 'bool'},
    }

    def __init__(self, *, name: str=None, display_name: str=None, internal_name: str=None, to_be_exported_for_shoebox: bool=None, **kwargs) -> None:
        super(Dimension, self).__init__(**kwargs)
        self.name = name
        self.display_name = display_name
        self.internal_name = internal_name
        self.to_be_exported_for_shoebox = to_be_exported_for_shoebox
