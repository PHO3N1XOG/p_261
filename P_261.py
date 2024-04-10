from etherpad_lite import EtherpadLiteClient

etherclient = EtherpadLiteClient(base_params={"api key":""})

group = etherclient.createGroup()

print("Your group is:", group)

create_pad = etherclient.createPad(padID = "whitehat", text = "Hello world!")

print("Your pad is:", createPad)