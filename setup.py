import json

def main():
    telegram_token = input("Bitte geben Sie den Telegram Token ein: ")
    chat_id = input("Bitte geben Sie die Chat ID ein: ")
    login = input("Bitte geben Sie den Login für die API-Anfrage ein: ")
    api_key = input("Bitte geben Sie den API Key für die API-Anfrage ein: ")
    print("Setup wurde erfolgreich abgeschlossen!")

    values = {
        "telegram_token": telegram_token,
        "chat_id": chat_id,
        "login": login,
        "api_key": api_key
    }
    with open("variables.txt", "w") as file:
        json.dump(values, file)