# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class SimpleEncodingVodJobStatus(Enum):
    CREATED = "CREATED"
    EXECUTING = "EXECUTING"
    FAILURE = "FAILURE"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    ERROR = "ERROR"
    CANCELED = "CANCELED"
