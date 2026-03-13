import json

def log_route(intent, message, response):

    log = {
        "intent": intent["intent"],
        "confidence": intent["confidence"],
        "message": message,
        "response": response
    }

    with open("route_log.jsonl","a") as f:
        f.write(json.dumps(log) + "\n")