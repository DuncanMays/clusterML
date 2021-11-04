import comms.client as client
import json

cl = client.Client()

payload = 'hello there'

msg = json.dumps(payload)

response = cl.send(msg)

print(response)