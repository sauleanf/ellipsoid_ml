from geodata.geodata_server import GeoDataServer
import os

if __name__ == "__main__":
    if os.environ.get('https_proxy'):
        del os.environ['https_proxy']
    if os.environ.get('http_proxy'):
        del os.environ['http_proxy']

    GeoDataServer.serve()
