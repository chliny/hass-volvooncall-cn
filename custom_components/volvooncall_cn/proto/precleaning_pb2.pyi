from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    START_REASON_UNSPECIFIED: _ClassVar[StartReason]
    REMOTE: _ClassVar[StartReason]
    MANUALLY_FROM_CAR: _ClassVar[StartReason]

class RunningStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUNNING_STATUS_UNSPECIFIED: _ClassVar[RunningStatus]
    ON: _ClassVar[RunningStatus]
    OFF: _ClassVar[RunningStatus]
    PENDING: _ClassVar[RunningStatus]

class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_TYPE_UNSPECIFIED: _ClassVar[ErrorType]
    GENERIC_ERROR: _ClassVar[ErrorType]
    INTERRUPTED: _ClassVar[ErrorType]
START_REASON_UNSPECIFIED: StartReason
REMOTE: StartReason
MANUALLY_FROM_CAR: StartReason
RUNNING_STATUS_UNSPECIFIED: RunningStatus
ON: RunningStatus
OFF: RunningStatus
PENDING: RunningStatus
ERROR_TYPE_UNSPECIFIED: ErrorType
GENERIC_ERROR: ErrorType
INTERRUPTED: ErrorType

class Timestamp(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class GetPreCleaningReq(_message.Message):
    __slots__ = ("id", "vin")
    ID_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    vin: str
    def __init__(self, id: _Optional[str] = ..., vin: _Optional[str] = ...) -> None: ...

class PreCleaningData(_message.Message):
    __slots__ = ("timestamp", "lastCycleCompleted", "measurementDate", "startedAt", "endingAt", "runningStatus", "startReason", "lastCycleValid", "measuredAirQualityIndex", "measuredParticulateMatter25", "runtimeLeftMinutes", "error")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LASTCYCLECOMPLETED_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENTDATE_FIELD_NUMBER: _ClassVar[int]
    STARTEDAT_FIELD_NUMBER: _ClassVar[int]
    ENDINGAT_FIELD_NUMBER: _ClassVar[int]
    RUNNINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    STARTREASON_FIELD_NUMBER: _ClassVar[int]
    LASTCYCLEVALID_FIELD_NUMBER: _ClassVar[int]
    MEASUREDAIRQUALITYINDEX_FIELD_NUMBER: _ClassVar[int]
    MEASUREDPARTICULATEMATTER25_FIELD_NUMBER: _ClassVar[int]
    RUNTIMELEFTMINUTES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    timestamp: Timestamp
    lastCycleCompleted: Timestamp
    measurementDate: Timestamp
    startedAt: Timestamp
    endingAt: Timestamp
    runningStatus: RunningStatus
    startReason: StartReason
    lastCycleValid: bool
    measuredAirQualityIndex: int
    measuredParticulateMatter25: int
    runtimeLeftMinutes: int
    error: ErrorType
    def __init__(self, timestamp: _Optional[_Union[Timestamp, _Mapping]] = ..., lastCycleCompleted: _Optional[_Union[Timestamp, _Mapping]] = ..., measurementDate: _Optional[_Union[Timestamp, _Mapping]] = ..., startedAt: _Optional[_Union[Timestamp, _Mapping]] = ..., endingAt: _Optional[_Union[Timestamp, _Mapping]] = ..., runningStatus: _Optional[_Union[RunningStatus, str]] = ..., startReason: _Optional[_Union[StartReason, str]] = ..., lastCycleValid: bool = ..., measuredAirQualityIndex: _Optional[int] = ..., measuredParticulateMatter25: _Optional[int] = ..., runtimeLeftMinutes: _Optional[int] = ..., error: _Optional[_Union[ErrorType, str]] = ...) -> None: ...

class GetPreCleaningResp(_message.Message):
    __slots__ = ("id", "vin", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    vin: str
    data: PreCleaningData
    def __init__(self, id: _Optional[str] = ..., vin: _Optional[str] = ..., data: _Optional[_Union[PreCleaningData, _Mapping]] = ...) -> None: ...
