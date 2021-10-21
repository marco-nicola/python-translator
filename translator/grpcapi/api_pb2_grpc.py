# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import api_pb2 as api__pb2


class ApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TranslateText = channel.unary_unary(
                '/api.Api/TranslateText',
                request_serializer=api__pb2.TranslateTextRequest.SerializeToString,
                response_deserializer=api__pb2.TranslateTextResponse.FromString,
                )


class ApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TranslateText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TranslateText': grpc.unary_unary_rpc_method_handler(
                    servicer.TranslateText,
                    request_deserializer=api__pb2.TranslateTextRequest.FromString,
                    response_serializer=api__pb2.TranslateTextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Api', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Api(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TranslateText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Api/TranslateText',
            api__pb2.TranslateTextRequest.SerializeToString,
            api__pb2.TranslateTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
