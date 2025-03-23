from discord.ext import commands
import discord
import asyncio
from discord.ui import Button, View
from discord import ButtonStyle
import random, time

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

server = open("server.txt", 'a')
server.close()

fighting_ = "NONE"
buffordebiff = []
enemybuffordebuff = []
magic_use = []
enskill = []
health, dmg, sheld, enhealth, endmg, ensheld, turn = 100, 100, 100, 100, 100, 100, 0
battlemsg, usingmagic, ename = "", "", "NONE"

@bot.command()
async def 등록(ctx) :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()
    if str(ctx.author) in serverfile :
        await ctx.send("이미 등록이 된 마법사입니다! (해리포터 봇과 왜 비슷해진거 같지)")
    else :
        await ctx.send("당신은 과연 어떤 마법사가 될까요?")
        serverfile.append(str(ctx.author))
        print(serverfile)
        newplayer = open(f"{str(ctx.author)}.txt", 'a')
        newplayer.write("0\n") # 돈 0
        newplayer.write("0\n") # 경험치 1
        newplayer.write("0\n") # 레벨 2
        newplayer.write("0\n") # 사건 3
        newplayer.write("00000000\n") # 마법 4
        newplayer.write("0\n") # 출쵁 5
        newplayer.write("0\n") # 컨디션 6 최악, 힘듬, 집중이 안됨, 집중이 산만함, 졸림, 평범 (5), 좋음, 집중이 잘됨, 행복함, 기운이 엄청 참, 엄청난 집중력 (상위 마법도 레벨에 불구하고 배움)
        newplayer.write("0\n") # 지팡이 (단계 - 능력들) 7
        newplayer.write("0000000000\n") # 아이템 8
        newplayer.write("10\n") # 공격 9
        newplayer.write("100\n") # 체력 10
        newplayer.write("NONE\n") # 펫 11
        newplayer.write("0\n") # 쿨타임 12
        newplayer.write("0") # 퀘스트 13
        newplayer.close()
    
    GF = open("server.txt", 'w')
    for i in range(0, len(serverfile) - 1):
        GF.write(str(serverfile[i]))
        GF.write("\n")
    GF.write(str(serverfile[len(serverfile) - 1]))
    GF.write("\n")
    GF.close()

@bot.command()
async def 할일(ctx) :
    await ctx.send("```diff\n+ 무엇을 할것인가?\n+ 1. 마법 배우기\n+ 2. 퀴디츠 보기\n+ 3. 학교 둘러 보기\n+ 4. 쉬기\n+ 5. 자기의 힘 확인하기\n+ 6. 시간표 확인하기\n```")

@bot.command()
async def 시간표(ctx) :
    now = time.localtime()
    day = time.strftime('%a', now)
    wat = time.strftime('%w', now)
    print(wat)
    embed = discord.Embed(title=f"{day}의 시간표", description=f"매주 마다 스케줄 표가 같은 거 같다...")
    if (int(wat) == 6) :
        embed.add_field(name="", value=f"```diff\n+ 9시 : 아침 식사\n+ 10시 : 공중학\n+ 11시 : 도서관 연구\n+ 11시 반 : 점심시간\n+ 12시 : 비행수업\n+ 1시 : 숲 탐험\n+ 2시 : 바다 탐험\n+ 3시 : 자유시간\n+ 6시 : 저녁시간\n+ 10시 : 수면 시간```")
    elif (int(wat) == 0) :
        embed.add_field(name="", value=f"```diff\n일요일에는 별다른 수업이 진행 되지 않는다```")
    elif (int(wat)==1) :
        embed.add_field(name="", value=f"```diff\n+ 9시 : 아침 식사\n+ 10시 : 생태학\n+ 11시 : 점술\n+ 11시 반 : 점심시간\n+ 12시 : 비행수업\n+ 1시 : 숲 탐험\n+ 2시 : 바다 탐험\n+ 3시 : 자유시간\n+ 6시 : 저녁시간\n+ 10시 : 수면 시간```")
    elif (int(wat)==2) :
        embed.add_field(name="", value=f"```diff\n+ 9시 : 아침 식사\n+ 10시 : 공중학\n+ 11시 : 도서관 연구\n+ 11시 반 : 점심시간\n+ 12시 : 비행수업\n+ 1시 : 숲 탐험\n+ 2시 : 바다 탐험\n+ 3시 : 자유시간\n+ 6시 : 저녁시간\n+ 10시 : 수면 시간```")
    await ctx.send(embed=embed)

    # 일, 월, 화, 수, 목, 금, 토 (0 ~ 6)

@bot.command()
async def 쉬기(ctx, how = "NONE") :
    now = time.localtime()
    hour = int(time.strftime('%H', now))
    print(hour)
    if (22<=hour or hour<9) :
        await ctx.send("수면 시간입니다, 내일도 많은 일이 있겠죠?")

@bot.command()
async def 수업_듣기(ctx) :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()

    if str(ctx.author) in serverfile :
        classes = []
        now = time.localtime()
        wrait = time.strftime('%w', now)
        if (int(wrait)==1) :
            classes = ['생태학', '점술']
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()

        now = time.localtime()
        hour = int(time.strftime('%H', now))
        print(hour)
        if (22<=hour or hour<9) :
            await ctx.send("수면 시간입니다, 이를 어길시 혼이 날수 있으니 가만히 자야겠네요")
        if (10<=hour<11) :
            await ctx.send(f"현재 진행중인 수업 : {classes[0]}")
        elif (11<=hour<12) :
            await ctx.send(f"현재 진행중인 수업 : {classes[1]}")

@bot.command()
async def 출석체크(ctx) :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()

    if str(ctx.author) in serverfile :
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()
        now = time.localtime()
        date = int(time.strftime('%Y', now) + time.strftime('%m', now) + time.strftime('%d', now))
        if int(player_info[5]) != date :
            embed = discord.Embed(title=f"출석체크 성공!", description=f"학생 확인서에 적혔다!, 보상도 주니 얼마나 좋아 ㅎ (+10 아이언너겟)", color=0x61ff71)
            player_info[0] = str(int(player_info[0])+100)
            player_info[5] = str(date)
        else :
            embed = discord.Embed(title=f"출석체크 이미 함...", description=f"학생 확인서에 이미 적혀있데.... 내일도 해야겠다", color=0xff6161)
        await ctx.send(embed=embed)
        GF = open(f"{str(ctx.author)}.txt", 'w')
        for i in range(0, len(player_info) - 1):
            GF.write(str(player_info[i]))
            GF.write("\n")
        GF.write(str(player_info[len(player_info) - 1]))
        GF.write("\n")
        GF.close()
    else :
        await ctx.send("어 근데 생각해보니 나 아직 학교의 학생이 아닌데...?")

@bot.command()
async def 이동(ctx, place="NONE") :
    if (place=="NONE") :
        await ctx.send("이동이 가능한 장소를 모두 보입니다")
        await ctx.send("```diff\n+ 허락된 장소\n+ 1. 도서관\n+ 2. 비행 수업실\n+ 3. 운동장\n- 금지된 장소\n- 1. 숲\n- 2. 바다\n```")

helperjw = 0
@bot.command()
async def 독서(ctx, book="NONE") :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()
    if str(ctx.author) in serverfile :
        if (str(book)=="마법의 시초자들을 위한 마법의 세계") :
            thebook = ["마법의 세계는 코인을 사파이어 코인, 에메랄드 코인, 루비 코인, 그리고 다이아 코인으로 이루워진다\n100SC=1EC/100EC=1RC/100RC=1DC", "배틀은 방어/공격/디버프/버프/힐/협상 마법으로 대결을 한다", "돈은 퀘스트/제작/판매/작업/레벨업 등으로 얻을 수 있다"]
            embed = discord.Embed(title="마법의 시초자들을 위한 마법의 세계", description=thebook[0])
            btn1 = Button(label="다음 페이지", style = discord.ButtonStyle.blurple)
            btn2 = Button(label="이전 페이지", style = discord.ButtonStyle.blurple)
            btn3 = Button(label="책 덮기", style = discord.ButtonStyle.green)
            
            async def btncall1(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw + 1
                changembed = discord.Embed(title="마법의 시초자들을 위한 마법의 세계", description=thebook[helperjw%3])
                await msg.edit(embed=changembed)
            async def btncall2(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw - 1
                changembed = discord.Embed(title="마법의 시초자들을 위한 마법의 세계", description=thebook[helperjw%3])
                await msg.edit(embed=changembed)
            async def btncall3(interaction:discord.Interaction) :
                await msg.delete()
            btn1.callback = btncall1
            btn2.callback = btncall2
            btn3.callback = btncall3
            view = View()
            view.add_item(btn1)
            view.add_item(btn2)
            view.add_item(btn3)
            msg = await ctx.send(embed=embed, view=view)
        elif str(book) == "NONE" :
            await ctx.send("무슨 책을 찾고 있나요?\n도서관에 있는 책을 보여주겠습니다")
            await ctx.send("```diff\n+ 도서관 책\n+ 마법의 시초자들을 위한 마법의 세계\n+ 불 마법과 그 예외\n+ 펫들의 종류와 힘\n- 아직은 책을 더 받는 중이다...```")
        elif book=="불 마법과 그 예외" :
            thebook = ["**THE FIRST FIRE**\n불 가문의 마법 1번째로 추정\n적에게 주위에 불이 적을 향해 오는 것 같은 착각을 들게 한다", "**THE FLAME FESTIVAL**\n불의 가문 마법 3번째로 추정\n적에게 땅에 불이 폭발하는 것 같은 착각을 들게 한다\n주변에 불을 피워 화상을 입힌다", "**THE REALITY HEAT**\n불 가문 마법 6번쨰로 추정\n강력한 불로 적을 공격한다\n적에게 33%로 심한 화상을 입힌다", "**THE LAST FIRE**\n유일하게 불의 마법이자 선의 마법\n주위에 불로 감싼고, 그 불에 생명을 부여해 불에 공격한다\n불에 닿으면 고통스럽게 재가 된다 (영웅불에 맞을 시 0.01%로 소멸된다)\n적이 영웅불의 칼 돌진을 맞을 시 무조건 고온 화상을 입는다"]
            embed = discord.Embed(title="불 마법과 그 예외", description=thebook[0])
            btn1 = Button(label="다음 페이지", style = discord.ButtonStyle.blurple)
            btn2 = Button(label="이전 페이지", style = discord.ButtonStyle.blurple)
            btn3 = Button(label="책 덮기", style = discord.ButtonStyle.green)
            
            async def btncall1(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw + 1
                changembed = discord.Embed(title="불 마법과 그 예외", description=thebook[helperjw%len(thebook)])
                await msg.edit(embed=changembed)
            async def btncall2(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw - 1
                changembed = discord.Embed(title="불 마법과 그 예외", description=thebook[helperjw%len(thebook)])
                await msg.edit(embed=changembed)
            async def btncall3(interaction:discord.Interaction) :
                await msg.delete()
            btn1.callback = btncall1
            btn2.callback = btncall2
            btn3.callback = btncall3
            view = View()
            view.add_item(btn1)
            view.add_item(btn2)
            view.add_item(btn3)
            msg = await ctx.send(embed=embed, view=view)
        elif book=="펫들의 종류와 힘" :
            thebook = ["**생명의 크렌피**\n등급 : A급\n특징 : 만약 주인이 데미지를 입었을 경우 데미지의 일부를 회복한다\n특성 *광합성* : 오직 턴이 4의 배수 일때만 적용 된다", "**축복의 엠라**\n등급 : A급\n마법을 성공할 확률이 는다\n특성 *파손* : 턴이 지나면 지날수록 확률이 더 적게 는다", "****\n불 가문 마법 6번쨰로 추정\n강력한 불로 적을 공격한다\n적에게 33%로 심한 화상을 입힌다", "**THE LAST FIRE**\n유일하게 불의 마법이자 선의 마법\n주위에 불로 감싼고, 그 불에 생명을 부여해 불에 공격한다\n불에 닿으면 고통스럽게 재가 된다 (영웅불에 맞을 시 0.01%로 소멸된다)\n적이 영웅불의 칼 돌진을 맞을 시 무조건 고온 화상을 입는다"]
            urls = ["https://cdn.discordapp.com/attachments/1142471384027648000/1150717040382980116/image.png", "https://cdn.discordapp.com/attachments/1142471384027648000/1152411713254207612/the_emerald.png", "", "", "", "",""]
            embed = discord.Embed(title="펫들의 종류와 힘", description=thebook[0])
            embed.set_thumbnail(url=urls[0])
            btn1 = Button(label="다음 페이지", style = discord.ButtonStyle.blurple)
            btn2 = Button(label="이전 페이지", style = discord.ButtonStyle.blurple)
            btn3 = Button(label="책 덮기", style = discord.ButtonStyle.green)
            
            async def btncall1(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw + 1
                changembed = discord.Embed(title="펫들의 종류와 힘", description=thebook[helperjw%len(thebook)])
                changembed.set_thumbnail(url=urls[helperjw%len(thebook)])
                await msg.edit(embed=changembed)
            async def btncall2(interaction:discord.Interaction) :
                global helperjw
                helperjw = helperjw - 1
                changembed = discord.Embed(title="펫들의 종류와 힘", description=thebook[helperjw%len(thebook)])
                changembed.set_thumbnail(url=urls[helperjw%len(thebook)])
                await msg.edit(embed=changembed)
            async def btncall3(interaction:discord.Interaction) :
                await msg.delete()
            btn1.callback = btncall1
            btn2.callback = btncall2
            btn3.callback = btncall3
            view = View()
            view.add_item(btn1)
            view.add_item(btn2)
            view.add_item(btn3)
            msg = await ctx.send(embed=embed, view=view)
        else :
            await ctx.send("여기 도서관에는 그런 책은 없습니다만......")
    else :
        await ctx.send("내가 모르는 일인데 왜 신경을 써야하는 거지?")

@bot.command()
async def 나(ctx) :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()

    if str(ctx.author) in serverfile :
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()
        RI = int(int(player_info[0]) / 1000000)
        GP = int((int(player_info[0]) - RI*1000000) / 10000)
        SN = int((int(player_info[0]) - RI*1000000 - GP*10000) / 100)
        BT = int(int(player_info[0]) - RI*1000000 - GP*10000 - SN*100) # 컨디션 6 최악, 힘듬, 집중이 안됨, 집중이 산만함, 졸림, 평범 (5), 좋음, 집중이 잘됨, 행복함, 기운이 엄청 참, 엄청난 집중력 (상위 마법도 레벨에 불구하고 배움)
        Condition = ""
        if int(player_info[6]) == 0 :
            Condition = "최악"
        elif int(player_info[6]) == 1 :
            Condition = "힘듦"
        elif int(player_info[6]) == 2 :
            Condition = "집중이 안됨"
        elif int(player_info[6]) == 3 :
            Condition = "집중이 산만함"
        elif int(player_info[6]) == 4 :
            Condition = "졸림"
        elif int(player_info[6]) == 5 :
            Condition = "평범"
        elif int(player_info[6]) == 6 :
            Condition = "좋음"
        elif int(player_info[6]) == 7 :
            Condition = "집중이 잘됨"
        elif int(player_info[6]) == 8 :
            Condition = "행복함"
        elif int(player_info[6]) == 9 :
            Condition = "기운이 엄청 참"
        else :
            Condition = "엄청난 집중력!!!"
        await ctx.send(f"```\n<<{ctx.author}>>\n돈 : 다이아 코인 : {RI}/ 루비 코인 : {GP}/ 에메라드 코인 : {SN}/ 사파이어 코인 : {BT}\n레벨 : {player_info[2]}\n경험치 : {player_info[1]}/{(int(player_info[2])+1)*100}\n컨디션 : {Condition} (컨디션은 /도움 마법_배우기에서 자세히)```")
    else :
        await ctx.send("나? 나는 그냥 평범한 한국의 시민이지")

px, py, screenx, screeny, bpy, bpx, NWSE = 0, 0, 0, 0, 0, 0, 'N'

@bot.command()
async def 개발자_권한(ctx, type = "NONE", player: discord.User = "NONE", amount = "NONE") :
    global fighting_
    if str(ctx.author) == ".wincat" :
        server = open("server.txt", 'r')
        surver = server.readlines()
        serverfile = []
        for line in surver :
            serverfile.append(str(line.strip()))
        server.close()
        if int(type) == 3 :
            fighting_ = "NONE"
            await ctx.send("싸우는 상황이 없습니다")
        if int(type) == 4 :
            global px, py, screenx, screeny, bpy, bpx, NWSE
            await ctx.send("현재 테스트 상황 : 보드게임 `⬛`")
            await ctx.send("여기에서는 프로그레밍에 한계가 있으므로, 완전판은 다른 방식으로 만들 것입니다 (앱등으로 계발 예정)")
            row, colume = 51, 51
            screenx, screeny = 0, 0 # 24, 24
            py, px = int(2), int(2) # 26, 26
            bpy, bpx = py, px
            print(py, px)
            MAP = [['⬜' for j in range(colume)] for i in range(row)]
            for i in range(1, row-1) :
                for j in range(1, colume-1) :
                    MAP[i][j] = '⬛'
            MAP[py][px] = '🟥'
            embed = discord.Embed(title="감옥 탈출", description="")
            addfieldstr = ""
            for i in range(screeny, screeny+5) :
                for j in range (screenx, screenx+5) :
                    addfieldstr = addfieldstr + str(MAP[i][j])
                addfieldstr = addfieldstr + "\n"
            embed.add_field(name="", value=f"{addfieldstr}")
            embed.add_field(name="현재 상황", value="**선택된 아이템**\nNaN\nNaN/NaN", inline=True)
            embed.add_field(name="", value="인벤토리\n`⬛⬛⬛⬛⬛⬛⬛ㄷㄷㄷㄷ⬛⬛⬛`", inline=False)
            embed.add_field(name="플레이어 스탯", value="0\n0\n0")
            embed.add_field(name="", value=f"보는 방향 : {NWSE}", inline=True)
            
            btn1 = Button(label="⬆️", style = discord.ButtonStyle.blurple)
            btn2 = Button(label="⬇️", style = discord.ButtonStyle.blurple)
            btn3 = Button(label="➡️", style = discord.ButtonStyle.blurple)
            btn4 = Button(label="⬅️", style = discord.ButtonStyle.blurple)
            btn5 = Button(label="🧭", style=discord.ButtonStyle.green)
            btn_interact = Button(label="Interact", style=discord.ButtonStyle.secondary)

            async def btncall1(interaction:discord.Interaction) :
                global px, py, screenx, screeny, bpy, bpx, NWSE
                print(py, px, bpy, bpx, screenx, screeny)
                py = int(py) - 1
                if (not(py==bpy and px==bpx) and (screeny+2==py+1 and screenx+2 == px) or (px==1 or px==50)) :
                    screeny = screeny-1
                if (MAP[py][px]=='⬜') :
                    py = bpy
                    screeny = screeny +1
                if (screeny <0) :
                    screeny = 0
                MAP[bpy][bpx] = '⬛'
                MAP[py][px] = '🟥'
                print(py, px, bpy, bpx, screenx, screeny)
                bpy = int(py)
                bpx = int(px)
                changembed = discord.Embed(title="감옥 탈출", description="")
                addfieldstr = ""
                print(MAP[screeny+2][screenx+2])
                for i in range(screeny, screeny+5) :
                    for j in range (screenx, screenx+5) :
                        addfieldstr = addfieldstr + str(MAP[i][j])
                    addfieldstr = addfieldstr + "\n"
                changembed.add_field(name="", value=f"{addfieldstr}")
                changembed.add_field(name="현재 상황", value="**선택된 아이템**\nNaN\nNaN/NaN", inline=True)
                changembed.add_field(name="", value="인벤토리\n`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛`", inline=False)
                changembed.add_field(name="플레이어 스탯", value="0\n0\n0")
                changembed.add_field(name="", value=f"보는 방향 : {NWSE}", inline=True)
                await msg.edit(embed= changembed)

            async def btncall2(interaction:discord.Interaction) :
                global px, py, screenx, screeny, bpy, bpx, NWSE
                print(py, px, bpy, bpx, screenx, screeny)
                py = int(py) + 1
                if (not(py==bpy and px==bpx) and (screeny+2==py-1 and screenx+2 == px) or (px==1 or px==50)) :
                    screeny = screeny+1
                if (MAP[py][px]=='⬜') :
                    py = bpy
                    screeny = screeny -1
                if (screeny <0) :
                    screeny = 0
                MAP[bpy][bpx] = '⬛'
                MAP[py][px] = '🟥'
                bpy = int(py)
                bpx = int(px)
                changembed = discord.Embed(title="감옥 탈출", description="")
                addfieldstr = ""
                print(MAP[screeny+2][screenx+2])
                for i in range(screeny, screeny+5) :
                    for j in range (screenx, screenx+5) :
                        addfieldstr = addfieldstr + str(MAP[i][j])
                    addfieldstr = addfieldstr + "\n"
                changembed.add_field(name="", value=f"{addfieldstr}")
                changembed.add_field(name="현재 상황", value="**선택된 아이템**\nNaN\nNaN/NaN", inline=True)
                changembed.add_field(name="", value="인벤토리\n`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛`", inline=False)
                changembed.add_field(name="플레이어 스탯", value="0\n0\n0")
                changembed.add_field(name="", value=f"보는 방향 : {NWSE}", inline=True)
                await msg.edit(embed= changembed)

            async def btncall4(interaction:discord.Interaction) :
                global px, py, screenx, screeny, bpy, bpx, NWSE
                print(py, px, bpy, bpx, screenx, screeny)
                px = int(px) - 1
                if (not(py==bpy and px==bpx) and (screeny+2==py and screenx+2 == px+1) or (py==1 or py==50)) :
                    screenx = screenx-1
                if (MAP[py][px]=='⬜') :
                    px = bpx
                    screenx = screenx +1
                if (screenx <0) :
                    screenx = 0
                MAP[bpy][bpx] = '⬛'
                MAP[py][px] = '🟥'
                print(py, px, bpy, bpx, screenx, screeny)
                bpy = int(py)
                bpx = int(px)
                changembed = discord.Embed(title="감옥 탈출", description="")
                addfieldstr = ""
                print(MAP[screeny+2][screenx+2])
                for i in range(screeny, screeny+5) :
                    for j in range (screenx, screenx+5) :
                        addfieldstr = addfieldstr + str(MAP[i][j])
                    addfieldstr = addfieldstr + "\n"
                changembed.add_field(name="", value=f"{addfieldstr}")
                changembed.add_field(name="현재 상황", value="**선택된 아이템**\nNaN\nNaN/NaN", inline=True)
                changembed.add_field(name="", value="인벤토리\n`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛`", inline=False)
                changembed.add_field(name="플레이어 스탯", value="0\n0\n0")
                changembed.add_field(name="", value=f"보는 방향 : {NWSE}", inline=True)
                await msg.edit(embed= changembed)
            
            async def btncall3(interaction:discord.Interaction) :
                global px, py, screenx, screeny, bpy, bpx, NWSE
                print(py, px, bpy, bpx, screenx, screeny)
                px = int(px) + 1
                print(">>> ", px==1 or px==50)
                if (not(py==bpy and px==bpx) and (screeny+2==py and screenx+2 == px-1)) or (py==1 or py==50) :
                    screenx = screenx+1
                if (MAP[py][px]=='⬜') :
                    px = bpx
                    screenx = screenx -1
                if (screenx <0) :
                    screenx = 0
                MAP[bpy][bpx] = '⬛'
                MAP[py][px] = '🟥'
                print(py, px, bpy, bpx, screenx, screeny)
                bpy = int(py)
                bpx = int(px)
                changembed = discord.Embed(title="감옥 탈출", description="")
                addfieldstr = ""
                print(MAP[screeny+2][screenx+2])
                for i in range(screeny, screeny+5) :
                    for j in range (screenx, screenx+5) :
                        addfieldstr = addfieldstr + str(MAP[i][j])
                    addfieldstr = addfieldstr + "\n"
                changembed.add_field(name="", value=f"{addfieldstr}")
                changembed.add_field(name="현재 상황", value="**선택된 아이템**\nNaN\nNaN/NaN", inline=True)
                changembed.add_field(name="", value="인벤토리\n`⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛`", inline=False)
                changembed.add_field(name="플레이어 스탯", value="0\n0\n0")
                changembed.add_field(name="", value=f"보는 방향 : {NWSE}", inline=True)
                await msg.edit(embed= changembed)

            btn1.callback = btncall1
            btn2.callback = btncall2
            btn3.callback = btncall3
            btn4.callback = btncall4
            view = View()
            view.add_item(btn1)
            view.add_item(btn2)
            view.add_item(btn4)
            view.add_item(btn3)
            view.add_item(btn5)
            view.add_item(btn_interact)
            msg = await ctx.send(embed=embed, view = view)

        elif str(player) in serverfile :
            user = open(f"{str(player)}.txt", 'r')
            playerfile = user.readlines()
            player_info = []
            for line in playerfile :
                player_info.append(str(line.strip()))
            user.close()
            if int(type) == 1 :
                player_info[0] = str(int(player_info[0]) + int(amount))
                await ctx.send("돈 기부 성공 :)")
                GF = open(f"{str(player)}.txt", 'w')
                for i in range(0, len(player_info) - 1):
                    GF.write(str(player_info[i]))
                    GF.write("\n")
                GF.write(str(player_info[len(player_info) - 1]))
                GF.write("\n")
                GF.close()
            elif int(type) == 2 :
                player_info[0] = str(int(player_info[0]) - int(amount))
                if (int(player_info[0])<0) :
                    player_info[0] = str(0)
                await ctx.send("돈 압수 성공 :)")
                GF = open(f"{str(player)}.txt", 'w')
                for i in range(0, len(player_info) - 1):
                    GF.write(str(player_info[i]))
                    GF.write("\n")
                GF.write(str(player_info[len(player_info) - 1]))
                GF.write("\n")
                GF.close()
            else :
                await ctx.send("가능한 기능 발견 미확인")
        else :
            await ctx.send(f"{player}는 이 프로그램에 포함이 안돼어 있습니다")
    else :
        await ctx.send("개발자 아님")

@bot.command()
async def 배틀(ctx, enemy="NONE") :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()

    if str(ctx.author) in serverfile :
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()
        global fighting_, health, dmg, sheld, enhealth, endmg, ensheld, battlemsg, usingmagic, ename, turn, magic_use, enskill
        health = player_info[10]
        dmg = player_info[9]
        if (fighting_=="NONE") :
            if enemy=="테스트적" :
                magic_use.clear()
                turn = 0
                ename = enemy
                fighting_ = str(ctx.author)
                buffordebiff.clear()
                enemybuffordebuff.clear()
                embed = discord.Embed(title=f"{ctx.author} VS {enemy}")
                embed.add_field(name = f"{ctx.author}", value=f"체력 : {health}\n공격 : {dmg}\n방어 : {sheld}\n{buffordebiff}")
                embed.add_field(name = f"{enemy}", value=f"체력 : {enhealth}\n공격 : {endmg}\n방어 : {ensheld}\n{enemybuffordebuff}")
                embed.add_field(name = "전투상황", value="```diff\n해포봇이랑 똑같습니다~~```", inline=False)
                battlemsg = await ctx.send(embed=embed)
                enskill = ["테스트마법", "우트라", "캔터스"]

@bot.command()
async def 마법_사용(ctx, magic) :
    global fighting_, health, dmg, sheld, enhealth, endmg, ensheld, usingmagic, battlemsg, ename, magic_use, turn, enskill
    if str(ctx.author) == fighting_ :
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()
        if magic == "우트라" and str(player_info[4][0]) == '1' :
            turn += 1
            magic_use.append(magic)
            usingmagic = magic
            sheld += 10
            changembed = discord.Embed(title=f"{ctx.author} VS {ename}")
            changembed.add_field(name = f"{ctx.author}", value=f"체력 : {health}\n공격 : {dmg}\n방어 : {sheld}\n{buffordebiff}")
            changembed.add_field(name = f"{ename}", value=f"체력 : {enhealth}\n공격 : {endmg}\n방어 : {ensheld}\n{enemybuffordebuff}")
            changembed.add_field(name = "전투상황", value="```diff\n+ 상대방의 진실을 보았다!\n+ 상대방의 움직임을 간파했다!```", inline=False)
            await battlemsg.edit(embed=changembed)
            await asyncio.sleep(1.3)
            


@bot.command()
async def 포기(ctx) :
    global fighting_
    if fighting_==str(ctx.author) :
        await ctx.send("배틀을 포기합니다...")
        fighting_ = "NONE"
    else :
        await ctx.send(f"당신은 배틀을 안하고 있는데요? 현재 싸우는 사람 : {fighting_}")

@bot.command()
async def 도움(ctx, categori = "NONE") :
    if (categori=="NONE") :
        embed=discord.Embed(title=f"도움 커멘드 사용 방법", description="/도움 {\종목}")
        embed.add_field(name="", value="기본적으로 커멘드의 작동 방법과 뭐를 하는지 알려줍니다")
    elif (categori=="독서") :
        embed=discord.Embed(title="독서 커멘드 사용 방법", description="/독서 [책 제목]")
        embed.add_field(name="", value="독서 커멘드는 책을 읽는 커멘드입니다, 주로 팁을 주거나 새로운 마법의 종류를 깨우칠 수 있습니다.\n또 도움을 대신하는 커멘드이기도 합니다")
    elif (categori=="마법_배우기") :
        embed=discord.Embed(title=f"마법 배우기 커멘드 사용 방법", description="/마법_배우기")
        embed.add_field(name="", value="마법 배우기 커멘드는 현재 시간과 시간표에 따라 배우는 마법이 달라지며 그를 배우는 커멘드입니다\n마법을 배울때는 컨디션이 `집중이 산만함`부터 배울수 있고, 더 좋아 질때 마다 더 높은 등급의 마법과 배울 확률이 늘어납니다")
    elif categori=="우트라" :
        embed = discord.Embed(title="우트라 (하급)", description=f"+ 상대방의 진실을 보았다!")
        embed.add_field(name=f"", value=f"`공격 : 0`\n`방어 : 10`\n`회복 : 0`\n`협상 : false`")
    embed.add_field(name="", value="{\}는 입력 사항 []는 \"\"를 포함한 문자열", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 독학(ctx, magic="NONE") :
    server = open("server.txt", 'r')
    surver = server.readlines()
    serverfile = []
    for line in surver :
        serverfile.append(str(line.strip()))
    server.close()
    if str(ctx.author) in serverfile :
        player = open(f"{str(ctx.author)}.txt", 'r')
        playerfile = player.readlines()
        player_info = []
        for line in playerfile :
            player_info.append(str(line.strip()))
        player.close()
        player.close()
        if magic == "NONE" :
            await ctx.send("배울 수 있는 마법 종류를 알기 위해서는 도감 명령어를 쓰세요")
        elif magic=="우트라" :
            now = time.localtime()
            date = int(time.strftime('%Y', now) + time.strftime('%m', now) + time.strftime('%d', now) + time.strftime('%H', now) + time.strftime('%M', now) + time.strftime('%S', now))
            if player_info[4][0] != '1' and int(player_info[12]) + 10 < date :
                persent = random.randint(1, 100)
                if (persent<=75) :
                    embed = discord.Embed(title = f"마법 : {magic}을 배웠습니다!", color=0x6cf542)
                    print(player_info[4][0])
                    player_info[4] = "1" + player_info[4][1] + player_info[4][2] + player_info[4][3]+ player_info[4][4]+ player_info[4][5]+ player_info[4][6]+ player_info[4][7]
                    print(player_info[4])
                else :    
                    embed = discord.Embed(title=f"마법 {magic}을 못 배웠습니다....", color=0x292929)
                    player.close()
                    player_info[12] = str(date)
                await ctx.send(embed=embed)
            else :
                if int(player_info[12]) + 10 > date :
                    await ctx.send("쿨타임을 돌고 있습니다")
                else :
                    await ctx.send("이미 이 마법을 배웠습니다!")
        elif magic=="테스트공격" :
            now = time.localtime()
            date = int(time.strftime('%Y', now) + time.strftime('%m', now) + time.strftime('%d', now) + time.strftime('%H', now) + time.strftime('%M', now) + time.strftime('%S', now))
            if player_info[4][1] != '1' and int(player_info[12]) + 10 < date :
                persent = random.randint(1, 100)
                if (persent<=65) :
                    embed = discord.Embed(title = f"마법 : {magic}을 배웠습니다!", color=0x6cf542)
                    print(player_info[4][0])
                    player_info[4] = player_info[4][0] + "1" + player_info[4][2] + player_info[4][3]+ player_info[4][4]+ player_info[4][5]+ player_info[4][6]+ player_info[4][7]
                    print(player_info[4])
                else :    
                    embed = discord.Embed(title=f"마법 {magic}을 못 배웠습니다....", color=0x292929)
                    player.close()
                    player_info[12] = str(date)
                await ctx.send(embed=embed)
            else :
                if int(player_info[12]) + 10 > date :
                    await ctx.send("쿨타임을 돌고 있습니다")
                else :
                    await ctx.send("이미 이 마법을 배웠습니다!")
        GF = open(f"{str(ctx.author)}.txt", 'w')
        for i in range(0, len(player_info) - 1):
            GF.write(str(player_info[i]))
            GF.write("\n")
        GF.write(str(player_info[len(player_info) - 1]))
        GF.write("\n")
        GF.close()
    else :
        await ctx.send("마법이 존재하는 지도 모르곘는데 뭘 배워;;")

@bot.command()
async def 도감(ctx, type="NONE") :
    if (type=="하급") :
        embed = discord.Embed(title=f"하급 마법 도감", description="")
        embed.add_field(name="", value="우트라")
    await ctx.send(embed=embed)

@bot.command()
async def 보강수업(ctx, CLASS="NONE") :
    if CLASS == "NONE" :
        await ctx.send("보강수업 리스트")
        await ctx.send("```diff\n아직 만들고 있는데요!```")

@bot.command()
async def 펫(ctx, type="NONE") :
    await ctx.send("아직 테스트용")
    await ctx.send("https://cdn.discordapp.com/attachments/1142471384027648000/1150717040382980116/image.png")
    await ctx.send("재밌는 사실 : 캐릭터를 그렸는 데 펫으로 어울려서 사용했다")
    await ctx.send("https://cdn.discordapp.com/attachments/1142471384027648000/1152411713254207612/the_emerald.png")
    if (type=="입양") :
        await ctx.send("```diff\n??? : 입양 하시게요? 입양을 할 것 이라면 다음을 주의 해주세요\n1번. 나는 얘를 끝까지 책임 질 것이다\n2번. 이를 어길시 벌금과 기분이 나빠질 것이다```")

bot.run('') # ephemeral=True 사용자만 보기