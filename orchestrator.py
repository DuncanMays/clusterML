import comms.server as srvr
from messages import Base as base_msg
import json

def response_policy(msg_json: str):
    """The manager's response policy to different messages. Returns a message."""
    msg_dict = json.loads(msg_json)

    # if msg_dict["type"] == "init":
    #     msg = Init(msg_dict)
    #     resp_obj = Init_Response(serial.serializeModel(model))
    # elif msg_dict["type"] == "fetch":
    #     resp_obj = Fetch_Response(serial.serializeArray(model.get_weights()))
    # elif msg_dict["type"] == "push":        # do we have policy on this yet???
    #     # for testing purposes, obviously we dont want to kill the worker right after it pushes its weights
    #     resp_obj = Terminate()
    #     weightArray = serial.deserializeArray(msg_dict['weights'])
    #     model.set_weights(weightArray)
    # else: raise TypeError("Didn't receive a known message type.")

    resp_obj = {'payload': 'this is a response'}

    resp = json.dumps(resp_obj)
    # print(resp)

    return resp

def main():
    server = srvr.Server(response_policy)
    server.run()

    """server.run() activates the workflow, and should probably be defined in the manager module.
    We could develop a class for different ML jobs. This would let us provide the job type (specify
    model specs like loss function, model type, optimizer, etc.) and the job structure for workers."""

if __name__ == "__main__":
    main()