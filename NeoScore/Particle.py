import pyOSC3


def send_particle(client, region):
    # This sends a message to SuperCollider.
    msg = pyOSC3.OSCMessage()
    msg.setAddress("/print")
    msg.clearData()
    if region == "scrape":
        name = "scratchy_string"
    elif region == "B":
        name = "plinky_wood"
    elif region == "C":
        name = "cavernous_thunk"
    elif region == "Null":
        name = "Null"
    else:
        print("what region is this!?")
    msg.append(name)
    try:
        client.send(msg)
    except ValueError:
        print("message failed to send to SuperCollider")


def update_effect(client, effect_name):
    msg = pyOSC3.OSCMessage()
    msg.setAddress("/print")
    msg.clearData()
    msg.append(effect_name)
    try:
        client.send(msg)
    except ValueError:
        print("message failed to send to SuperCollider")


if __name__ == '__main__':
    my_client = pyOSC3.OSCClient()
    my_client.connect(('127.0.0.1', 57120))
