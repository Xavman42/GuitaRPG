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
    elif region == "tambura":
        name = "tamb"
    elif region == "bartok":
        name = "bart"
    elif region == "none":
        name = "scrape"
        level = 1
    elif region == "rake":
        name = "rake"
    elif region == "triad":
        name = "triad"
    elif region == "harmonic":
        name = "harmonic"
    elif region == "melody":
        name = "melody"
    elif region == "rasg":
        name = "rasg"
    elif region == "adv_harm":
        name = "adv_harm"
    elif region == "tremolo":
        name = "trem"
    elif region == "end":
        name = "end"
    elif region == "Null":
        name = "Null"
    else:
        print("what region is this!?")
        print(region)
        name = "nope"
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
    send_particle(my_client, "bart", 2)
