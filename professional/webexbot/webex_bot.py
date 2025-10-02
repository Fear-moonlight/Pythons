import Flask, request, jsonify
import requests
app = Flask(__name__)
# Replace 'YOUR_BOT_ACCESS_TOKEN' with your actual bot access token
WEBEX_BOT_ACCESS_TOKEN = 'ZDA5YTU0ODItMWZiNi00YzA3LWJmMGItN2U4MGY4YzBmYTJlM2FiNzFiMjYtZWRj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
WEBEX_API_URL = 'https://webexapis.com/v1/messages'
def send_message(room_id, message):
    headers = {
        'Authorization': f'Bearer {WEBEX_BOT_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'roomId': room_id,
        'markdown': message
    }
    response = requests.post(WEBEX_API_URL, headers=headers, json=data)
    return response.json()
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Print the received data for debugging
    if 'data' in data and 'roomId' in data['data']:
        room_id = data['data']['roomId']
        message_id = data['data']['id']
        # Retrieve the message sent to the bot
        response = requests.get(f'{WEBEX_API_URL}/{message_id}', headers={
            'Authorization': f'Bearer {WEBEX_BOT_ACCESS_TOKEN}'
        })
        message_data = response.json()
        message_text = message_data.get('text', '').lower()
        # Respond to specific commands
        if 'hello' in message_text:
            send_message(room_id, 'Hello! How can I assist you today?')
        elif 'help' in message_text:
            send_message(room_id, 'Sure, here are some commands you can use...')
        else:
            send_message(room_id, 'I didn\'t understand that. Type "help" for assistance.')
    return jsonify({'status': 'ok'})
if __name__ == '__main__':
    app.run(port=5000)