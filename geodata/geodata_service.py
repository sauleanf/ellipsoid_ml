import grpc
from mordecai import Geoparser

import geodata_pb2
import geodata_pb2_grpc


class GeoDataService(geodata_pb2_grpc.GeoDataServicer):
    def GetData(self, request, context):
        geo = Geoparser()

        res = geo.geoparse(request.sentence)
        res.sort(key=lambda x: x['country_conf'])

        if not res:
            grpc.ServicerContext.abort(self=context,
                                       code=grpc.StatusCode.INVALID_ARGUMENT,
                                       details="Location could not found in sentence!")
        else:
            geo = res[0]['geo']

            return geodata_pb2.GeoDataReply(
                country=geo["admin1"],
                placeName=geo["place_name"],
                lat=float(geo["lat"]),
                lng=float(geo["lon"])
            )
