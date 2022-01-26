import json
from email.message import Message
from json.tool import main
from random import randint
from tkinter.tix import MAIN
 
from telegram import Bot, Update
from telegram.ext import (CallbackContext, CommandHandler, Dispatcher, Filters,
                          MessageHandler, Updater)

random_word = ''

def start(update:Update, context:CallbackContext):
    random_word = choose_word()
    print(random_word)
    update.message.reply_text('_ _ _ _ _')


def verify_answer(update: Update, context: CallbackContext):
    print("palavra é: {}".format(random_word))
    update.message.reply_text('blablabla')


def choose_word():
    n = randint(0, 999)
    f = open("termos.txt", "r")
    for i, line in enumerate(f):
        if i==n:
            word = line.upper()
            f.close
            return word

if __name__ == '__main__':
    with open('private.txt', 'r') as private_key:
        updater = Updater(private_key.readline())

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, verify_answer))
    
    updater.start_polling()

    updater.idle()

