import json
from email.message import Message
from json.tool import main
from random import randint
from tkinter.tix import MAIN
from datetime import datetime, timedelta
 
from telegram import Bot, Update
from telegram.ext import (CallbackContext, CommandHandler, Dispatcher, Filters,
                          MessageHandler, Updater)


def start(update:Update, context:CallbackContext):
    random_word = choose_word()
    f = open("setup.txt", "r+")
    f.truncate(0)
    f.write(random_word)
    f.close()
    update.message.reply_text('_ _ _ _ _')


def verify_answer(update: Update, context: CallbackContext):
    f = open("setup.txt", "r")
    random_word = f.readline()
    input_wrd = update.message.text.upper()
    if update.message.text.upper()==random_word:
        update.message.reply_text(input_wrd)
    elif len(input_wrd) != 5:
        update.message.reply_text('DIGITE UMA PALAVRA COM 5 LETRAS')
    else:
        tmp_wrd = []
        for i in range(5):
            if random_word[i]==input_wrd[i]:
                tmp_wrd.append(input_wrd[i])
            elif input_wrd[i] in random_word:
                tmp_wrd.append('**__{}__**'.format(input_wrd[i]))
            else:
                tmp_wrd.append('_')
        update.message.reply_text(' '.join(tmp_wrd))

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

