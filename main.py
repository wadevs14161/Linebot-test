from flask import Flask, jsonify, request, abort
import os
import sys
import requests
from argparse import ArgumentParser

from linebot.v3 import (
    WebhookParser,
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    ImageMessageContent,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage
)

# from imgurpython import ImgurClient
# # Imgur API client
# client_id = 'YOUR CLIENT ID'
# client_secret = 'YOUR CLIENT SECRET'

from crawl import product_crawl


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)

configuration = Configuration(
    access_token=channel_access_token
)


@app.route("/find_product", methods=['POST'])
def find_product():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def message_text(event):
# for event in events:
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        message_input = event.message.text
        if message_input == "1":
            img_url = "https://i.imgur.com/HLw9BhO.jpg"
            reply = ImageMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(
                ReplyMessageRequest(
                replyToken=event.reply_token,
                messages=[reply]))
            # break

        result = product_crawl(message_input)
        # result = crawl(message_input)
        if result == -1:
            reply1 = "商品不存在日本Uniqlo哦! (期間限定價格商品可能找不到)"
            reply2 = "請重新輸入或按 1 看範例~"
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                replyToken=event.reply_token, 
                messages=[TextMessage(text=reply1),
                            TextMessage(text=reply2)]))
        else:
            reply1 = "商品連結:\n %s\n商品價格: %s日圓\n折合台幣: %s元" % (result[1], result[2], result[3])
            # reply1 = "商品連結:\n %s\n商品價格: %s日圓\n折合台幣: %s元\n臺灣官網售價: %s元" % (result[1], result[2], result[3], result[4][2])
            if len(result[4]) != 0:
                try:
                    reply1 += "\n臺灣官網售價: {}元".format(result[4][2])
                except:
                    reply1 += "\n臺灣官網售價: {}元".format(result[4][1])
            available_dict = {}
            if len(result) == 6:
                for item in result[5]:
                    if item['stock'] != 'STOCK_OUT' and item['color'] not in available_dict:
                        available_dict[item['color']] = []
                    if item['stock'] != 'STOCK_OUT' and item['color'] in available_dict:
                        available_dict[item['color']].append(item['size'])

                reply2 = "日本官網庫存:"
                for color in available_dict:
                    reply2 += "\n{}: ".format(color)
                    reply2 += "{}".format(', '.join(available_dict[color]))
            else:
                reply2 = "日本官網庫存查不到"

            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                replyToken=event.reply_token, 
                messages=[TextMessage(text=reply1),
                            TextMessage(text=reply2)]))           
    return 'OK'

@handler.add(MessageEvent, message=ImageMessageContent)
def message_image(event):
    with ApiClient(configuration) as api_client:
        reply1 = 'You send a image!!! (TESTING RECOGNITION SERVICE'

        line_bot_api = MessagingApi(api_client)

        messageId = event.message.id

        url = "https://api-data.line.me/v2/bot/message/{}/content".format(messageId)
        headers = {"Authorization": "Bearer {}".format(channel_access_token)}
        r = requests.get(url, headers=headers)
        print(r)
        print(r.url)
        reply2 = r.url

        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=reply1),
                    TextMessage(text=url),
                    TextMessage(text=reply2)
                ]
            )
        )


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)