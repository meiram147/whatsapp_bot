import random
import string
import pyautogui as pg
import pytesseract
import cv2
import matplotlib.pyplot as plt
import requests as requests
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

hello = ['Здравствуйте', 'привет', 'добрый день', 'добрый утро']
answer = ['да,хорошо', 'да, конечно']
zakaz = ['продается', 'оформить', 'объявление', 'купить', 'приобрести', 'смотреть', 'объявление', 'отправить',
         'доставка', 'получить', 'забрать', 'курьер', 'оплатить']
data = ['фио', 'город']
temp = 'https'


def postScammer(number, link):
    BASE_URL = 'http://localhost:8080'
    endPoint = '/scammers'
    scammerJsonString = {'id': 1, 'number': number, 'initLink': link}
    serverResponse = requests.post(BASE_URL + endPoint, json=scammerJsonString)
    print(serverResponse)


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 1)  # transposition
    excs = d[lenstr1 - 1, lenstr2 - 1]
    if excs <= len(s2) / 2:
        return s2
    else:
        return False


def screen_number():
    pg.screenshot('screenshot.png', region=(1423, 52, 180, 30))

    image = cv2.imread("screenshot.png")
    string = pytesseract.image_to_string(image)
    string1 = string.replace(' ', '')
    s = string1[1:]
    try:
        s = int(s)
        print(f"user say:{s}")
        return s
    except ValueError:
        print("errrr")

def response(message):
    mes = message.lower()
    mes_list = mes.split(' ')
    for m in mes_list:
        tt = str.maketrans(dict.fromkeys(string.punctuation))
        m = m.translate(tt)
        if mes_list[0].find(temp) == 0:
            link = mes_list[0]
            number = screen_number()
            # postScammer(number, link)
            return 'Спасибо, вы попали в базу мошенников'
        for w in data:
            if damerau_levenshtein_distance(m, w):
                return 'Ралиев Кайсар Романович г.Караганда'
        for w in zakaz:
            if damerau_levenshtein_distance(m, w):
                return random.choice(answer)
        for w in hello:
            if damerau_levenshtein_distance(m, w):
                return random.choice(hello)
    else:
        return 'не понимаю'

#
# print(response('https://kzpochta.youroplata.online/track64458075'))
# print(response('здраствуйте!'))
# print(response('объявление еще актуально?'))
# print(response('можно будет оформить доставку через казпочту. Я живу в другом городе, '))
# print(response('отправите на индрайвере, я оплачу'))
# print(response(
#     'у меня не получится забрать на этой неделе, могу я скинуть вам залог или редоплату, чтобы вы пока не продавали'))
#
