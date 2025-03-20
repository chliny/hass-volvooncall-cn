# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import dtlinternet_pb2 as dtlinternet__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in dtlinternet_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class DtlInternetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamLastKnownLocations = channel.unary_stream(
            '/dtlinternet.DtlInternetService/StreamLastKnownLocations',
            request_serializer=dtlinternet__pb2.StreamLastKnownLocationsReq.SerializeToString,
            response_deserializer=dtlinternet__pb2.StreamLastKnownLocationsResp.FromString,
            _registered_method=True)


class DtlInternetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamLastKnownLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DtlInternetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'StreamLastKnownLocations': grpc.unary_stream_rpc_method_handler(
            servicer.StreamLastKnownLocations,
            request_deserializer=dtlinternet__pb2.StreamLastKnownLocationsReq.FromString,
            response_serializer=dtlinternet__pb2.StreamLastKnownLocationsResp.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'dtlinternet.DtlInternetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('dtlinternet.DtlInternetService', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class DtlInternetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamLastKnownLocations(request,
                                 target,
                                 options=(),
                                 channel_credentials=None,
                                 call_credentials=None,
                                 insecure=False,
                                 compression=None,
                                 wait_for_ready=None,
                                 timeout=None,
                                 metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/dtlinternet.DtlInternetService/StreamLastKnownLocations',
            dtlinternet__pb2.StreamLastKnownLocationsReq.SerializeToString,
            dtlinternet__pb2.StreamLastKnownLocationsResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
