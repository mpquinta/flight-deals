class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, stop_overs=0, via_city=""):
        self.stop_overs=stop_overs,
        self.via_city=via_city