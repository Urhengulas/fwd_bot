from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters
)
import logging
import os

from texts import START_TEXT, THANK_TEXT


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get('TOKEN', default="")
GROUP_ID = os.environ.get('GROUP_ID', default=0)

if TOKEN == "" or GROUP_ID == 0:
    try:
        from secret import TOKEN as sec_TOKEN, GROUP_ID as sec_GROUP_ID

        TOKEN = sec_TOKEN
        GROUP_ID = sec_GROUP_ID

    except:
        logging.error("Could not load variables from secret.py")


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):

    chat_id = update.message.chat_id

    context.bot.send_message(chat_id=chat_id, text=START_TEXT.format(chat_id))


dispatcher.add_handler(CommandHandler('start', start))


def forward(update, context):

    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    chat_id = update.message.chat_id

    # forward message to the GROUP
    context.bot.send_message(
        chat_id=GROUP_ID, text=f"@{username} wrote:\n{update.message.text}")

    # send a thank you message to user
    context.bot.send_message(
        chat_id=chat_id, text=THANK_TEXT.format(username))

    # log the activity
    logging.info(
        f"Forwarded message from @{username} to Channel")


echo_handler = MessageHandler(Filters.text, forward)
dispatcher.add_handler(echo_handler)


def main():

    updater.start_polling()
    logging.info("Bot started polling")
    updater.idle()


if __name__ == "__main__":
    main()
