#__________________##______________________#

# Game Squad 5
# Grupo 5
# Caio Correa Monteiro
# Derildo dos Santos Pessoa Junior
# Luigi Calderan Tineli
# Marco Antonio Alonso


# ----- Importação de Bibliotecas ----- #

import pygame
from pygame.locals import *
from random import randint

                # ____________________ Dados ____________________ #

# ----- Geral ----- #

jogo = 0 # 0 = menu / 1 = jogo / 2 = game over / 3 = venceu / 4 = animação final
AreaGraf = (800,600)
pygame.init()
tela = pygame.display.set_mode(AreaGraf, 0, 32)
pygame.display.set_caption('Squad 5')
clock = pygame.time.Clock() # clock para controlar fps
clock2 = 20 # controla a pausa antes da animação final
anif = 1 # controle da animação final

# ----- Som ----- #

pygame.mixer.music.load(r'art/som/alienblues.wav')
som_bg = 0
som_tiro = pygame.mixer.Sound(r'art/som/shot.wav')
som_exp = pygame.mixer.Sound(r'art/som/explosao.wav')
som_ast = pygame.mixer.Sound(r'art/som/asteroid.wav')

# ----- Menu ----- #

menu = pygame.image.load(r'art/menu2.png')

# ----- Game Over ----- #

gameover = pygame.image.load(r'art/game_over.png')

# ----- Vitória ----- #

venceu = pygame.image.load(r'art/venceu.png')

# ----- Asteroid (_ast)----- #

asteroid = [] # armazena todos os asteriods criados 
num_ast = [] # armazena cada um dos 4 frames diferentes do asteroid
dat_ast = [0,0,0,0,0]# armazena os dados de um asteroid / [0]frame do asteroid / [1]posição X / [2]posição Y / [3]velocidade / [4]colisão
cont_ast = 25 # contador para criar asteroids
passo_ast = 7 # velocidade inicial de movimento
X_ast = 850 # posição inicial de X
Y_ast = randint(0, 565) # posição aleatória de Y
N_ast = 1 # variavel para controlar o numero do frame
while N_ast <= 4: # laço para carregar os frames 
    img_ast = pygame.image.load(r'art/frame pequeno/meteoro{}.png'.format(N_ast))
    num_ast.append(img_ast)
    N_ast = N_ast + 1

# ----- avoider - nave (_avo)----- #

avoider = [] # armazaneda todos os frames individualmente
ani_avo = 0 # controla os frames da animação
passo_ani_avo = 0.3 # controla a velocidade de animação
passo_avo = 7 # velocidade de movimento
X_avo = 100 # posição X inicial da nave
Y_avo = 300 # posição Y inicial da nave
N_avo = 1 # variavel para controlar o numero do frame
while N_avo <= 8: # laço para carregar os frames
    img_avo = pygame.image.load(r'art/frame pequeno/nave_cinza_vinho_v6_f{}.png'.format(N_avo))
    avoider.append(img_avo)
    N_avo = N_avo + 1

# ----- explorer - nave (_xpr)----- #

X_xpr = 801 # posição X inicial da explorer
Y_xpr = 200 # posição Y inicial da explorer
passo_xpr = 5 # velocidade de movimento
explorer = pygame.image.load(r'art/frame pequeno/explorer_teste.png')

# ----- explosão (_exp)----- #

explosao = [] # armazena todos os frames individualmente
ani_exp = 0 # controla o frame de animação
passo_ani_exp = 0.3 # controla a velocidade da animação
N_exp = 1 # variavel para controlar o numero do frame
while N_exp <= 13: # laço para carregar os frames
    img_exp = pygame.image.load(r'art/frame pequeno/teste_explosao_f{}.png'.format(N_exp))
    img_exp2 = pygame.transform.scale2x(img_exp)
    explosao.append(img_exp2)
    N_exp = N_exp + 1

# ----- tiro (_tiro)----- #

dat_tiro = [0,0,0] # grava a posição inicial do tiro e a colisão [0] posição X / [1] posição Y / [2] colisão
tiro = [] # grava dados de cada tiro separadamente
passo_tiro = 10 # velocidade do tiro
cont_tiro = 5 # contador para limitar a quantidade de tiro
img_tiro = pygame.image.load(r'art/frame pequeno/tiro.png')

# ----- Background (_BG) ----- #

BG_1 = pygame.image.load(r'art/BG_1.png')
BG_2 = pygame.image.load(r'art/BG_2.png')
BG_3 = pygame.image.load(r'art/BG_3.png')
BG_4 = pygame.image.load(r'art/BG_4.png')
passo_BG = 0.6 # velocidade do background
X_BG_1 = 0 # posição da primeira parte do background
X_BG_2 = 801 # posição da segunda parte do background
X_BG_3 = 1601 # posição da terceira parte do background
X_BG_4 = 2401 # posição da quarta parte do background

# ----- Background parallax 1 (_BG_p1) ----- #

BG_p1 = pygame.image.load(r'art/BG_paralax1.png')
BG_p1_1 = BG_p1 # cria uma cópia do background parallax 1
X_BG_p1 = 0 # posição inicial do background parallax 1
X_BG_p1_1 = 1601 #posição inicial da cópia do background parallax 1
passo_BG_p1 = 1.1 # velocidade do background parallax 1

# ----- Background parallax 2 (_BG_p2) ----- #

BG_p2 = pygame.image.load(r'art/BG_paralax2.png')
BG_p2_1 = BG_p2 # cria uma cópia do background parallax 2
X_BG_p2 = 0 # posição inicial do background parallax 2
X_BG_p2_1 = 1601 # posição inicial da cópia do background parallax 2
passo_BG_p2 = 1.6 # velocidade do background parallax 2

# ----- Planetas (_P_)----- #

P_1 = pygame.image.load(r'art/frame pequeno/planeta1.png')
passo_P_1 = 0.6 # velocidade inicial do planeta 1 para acompanhar o BG
X_P_1 = 3150 # posição inicial do planeta 1
P_2 = pygame.image.load(r'art/frame pequeno/planeta2.png')
passo_P_2 = 0.6 # velocidade inicial do planeta 2 para acompanhar o BG
X_P_2 = 3050 # posição inicial do planeta 1
P_3 = pygame.image.load(r'art/frame pequeno/planeta3.png')
passo_P_3 = 0.6 # velocidade inicial do planeta 3 para acompanhar o BG
X_P_3 = 2200 # posição inicial do planeta 1
P_4 = pygame.image.load(r'art/frame pequeno/planeta4.png')
passo_P_4 = 0.6 # velocidade inicial do planeta 4 para acompanhar o BG
X_P_4 = 1500 # posição inicial do planeta 1
    
                  # ____________________ Loop Principal ____________________ #

fim = False
while not fim:          
    tela.fill((150, 150, 255))

                   # ____________________ Desenhando ____________________ #
                   
    # __________ menu __________ #
    
    if jogo == 0: #desenha o menu
        tela.blit(menu, (0,0))
        
    # _________ jogo __________ #
    
    if jogo >= 1: #desenha os elementos do jogo
        if som_bg == 1:
            pygame.mixer.music.play(-1) # inicia a musica
            som_bg = 2
            
        # ----- background ----- #
        if X_BG_1 >= -800:
            tela.blit(BG_1, (X_BG_1, 0))
        if X_BG_2 >= -800:
            tela.blit(BG_2, (X_BG_2, 0))
        if X_BG_2 <= 1 and X_BG_3 >= -801:
            tela.blit(BG_3, (X_BG_3, 0))
        if X_BG_3 <= 1 and X_BG_4 >= -1670:
            tela.blit(BG_4, (X_BG_4, 0))

        # ----- planetas ----- #
        if X_P_1 <=801:
            tela.blit(P_1, (X_P_1, 30))
        if X_P_2 <=801:
            tela.blit(P_2, (X_P_2, 350))
        if X_P_3 <=801:
            tela.blit(P_3, (X_P_3, 350))
        if X_P_4 <=801:
            tela.blit(P_4, (X_P_4, 480))
        
        # ----- background parallax 1 -----#
        if X_BG_p1 > -1600:
            tela.blit(BG_p1, (X_BG_p1, 0))
        if X_BG_p1 < -800 or X_BG_p1 > 0:
            tela.blit(BG_p1_1, (X_BG_p1_1, 0))
        if X_BG_p1_1 < -800 or X_BG_p1_1 > 0:
            tela.blit(BG_p1, (X_BG_p1, 0))
       
        # ----- avoider - nave ----- #
        if jogo == 1 or jogo > 2:
            tela.blit(avoider[int(ani_avo)], (X_avo, Y_avo))
        
        # ----- tiro ----- #
        for t in tiro: # desenha um tiro para cada indice da lista principal
            tela.blit(img_tiro, (t[0],t[1]))

        # ----- explorer - nave ----- #
        if jogo > 2: # desenha a explorer apenas no final da tela
            tela.blit(explorer, (X_xpr, Y_xpr))

        # ----- asteroid ----- #
        cont_ast = cont_ast - 1 # controla o tempo que cada asteroid nasce
        if cont_ast < 0: # quando o contador chega a 0 são criados dados para um novo asteroid
            f_ast = randint(0,3) # numero aleatório do frame do asteroid criado
            Y_ast = randint(0, 565) # posição Y aleatória do asteroid criado
            if X_BG_4 > 1685: # dificuldade inicial
                passo_ast = randint(6, 8) # velocidade inicial 
            if X_BG_4 <= 1685: # dificuldade 3
                passo_ast = randint(9, 11) # aumenta a velocidade
            if X_BG_4 <= 970: # dificuldade 5
                passo_ast = randint(12, 14) # aumenta a velocidade
            if X_BG_4 <= 255: # dificuldade 7
                passo_ast = randint(15, 17) # aumenta a velocidade
            if X_BG_4 <= -300: # final da tela
                passo_ast = 0 # zera a velocidade
            dat_ast[0] = num_ast[f_ast] # armazena o frame do asteroid criado
            dat_ast[1] = X_ast # armazena a posição X do asteroid criado
            dat_ast[2] = Y_ast # armazena a posição Y do asteroid criado
            dat_ast[3] = passo_ast # armazena a velocidade do asteroid criado
            dat_ast2 = dat_ast[:] # clona a lista dat_ast
            asteroid.append(dat_ast2) # adiciona os dados da lista dat_ast2 na lista principal de asteroids
            if X_BG_4 > 2045: # dificuldade inicial
                cont_ast = 50 # retorna o contador para o numero inicial
            if X_BG_4 <= 2045: # dificuldade 2
                cont_ast = 30 # diminui o contador
            if X_BG_4 <= 1325: # dificuldade 4
                cont_ast = 15 # diminui o contador
            if X_BG_4 <= 615: # dificuldade 6
                cont_ast = 10 # diminui o contador
            if X_BG_4 <= -100: # dificuldade 8
                cont_ast = 5 # diminui o contador
            if X_BG_4 <= -300: # final da tela
                cont_ast = 1000000 # para a criação de asteroids
            
        
        for a in asteroid: # desenha um asteroid para cada indice da lista geral de asteroids
            tela.blit(a[0], (a[1], a[2]))

        # ----- background parallax 2 ----- #
        if X_BG_p2 > -1600:
            tela.blit(BG_p2, (X_BG_p2, 0))
        if X_BG_p2 < -800 or X_BG_p2 > 0:
            tela.blit(BG_p2_1, (X_BG_p2_1, 0))
        if X_BG_p2_1 < -800 or X_BG_p2_1 > 0:
            tela.blit(BG_p2, (X_BG_p2, 0))

    # __________ game over __________ #
    
    if jogo == 2: # game over
       
        # ----- explosão ----- #
        if ani_exp <= 12: # controla a animação da explosao
            tela.blit(explosao[int(ani_exp)], (X_avo, Y_avo-51))

        # ----- game over ----- #
        if ani_exp > 12: # condição para desenhar o game over
            tela.blit(gameover, (263, 196))

    # __________ venceu __________ #
    
    if jogo == 4: # venceu
        if X_xpr > 810: # condição para desenhar a mensagem de vitoria
            tela.blit(venceu, (224, 155))
        
    
    pygame.display.update()

                    # ____________________ atualizando posições ____________________ #
          
    if jogo >= 1: #atualiza os elementos do jogo
        
        # ----- animação avoider ----- #
        ani_avo = ani_avo + passo_ani_avo #anima a avoider
        if ani_avo > 7: # a animação possui 8 frames  
            ani_avo = 0 # quando ani_avo chega a 7 ela é zerada

         # ----- animação parallax 1 -----#
        X_BG_p1 = X_BG_p1 - passo_BG_p1
        if X_BG_p1 <= -1600:
            X_BG_p1 = 1601
            
        X_BG_p1_1 = X_BG_p1_1 - passo_BG_p1
        if X_BG_p1_1 <= -1601:
            X_BG_p1_1 = 1601

        # ----- animação parallax 2 -----#    
        X_BG_p2 = X_BG_p2 - passo_BG_p2
        if X_BG_p2 <= -1601:
            X_BG_p2 = 1601
            
        X_BG_p2_1 = X_BG_p2_1 - passo_BG_p2
        if X_BG_p2_1 <= -1601:
            X_BG_p2_1 = 1601

        # ----- animação tiro ----- #
        for t in tiro:             
            if t[2] != 0 or t[0] > 800: # remove os tiros que colidiram ou sairam da tela grafica
                tiro.remove(t)
            t[0] = t[0] + passo_tiro # movimenta o tiro
        if cont_tiro < 10: # controla o contador de tiro
            cont_tiro = cont_tiro + 1
            
        if jogo < 3: # atualiza apenas se não for fim de jogo
            
            # ---- animação asteroid ---- #
            for a in asteroid:
                if a[1] < -200 or a[4] != 0: # remove os asteroids que não estão na tela grafica ou colidiram
                    asteroid.remove(a)
                a[1] = a[1] - a[3] # movimenta o asteroid

            # -----  animação background ----- #

            if X_BG_4 <= -370:
                if jogo != 2:
                    jogo = 3
            else:
                X_BG_1 = X_BG_1 - passo_BG
                X_BG_2 = X_BG_2 - passo_BG
                X_BG_3 = X_BG_3 - passo_BG
                X_BG_4 = X_BG_4 - passo_BG
                
            # ----- animação planetas ----- #
            X_P_1 = X_P_1 - passo_P_1 # atualiza a posição do planeta 1
            if X_P_1 < 801: # até que o planeta entre na tela gráfica
                passo_P_1 = 1.5 # altera a veloidade do planeta 1

            X_P_2 = X_P_2 - passo_P_2 # atualiza a posição do planeta 2
            if X_P_2 < 801: # até que o planeta entre na tela gráfica
                passo_P_2 = 1.3 # altera a veloidade do planeta 2

            X_P_3 = X_P_3 - passo_P_3 # atualiza a posição do planeta 3
            if X_P_3 < 801: # até que o planeta entre na tela gráfica
                passo_P_3 = 1.2 # altera a veloidade do planeta 3

            X_P_4 = X_P_4 - passo_P_4 # atualiza a posição do planeta 4
            if X_P_4 < 801: # até que o planeta entre na tela gráfica
                passo_P_4 = 1.1 # altera a veloidade do planeta 4


                  # ____________________ colisão ____________________ #
                  
        if jogo == 1:
            for t in tiro:          #| verifica a colisão de cada tiro 
                for a in asteroid:  #| com cada asteroid
                    col = ((t[0] - a[1])**2 + (t[1] - a[2])**2)**0.5 # condição de colisão
                    if col <= 30: # tamanho do tiro
                        t[2] = 1 # ativa a colisão na tabela de tiro
                        a[4] = 1 # ativa a colisão na tabela de asteroid
                        som_ast.set_volume(0.2)
                        som_ast.play()
                        
            for A in asteroid: # verifica a colisão da nave com os asterois
                # 1 - Frontal collision / 2 - Rear collision / 3 - Bottom collision / 4 - Top collision
                if X_avo + 98 > A[1] and X_avo < A[1] + 40 and Y_avo + 40 > A[2] and Y_avo < A[2] + 30: # condição de colisão
                    A[4] = 1 # ativa a colisão na tabela de asteroid
                    som_exp.set_volume(0.4)
                    som_exp.play()
                    pygame.mixer.music.stop()
                    jogo = 2 # game over

                
    if jogo == 2: # atualiza a tela de game over
        
        # ----- explosão ----- #
        ani_exp = ani_exp + passo_ani_exp

    if jogo == 3: # inicia uma pausa antes da animação final
        clock2 = clock2 - 1 # controla o tempo da pausa
        if clock2 < 0: # inicia a animação
            jogo = 4 

    if jogo == 4: # animação final
        
        if anif == 1:
            if X_avo < 100:
                X_avo = X_avo + passo_avo
            if X_avo > 100:
                X_avo = X_avo - passo_avo
            if Y_avo < 300:
                Y_avo = Y_avo + passo_avo
            if Y_avo > 300:
                Y_avo = Y_avo - passo_avo
            if X_xpr > 500:
                X_xpr = X_xpr - passo_xpr
            if Y_avo >= 290 and Y_avo <= 310 and X_xpr <= 500:
                anif = 2
            
        if anif == 2:
            if X_avo < 650:
                X_avo = X_avo + passo_avo
            if X_avo >= 650:
                anif = 3
                
        if anif == 3:
            pygame.time.delay(10)
            X_xpr = X_xpr + passo_xpr
            X_avo = X_avo + passo_avo
                     
         
                  # ____________________ delay ____________________ #
                  
    clock.tick(20)

                 # ____________________ eventos ____________________ #

    teclas = pygame.key.get_pressed()
            
    if jogo == 1: # jogo
        # ----- controle da nave ----- #
        if teclas[K_a] or teclas[K_LEFT]:
            X_avo = X_avo - passo_avo
            if X_avo < 0:
                X_avo = 0
        if teclas[K_d] or teclas[K_RIGHT]:
            X_avo = X_avo + passo_avo
            if X_avo > 700: # X_avo + img size = 800 (window size), so, 800-100(img size) = 700
                X_avo = 700
        if teclas[K_s] or teclas[K_DOWN]:
            Y_avo = Y_avo + passo_avo
            if Y_avo > 558: # Y_avo + img size = 600 (window size), so, 600-42(img size) = 558
                Y_avo = 558
        if teclas[K_w] or teclas[K_UP]:
            Y_avo = Y_avo - passo_avo
            if Y_avo < 0:
                Y_avo = 0

    
    for event in pygame.event.get():
        if event.type == KEYUP:
            # ----- atirar ----- #
            if event.key == K_SPACE:
                if jogo == 1:
                    if cont_tiro == 10:
                        dat_tiro[0] = X_avo + 70
                        dat_tiro[1] = Y_avo + 22
                        dat_tiro2 = dat_tiro[:]
                        tiro.append(dat_tiro2)
                        cont_tiro = 0
                        som_tiro.set_volume(0.2)
                        som_tiro.play()
                        
            if event.key == K_RETURN:
                # ----- começar o jogo ----- #
                if jogo == 0:
                    pygame.time.delay(100)
                    som_bg = 1
                    jogo = 1
                # ----- reiniciar o jogo ----- #
                if jogo >= 2:
                    if jogo == 2 or X_xpr > 810:                      
                        pygame.time.delay(1000)                        
                        anif = 1         #|
                        clock2 = 20      #|
                        asteroid = []    #|
                        cont_ast = 25    #|
                        passo_ast = 7    #|
                        X_avo = 100      #|
                        Y_avo = 300      #|
                        X_xpr = 801      #|
                        Y_xpr = 200      #|
                        ani_exp = 0      #|
                        tiro = []        #|
                        cont_tiro = 5    #| reseta todas as variaveis necessarias
                        X_BG_1 = 0       #|
                        X_BG_2 = 801     #|
                        X_BG_3 = 1601    #|
                        X_BG_4 = 2401    #| 
                        X_BG_p1 = 0      #|
                        X_BG_p1_1 = 1601 #|
                        X_BG_p2 = 0      #|
                        X_BG_p2_1 = 1601 #|
                        X_P_1 = 3150     #|
                        X_P_2 = 3050     #|
                        X_P_3 = 2200     #|
                        X_P_4 = 1500     #|
                        som_bg = 0       #|
                        pygame.mixer.music.stop() # para a musica
                        jogo = 0 # volta para o menu
                        
        elif event.type == QUIT:
            fim = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                fim = True
            
                        
pygame.mixer.music.stop()
pygame.display.quit()
print("Fim do programa")
