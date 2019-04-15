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

from enum import Enum


class SkuName(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SkuTier(str, Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class NameSpaceType(str, Enum):

    messaging = "Messaging"
    notification_hub = "NotificationHub"
    mixed = "Mixed"
    event_hub = "EventHub"
    relay = "Relay"


class AccessRights(str, Enum):

    manage = "Manage"
    send = "Send"
    listen = "Listen"


class KeyType(str, Enum):

    primary_key = "PrimaryKey"
    secondary_key = "SecondaryKey"


class EntityStatus(str, Enum):

    active = "Active"
    disabled = "Disabled"
    restoring = "Restoring"
    send_disabled = "SendDisabled"
    receive_disabled = "ReceiveDisabled"
    creating = "Creating"
    deleting = "Deleting"
    renaming = "Renaming"
    unknown = "Unknown"


class UnavailableReason(str, Enum):

    none = "None"
    invalid_name = "InvalidName"
    subscription_is_disabled = "SubscriptionIsDisabled"
    name_in_use = "NameInUse"
    name_in_lockdown = "NameInLockdown"
    too_many_namespace_in_current_subscription = "TooManyNamespaceInCurrentSubscription"


class FilterType(str, Enum):

    sql_filter = "SqlFilter"
    correlation_filter = "CorrelationFilter"


class EncodingCaptureDescription(str, Enum):

    avro = "Avro"
    avro_deflate = "AvroDeflate"


class ProvisioningStateDR(str, Enum):

    accepted = "Accepted"
    succeeded = "Succeeded"
    failed = "Failed"


class RoleDisasterRecovery(str, Enum):

    primary = "Primary"
    primary_not_replicating = "PrimaryNotReplicating"
    secondary = "Secondary"


class NetworkRuleIPAction(str, Enum):

    allow = "Allow"


class DefaultAction(str, Enum):

    allow = "Allow"
    deny = "Deny"
