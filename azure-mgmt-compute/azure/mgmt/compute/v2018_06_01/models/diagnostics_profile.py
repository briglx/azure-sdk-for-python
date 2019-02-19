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


class DiagnosticsProfile(Model):
    """Specifies the boot diagnostic settings state. <br><br>Minimum api-version:
    2015-06-15.

    :param boot_diagnostics: Boot Diagnostics is a debugging feature which
     allows you to view Console Output and Screenshot to diagnose VM status.
     <br><br> You can easily view the output of your console log. <br><br>
     Azure also enables you to see a screenshot of the VM from the hypervisor.
    :type boot_diagnostics:
     ~azure.mgmt.compute.v2018_06_01.models.BootDiagnostics
    """

    _attribute_map = {
        'boot_diagnostics': {'key': 'bootDiagnostics', 'type': 'BootDiagnostics'},
    }

    def __init__(self, **kwargs):
        super(DiagnosticsProfile, self).__init__(**kwargs)
        self.boot_diagnostics = kwargs.get('boot_diagnostics', None)
