import socket, requests, re # project 02 (+ requests project 07)
from gtts import gTTS #project 03
from playsound import playsound # project 03
import qrcode, psutil # project 04, 05
from bs4 import BeautifulSoup # project 07
import googletrans # project 09
import pyautogui, time, pyperclip #project 10 + 11

class PY40 :
    def PJ01() :
        print("the guy who programed this said \"I know this\"")

    def PJ02() : # main : socket, requests (+re)
        in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        in_addr.connect(("www.google.co.kr", 443))
        print("내부 IP: ", in_addr.getsockname()[0])

        try :
            req = requests.get("https://ip.pe.kr/")
            out_addr = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

            print("외부 IP: ", out_addr)
        except Exception as e :
            print(e)

    def PJ03() :
        text = "물고기는 물에 사는 고기다"
        tts = gTTS(text=text, lang='ko')
        tts.save(r"test.mp3")
        playsound(r"test.mp3")

    def PJ04() :
        qr_data = 'www.google.com'
        qr_img = qrcode.make(qr_data)
        qr_img.save(qr_data+'.png')

    def PJ05() :
        cpu = psutil.cpu_freq()
        cpu_core = psutil.cpu_count(logical=False)
        memory = psutil.virtual_memory()
        disk = psutil.disk_partitions()
        net = psutil.net_io_counters()

        print(cpu, cpu_core, memory, disk, net)

    def PJ06() :
        print("Security thing (skip for now)")

    def PJ07() :
        target1, target2 = 'usd', 'krw'

        headers = {
            'User-Agent' : 'Mozilla/5.0',
            'Content-Type' : 'text/html; charset=utf-8'
        }

        response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        print(content)
        containers = content.find('span', {'id':'last_last'})
        print(containers)

    def PJ08() :
        print("Yeah another skip")

    def PJ09() :
        translator = googletrans.Translator()
        lan1, lan2, lan3 = "en", "ko", "ja"
        string = "Can it translate?"
        print("EN :", string)
        print("KR :", translator.translate(string, dest=lan2, src=lan1).text)
        print("JA :", translator.translate(string, dest=lan3, src=lan1).text)

    def PJ1011() :
        time.sleep(1)
        pos = pyautogui.locateOnScreen("capbel.png")
        print(pos)
        pos = (pos[0], pos[1], 500, 300)
        pyautogui.screenshot('test.png', region=pos)

    def Bonus1() :
        pyautogui.hotkey('alt','tab')
        pyautogui.moveTo(1500,100)
        pyautogui.click()

        time.sleep(0.1)
        pos = pyautogui.locateOnScreen("bonus1.png")
        pyautogui.moveTo(pos[0]+pos[2]/2, pos[1]+pos[3]/2)
        pyautogui.click()
        time.sleep(0.1)

        pyperclip.copy("이것은 테스트이다. 315는 떡인데 안에 팥이 너무 많이 흰색이 눈과 입 부분 밖에 없다")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.write(['enter'])
        time.sleep(1)

PY40.Bonus1()

'''
this is the skipped part

chapter I, II
project_01

reason : already know
'''