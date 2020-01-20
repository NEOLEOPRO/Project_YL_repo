import pygame
import os


LABELS = ['Название', 'Новая игра', 'Продолжить', 'Достижения', 'Настройки', 'Выход']
Frases = ['Никто из нас уже не сможет сказать, как выглядят трава, деревья и реки.',
          'Раньше эти края были прекрасной зелёной долиной, в которой все жили в радости и достатке',
          '*Показываем картинку деревни*',
          'Но всё изменилось, когда один из нас, возомнивший себя всемогущим, назвал себя Повелителем этого мира и бросил вызов Титанам',
          'Он явно переоценил свои силы и за его надменность поплатились все мы...',
          '*Показываем картину пустоши, выжженной земли, разорённой деревни и тд*',
          'Звали его ..... (Надо придумать). После его поединка с Титанами никто из нашего племени больше не видел его, ',
          'Скорее всего его заточили в ... - тюрьму, откуда нет выхода. Ах, да. Забыл представиться.',
          'Меня зовут ... (Тут вылазит окно, пользователь вводит имя персонажа)',
          'Я его сын. (Вот это поворот)',
          'И я во что бы то ни стало должен найти своего отца и с его помощью восстановить мир в наших землях.',
          'Для этого мне нужно спуститься в подземелья ... и освободить его, чтобы после с его помощью выкрасть у Титанов',
          '... - древний, могущественный артефакт, дарующий владельцу власть над всем/всей ... (Название мира)',
          'Итак, да начнётся приключение.',
          '*Показываем вход в ту тюрьму, перс заходит в неё*']

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((1000, 600), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('Super Game')

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def music(name):
    fullname = os.path.join('data', name)
    if name[-3:] == 'mp3':
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play()
    elif name[-3:] == 'ogg' or name[-3:] == 'wav':
        return pygame.mixer.Sound(fullname)
    else:
        print('error sound')

def static_labels():
    font = pygame.font.Font(None, 25)
    screen.blit(font.render(LABELS[0], 1, (255, 255, 255), (0, 0, 0)), (450, 100))
    pygame.draw.rect(screen, (123, 0, 123), (435, 90, 150, 30), 1)
    screen.blit(font.render(LABELS[1], 1, (255, 255, 255), (0, 0, 0)), (100 + xl, 150 + yl))
    pygame.draw.rect(screen, (123, 0, 123), (90 + xl, 140 + yl, 130, 30), 1)
    if save:
        pass
    else:
        screen.blit(font.render(LABELS[2], 1, (100, 100, 100), (0, 0, 0)), (100 + xl, 200 + yl))
        pygame.draw.rect(screen, (123, 0, 123), (90 + xl, 190 + yl, 130, 30), 1)
    screen.blit(font.render(LABELS[3], 1, (255, 255, 255), (0, 0, 0)), (100 + xl, 250 + yl))
    pygame.draw.rect(screen, (123, 0, 123), (90 + xl, 240 + yl, 130, 30), 1)
    screen.blit(font.render(LABELS[4], 1, (255, 255, 255), (0, 0, 0)), (100 + xl, 300 + yl))
    pygame.draw.rect(screen, (123, 0, 123), (90 + xl, 290 + yl, 130, 30), 1)
    screen.blit(font.render(LABELS[5], 1, (255, 255, 255), (0, 0, 0)), (100 + xl, 350 + yl))
    pygame.draw.rect(screen, (123, 0, 123), (90 + xl, 340 + yl, 130, 30), 1)

K = -1
xl, yl = 0, 50
save = False
Flag = False
dialog = False
gamerun = True
menu = True
music('TownTheme.mp3')
while gamerun:
    if dialog:
        menu = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamerun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Flag == False and K < 14:
                        K += 1
                        Flag = True
                    elif Flag == True and K < 14:
                        K += 1
                    else:
                        Flag = False
                        K = -1
        screen.fill((10, 10, 10))
        if Flag:
            if K not in [2, 5]:
                screen.blit(pygame.font.Font(None, 18).render(Frases[K], 1, (255, 0, 0), (0, 0, 0)), (0, 401))
            elif K == 2:
                screen.blit(pygame.font.Font(None, 18).render(Frases[K], 1, (255, 0, 0), (0, 0, 0)), (0, 401))
            elif K == 5:
                pass
        pygame.draw.line(screen, (123, 0, 123), [0, 400], [1000, 400], 1)
        pygame.display.flip()
    elif menu:
        screen.fill((10, 10, 10))
        static_labels()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamerun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if event.button == 1 and (90 < (x - xl) < 220) and (140 < (y - yl) < 170):
                    dialog = True
                if event.button == 1 and (90 < (x - xl) < 220) and (340 < (y - yl) < 370):
                    gamerun = False
    pygame.display.update()
pygame.quit()
