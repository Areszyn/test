from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # Replace with your bot token

# Dictionary to store donations
donations = {}

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the Star Donation Bot!')

def donate(update: Update, context: CallbackContext):
    user = update.message.from_user
    stars = int(context.args[0]) if context.args else 0

    if user.username not in donations:
        donations[user.username] = 0
    
    donations[user.username] += stars
    update.message.reply_text(f'Thank you, {user.username}! You have donated {stars} stars. Total stars donated: {donations[user.username]}')

def total(update: Update, context: CallbackContext):
    user = update.message.from_user
    total_stars = donations.get(user.username, 0)
    update.message.reply_text(f'{user.username}, you have donated a total of {total_stars} stars.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('donate', donate))
    dp.add_handler(CommandHandler('total', total))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
