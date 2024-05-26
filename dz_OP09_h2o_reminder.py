import telebot, datetime, time, threading, random

bot = telebot.TeleBot('7030559887:AAF0kkNPCqKzk3j7eJmWHWI-l89WA4EzJVw')

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, 'Это чат бот, который может напоминать тебе о некоторых периодических событиях.\nМеню:'
                          '\n /fact -    случайный факт о воде'
                          '\n /water -   включить напоминания о воде'
                          '\n /vitamin - включить напоминания о витаминах и микроэлементах'
                          '\n /pause -   остановить все напоминания')

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ["1. Вода на Земле может быть старше самой Солнечной системы: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
            "2. Горячая вода замерзает быстрее холодной: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
            "3. Больше воды в атмосфере, чем во всех реках мира: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете.",
            4, 5, 6, 7, 8, 9, 10]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде.\n{random_fact}')

@bot.message_handler(commands=['water'])
def water_message(message):
    global rem_stop
    rem_stop = 0
    reminder_thread = threading.Thread(target=send_rem_water, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['vitamin'])
def vitamin_message(message):
    global rem_stop
    rem_stop = 0
    reminder_thread1 = threading.Thread(target=send_rem_vitamin, args=(message.chat.id,))
    reminder_thread1.start()

@bot.message_handler(commands=['pause'])
def end_message(message):
    global rem_stop
    rem_stop = 1

def send_rem_water(chat_id):
    time_point = ['07:00', '09:00', '10:30', '12:00', '14:00', '15:30', '17:00', '18:00', '20:20']
    global rem_stop
    while rem_stop == 0:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in time_point:
            bot.send_message(chat_id, 'Пора выпить воды 💦))')
            time.sleep(60)
        time.sleep(20)

def send_rem_vitamin(chat_id):
    time_point = ['10:00', '14:30', '20:20']
    global rem_stop
    while rem_stop == 0:
        now = datetime.datetime.now().strftime('%H:%M')
        if now in time_point:
            bot.send_message(chat_id, 'Витамины и минералы весьма полезны, пора принять для вашего здоровья 💊))')
            time.sleep(60)
        time.sleep(20)

bot.polling(none_stop=True)
