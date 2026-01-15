import telebot

# BotFather bergan yangi Token
TOKEN = '8266243140:AAGjo_Ehr-lSAg5RaVFDehli-eAQdn9Jkzo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Faqat matnli xabar, xato tugma endi chiqmaydi
    text = "Xush kelibsiz! INGCO do'konimizga kirish uchun pastdagi ko'k 'MARKET INGCO 🛒' tugmasini bosing."
    bot.send_message(message.chat.id, text)

if __name__ == "__main__":
    bot.polling(none_stop=True)
