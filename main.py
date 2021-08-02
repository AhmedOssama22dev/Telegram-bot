from datetime import date
import json
import os
import telebot
import requests


API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
PASSWORD = os.getenv('PASSWORD')


@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, '''Welcome to our bot!\nSome helpful commands:
    \n1)students list [To show all students names]\n2)search (student name or id) [To show a certain student detail\n3)create session (title) (YYYY-MM-DD) (HR:MIN:SEC)]
    ''')


def get_students(message):
    req = message.text.split()
    if req[-1] != PASSWORD:
        return False
    else:
        if len(req) < 2 or req[0].lower() not in "students":
            return False
        else:
            return True


@bot.message_handler(func=get_students)
def reply_get_students(message):
    students = requests.get("http://127.0.0.1:8000/students/").json()
    msg = ""
    for student in students:
        msg += str(student['id']) + "]" + student['name'] + '\n'

    bot.reply_to(message, msg)


def search_student(message):
    req = message.text.split()
    if req[-1] != PASSWORD:
        return False
    else:
        if len(req) < 2 or req[0].lower() not in "search":
            return False
        else:
            return True


@bot.message_handler(func=search_student)
def reply_search_student(message):
    name = ""
    counter = 0
    msg_lst = list(message.text.split(" "))
    for word in msg_lst:
        if counter > 0:
            name += word
            name += "%20"
        counter += 1
    name_query = name[:-3]
    url = f"http://127.0.0.1:8000/students/{name_query}"
    student = requests.get(url).json()

    student_data = f"id:{student['id']}\nName: {student['name']}\nEmail: {student['email']}\nContact: {student['number']}\nTelegram id: {student['telegram_id']}"
    bot.reply_to(message, student_data)


def create_session(message):
    req = message.text.split()
    if req[-1] != PASSWORD:
        return False
    else:
        if "session" not in req:
            bot.reply_to(message, 'Enter a valid format\nfor help type /start')
            return False
        elif len(req) < 5:
            bot.reply_to(message, 'Enter a valid format\nfor help type /start')
            return False
        else:
            return True


@bot.message_handler(func=create_session)
def create_new_session(message):
    form_data = []
    counter = 0
    msg_lst = list(message.text.split(" "))
    for word in msg_lst:
        if counter > 1:
            form_data.append(word)
        counter += 1

    url = "http://127.0.0.1:8000/create/session/"

    data = {
        'title': form_data[0], 'date': form_data[1], 'time': form_data[2]
    }
    response = requests.request("POST", url, data=data)
    bot.send_message(chat_id='-1001503615060',
                     text=f"A new session has just created: \nTitle:{form_data[0]}\nDate:{form_data[1]}\nTime:{form_data[2]}")
    bot.reply_to(message, "Session scheduled successfully")


bot.polling()
