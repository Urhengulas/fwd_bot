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

try:
    from secret import TOKEN, GROUP_ID

    logging.info("Successfully loaded TOKEN and GROUP_ID from secret.py")
except:
    TOKEN = str(os.environ.get('TOKEN', default=""))
    GROUP_ID = int(os.environ.get('GROUP_ID', default=0))

    logging.info("Successfully loaded TOKEN and GROUP_ID from environ")
finally:
    logging.info(
        f"TOKEN: {TOKEN} ({type(TOKEN)}, GROUP_ID: {GROUP_ID} ({type(GROUP_ID)})")


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):

    first_name = update.message.from_user.first_name
    chat_id = update.message.chat_id

    context.bot.send_message(chat_id=chat_id, text=START_TEXT.format(name=first_name, chat_id=chat_id))


dispatcher.add_handler(CommandHandler('start', start))


def forward(update, context):

    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    chat_id = update.message.chat_id

    # forward message to the GROUP
    context.bot.forward_message(
        chat_id=GROUP_ID,
        from_chat_id=chat_id,
        message_id=update.message.message_id,
        text=update.message.text
    )

    # send a thank you message to user
    context.bot.send_message(
        chat_id=chat_id, text=THANK_TEXT.format(name=first_name)
    )

    # log the activity
    logging.info(
        f"Forwarded message from @{username} to Channel"
    )


echo_handler = MessageHandler(Filters.text, forward)
dispatcher.add_handler(echo_handler)


def main():

    updater.start_polling()
    logging.info("Bot started polling")
    updater.idle()


if __name__ == "__main__":
    main()
