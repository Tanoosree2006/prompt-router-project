from classifier import classify_intent
from router import route_and_respond
from logger import log_route

def main():

    while True:

        message = input("\nUser: ")

        intent = classify_intent(message)

        print("Detected Intent:", intent)

        response = route_and_respond(message, intent)

        log_route(intent, message, response)

        print("\nAssistant:", response)

if __name__ == "__main__":
    main()