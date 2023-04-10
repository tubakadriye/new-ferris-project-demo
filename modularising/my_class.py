import json

class MyClass():
    @staticmethod
    def print_payload(payload):
        #print(payload)
        for k, v in payload.items():
            print(k, v)
        


