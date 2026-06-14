import json
import os
from pprint import pprint

import requests
from telegram import Update, Bot
from telegram.ext import CommandHandler

from tg_bot import dispatcher

# Ginger grammar correction API key - set GINGER_API_KEY env var to enable
API_KEY = os.environ.get("GINGER_API_KEY", "")
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"


def translate(bot: Bot, update: Update):
    if not API_KEY:
        update.effective_message.reply_text("Translation is not configured (GINGER_API_KEY not set).")
        return

    if update.effective_message.reply_to_message:
        msg = update.effective_message.reply_to_message

        params = dict(
            lang="US",
            clientVersion="2.0",
            apiKey=API_KEY,
            text=msg.text
        )

        res = requests.get(URL, params=params)
        pprint(json.loads(res.text))
        changes = json.loads(res.text).get('LightGingerTheTextResult')
        curr_string = ""

        prev_end = 0

        for change in changes:
            start = change.get('From')
            end = change.get('To') + 1
            suggestions = change.get('Suggestions')
            if suggestions:
                sugg_str = suggestions[0].get('Text')
                curr_string += msg.text[prev_end:start] + sugg_str

                prev_end = end

        curr_string += msg.text[prev_end:]
        print(curr_string)
        update.effective_message.reply_text(curr_string)


__help__ = """
 - /t: while replying to a message, will reply with a grammar corrected version
"""

__mod_name__ = "Translator"


TRANSLATE_HANDLER = CommandHandler('t', translate)

dispatcher.add_handler(TRANSLATE_HANDLER)
