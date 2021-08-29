from __future__ import print_function

import grpc

import geodata_pb2
import geodata_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub = geodata_pb2_grpc.GeoDataStub(channel)
        response = stub.GetData(geodata_pb2.GeoDataRequest(sentence="I like  london!"))
    print(response)


if __name__ == '__main__':
    run()
