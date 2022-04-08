import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Command Handlers
def start(update, context):
    update.message.reply_text('Hello world!!')

#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not smart enough to help you!! MAKE ME SMART! MAKE ME FEEL GUUUUUDD!!! (P.S. I can also send you a youtube video, just type "/vid".)')

#function to echo the users message
def echo(update, context):
    if ((update.message.text == 'hi') or (update.message.text == 'Hi') or (update.message.text == 'Hello') or (update.message.text == 'hello')):
        update.message.reply_text('Que onda Pops!')

    else:
        update.message.reply_text(update.message.text + '' + ' cuh!')

#function that sends videos
def vid(update, context):
    import random

    youtubeVideos = [
        'https://www.youtube.com/watch?v=NVOL3tMDzEs&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=9',
        'https://www.youtube.com/watch?v=khFb4FTJ4Jo&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=32',
        'https://www.youtube.com/watch?v=m7NuVjpi72c&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=29',
        'https://www.youtube.com/watch?v=n29thSVq8Mg&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=30',
        'https://www.youtube.com/watch?v=qG4IaHgqH00&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=28',
        'https://www.youtube.com/watch?v=Sg3iUm2QqCs&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=27',
        'https://www.youtube.com/watch?v=rPNrHN83Bdk&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=26',
        'https://www.youtube.com/watch?v=6wFHmxe4TyQ&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=25',
        'https://www.youtube.com/watch?v=HtBuNU7XhQo&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=24',
        'https://www.youtube.com/watch?v=8MwHNGYvZYE&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=21',
        'https://www.youtube.com/watch?v=zwdX0JEQooo&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=22',
        'https://www.youtube.com/watch?v=rCOcxHEZ8-I&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=11', 
        'https://www.youtube.com/watch?v=aPD9I4aI500&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=8',
        'https://www.youtube.com/watch?v=-qWPkiDwXA0&list=PLEh4rX_gBRfpFgaLqDEi3J_yhmu_360UL&index=10'
    ]
    update.message.reply_text(random.choice(youtubeVideos))

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("5220278243:AAHw4jhtkf61iem82jyBHT7MuRfxWvACEIc", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("vid", vid))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()