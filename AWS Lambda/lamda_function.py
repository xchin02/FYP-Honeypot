import os
import json
from urllib import request, parse, error
from textwrap import wrap

MAX_CHUNK_SIZE = 4096  # Maximum Telegram message length

def lambda_handler(event, context):
    url = 'https://api.telegram.org/bot%s/sendMessage' % os.environ['TOKEN']
    message = event['Records'][0]['Sns']['Message']

    chunks = wrap(message, MAX_CHUNK_SIZE)
    
    update = request.urlopen("https://api.telegram.org/bot%s/getUpdates" % os.environ['TOKEN'])
    updated = json.loads(update.read())['result']
    chat_ids = []
    for i in range(len(updated)):
        id = updated[i]["message"]["from"]["id"]
        if id not in chat_ids:
            chat_ids.append(id)

    for id in chat_ids:
        for chunk in chunks:
            data = parse.urlencode({'chat_id': id, 'text': chunk})
            try:
                # Send the SNS message chunk to Telegram
                request.urlopen(url, data.encode('utf-8'))
            except error.HTTPError as e:
                print('Failed to send the SNS message below:\n%s' % chunk)
                response = json.load(e)
                if 'description' in response:
                    print(response['description'])
                raise e