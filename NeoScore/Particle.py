from pyOSC3 import OSCClient, OSCMessage

class Particle:
    """Sends OSC messages to SuperCollider
    
    """
    
    def __init__(
        self,
        area: str = "null area",
        region: str = "null region",
        level: int = 1
    ):
        self.area = area
        self.region = region
        self.level = level
        self.client = OSCClient()
        self.client.connect( ( '127.0.0.1', 57120 ) )
        self.msg = OSCMessage()
        self.msg.setAddress("/print")
        
    def send_particle(self):
    #This sends a message to SuperCollider. 
        self.msg.clearData()
        if(self.area == "A"):
            self.msg.append(self.area)
            self.msg.append(self.region)
            self.msg.append(self.level)
        try:
            self.client.send(self.msg)
        except:
            print("message failed to send to SuperCollider")


if __name__ == '__main__':
    my_particle = Particle("A", "perc", 3)

    my_particle.send_particle()