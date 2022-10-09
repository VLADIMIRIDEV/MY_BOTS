import telebot
import wikipedia
import re


bot = telebot.TeleBot('5496717190:AAHCPd1o_C_SUo5Ktbyzi1EXx27iEQvz5-g')
wikipedia.set_lang('ru')


def getwiki(s):
	try:
		ny = wikipedia.page(s)
		wikitext = ny.content[:1000]
		wikimas = wikitext.split('.')[:-1]
		wikitext_2 = ''
		for x in wikimas:
			if not ('==' in x):
				if len(x.strip()) > 3:
					wikitext_2 = wikitext_2 + x + '.'
			else:
				break
		wikitext_2 = re.sub('\([^()]*\)', '', wikitext_2)
		wikitext_2 = re.sub('\{[^\{\}]*\}', '', wikitext_2)
		return wikitext_2
	except Exception as e:
		return 'В энциклопедии нет такой информации.'


@bot.message_handler(commands=['start'])
def start(m, res=False):
	bot.send_message(m.chat.id, 'Напиши слово, значение которого нужно найти.')


@bot.message_handler(content_types=['text'])
def handle_text(m):
	bot.send_message(m.chat.id, getwiki(m.text))


bot.polling(none_stop=True, interval=0)