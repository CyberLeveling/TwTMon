import requests
import time

# Function to send message to Telegram channel
def send_message(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Status code:", response.status_code)

# Replace these values with your bot token and chat ID
bot_token = ""
chat_id = ""

# Function to read output file, send unique messages, and update sent messages list
def process_output_file():
    sent_messages = set()
    with open("sent_messages.txt", "r") as f:
        for line in f:
            sent_messages.add(line.strip())

    with open("output.txt", "r") as f:
        for line in f:
            message = line.strip()
            # Check if the message has been sent before
            if message not in sent_messages:
                send_message(bot_token, chat_id, message)
                # Record the sent message in the sent file
                with open("sent_messages.txt", "a") as sent_file:
                    sent_file.write(message + "\n")

# Main loop to process output file every 5 minutes
while True:
    process_output_file()
    time.sleep(100)  # Sleep for 5 minutes
