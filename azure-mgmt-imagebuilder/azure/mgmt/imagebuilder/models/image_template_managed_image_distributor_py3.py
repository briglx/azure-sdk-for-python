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

from .image_template_distributor_py3 import ImageTemplateDistributor


class ImageTemplateManagedImageDistributor(ImageTemplateDistributor):
    """Distribute as a Managed Disk Image.

    All required parameters must be populated in order to send to Azure.

    :param run_output_name: Required. The name to be used for the associated
     RunOutput.
    :type run_output_name: str
    :param artifact_tags: Tags that will be applied to the artifact once it
     has been created/updated by the distributor.
    :type artifact_tags: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    :param image_id: Required. Resource Id of the Managed Disk Image
    :type image_id: str
    :param location: Required. Azure location for the image, should match if
     image already exists
    :type location: str
    """

    _validation = {
        'run_output_name': {'required': True, 'pattern': r'^[A-Za-z0-9-_]{1,64}$'},
        'type': {'required': True},
        'image_id': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'run_output_name': {'key': 'runOutputName', 'type': 'str'},
        'artifact_tags': {'key': 'artifactTags', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, run_output_name: str, image_id: str, location: str, artifact_tags=None, **kwargs) -> None:
        super(ImageTemplateManagedImageDistributor, self).__init__(run_output_name=run_output_name, artifact_tags=artifact_tags, **kwargs)
        self.image_id = image_id
        self.location = location
        self.type = 'ManagedImage'
