import telebot

bot = telebot.TeleBot('6666073833:AAGqqXi2Z4MHfXU6uxOcmD1ARdR3xUZ2SVQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     '⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣶⣶⣦⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄/n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠄⠄⠄⠄⠄⠄/n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣷⣤⠄⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄/n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⠆⠰⠶⠄⠘⢿⣿⣿⣿⣿⣿⣆⠄⠄⠄/n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿⣿⠏⠄⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠄/n⠄⠄⠄⠄⠄⠄⠄⠄⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀/n⠄⠄⠄⠄⠄⠄⠄⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠄⡻⣿⣿⣿⣿⡇/n⠄⠄⠄⠄⠄⢀⠜⠁⠸⣿⣿⣿⠟⠄⠄⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇/n⠄⠄⠄⠄⡰⠉⠖⣀⠄⠄⢁⣀⠄⣴⣶⣦⠄⢴⡆⠄⠄⢀⣀⣀⣉⡽⠷⠶⠋⠄/n⠄⠄⠄⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠄⠄⣐⣲⣤⣯⠞⠉⠁⠄⠄⠄⠄⠄/n⠄⢀⠔⠁⣿⣿⣿⣿⣿⡟⠄⠄⠄⢀⣄⣀⡞⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄/n⠄⡜⠄⠄⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄/n⢰⠁⠄⡤⠖⠺⢶⡾⠃⠄⠈⠙⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄/n⠈⠓⠾⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄',
                     parse_mode='Markdown')


bot.infinity_polling()