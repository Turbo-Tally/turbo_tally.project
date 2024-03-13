#
# :: api_server.py 
# Set up API Server (REST + WS API)
# 
from scans.core.logger import Logger

class APIServer: 
    def __init__(self):
        Logger.clear("api_server")
        Logger.log("api_server", "> Hello, from API Server!")
        pass
        
    def init(self):
        Logger.log("api_server", "> Initializing API Server...") 

    def run(self):
        pass 