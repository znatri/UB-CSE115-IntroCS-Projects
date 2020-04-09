logfile = "chat.txt"

def get_chat():
    full_chat = []
    with open(logfile) as file:
        for line in file:
            rec = {"message": line.rstrip("\n\r")}
            full_chat.append(rec)
    return full_chat

def add_message(message):
    with open(logfile, "a") as file:
        file.write(message + '\n')