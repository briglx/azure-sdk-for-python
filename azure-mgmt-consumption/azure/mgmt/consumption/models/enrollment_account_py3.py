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

from .resource_py3 import Resource


class EnrollmentAccount(Resource):
    """An account resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :param account_name: The account name.
    :type account_name: str
    :param cost_center: The cost center name.
    :type cost_center: str
    :param account_owner: The account owner
    :type account_owner: str
    :param status: The status for account.
    :type status: str
    :param start_date: Account Start Date
    :type start_date: datetime
    :param end_date: Account End Date
    :type end_date: datetime
    :param department: Associated department. By default this is not
     populated, unless it's specified in $expand.
    :type department: ~azure.mgmt.consumption.models.Department
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'cost_center': {'key': 'properties.costCenter', 'type': 'str'},
        'account_owner': {'key': 'properties.accountOwner', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'start_date': {'key': 'properties.startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'properties.endDate', 'type': 'iso-8601'},
        'department': {'key': 'properties.department', 'type': 'Department'},
    }

    def __init__(self, *, account_name: str=None, cost_center: str=None, account_owner: str=None, status: str=None, start_date=None, end_date=None, department=None, **kwargs) -> None:
        super(EnrollmentAccount, self).__init__(**kwargs)
        self.account_name = account_name
        self.cost_center = cost_center
        self.account_owner = account_owner
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.department = department
