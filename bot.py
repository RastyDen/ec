import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import telebot
from telebot import types
import re
import datetime
import time
now = datetime.datetime.now()

bot = telebot.TeleBot('557427578:AAE8EC4tYFY85bRmSClQYfXBoMQrGP3zcm0')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Показать расписание')
gt = 0
rospis = []

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.first_name) + '. нажми на кнопку, чтобы посмотреть расписаниею' , reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Показать расписание':
        if globals()['gt'] == 0:
            rosp()
            bot.send_message(message.chat.id, f'{" ".join(rospis)}', reply_markup=keyboard1)
            globals()['gt'] = globals()['gt'] + 1
            time.sleep(43200)
            globals()['gt'] = globals()['gt'] - 1

        elif globals()['gt'] == 1:
            bot.send_message(message.chat.id, f'{" ".join(rospis)}', reply_markup=keyboard1)
    print("Текущий день: %d" %now.day)

def rosp():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://ecampus.ncfu.ru/schedule/group/14922")

    week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    days = []

    title = driver.find_element_by_xpath('//*[@id="page"]/ul/li[2]/div/span').text
    all = f'''{driver.find_element_by_xpath('//*[@id="home"]/table/tbody').text}'''.replace("/n", ' ')

    for i in range(0, 6):
        day = all.partition(week[i])
        #print(day)
        el = str(day[1])+str(day[2].split('\n')[0])+'\n'
        days.append(el)
        #print(el)

    pn = all.find(week[0])
    vt = all.find(week[1])
    sr = all.find(week[2])
    ct = all.find(week[3])
    pt = all.find(week[4])
    sb = all.find(week[5])

    #print(pn, vt, sr, ct, pt, sb)

    #понедельник
    pn1 = all[pn:vt].replace('\n', ' ')
    #print(pn1)
    p = 0
    par_pn = []
    while True:
        pn_f = pn1.find('пара', p, -1)
        if pn_f == -1:
            break
        par_pn.append(pn_f)
        p = pn_f+1
        #print(pn_f)
    ##print(days[0].strip())
    rospis.append("▫️" + days[0].strip()+'\n')
    #print(f'Всего пар: {len(par_pn)}')
    p_p = 0
    for o_o in range(0, len(par_pn)-1):
        rospis.append(pn1[par_pn[p_p]-2:par_pn[p_p]] + pn1[par_pn[p_p]:par_pn[p_p+1]-2] + '\n')
        ##print(pn1[par_pn[p_p]-2:par_pn[p_p]] + pn1[par_pn[p_p]:par_pn[p_p+1]-2])
        p_p = p_p+1
    ##print(pn1[par_pn[p_p]-2:par_pn[p_p]] + pn1[par_pn[-1]:-1])
    rospis.append(pn1[par_pn[p_p]-2:par_pn[p_p]] + pn1[par_pn[-1]:-1] + '\n')

    #вторник
    vt1 = all[vt:sr].replace('\n', ' ')
    p = 0
    par_vt = []
    while True:
        vt_f = vt1.find('пара', p, -1)
        if vt_f == -1:
            break
        par_vt.append(vt_f)
        p = vt_f+1
        #print(vt_f)
    ##print('\n' + days[1].strip())
    rospis.append('\n' + "▫️" + days[1].strip() + '\n')
    p_p = 0
    for o_o in range(0, len(par_vt)-1):
        ##print(vt1[par_vt[p_p]-2:par_vt[p_p]] + vt1[par_vt[p_p]:par_vt[p_p+1]-2])
        rospis.append(vt1[par_vt[p_p]-2:par_vt[p_p]] + vt1[par_vt[p_p]:par_vt[p_p+1]-2] + '\n')
        p_p = p_p+1
    ##print(vt1[par_vt[p_p]-2:par_vt[p_p]] + vt1[par_vt[-1]:-1])
    rospis.append(vt1[par_vt[p_p]-2:par_vt[p_p]] + vt1[par_vt[-1]:-1] + '\n')

    #среда
    sr1 = all[sr:ct].replace('\n', ' ')
    p = 0
    par_sr = []
    while True:
        sr_f = sr1.find('пара', p, -1)
        if sr_f == -1:
            break
        par_sr.append(sr_f)
        p = sr_f+1
        #print(sr_f)
    ##print('\n' + days[2].strip())
    rospis.append('\n' + "▫️" + days[2].strip() + '\n')
    p_p = 0
    for o_o in range(0, len(par_sr)-1):
        rospis.append(sr1[par_sr[p_p]-2:par_sr[p_p]] + sr1[par_sr[p_p]:par_sr[p_p+1]-2] + '\n')
        ##print(sr1[par_sr[p_p]-2:par_sr[p_p]] + sr1[par_sr[p_p]:par_sr[p_p+1]-2])
        p_p = p_p+1
    rospis.append(sr1[par_sr[p_p]-2:par_sr[p_p]] + vt1[par_sr[-1]:-1] + '\n')
    ##print(sr1[par_sr[p_p]-2:par_sr[p_p]] + vt1[par_sr[-1]:-1])

    #четверг
    ct1 = all[ct:pt].replace('\n', ' ')
    p = 0
    par_ct = []
    while True:
        ct_f = ct1.find('пара', p, -1)
        if ct_f == -1:
            break
        par_ct.append(ct_f)
        p = ct_f+1
        #print(ct_f)
    ##print('\n' + days[3].strip())
    rospis.append('\n' + "▫️" + days[3].strip() + '\n')
    p_p = 0
    for o_o in range(0, len(par_ct)-1):
        ##print(ct1[par_ct[p_p]-2:par_ct[p_p]] + sr1[par_ct[p_p]:par_ct[p_p+1]-2])
        rospis.append(ct1[par_ct[p_p]-2:par_ct[p_p]] + sr1[par_ct[p_p]:par_ct[p_p+1]-2] + '\n')
        p_p = p_p+1
    ##print(ct1[par_ct[p_p]-2:par_ct[p_p]] + ct1[par_ct[-1]:-1])
    rospis.append(ct1[par_ct[p_p]-2:par_ct[p_p]] + ct1[par_ct[-1]:-1] + '\n')

    if len(days) == 6:
        #пятница
        pt1 = all[pt:-1].replace('\n', ' ')
        p = 0
        par_pt = []
        while True:
            pt_f = pt1.find('пара', p, -1)
            if pt_f == -1:
                break
            par_pt.append(pt_f)
            p = pt_f + 1
            # print(pt_f)
        ##print('\n' + days[4].strip())
        rospis.append('\n' + "▫️" + days[4].strip() + '\n')
        p_p = 0
        for o_o in range(0, len(par_pt) - 1):
            ##print(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[p_p]:par_pt[p_p + 1] - 2])
            rospis.append(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[p_p]:par_pt[p_p + 1] - 2] + '\n')
            p_p = p_p + 1
        ##print(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[-1]:-1])
        rospis.append(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[-1]:-1] + '\n')

    elif len(days) == 7:
        #пятница
        pt1 = all[pt:sb].replace('\n', ' ')
        p = 0
        par_pt = []
        while True:
            pt_f = pt1.find('пара', p, -1)
            if pt_f == -1:
                break
            par_pt.append(pt_f)
            p = pt_f + 1
            # print(pt_f)
        ##print('\n' + "▫️" + days[4].strip())
        rospis.append('\n' + days[4].strip() + '\n')
        p_p = 0
        for o_o in range(0, len(par_pt) - 1):
            ##print(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[p_p]:par_pt[p_p + 1] - 2])
            rospis.append(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[p_p]:par_pt[p_p + 1] - 2] + '\n')
            p_p = p_p + 1
        ##print(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[-1]:-1])
        rospis.append(pt1[par_pt[p_p] - 2:par_pt[p_p]] + pt1[par_pt[-1]:-1] + '\n')

        #суббота
        sb1 = all[sb:-1].replace('\n', ' ')
        p = 0
        par_sb = []
        while True:
            sb_f = sb1.find('пара', p, -1)
            if sb_f == -1:
                break
            par_sb.append(sb_f)
            p = sb_f + 1
            # print(sb_f)
        ##print('\n' + days[5].strip())
        rospis.append('\n' + "▫️" + days[5].strip() + '\n')
        p_p = 0
        for o_o in range(0, len(par_sb) - 1):
            rospis.append(sb1[par_sb[p_p] - 2:par_sb[p_p]] + sb1[par_sb[p_p]:par_sb[p_p + 1] - 2] + '\n')
            ##print(sb1[par_sb[p_p] - 2:par_sb[p_p]] + sb1[par_sb[p_p]:par_sb[p_p + 1] - 2])
            p_p = p_p + 1
        ##print(sb1[par_sb[p_p] - 2:par_sb[p_p]] + sb1[par_sb[-1]:-1])
        rospis.append(sb1[par_sb[p_p] - 2:par_sb[p_p]] + sb1[par_sb[-1]:-1] + '\n')
#print(f"{title}")
#print(all)


if __name__ == "__main__":
    while True:
        try:
            print("BOT was started!")
            bot.polling(none_stop = True, interval = 0)
        except requests.exceptions.ConnectionError:
            print("Скрипт получил ошибку соединения 'ConnectionError'")
            time.sleep(10)
