import math,sys,numpy,pygame,time,random
from pygame.locals import KEYDOWN,MOUSEBUTTONDOWN,QUIT
import fileUpload
class player:
    def play(screen,filename,start=0):
        #variables

        pygame.init()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Consolas', 30)
        k = -3 * math.pi
        fl = 0
        stage = fileUpload.File.Load(filename)
        BPM = float(stage['setting']['bpm'])
        ln = len(stage['notes'])
        dir = 1
        FPS = 60
        tiles_ang = [(i['angle'] - 180) * math.pi / 180 for i in stage['notes']]
        default_ang = 0
        Judgment = font.render('', True, (0, 0, 255))
        fontp = 400
        dir_change = [i['dirchange'] for i in stage['notes']]
        dir_change.append(0)
        bpm_change = [i['bpmchange'] for i in stage['notes']]
        bpm_change.append(0)
        chkptlst = [i['chkpoint'] for i in stage['notes']]
        img = pygame.image.load(stage['setting']['background'])
        img = pygame.transform.scale(img,(800,600))
        ingame_default_ang = 0
        nearest_chkpt=start
        overload_bar=0
        dirchange_icon = pygame.image.load('dirchange.png')
        dirchange_icon = pygame.transform.scale(dirchange_icon,(40,40))
        rabbit = pygame.image.load('rabbit.png')
        rabbit = pygame.transform.scale(rabbit,(40,24))
        snail = pygame.image.load('snail.png')
        snail = pygame.transform.scale(snail,(40,24))
        chkpoint = pygame.image.load('chkpoint.png')
        visual_k = -3 * math.pi
        for i in range(0,start):
            default_ang += tiles_ang[i]
            ingame_default_ang += tiles_ang[i] * dir
            if dir_change[i + 1]:
                if dir == 1:
                    dir = -1
                else:
                    dir = 1
            fl = 0 if fl == 1 else 1
        k += ingame_default_ang


        #draw

        screen.blit(img,(0,0))
        ang = default_ang
        px = 400 - 25 * numpy.sin(ang) - 35 * numpy.cos(ang)
        py = 300 + 25 * numpy.cos(ang) - 35 * numpy.sin(ang)
        bpm_count = BPM
        for j in range(start,ln):
            i = tiles_ang[j]
            pygame.draw.polygon(screen, (stage['notes'][j]['color']/1000000, stage['notes'][j]['color']/1000%1000, stage['notes'][j]['color']%1000),
                                [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                 (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
            ang += i
            pygame.draw.circle(screen, (stage['notes'][j]['color']/1000000, stage['notes'][j]['color']/1000%1000, stage['notes'][j]['color']%1000), (px + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i),
                                                         py - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i)),
                               25)
            px += 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(math.pi / 2 - ang)
            py += -25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(math.pi / 2 - ang)
            pygame.draw.polygon(screen, (stage['notes'][j]['color']/1000000, stage['notes'][j]['color']/1000%1000, stage['notes'][j]['color']%1000),
                                [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                 (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
            if bpm_change[j]:
                if bpm_change[j] < bpm_count:
                    screen.blit(snail, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                                         py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) - 12))
                if bpm_change[j] > bpm_count:
                    screen.blit(rabbit, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                        math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                        py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                            math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                            ang - i) - 12))
                bpm_count = bpm_change[j]
            if dir_change[j]:
                screen.blit(dirchange_icon, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                    math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                    py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                        math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) - 20))
            if chkptlst[j]:
                screen.blit(chkpoint, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                    math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                    py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                        math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) - 20))
            px += 40 * numpy.cos(ang)
            py += 40 * numpy.sin(ang)

        Judgment = font.render("Press Any Key to Start", True, (255, 255, 255))
        fontp = 117.5 * 2
        if fl == 0:
            pygame.draw.circle(screen, "blue", (400, 300), 20)
        else:
            pygame.draw.circle(screen, "red", (400, 300), 20)
        screen.blit(Judgment, (fontp, 240))
        pygame.display.update()
        time.sleep(1)


        #wait

        while (1):
            fl_ = 0
            for event in pygame.event.get():
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    fl_ = 1
            if fl_ == 1:
                break


        #in-game

        music_on = False
        play_idx = start
        while True:
            clock.tick(FPS)
            screen.blit(img,(0,0))
            if play_idx == start:
                if k > -2 * math.pi and k < -1 * math.pi:
                    Judgment = font.render("3", True, (255, 255, 255))
                    fontp = 196.25 * 2
                elif k > -1 * math.pi and k < 0:
                    Judgment = font.render("2", True, (255, 255, 255))
                    fontp = 196.25 * 2
                elif k > 0 and k < 1 * math.pi:
                    Judgment = font.render("1", True, (255, 255, 255))
                    fontp = 196.25 * 2
                elif k > 1 * math.pi and k < 2 * math.pi:
                    Judgment = font.render("Start!", True, (255, 255, 255))
                    fontp = 177.5 * 2
            for event in pygame.event.get():
                # quit
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # judgment
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    if play_idx == ln-1:
                        pygame.mixer.music.stop()
                        return
                    elif play_idx == start and k < math.pi:
                        print("Not Started Yet!")
                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 14.5:
                        print("Late!!")
                        Judgment = font.render("Late!!", True, (255, 0, 0))
                        fontp = 177.5*2
                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 13.5:
                        print("Late!")
                        Judgment = font.render("Late!", True, (255, 128, 0))
                        fontp = 181.25*2
                        fl = 0 if fl == 1 else 1
                        k -= math.pi
                        visual_k -= math.pi*dir
                        default_ang += tiles_ang[play_idx]
                        ingame_default_ang += tiles_ang[play_idx] * dir
                        if dir_change[play_idx+1]:
                            if dir == 1:
                                dir = -1
                            else:
                                dir = 1
                        if bpm_change[play_idx+1]:
                            BPM = bpm_change[play_idx+1]
                        overload_bar -= 2.5
                        if overload_bar < 0:
                            overload_bar = 0
                        play_idx += 1
                        if chkptlst[play_idx]:
                            nearest_chkpt = play_idx
                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 12.5:
                        print("LPerfect!")
                        Judgment = font.render("LPerfect!", True, (100, 205, 50))
                        fontp = 166.25*2
                        fl = 0 if fl == 1 else 1
                        k -= math.pi
                        visual_k -= math.pi*dir
                        default_ang += tiles_ang[play_idx]
                        ingame_default_ang += tiles_ang[play_idx] * dir
                        if dir_change[play_idx+1]:
                            if dir == 1:
                                dir = -1
                            else:
                                dir = 1
                        if bpm_change[play_idx+1]:
                            BPM = bpm_change[play_idx+1]
                        overload_bar -= 2.5
                        if overload_bar < 0:
                            overload_bar = 0
                        play_idx += 1
                        if chkptlst[play_idx]:
                            nearest_chkpt = play_idx

                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 11.5:
                        print("Perfect!")
                        Judgment = font.render("Perfect!", True, (50, 205, 50))
                        fontp = 170*2
                        fl = 0 if fl == 1 else 1
                        k -= math.pi
                        visual_k -= math.pi*dir
                        default_ang += tiles_ang[play_idx]
                        ingame_default_ang += tiles_ang[play_idx] * dir
                        if dir_change[play_idx+1]:
                            if dir == 1:
                                dir = -1
                            else:
                                dir = 1
                        if bpm_change[play_idx+1]:
                            BPM = bpm_change[play_idx+1]
                        overload_bar -= 5
                        if overload_bar < 0:
                            overload_bar = 0
                        play_idx += 1
                        if chkptlst[play_idx]:
                            nearest_chkpt = play_idx

                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 10.5:
                        print("EPerfect!")
                        Judgment = font.render("EPerfect!", True, (100, 205, 50))
                        fontp = 166.25*2
                        fl = 0 if fl == 1 else 1
                        k -= math.pi
                        visual_k -= math.pi*dir
                        default_ang += tiles_ang[play_idx]
                        ingame_default_ang += tiles_ang[play_idx] * dir
                        if dir_change[play_idx+1]:
                            if dir == 1:
                                dir = -1
                            else:
                                dir = 1
                        if bpm_change[play_idx+1]:
                            BPM = bpm_change[play_idx+1]
                        overload_bar -= 2.5
                        if overload_bar < 0:
                            overload_bar = 0
                        play_idx += 1
                        if chkptlst[play_idx]:
                            nearest_chkpt = play_idx
                    elif k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 9.5:
                        print("Early!")
                        Judgment = font.render("Early!", True, (255, 128, 0))
                        fontp = 177.5*2
                        fl = 0 if fl == 1 else 1
                        k -= math.pi
                        visual_k -= math.pi*dir
                        default_ang += tiles_ang[play_idx]
                        ingame_default_ang += tiles_ang[play_idx] * dir
                        if dir_change[play_idx+1]:
                            if dir == 1:
                                dir = -1
                            else:
                                dir = 1
                        if bpm_change[play_idx+1]:
                            BPM = bpm_change[play_idx+1]
                        overload_bar -= 2.5
                        if overload_bar < 0:
                            overload_bar = 0
                        play_idx += 1
                        if chkptlst[play_idx]:
                            nearest_chkpt = play_idx
                    else:
                        print("Early!!")
                        fontp = 173.75*2
                        Judgment = font.render("Early!!", True, (255, 0, 0))
                        overload_bar += 25
                        if overload_bar >= 100:
                            ang = default_ang
                            px = 400 - 25 * numpy.sin(ang) - 35 * numpy.cos(ang)
                            py = 300 + 25 * numpy.cos(ang) - 35 * numpy.sin(ang)
                            bpm_count = BPM
                            for j in range(play_idx, ln):
                                i = tiles_ang[j]
                                pygame.draw.polygon(screen, (
                                    stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                                    stage['notes'][j]['color'] % 1000),
                                                    [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                                        px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                                        py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                                     (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                                ang += i
                                pygame.draw.circle(screen, (
                                    stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                                    stage['notes'][j]['color'] % 1000),
                                                   (px + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i),
                                                    py - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i)),
                                                   25)
                                px += 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                    math.pi / 2 - ang)
                                py += -25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                    math.pi / 2 - ang)
                                pygame.draw.polygon(screen, (
                                    stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                                    stage['notes'][j]['color'] % 1000),
                                                    [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                                        px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                                        py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                                     (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                                if bpm_change[j]:
                                    if bpm_change[j] < bpm_count:
                                        screen.blit(snail, (px - (
                                                25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                            math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                            ang - i) - 20,
                                                            py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                                ang - i) + 25 * numpy.sin(
                                                                math.pi / 2 - ang)) - 25 * numpy.cos(
                                                                ang - i) + 35 * numpy.sin(ang - i) - 12))
                                    if bpm_change[j] > bpm_count:
                                        screen.blit(rabbit,
                                                    (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                                        ang - i) - 25 * numpy.cos(
                                                        math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                                        ang - i) - 20,
                                                     py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                         ang - i) + 25 * numpy.sin(
                                                         math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                         ang - i) - 12))
                                    bpm_count = bpm_change[j]
                                if dir_change[j]:
                                    screen.blit(dirchange_icon,
                                                (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                                    ang - i) - 25 * numpy.cos(
                                                    math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                                    ang - i) - 20,
                                                 py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                     ang - i) + 25 * numpy.sin(
                                                     math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                     ang - i) - 20))
                                if chkptlst[j]:
                                    screen.blit(chkpoint, (
                                    px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                        math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                    py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                        math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) - 20))
                                px += 40 * numpy.cos(ang)
                                py += 40 * numpy.sin(ang)
                            if fl == 0:
                                pygame.draw.circle(screen, "blue", (400, 300), 20)
                            else:
                                pygame.draw.circle(screen, "red", (400, 300), 20)
                            fontp = 155 * 2
                            Judgment = font.render("Overloaded!!", True, (194, 12, 176))
                            screen.blit(Judgment, (fontp, 240))
                            pygame.display.update()
                            pygame.mixer.music.stop()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                                        player.play(screen, filename, nearest_chkpt)
                                        return

            # music
            if k > math.pi * 2 - play_idx * math.pi and music_on == False:
                pygame.mixer.music.load(stage['setting']['music'])
                pygame.mixer.music.play()
                music_on = True

            # kill
            if k > ingame_default_ang + tiles_ang[play_idx] * dir + math.pi / 6 * 18:
                if not play_idx == ln-1:
                    ang = default_ang
                    px = 400 - 25 * numpy.sin(ang) - 35 * numpy.cos(ang)
                    py = 300 + 25 * numpy.cos(ang) - 35 * numpy.sin(ang)
                    bpm_count=BPM
                    for j in range(play_idx, ln):
                        i = tiles_ang[j]
                        pygame.draw.polygon(screen, (
                        stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                        stage['notes'][j]['color'] % 1000),
                                            [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                                px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                                py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                             (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                        ang += i
                        pygame.draw.circle(screen, (
                        stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                        stage['notes'][j]['color'] % 1000), (px + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i),
                                                             py - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i)),
                                           25)
                        px += 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(math.pi / 2 - ang)
                        py += -25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(math.pi / 2 - ang)
                        pygame.draw.polygon(screen, (
                        stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                        stage['notes'][j]['color'] % 1000),
                                            [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                                px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                                py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                             (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                        if bpm_change[j]:
                            if bpm_change[j] < bpm_count:
                                screen.blit(snail, (px - (
                                            25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                        math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                                    py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                        ang - i) + 25 * numpy.sin(math.pi / 2 - ang)) - 25 * numpy.cos(
                                                        ang - i) + 35 * numpy.sin(ang - i) - 12))
                            if bpm_change[j] > bpm_count:
                                screen.blit(rabbit,
                                            (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                                math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                                ang - i) - 20,
                                             py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                                 math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                 ang - i) - 12))
                            bpm_count = bpm_change[j]
                        if dir_change[j]:
                            screen.blit(dirchange_icon,
                                        (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                            math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                            ang - i) - 20,
                                         py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                             math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                             ang - i) - 20))
                        if chkptlst[j]:
                            screen.blit(chkpoint,
                                        (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                            math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(
                                            ang - i) - 20,
                                         py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                             math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                             ang - i) - 20))
                        px += 40 * numpy.cos(ang)
                        py += 40 * numpy.sin(ang)
                    if fl == 0 :
                        pygame.draw.circle(screen, "blue", (400, 300), 20)
                    else:
                        pygame.draw.circle(screen, "red", (400, 300), 20)
                    fontp = 177.5*2
                    Judgment = font.render("Miss!!", True, (194, 12, 176))
                    screen.blit(Judgment, (fontp, 240))
                    pygame.display.update()
                    pygame.mixer.music.stop()
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                                player.play(screen, filename, nearest_chkpt)
                                return


            # draw
            ang = default_ang
            px = 400 - 25 * numpy.sin(ang) - 35 * numpy.cos(ang)
            py = 300 + 25 * numpy.cos(ang) - 35 * numpy.sin(ang)
            bpm_count=BPM
            for j in range(play_idx, ln):
                i = tiles_ang[j]
                pygame.draw.polygon(screen, (
                stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                stage['notes'][j]['color'] % 1000),
                                    [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                        px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                        py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                     (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                ang += i
                pygame.draw.circle(screen, (
                stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                stage['notes'][j]['color'] % 1000), (px + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i),
                                                     py - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i)),
                                   25)
                px += 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(math.pi / 2 - ang)
                py += -25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(math.pi / 2 - ang)
                pygame.draw.polygon(screen, (
                stage['notes'][j]['color'] / 1000000, stage['notes'][j]['color'] / 1000 % 1000,
                stage['notes'][j]['color'] % 1000),
                                    [(px, py), (px + 35 * numpy.cos(ang), py + 35 * numpy.sin(ang)), (
                                        px + 35 * numpy.cos(ang) + 50 * numpy.sin(ang),
                                        py + 35 * numpy.sin(ang) - 50 * numpy.cos(ang)),
                                     (px + 50 * numpy.sin(ang), py - 50 * numpy.cos(ang))])
                if bpm_change[j]:
                    if bpm_change[j] < bpm_count:
                        screen.blit(snail, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                            math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                            py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                                math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                ang - i) - 12))
                    if bpm_change[j] > bpm_count:
                        screen.blit(rabbit, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                            math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                            py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                                math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                                ang - i) - 12))
                    bpm_count = bpm_change[j]
                if dir_change[j]:
                    screen.blit(dirchange_icon,
                                (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                                    math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                 py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                     math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) - 20))
                if chkptlst[j]:
                    screen.blit(chkpoint, (px - (25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 25 * numpy.cos(
                        math.pi / 2 - ang)) + 25 * numpy.sin(ang - i) + 35 * numpy.cos(ang - i) - 20,
                                           py - (-25 * numpy.cos(ang - i) + 35 * numpy.sin(ang - i) + 25 * numpy.sin(
                                               math.pi / 2 - ang)) - 25 * numpy.cos(ang - i) + 35 * numpy.sin(
                                               ang - i) - 20))
                px += 40 * numpy.cos(ang)
                py += 40 * numpy.sin(ang)

            # move
            if (fl == 0):
                pygame.draw.circle(screen, "red", (400 + 80 * numpy.cos(visual_k), 300 + 80 * numpy.sin(visual_k)), 20)
                pygame.draw.circle(screen, "blue", (400, 300), 20)
                k += math.pi / 3600 * BPM
                visual_k += math.pi / 3600 * BPM * dir
            if (fl == 1):
                pygame.draw.circle(screen, "blue", (400 + 80 * numpy.cos(visual_k), 300 + 80 * numpy.sin(visual_k)), 20)
                pygame.draw.circle(screen, "red", (400, 300), 20)
                k += math.pi / 3600 * BPM
                visual_k += math.pi / 3600 * BPM * dir
            screen.blit(Judgment, (fontp, 240))
            pygame.display.update()
