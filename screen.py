import pygame

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((600,700))
    pygame.display.set_caption('Simulação de caminhos')

    state = {
        'size': 4,
        'board': [[0 for _ in range(4)] for _ in range(4)]
    }

    return screen,state

def events(state):
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0]<100 and event.pos[1] < 50 and state['size'] < 10:
                state['size'] +=1
                state['board'] = [[0 for _ in range(state['size'])] for _ in range(state['size'])]
            if 200>event.pos[0]>100 and event.pos[1] < 50 and state['size'] > 4:
                state['size'] -=1
                state['board'] = [[0 for _ in range(state['size'])] for _ in range(state['size'])]
            for i in range(state['size']):
                for j in range(state['size']):
                    if i*600//state['size']+ 100 <event.pos[1] and event.pos[1] <(i+1)*600//state['size'] + 100 and j*600//state['size']<event.pos[0]<(j+1)*600//state['size']:
                        if state['board'][i][j] == 1:
                            state['board'][i][j] = 0
                        elif state['board'][i][j] == 0:
                            state['board'][i][j] = 1
            
    return game

def draw(window,state):
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,0),(0,0,100,50))
    pygame.draw.rect(window, (0,0,255),(100,0,100,50))
    for i in range(state['size']):
        for j in range(state['size']):
            if state['board'][i][j] == 0:
                pygame.draw.rect(window,(0,0,0),(600//state['size'] * j,100+600//state['size'] * i,600/state['size'],600/state['size']),1)
            elif state['board'][i][j] == 1:
                pygame.draw.rect(window,(0,0,0),(600//state['size'] * j,100+600//state['size'] * i,600/state['size'],600/state['size']))
    pygame.display.update()

def gameloop(window,state):
    while events(state):
        draw(window, state)

screen,state = initialize()
gameloop(screen,state)