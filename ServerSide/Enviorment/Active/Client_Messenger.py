import threading
import queue
import firebase_admin.messaging as messaging

_Message_Queue_ = queue.Queue()

def EnqueueMessage(token, data):
    _Message_Queue_.put((token, data))

def _SendMessage_(token, data):
    message = messaging.Message(data = data, token=token)
    response = messaging.send(message)
    print('Message Sent: ', response)

def MessengerEntryPoint():

    shut_down = False
    def Shutdown_Messenger():
        nonlocal shut_down
        shut_down = True
    from Main import AddShutDownProcess
    AddShutDownProcess(Shutdown_Messenger)

    while True:

        if shut_down:
            break

        try:
            msg_info = _Message_Queue_.get(timeout=1/10)
        except:
            continue

        _SendMessage_(msg_info[0], msg_info[1])
