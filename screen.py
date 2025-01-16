import pygame
from pathfinding_algorithms.astar import a_star

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((600,700))
    pygame.display.set_caption('Simulação de caminhos')

    state = {
        'size': 4,
        'board': [[0 for _ in range(4)] for _ in range(4)],
        'start-end':[],
        'path': []
    }

    return screen,state

def events(state):
    game = True
    print(state['path'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #Deal with left-click events
            if event.button == 1:
                #Deal with zoom in and out;
                if event.pos[0]<100 and event.pos[1] < 50 and state['size'] < 10:
                    state['size'] +=1
                    state['board'] = [[0 for _ in range(state['size'])] for _ in range(state['size'])]
                    state['start-end'] = []
                if 200>event.pos[0]>100 and event.pos[1] < 50 and state['size'] > 4:
                    state['size'] -=1
                    state['board'] = [[0 for _ in range(state['size'])] for _ in range(state['size'])]
                    state['start-end'] = []

                #Create Path
                if 600>event.pos[0]>500 and event.pos[1] < 50 and len(state['start-end'])==2:
                    state['path'] = a_star(state['board'], state['start-end'][0],state['start-end'][1])

                #Change board state
                for i in range(state['size']):
                    for j in range(state['size']):
                        if i*600//state['size']+ 100 <event.pos[1] and event.pos[1] <(i+1)*600//state['size'] + 100 and j*600//state['size']<event.pos[0]<(j+1)*600//state['size']:
                            if state['board'][i][j] == 1:
                                state['board'][i][j] = 0
                            elif state['board'][i][j] == 0:
                                state['board'][i][j] = 1

            #Deal with right-click events
            if event.button == 3:
                for i in range(state['size']):
                    for j in range(state['size']):
                        if i*600//state['size']+ 100 <event.pos[1] and event.pos[1] <(i+1)*600//state['size'] + 100 and j*600//state['size']<event.pos[0]<(j+1)*600//state['size']:
                            if state['board'][i][j] == 3 and (i,j) in state['start-end']:
                                state['board'][i][j] = 0
                                state['start-end'].remove((i,j))
                            elif state['board'][i][j] == 0 and len(state['start-end']) <2:
                                state['board'][i][j] = 3
                                state['start-end'].append((i,j))

    return game

def draw(window,state):
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,0),(0,0,100,50))
    pygame.draw.rect(window, (0,0,255),(100,0,100,50))
    pygame.draw.rect(window, (0,255,0),(500,0,100,50))
    for tile in state['path']:
        pygame.draw.rect(window,(255,0,0),(600//state['size'] * tile[1],100+600//state['size'] * tile[0],600/state['size'],600/state['size']))
    for i in range(state['size']):
        for j in range(state['size']):

            if state['board'][i][j] == 0:
                pygame.draw.rect(window,(0,0,0),(600//state['size'] * j,100+600//state['size'] * i,600/state['size'],600/state['size']),1)
            elif state['board'][i][j] == 1:
                pygame.draw.rect(window,(0,0,0),(600//state['size'] * j,100+600//state['size'] * i,600/state['size'],600/state['size']))
            elif state['board'][i][j] == 3:
                pygame.draw.rect(window,(0,255,0),(600//state['size'] * j,100+600//state['size'] * i,600/state['size'],600/state['size']))
    pygame.display.update()

def gameloop(window,state):
    while events(state):
        draw(window, state)

screen,state = initialize()
gameloop(screen,state)