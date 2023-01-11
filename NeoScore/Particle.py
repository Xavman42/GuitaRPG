import pyOSC3


def send_particle(client, region, level):
    # This sends a message to SuperCollider.
    msg = pyOSC3.OSCMessage()
    msg.setAddress("/print")
    msg.clearData()
    if region == "scrape":
        name = "scrape"
    elif region == "perc":
        name = "perc"
    elif region == "tamb":
        name = "tamb"
    elif region == "bart":
        name = "bart"
    elif region == "none":
        name = "scrape"
        level = 1
    elif region == "Null":
        name = "Null"
    else:
        print("what region is this!?")
    msg.append("area")
    msg.append(name)
    msg.append(level)
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
    send_particle(my_client, "none", 2)
