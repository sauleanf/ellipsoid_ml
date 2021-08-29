from concurrent import futures

import grpc

import geodata_pb2_grpc
from geodata.geodata_service import GeoDataService


class GeoDataServer:
    @classmethod
    def serve(cls, port: int = 50051):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        geodata_pb2_grpc.add_GeoDataServicer_to_server(GeoDataService(), server)
        server.add_insecure_port(f'[::]:{port}')
        server.start()
        server.wait_for_termination()
