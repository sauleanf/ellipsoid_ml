# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from core.grpc import geodata_pb2 as core_dot_grpc_dot_geodata__pb2


class GeoDataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_unary(
                '/core.grpc.GeoData/GetData',
                request_serializer=core_dot_grpc_dot_geodata__pb2.GeoDataRequest.SerializeToString,
                response_deserializer=core_dot_grpc_dot_geodata__pb2.GeoDataReply.FromString,
                )


class GeoDataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeoDataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=core_dot_grpc_dot_geodata__pb2.GeoDataRequest.FromString,
                    response_serializer=core_dot_grpc_dot_geodata__pb2.GeoDataReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'core.grpc.GeoData', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeoData(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.grpc.GeoData/GetData',
            core_dot_grpc_dot_geodata__pb2.GeoDataRequest.SerializeToString,
            core_dot_grpc_dot_geodata__pb2.GeoDataReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
