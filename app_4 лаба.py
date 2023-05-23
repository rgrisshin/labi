import telebot
from telebot import types
import psycopg2
import datetime
conn = psycopg2.connect(host='localhost',
                        database="VVIT7",
                        user="postgres",
                        password="wbgflhbgf21")

cursor = conn.cursor()

token = '5950007624:AAFy8oNdaeacSUGpIFhm5crGEpgMyzj0jjg'

bot = telebot.TeleBot(token)

today = datetime.datetime.today() #дата сегодня
week_number = today.isocalendar()[1] # определяет  № недели

even_week = week_number % 2 == 0
                                    #четная или нечетная неделя
if even_week:
    week_num = 2
else:
    week_num = 1


def timetable(day, week_num):
    query = f"SELECT subject, room_numb, start_time, teacher_name FROM timetable WHERE day='{day}' AND week_numb='{week_num}'"

    cursor.execute(query)
    rows = cursor.fetchall()

    timetable_str = f'Расписание на {day} неделю №{week_num}:\n\n'
    for row in rows:                                #разбиваем на ряды, чтобы все было красиво
        subject, room_numb, start_time, teacher_name = row
        timetable_str += f'{start_time} {room_numb}\n{subject}\n{teacher_name}\n\n'

    return timetable_str


def get_week(week_num):
    query = f"SELECT subject, room_numb, start_time, teacher_name, day FROM timetable WHERE week_numb='{week_num}'"

    cursor.execute(query)
    rows = cursor.fetchall()

    week_str = f'Расписание на текущую неделю:\n\n'
    for row in rows:
        subject, room_numb, start_time, teacher_name, day = row
        week_str += f'{day}\n{start_time} {room_numb}\n{subject}\n{teacher_name}\n\n'

    return week_str


def get_next_week(week_num):
    query = f"SELECT subject, room_numb, start_time, teacher_name, day FROM timetable WHERE week_numb='{week_num}'"

    cursor.execute(query)
    rows = cursor.fetchall()

    week_str = f'Расписание на следующую неделю:\n\n'
    for row in rows:
        subject, room_numb, start_time, teacher_name, day = row
        week_str += f'{day}\n{start_time} {room_numb}\n{subject}\n{teacher_name}\n\n'

    return week_str


@bot.message_handler(commands=['currentweek'])
def handle_timetable(message):
    if even_week:
        week_num = 2                #текущая неделя
    else:
        week_num = 1
    week_str = get_week(week_num)
    bot.send_message(message.chat.id, week_str)


@bot.message_handler(commands=['week'])
def handle_timetable(message):
    if even_week:
        week_str = 'В данный момент - чётная неделя'
    else:
        week_str = 'В данный момент - нечётная неделя'
    bot.send_message(message.chat.id, week_str)


@bot.message_handler(commands=['nextweek'])
def handle_timetable(message):
    if even_week:
        week_num = 1
    else:
        week_num = 2
    week_str = get_next_week(week_num)
    bot.send_message(message.chat.id, week_str)


@bot.message_handler(commands=['Monday'])
def monday(message):
    day = 'Понедельник'
    if even_week:
        week_num = 2
    else:
        week_num = 1
    timetable_str = timetable(day, week_num)
    bot.send_message(message.chat.id, timetable_str)


@bot.message_handler(commands=['Tuesday'])
def handle_timetable(message):
    day = 'Вторник'
    if even_week:
        week_num = 2
    else:
        week_num = 1
    timetable_str = timetable(day, week_num)
    bot.send_message(message.chat.id, timetable_str)


@bot.message_handler(commands=['Wednesday'])
def handle_timetable(message):
    day = 'Среда'
    if even_week:
        week_num = 2
    else:
        week_num = 1
    timetable_str = timetable(day, week_num)
    bot.send_message(message.chat.id, timetable_str)


@bot.message_handler(commands=['Thursday'])
def handle_timetable(message):
    day = 'Четверг'
    if even_week:
        week_num = 2
    else:
        week_num = 1
    timetable_str = timetable(day, week_num)
    bot.send_message(message.chat.id, timetable_str)


@bot.message_handler(commands=['Friday'])
def handle_timetable(message):
    day = 'Пятница'
    if even_week:
        week_num = 2
    else:
        week_num = 1
    timetable_str = timetable(day, week_num)
    bot.send_message(message.chat.id, timetable_str)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('/help', '/mtuci',
                 '/currentweek', '/nextweek',
                 '/week', '/Monday', '/Tuesday',
                 '/Wednesday', '/Thursday',
                 '/Friday')
    bot.send_message(message.chat.id, 'Добрый день, это бот с расписанием группы БВТ2208! ',
                     reply_markup=keyboard)


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Вся информация о МТУСИ - https://mtuci.ru/')


@bot.message_handler(commands=['help'])
def start_message(message):
        bot.send_message(message.chat.id, 'Мои возможности :\n/help - мои команды\n'
                                          '/currentweek - расписание на текущую неделю\n'
                                          '/nextweek - расписание на следующую неделю\n'
                                          '/week - узнать неделю\n'
                                          '/Monday - расписание на понедельник текущей недели\n'
                                          '/Tuesday - расписание на вторник текущей недели\n'
                                          '/Wednesday - расписание на среду текущей недели\n'
                                          '/Thursday - расписание на четверг текущей недели\n'
                                          '/Friday - расписание на пятницу текущей недели\n'
                                          '/mtuci - вся информация о МТУСИ'
                         )


@bot.message_handler(content_types=['text'])
def answer_(message):
    bot.send_message(message.chat.id, 'Прошу прощения, я Вас не понимаю. Пожалуйста, убедитесь, что ваше сообщение корректно!')

bot.polling(none_stop=True)