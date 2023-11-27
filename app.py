from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['0I0A4VMQ0nPph/vzWqyxMY30vxg5+3jvJ6BHQ1QetROW4UjQ7x7WiZf3QvP+r17CAB1Ot9NzCVvBB+4MxswW+gFrfxcC6j50zH6DO8Gr4tvKjBxA/Z5RpB3RcpnHeRG6rduR/+nQ4eShnNZ5Xv9MqwdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['33a38cfcfa226a5e585a1921c77b90ba'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)