from telegram.ext import Updater, CommandHandler
import nekos

def pat(update, context):
    reply_user = update.message.reply_to_message
    user = update.message.from_user
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + word.join(context.args) + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + reply_user.from_user['first_name'] + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + reply_user.from_user['first_name'] + ' ' + '(@'+ reply_user.from_user['username'] + ')' + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))

def baka(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:        
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + word.join(context.args) + ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
        else:   
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + reply_user.from_user['first_name'] + ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + reply_user.from_user['first_name'] + '(@' + reply_user.from_user['username'] + ')'+ ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))    

def main():
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pat', pat))
    dp.add_handler(CommandHandler('baka', baka))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()