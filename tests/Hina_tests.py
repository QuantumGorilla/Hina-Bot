from telegram.ext import Updater, CommandHandler

def despegala(update, context):
    try:    
        user = update.message.reply_to_message
        if user != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Omae wa mou... Shindeiru')
            context.bot.kickChatMember(chat_id=update.effective_chat.id, user_id=user.from_user['id'])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='No mandaste a despegarla a nadie, cachón')
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hpta, el cv es admin')

def butifarra(update, context):
    user = update.message.reply_to_message
    print(user)
    if user == None:
        if len(context.args) != 0:
            word = ' '   
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Butifarra.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Butifarra.mp4', 'rb'), supports_streaming=True)
    else:
        if user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + user.from_user['first_name'])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Butifarra.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + user.from_user['first_name'] + ' ' + '( @' + user.from_user['username']+')')        
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('media/Butifarra.mp4', 'rb'), supports_streaming=True)
    

def main():
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('metienesque', butifarra))
    dp.add_handler(CommandHandler('despegala', despegala))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()