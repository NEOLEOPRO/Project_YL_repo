# пихаешь это в код
def draw_trap():
    global k
    im1 = pygame.image.load('ловушка1.png')
    im0 = pygame.image.load('ловушка0.png')
    f = pygame.image.load('огонь.png')
    if int(str(k)[-2::]) < 50:
        screen.blit(im0, (100, 100))
    else:
        screen.blit(im1, (100, 100))
        screen.blit(f, (200, 200))
    print(int(str(k)[-2::]))
    k += 1


# в основном цикле просто дописываешь:
draw_trap()
