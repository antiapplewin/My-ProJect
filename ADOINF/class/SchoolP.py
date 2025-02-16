from tkinter import *
from random import *
import random
import time
from tkinter import messagebox

ingrediant = []
canObtain = {'milk':0, 'wheat':0, 'egg':0, 'sugar':5}
nowBtns = []

isTexting = False
didTalked = False
tree = 10
ending = []

def Texting(textbox, color) :
    global isTexting
    isTexting = True
    for i in textbox :
        print(f"\033[{color}m"+i, end="")
        time.sleep(0.04)
    print()
    isTexting = False

def NOTHING(a) :
    try :
        a
    except TypeError :
        Texting("[?] 왜 눌러보신거죠", 91)


def Ending(type) : # checkpoint4
    if type not in ending :
        if type==1 :
            Texting("한번 케이크를 만들어봐야지!", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[0])
            lbl.grid(row=0, column=0)
            Texting("[!] 기본적인 케이크를 만들었습니다!", 33)
            Texting("흐음 재료가 좀 남았네? 한번 다른 걸로도 꾸며볼까?", 35)
        if type==5 :
            Texting("초코 케이크 만큼 달달한 건 없지!", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[5])
            lbl.grid(row=0, column=0)
            Texting("[!] 초코 케이크를 만들었습니다!", 33)
            Texting("생일 파티에 부족한 케이크라는 말은 없지!", 35)
        if type==6 :
            Texting("할로윈도 곧 오니까 으스스한 케이크도 있으면 좋겠지?", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[6])
            lbl.grid(row=0, column=0)
            Texting("[!] 호박 파이를 만들었습니다!", 33)
            Texting("왜 파이를 만들었을까?", 35)
        if type==7:
            Texting("내 생일은 좀 아름다운것도 괜찮을 것 같아", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[7])
            lbl.grid(row=0, column=0)
            Texting("[!] 꽃 모양 케이크를 만들었습니다!", 33)
            Texting("힘든 만큼과 아름다운 만큼은 차이가 너무 컸다", 35)
        if type==8:
            Texting("케이크무침을 만들어야겠어", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[8])
            lbl.grid(row=0, column=0)
            Texting("[!] 무 케이크를 만들었습니다!", 33)
            Texting("생각보다 맛있어요", 35)
            Texting("그래?", 97)
        if type==2 :
            Texting("주황색 케이크라... 맛있겠다", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[1])
            lbl.grid(row=0, column=0)
            Texting("[!] 오렌지 케이크를 만들었습니다!", 33)
            Texting("달달하고 예쁘네", 35)
        if type==3 :
            Texting("사과는 왜 겉은 빨갛고 속은 하얄까?", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[2])
            lbl.grid(row=0, column=0)
            Texting("[!] 사과 케이크를 만들었습니다!", 33)
            Texting("앵두 같기도 하고", 35)
        if type==4 :
            Texting("메론 멜론 메롱 마롱 마카롱 먹고 싶다", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[3])
            lbl.grid(row=0, column=0)
            Texting("[!] 메론 케이크를 만들었습니다!", 33)
            Texting("음 왜 악마의 열매 같지?", 35)
        if type==9 :
            Texting("애플 망고로 가져올 껄 그랬나?", 35)
            ending.append(type)
            time.sleep(3)
            lbl = Label(menu_, image=cakes[4])
            lbl.grid(row=0, column=0)
            Texting("[!] 망고 케이크를 만들었습니다!", 33)
            Texting("진짜로 애플 망고로 가져올 껄 그랬나?", 35)
        if len(ending)==9 :
            Texting("벌써 케이크가 9개네, 더이상 만들 게 없는데...", 35)
            Texting("그냥 케이크를 먹으며 내 생일을 즐겨야지!", 35)
            Texting("맛있게 먹겠습니다!", 35)
            for i in "-ENDING-" :
                print(i, end="")
                time.sleep(0.5)

            time.sleep(5)
            Texting("\n\n\n게임 프로그래밍 : ME", 37)
            Texting("게임 디자인 : ME", 37)
            Texting("편집 : ME", 37)
            Texting("노래 : Have a party time", 37)

        move_btns[0]['text'] = '무를 만나기'
        move_btns[0]['command'] = lambda : eVent("MOO")
        move_btns[0]['bg'] = 'pink'
        move_btns[0]['fg'] = 'red'

        move_btns[1]['text'] = '과일 농장 가기'
        move_btns[1]['command'] = lambda : Fruit()
        move_btns[1]['bg'] = 'yellow'
        move_btns[1]['fg'] = 'gold'

        move_btns[2]['text'] = 'NONE'
        move_btns[2]['command'] = lambda : NOTHING(1)
        move_btns[2]['bg'] = 'white'
        move_btns[2]['fg'] = 'black'

        move_btns[3]['text'] = 'NONE'
        move_btns[3]['command'] = lambda : NOTHING(1)
        move_btns[3]['bg'] = 'white'
        move_btns[3]['fg'] = 'black'

def Fruit(smt = "NONE") :
    if smt=="NONE" :
        Texting("어디로 갈까?", 35)
        move_btns[0]['text'] = '오렌지'
        move_btns[0]['command'] = lambda : Fruit("ong")
        move_btns[0]['bg'] = 'pink'
        move_btns[0]['fg'] = 'red'

        move_btns[1]['text'] = '사과'
        move_btns[1]['command'] = lambda : Fruit("apl")
        move_btns[1]['bg'] = 'yellow'
        move_btns[1]['fg'] = 'gold'

        move_btns[2]['text'] = '메론'
        move_btns[2]['command'] = lambda : Fruit("mln")
        move_btns[2]['bg'] = 'lime'
        move_btns[2]['fg'] = 'green'

        move_btns[3]['text'] = '망고'
        move_btns[3]['command'] = lambda : Fruit("mgo")
        move_btns[3]['bg'] = 'light blue'
        move_btns[3]['fg'] = 'blue'
    if smt == "ong" :
        Texting("안녕하세요 오렌지 좀 가지러 왔습니다!", 35)
        Texting("어 그래 외상이지?", 37)
        Texting("넵! 먼저 주세요!", 35)
        Texting("그래 자 여깄다", 37)
        Texting("감사합니다!", 35)
        Ending(2)
    if smt == "apl" :
        Texting("안녕하세요 사과 좀 가지러 왔습니다!", 35)
        Texting("어 그래 외상이지?", 37)
        Texting("넵! 먼저 주세요!", 35)
        Texting("그래 자 여깄다", 37)
        Texting("감사합니다!", 35)
        Ending(3)
    if smt == "mln" :
        Texting("안녕하세요 메론 좀 가지러 왔습니다!", 35)
        Texting("어 그래 외상이지?", 37)
        Texting("넵! 먼저 주세요!", 35)
        Texting("그래 자 여깄다", 37)
        Texting("감사합니다!", 35)
        Ending(4)
    if smt=="mgo" :
        Texting("안녕하세요 애플망고 말고 망고 좀 가지러 왔습니다!", 35)
        Texting("어 그래 외상이지?", 37)
        Texting("넵! 먼저 주세요!", 35)
        Texting("그래 자 여깄다", 37)
        Texting("감사합니다!", 35)
        Ending(9)

def eVent(type) :
    global didTalked
    if (type=='milk') :
        if (canObtain['milk']==0) :
            Texting("생일 축하해! 오늘 너 생일이지?", 90)
            Texting("아 감사합니다 우유 파시는 상인님", 35)
            Texting("오늘 제 생일이여서 한번 케이크를 만들어 보려고요!", 35)
            Texting("아 그래? 그럼 우유가 필요할텐데?", 90)
            Texting("그래서 왔잖아요", 35)
            Texting("음 그래~ 너 돈 있어?", 90)
            Texting("아니요", 35)
            Texting("그럼 주기는 좀 힘든데...", 90)
            Texting("아 그럼 부탁 하나만 들어주면 줄께", 90)
            Texting("뭔데요?", 35)
            Texting("소들을 위한 잡초를 가져다 줘", 90)
            Texting("\n[!] 평지에 가서 잡초 5개를 가져옵시다!", 33)

            move_btns[0]['text'] = '평지 잡초 뽑기'
            move_btns[0]['command'] = lambda : Item('weed')
        else :
            Texting("잡초를 가져왔습니다!", 35)
            Texting("오 그래? 잘헀다", 90)
            Texting("자 수고했다고 우유를 좀 나눠줄께", 90)
            Texting("부족하면 다시 오고 케이크 잘 만들어", 90)
            Texting("\n[!] 우유를 얻었습니다!", 33)
            move_btns[0]['text'] = 'NONE'
            move_btns[0]['command'] = lambda : NOTHING(1)
            move_btns[0]['bg'] = 'white'
            move_btns[0]['fg'] = 'black'

    if type=='sugar' :
        Texting("안녕하세요 누구있나요?", 35)
        time.sleep(2)
        Texting("어라 사탕수수 농장 주인님이 어딨으시지?", 35)
        Texting("앞에 표지판이 있네?", 35)
        Texting("[창고가 부족하기에 사탕수수를 무료로 나눠줍니다 양심있게 가져가세요]", 37)
        Texting("뭐지 🤔 일단 가져가야겠다", 35)
        Texting("\n[!] 설탕을 얻었습니다!", 33)

        move_btns[3]['text'] = 'NONE'
        move_btns[3]['command'] = lambda : NOTHING(1)
        move_btns[3]['bg'] = 'white'
        move_btns[3]['fg'] = 'black'

    if type=='wheat' :
        if canObtain["wheat"]==0 :
            Texting("안녕하세요", 35)
            Texting("어어 안녕?", 32)
            Texting("왜 얼굴에 그림자가 있죠?", 35)
            Texting("어 요즘 밀이 잘 안 자라", 32)
            Texting("아 그런가요?", 35)
            Texting("안타깝네요... 생일 케이크에는 밀가루가 필요한데...", 35)
            Texting("... 혹시 나를 도와줄 생각 있니?", 32)
            Texting("도와주면 내가 너에게 무료로 밀을 줄께", 32)
            Texting("좀 힘들겠지만 돈이 없으니까", 35)
            Texting("무엇을 해드릴까요?", 35)
            Texting("덤불에 가끔씩 자라는 영양제 2개만 가져다줘", 32)
            Texting("\n[!] 영양제 2개를 얻으세요!", 33)

            move_btns[1]['text'] = '영양제 2개 얻기'
            move_btns[1]['command'] = lambda : Item('grower')
        elif canObtain['wheat']==2 :
            Texting("가져왔습니다!!!", 35)
            Texting("소리 지를 필요는 없어", 32)
            Texting("아 네 밀은 이것을 쓰면 얻을 수 있는 거죠?", 35)
            Texting("그치... 아 맞다", 32)
            Texting("영양제 말고도 영양수가 필요한데...", 32)
            Texting("예?", 35)
            Texting("간단히 말하자면 물이 필요해", 32)
            Texting("그것도 좀 가져다 줄래?", 32)
            Texting("와 일이 생겼다!", 35)
            Texting("\n[!] 영양수 3개를 얻으세요!", 33)
            
            move_btns[1]['text'] = '영양수 얻기'
            move_btns[1]['command'] = lambda : Item('water')
        else :
            Texting("와 드디어 다 얻었다;;", 35)
            Texting("그래 잘했어 자 좀만 기다려줘", 32)
            time.sleep(1)
            Texting("됬다", 32)
            Texting("벌써요?", 35)
            Texting("그래 자 여기", 32)
            Texting("아 그리고 생일 축하해", 32)
            Texting("\n[!] 밀가루를 얻었다!", 33)

            move_btns[1]['text'] = 'NONE'
            move_btns[1]['command'] = lambda : NOTHING(1)
            move_btns[1]['bg'] = 'white'
            move_btns[1]['fg'] = 'black'
    
    if type=='egg' :
        if (canObtain["egg"]==0) :
            Texting("안녕하ㅅ..", 35)
            Texting("(쾅-⭐)", 37)
            Texting("어우 뭐지?", 35)
            Texting("어 잠시만요", 31)
            time.sleep(1)
            Texting("어어 너구나? 생일 축하한다", 31)
            Texting("아 감사합니다 ㅎㅎ 혹시 달걀있나요?", 35)
            Texting("달걀? 달걀은 왜?", 31)
            Texting("케이크를 만들고 싶은데 지금 달걀이 없어서요", 35)
            Texting("아 그래? 지금 닭 울타리가 뚫려있어서 닭이 다 달아갔어", 31)
            Texting("달걀은 지금 주기 힘들것 같은데 나 좀 도와주라", 31)
            Texting("도와주면 너에게 달걀을 줄께", 31)
            Texting("아..넵! 맡겨만 주세요", 35)
            Texting("닭 3마리만 다시 잡아다 줘!", 31)
            Texting("\n[!] 닭 3마리를 잡아다 주자!", 33)

            move_btns[2]['text'] = '닭 잡기'
            move_btns[2]['command'] = lambda : Item("chick")
        if canObtain["egg"]==3 :
            Texting("저 왔어요~", 35)
            Texting("(우당탕탕-⭐)", 37)
            Texting("어 너왔어? 닭은?", 31)
            Texting("아 나 줘 다음은 나무 하나만 베주고 가공해서 판자 상태로 나한테 줘", 31)
            Texting("어우 정신 없으신가 보네", 35)
            Texting("아침에도 저러셨나?", 35)
            Texting("\n[!] 나무를 한그루 베자! (총 10번)", 33)

            move_btns[2]['text'] = '나무 베기'
            move_btns[2]['command'] = lambda : Item("chop")
        if canObtain["egg"]==5 :
            Texting("왔습니다!", 35)
            Texting("어 그래, 기다리고 있었어", 31)
            Texting("여기 판자요!", 35)
            Texting("근데 전보다 훨씬 여유로워 보이네요?", 35)
            Texting("닭이 집 안에 계속 돌아다녔지만 일단 잡아뒀어", 31)
            Texting("아 그리고 여기 달걀", 31)
            Texting("아 감사합니다!", 35)
            Texting("그래 몸 조심하고~", 31)
            Texting("\n[!] 달걀을 얻었습니다", 37)

            move_btns[2]['text'] = 'NONE'
            move_btns[2]['command'] = lambda : NOTHING(1)
            move_btns[2]['bg'] = 'white'
            move_btns[2]['fg'] = 'black'

    if type=="MOO" :
        if not(didTalked) :
            Texting("여기는 어디지?", 35)
            Texting("오 새로운 사람이네?", 97)
            Texting("누구세요?", 35)
            Texting("보아하니 너 생일인가보지?", 97)
            Texting("에? 어떻게...", 35)
            Texting("보면 알지 데코레이션 하려고?", 97)
            Texting("어... 네...", 35)
            Texting("우리 마을에는 5개의 말하는 식물이 있고,", 97)
            Texting("식물은 각각 음식을 데코하는 마법의 젤리가 있어", 97)
            Texting("넌 케이크를 만들꺼지?", 97)
            Texting("아... 네", 35)
            Texting("내가 여기 모든 식물의 위치를 알고 있어서 물어볼께 있으면 나한테 와", 97)
            Texting("아 넵!", 35)
            didTalked = True
        else :
            Texting("또 왔네, 뭐 물어볼꺼 있나?", 97)
            Texting("아 네 뭐 물어볼께 있습니다!", 35)
            Texting("자유롭게 말해봐", 97)

        move_btns[0]['text'] = '카카오 톡'
        move_btns[0]['command'] = lambda : eVent("choc")
        move_btns[0]['bg'] = 'pink'
        move_btns[0]['fg'] = 'red'

        move_btns[1]['text'] = '수박 같은 호박'
        move_btns[1]['command'] = lambda : eVent("pumkin")
        move_btns[1]['bg'] = 'yellow'
        move_btns[1]['fg'] = 'gold'                                       # checkpoint2

        move_btns[2]['text'] = '해바라기 CU'
        move_btns[2]['command'] = lambda : eVent("sun")
        move_btns[2]['bg'] = 'lime'
        move_btns[2]['fg'] = 'green'

        move_btns[3]['text'] = '오이무침!'
        move_btns[3]['command'] = lambda : eVent("MO")
        move_btns[3]['bg'] = 'light blue'
        move_btns[3]['fg'] = 'blue'

    if type=="choc" or type=="MO" or type =="pumkin" or type=="sun" :
        if type =="choc" :
            Texting("안...............녕", 36)
            Texting("어 예 안녕하세요?", 35)
            Texting("하암 너가 생일인 얘인가 보구나? 생일 축하해", 36)
            Texting("아 감사한데... 어떻게 아셨어요?", 35)
            Texting("다 아는 방법이 있어 아무튼 나는 코코아 열매야", 36)
            Texting("난 초코릿 음식을 만드는 젤리가 있어", 36)
            Texting("오! 혹시 저 주실 수 있나요?", 35)
            Texting("당연하지! 근데 혹시 달다 말고 따른 맛이 뭐가 있는 줄 알아?", 36)
            Texting("내가 현재 달다라는 것만 알아서 따른 맛이 뭐가 있는 지 늘 궁금했어", 36)
            Texting("어... 여기 딸기 꼭다리요", 35)
            Texting("딸기 꼭다리? 이건 무슨 맛이야?", 36)
            Texting("엄... 떫다?", 35)
            Texting("으음 옆에다가 두고 가줘 자 아무튼 여기 코코아 젤리", 36)
            Texting("생각보다 단순하게 주셨네?", 35)
            Texting("[!] 초코 젤리를 얻었습니다!", 33)
            Ending(5)
        elif type=="pumkin" :
            Texting("안녕? 🎃", 37)
            Texting("안녕하세요?", 35)
            Texting("생일 축하해 🎃", 37)
            Texting("아... 네 감사합니다?", 35)
            Texting("여기 호박 젤리 🎃", 37)
            Texting("? 그냥 주시는 건가요?", 35)
            Texting("너 보니까 할로윈을 좋아하더라 🎃", 37)
            Texting("그래서 그냥 주는 거야 🎃", 37)
            Texting("아 예 감사합니다!", 35)
            
            Texting("[!] 할로윈 젤리를 얻었습니다!", 33)
            Ending(6)
        elif type=="sun" :
            Texting("안녕하세요? 저 꽃만 유일하게 크게 서있는 것을 보니 살아 계시는 것 같은데", 35)
            Texting("어 안녕, 지금 내가 태양을 바라 볼 수 밖에 없어서 널 바라 볼 수 없네", 94)
            Texting("누구 왔어?", 95)
            Texting("내가 어떻게 알아", 94)
            Texting("아 여기 2분이 살아 계셨구나", 35)
            Texting("내 혹시 제가 뭐를 해야지 젤리를 얻을 수 있죠?", 35)
            Texting("젤리? 아 너가 생일 친구구나?", 94)
            Texting("아 생일 친구야 반갑다!", 95)
            Texting("아 감사합니다! 혹시 젤리는...", 35)
            Texting("음 그냥 나에게 달이 어떻게 생겼는 지 알려줘", 94)
            Texting("그리고 나한테는 어떻게 해가 생겼는 지 알려줘!", 95)
            Texting("아 해바라기랑 달맞이꽃이구나", 35)
            Texting("달은 태양인데 좀 더 어둡고 울퉁불퉁해요", 35)
            Texting("해는 너무 눈부셔서 똑바로 보기 힘들고요", 35)
            Texting("아 그래 생각보다 단순하구나?", 95)
            Texting("그래 고마웠다 자 여기 꽃 젤리", 94)
            Texting("[!] 꽃 젤리를 얻었습니다!", 33)
            Ending(7)

        else :
            Texting("응? 내 젤리를 얻고 싶다고?", 97)
            Texting("네 한번 무 케이크도 먹어보고 싶어서", 35)
            Texting("나 같은 채소를 어떤 디져트에 쓴다고...", 97)
            Texting("에이 그래도 무 스테이크, 깎두기, 오이무침도 있는데요", 35)
            Texting("내가 알기론 오이무침은 오이로 만들어진거야", 97)
            Texting("아 그런가? 아무튼 생각보다 어울릴 수도 있죠!", 35)
            Texting("그럼 무 젤리도 줄께", 97)
            Texting("먹어보고 어떤지 알려줘", 97)
            Texting("넵 알겠습니다!", 35)
            Texting("[!] 무 젤리를 얻으셨습니다!", 33)
            Ending(8)

def Ingre(type) :
    if not(isTexting) :
        eVent(type)
        if canObtain[type]>=5 :
            if not(type in ingrediant) :
                ingrediant.append(type)
        if len(ingrediant)==4 :
            Texting("으아 드디어 재료 다 모았다!", 35)
            Ending(1)

def Item(type) :
    global isTexting, tree
    if (type=='weed') :
        Texting("[~] 잡초를 뽑는 중 입니다...", 96)
        isTexting = True
        time.sleep(1.3)
        canObtain["milk"]+=1
        isTexting = False
        Texting("[!] 잡초를 하나 얻었습니다!", 33)
        if canObtain['milk'] == 5 :
            Texting("[!!] 잡초를 총 5개 얻었습니다!", 93)
            move_btns[0]['text'] = '잡초 5개를 주기'
            move_btns[0]['command'] = lambda : Ingre('milk')
    elif type=='grower' :
        Texting("[~] 탐색 중입니다...", 96)
        isTexting = True
        time.sleep(1)
        ran = random.randint(1, 10)
        if ran<=3 :
            isTexting = False
            Texting("[!] 영양제를 얻었습니다!", 33)
            canObtain['wheat'] += 1
            if canObtain["wheat"] == 2 :
                Texting("[!!] 영양제를 총 2개 얻었습니다!", 93)
                move_btns[1]['text'] = '영양제 2개를 주기'
                move_btns[1]['command'] = lambda : Ingre('wheat')
        else :
            isTexting = False
            Texting("[?] 허탕을 치고 말았습니다...", 91)
    
    elif type=='water' :
        Texting("[~] 탐색 중입니다...", 96)
        isTexting = True
        time.sleep(1)
        ran = random.randint(1, 10)
        if ran<=5 :
            isTexting = False
            Texting("[!] 영양수를 얻었습니다!", 33)
            canObtain['wheat'] += 1
            if canObtain["wheat"] == 5 :
                Texting("[!!] 영양수를 총 3개 얻었습니다!", 93)
                move_btns[1]['text'] = '영양제 3개를 주기'
                move_btns[1]['command'] = lambda : Ingre('wheat')
        else :
            isTexting = False
            Texting("[?] 허탕을 치고 말았습니다...", 91)

    elif type=='chick' :
        Texting("[~] 닭을 쫒는 중입니다", 96)
        isTexting = True
        time.sleep(3.5)
        isTexting = False
        Texting("[!] 닭을 잡았습니다!", 33)
        canObtain['egg'] += 1
        if (canObtain["egg"]==3) :
            Texting("[!!] 닭 3마리를 잡았습니다!", 93)
            move_btns[2]['text'] = '닭 돌려주기'
            move_btns[2]['command'] = lambda : Ingre("egg")
    
    elif type=='chop' :
        Texting("[~] 나무를 한번 찍었습니다", 96)
        time.sleep(1)
        tree-=1
        Texting(f"[!] 나무를 찍었습니다! 현재 {10-tree}번 찍었습니다", 33)
        if (tree==0) :
            canObtain["egg"] += 1
            Texting("[!!] 나무가 넘어갔습니다!", 93)
            move_btns[2]['text'] = '나무 가공하기'
            move_btns[2]['command'] = lambda : Item("plank")
    
    elif type=='plank' :
        Texting("[~] 나무를 가공하고 있습니다", 96)
        time.sleep(5)
        Texting("[!!] 나무가 가공됬습니다!", 93)
        canObtain['egg'] += 1
        move_btns[2]['text'] = '나무 판자 주기'
        move_btns[2]['command'] = lambda : Ingre('egg')


Texting("게임을 하기 전에 알면 좋은 상식", 37)
Texting("[!]는 알림을 뜻합니다", 33)
Texting("[?]은 실패를 했을 때 뜹니다", 91)
Texting("[~]는 작업 중/로딩 중을 뜻합니다", 96)
Texting("[!!]는 퀘스트를 완료했다를 뜻합니다", 93)
Texting("참고로 [*] (*는 ? ! ~ !! 중하나)가 없다면 캐릭터의 대사입니다", 37)
Texting("\n", 37)

Texting("오늘은 내 생일이다", 35)
Texting("내 생일에는 역시 케이크지", 35)
Texting("하지만 오늘은 사지 않고 구울 것이다", 35)
Texting("내가 내 케이크를 만드는게 사는 것 보다 좋은 추억이 되겠지?", 35)
Texting("케이크를 만들려면 밀가루, 우유, 달걀 그리고 설탕이 필요하네", 35)
Texting("구해야겠다", 35)

Texting("\n[!] console 탭에 있는 버튼을 눌러서 재료를 구하세요!", 33)

menu_ = Tk()

cakes = [PhotoImage(file="strawberry_cake.png"), PhotoImage(file="orange.png"), PhotoImage(file="apple.png"), 
        PhotoImage(file="melon.png"), PhotoImage(file="mango.png"), PhotoImage(file="choc.png"),
        PhotoImage(file="pumkin.png"), PhotoImage(file="flower.png"), PhotoImage(file="moo.png")] # checkpoint3

menu_.title("menu")

mover = Tk()

all_btns = [Button(mover, text="우유 얻기", command=lambda:Ingre("milk"), width=30, height=2, bg="pink", fg="red"),
            Button(mover, text="밀가루 얻기", command=lambda:Ingre('wheat'), width=30, height=2, bg="yellow", fg="gold"),
            Button(mover, text="달걀 얻기", command=lambda:Ingre('egg'), width=30, height=2, bg='lime', fg='green'), 
            Button(mover, text="설탕 얻기", command=lambda:Ingre('sugar'), width=30, height=2, bg='light blue', fg='blue')] # checkpoint1
move_btns = [all_btns[0], all_btns[1], all_btns[2], all_btns[3]]

for i in range(len(move_btns)) :
        move_btns[i].grid(row=i, column=0)

mover.title("console")

mover.mainloop()

menu_.mainloop()

# 마지막으로 달걀만 남았다 ㅓㄹ ㅐㅓ랮더대ㅑㄼ3ㅐㅑ러대ㅑㅓ대ㅑ러대ㅕㄱ루배ㅑ루댜루ㅑㅐ
# 끝이 보인다
# 만뢔ㅑ롭댜ㅐ뱌개ㅓㅂㅈ햗뱆모ㅑ럽주ㅑㅐ호냐루내ㅕㅣㅁ코루ㅐ져보ㅑ누래ㅑ좋




# 남은 것은 케이크 그리기 밖에 안남았따
# 그리고 편집