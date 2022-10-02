from pyOSC3 import OSCClient, OSCMessage

class Particle:
    """Sends OSC messages to SuperCollider
    
    """
    
    def __init__(
        self,
        message: str = "placeholder message",
        area: str = "null area",
        region: str = "null region",
    ):
        
        self.client = OSCClient()
        self.client.connect( ( '127.0.0.1', 57120 ) )
        self.sender = OSCMessage()
        self.sender.setAddress("/print")
        
    @property
    def area(self) -> str:
        """There are a total of three areas in this piece, each of which will have names."""
        return self._area
    
    @property
    def region(self) -> str:
        """There are a number of regions in each area"""
        return self._region
    
    @property
    def message(self) -> str:
        """This is the OSC message to be sent to SuperCollider"""
        return self._message
           
    def send_particle(self):
    #This sends a message to SuperCollider. 
        self.sender.clearData()
        if(self.area == "A"):
            self.sender.append("area A: ")
            if(self.region == "A"):self.sender.append("scratchy_string")
            elif(self.region == "B"):self.sender.append("plinky_wood")
            elif(self.region == "C"):self.sender("cavernous_thunk")
            elif(self.region == "Null"):self.sender.append("Null")
            else: print("what region is this!?")
        try:
            self.client.send(self.sender)
        except:
            print("message failed to send to SuperCollider")