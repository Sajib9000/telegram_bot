from telegram.ext import Updater, CommandHandler

# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Hello! I am your bot!")

def main():
    # Replace 'YOUR_API_TOKEN' with your actual Bot API Token
    updater = Updater("YOUR_API_TOKEN", use_context=True)

    dp = updater.dispatcher

    # Command handler for /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
