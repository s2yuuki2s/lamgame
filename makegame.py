import pgzrun;;;
from random import randint;;;
WIDTH = 800
HEIGHT = 650
score = 0 
dem = 0
gameover = 0

bowl = Actor('bowl') 
bowl.x = 250
bowl.y = 330
tao = Actor('apple')
tao.x = randint(40, 780) 
tao.y = 0
def update ():
    global score,gameover,dem
    tao.y = tao.y + score/10 
    if tao.colliderect(bowl) :
        tao.y = 0 
        tao.x = randint(40,780)
        score = score + 10
        sounds.vacham.play()
    if(tao.y > 650) :
        dem = dem + 1 
    if(dem > 10) :
        gameover = 1
    else : gameover = 0 
def on_mouse_move(pos,rel,buttons):
    bowl.x = pos[0]
    bowl.y = pos[1]
def draw() :
    if gameover == 1 :
        screen.draw.text('game over',(360,300),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score:'+str(score),(360,350),color=(255,0,255),fontsize=80) 
    if (gameover == 0):
        screen.fill((30,144,255))
        bowl.draw()
        tao.draw()
        screen.draw.text('score:'+str(score),(10,10) ,color=(255,0,0), fontsize = 60)

pgzrun.go()