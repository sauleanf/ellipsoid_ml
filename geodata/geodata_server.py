from concurrent import futures

import grpc

from core.grpc import geodata_pb2_grpc
from geodata.geodata_service import GeoDataService


class GeoDataServer:
    """
    Runs a GRPC Server
    """
    @classmethod
    def serve(cls, port: int = 50051):
        """
        Runs server

        :param port: the port for the server
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        geodata_pb2_grpc.add_GeoDataServicer_to_server(GeoDataService(), server)
        server.add_insecure_port(f'[::]:{port}')
        server.start()
        server.wait_for_termination()
