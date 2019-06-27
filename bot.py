from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters
)
import logging

from secret import TOKEN, GROUP_ID
from texts import START_TEXT, THANK_TEXT


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(update, context):

    context.bot.send_message(chat_id=update.message.chat_id, text=START_TEXT)

dispatcher.add_handler(CommandHandler('start', start))


def forward(update, context):

    username = update.message.from_user.first_name

    # forward message to the GROUP
    context.bot.send_message(
        chat_id=GROUP_ID, text=f"{username} wrote:\n{update.message.text}")

    # send a thank you message to user
    context.bot.send_message(
        chat_id=update.message.chat_id, text=THANK_TEXT.format(username))

    # log the activity
    logging.info(f"Forwarded message from {username} to Channel")

echo_handler = MessageHandler(Filters.text, forward)
dispatcher.add_handler(echo_handler)


def main():
    
    updater.start_polling()
    logging.info("Bot started polling")
    updater.idle()


if __name__ == "__main__":
    main()
