from Tkinter import *
import math
import random
import subprocess
from multiprocessing import Process

root = Tk()
root.geometry("1366x768+11+0")
root.title("TDE")
root.config(bg="black")
canvas = Canvas()
canvas.config(width=1344,height=700,bg="light blue")       
 

class Powerup(object):
    def __init__(self,coords):
        if random.randint(0,1) == 0:
            self.type = "shield"
            self.p_img = PhotoImage(file='shield.gif')
        else:
            self.type = "health"
            self.p_img = PhotoImage(file='full_health.gif')
        self.coords = coords
        Enemy.enemy_list.append(self)
        self.img = canvas.create_image(*self.coords,image=self.p_img,tags="powerup")
    def move(self):
        if cannon.powerup == "beans":
            canvas.coords(self.img,canvas.coords(cannon.powerup_container)[0]+25,canvas.coords(cannon.powerup_container)[1]+25)
            Enemy.enemy_list.remove(self)
            cannon.powerup = self
        elif cannon.powerup != "beans":
            canvas.coords(self.img,canvas.coords(cannon.powerup_container_2)[0]+25,canvas.coords(cannon.powerup_container_2)[1]+25)
            Enemy.enemy_list.remove(self)
            cannon.powerup_2 = self
        
    def destroy(self):
        canvas.delete(self.img)
        Enemy.enemy_list.remove(self)
        
    
        
        
        
        
        
class Junior(object):
    alvizar = PhotoImage(file="junebug_boss.gif")  
    def __init__(self):
        self.coords = [1200,200]
        self.img = canvas.create_image(*self.coords,image=Junior.alvizar,tags="enemy")
        self.health = 1000
        self.alive = True
        
        self.switch = 0
        self.ball_list = []
        cannon.can_spawn = False
        
        self.hb_outline = canvas.create_rectangle(172,5,1172,26)
        self.hb = canvas.create_rectangle(173,7,1171,25,fill="green",outline="")
        self.junes = canvas.create_text(672,40,text="Junebug",font=("Courier","20"))

    
        
        
        
        self.update()
    def update(self):
        canvas.delete(self.hb)
        self.hb = canvas.create_rectangle(173,8,172+self.health,24,fill="green",outline="")
        for colliding_item in canvas.find_overlapping(*canvas.bbox(self.img)):
            if "cannonball" in canvas.gettags(colliding_item) and self.alive and cannon.alive:
                self.health -= .07
        if self.alive and self.health < 1:
            self.alive = False
            
            
                
        if self.switch == 0 and self.alive and cannon.alive:
            canvas.move(self.img,-5,0)
        elif self.switch == 1 and self.alive and cannon.alive:
            canvas.move(self.img,5,0)
            
        if canvas.coords(self.img)[0] < 100 and cannon.alive:
            self.switch = 1
            self.fire()
        elif canvas.coords(self.img)[0] > 1200 and cannon.alive:
            self.switch = 0
            self.fire()
                    
        
        for i in self.ball_list:
            canvas.move(i.image,i.norm[0],i.norm[1])
            
            if canvas.coords(i.image)[1] > 768:
                canvas.delete(i.image)
                self.ball_list.remove(i)
            
            for colliding_shape in canvas.find_overlapping(*canvas.bbox(i.image)):
                if "cannon" in canvas.gettags(colliding_shape):
                    if cannon.health > 0:
                        cannon.health -= 30
                    try:
                        canvas.delete(i.image)
                        self.ball_list.remove(i)
                    except IndexError:
                        pass
                elif "powerup" in canvas.gettags(colliding_shape):
                    try:
                        canvas.delete(i.image)
                        self.ball_list.remove(i)
                    except:
                        pass
        
            
        if self.alive:
            root.after(1,self.update)
        else:
            for i in self.ball_list:
                canvas.delete(i.image)
            canvas.delete(self.img)
            canvas.delete(self.hb)
            canvas.delete(self.hb_outline)
            canvas.delete(self.junes)
            del self
            cannon.health = 100
            
            
            
            def me4sad2():
                sadsong = "/Users/cisnerosa/documents/dcg/dank_sanic.mp3"
                awww = subprocess.call(["afplay", sadsong])
            def go():
                cannon.can_spawn = True
                cannon.round = True
            def fin():
                global readym8
                canvas.delete(readym8)
                root.after(500,go)
                
            def settrue():
                global readym8
                canvas.delete(rip_in_spaghetti)
                readym8 = canvas.create_text(673,284,text="Round 3!",font=("Courier","30"))
                root.after(2000,fin)
            pp = Process(target=me4sad2)
            pp.start()
            rip_in_spaghetti = canvas.create_text(672,284,text="Junebug,\nrip in spagetti,\nnvr 4getti :(",font=("Courier","30"))
            root.after(22000,settrue)
            
            
            
            
        
            
    def fire(self):  
        self.x,self.y = canvas.coords(self.img)
        ball = Cannonball(x=self.x,y=self.y,mouse=[672,580],image="june_ball") 
        self.ball_list.append(ball)       
class Evan(object):
    berg = PhotoImage(file="evan_boss.gif")  
    def __init__(self):
        self.coords = [1200,200]
        self.img = canvas.create_image(*self.coords,image=Evan.berg,tags="enemy")
        self.health = 1000
        self.alive = True
        
        self.switch = 0
        self.ball_list = []
        cannon.can_spawn = False
        
        self.hb_outline = canvas.create_rectangle(172,5,1172,26)
        self.hb = canvas.create_rectangle(173,7,1171,25,fill="green",outline="")
        self.bergemeister = canvas.create_text(672,40,text="The Bergemeister",font=("Courier","20"))

    
        
        
        
        self.update()
    def update(self):
        canvas.delete(self.hb)
        self.hb = canvas.create_rectangle(173,8,172+self.health,24,fill="green",outline="")
        for colliding_item in canvas.find_overlapping(*canvas.bbox(self.img)):
            if "cannonball" in canvas.gettags(colliding_item) and self.alive and cannon.alive:
                self.health -= 1
        if self.alive and self.health < 1:
            self.alive = False
            
            
                
        if self.switch == 0 and self.alive and cannon.alive:
            canvas.move(self.img,-8,0)
        elif self.switch == 1 and self.alive and cannon.alive:
            canvas.move(self.img,8,0)
            
        if canvas.coords(self.img)[0] < 100 and cannon.alive:
            self.switch = 1
            self.fire()
        elif canvas.coords(self.img)[0] > 1200 and cannon.alive:
            self.switch = 0
            self.fire()
        
            
            
            
        
        for i in self.ball_list:
            canvas.move(i.image,i.norm[0],i.norm[1])
            
            if canvas.coords(i.image)[1] > 768:
                canvas.delete(i.image)
                self.ball_list.remove(i)
            
            for colliding_shape in canvas.find_overlapping(*canvas.bbox(i.image)):
                if "cannon" in canvas.gettags(colliding_shape) and cannon.alive:
                    if cannon.health > 0:
                        cannon.health -= 10
                    try:
                        canvas.delete(i.image)
                        self.ball_list.remove(i)
                    except IndexError:
                        pass
                elif "shield" in canvas.gettags(colliding_shape):
                    try:
                        canvas.delete(i.image)
                        self.ball_list.remove(i)
                    except IndexError:
                        pass
        
            
        if self.alive:
            root.after(1,self.update)
        else:
            for i in self.ball_list:
                canvas.delete(i.image)
            canvas.delete(self.img)
            canvas.delete(self.hb)
            canvas.delete(self.hb_outline)
            canvas.delete(self.bergemeister)
            del self
            cannon.health = 100
            def go():
                cannon.can_spawn = True
                cannon.round = True
            def fin():
                global readym8
                canvas.delete(readym8)
                root.after(500,go)
                
            def settrue():
                global readym8
                canvas.delete(rip_in_spaghetti)
                readym8 = canvas.create_text(673,284,text="Round 2!",font=("Courier","30"))
                root.after(2000,fin)
            rip_in_spaghetti = canvas.create_text(672,284,text="bergemeister,\nrip in spagetti,\nnvr 4getti :(",font=("Courier","30"))
            root.after(5000,settrue)
            
            
            
            
        
            
    def fire(self):  
        self.x,self.y = canvas.coords(self.img)
        ball = Cannonball(x=self.x,y=self.y,mouse=[672,580],image="evan_ball") 
        self.ball_list.append(ball)
        
        
        

        
        
        
class Enemy(object):
    enemy_list = []
    @classmethod
    def enemy_loop(cls):
        for enemy in cls.enemy_list:
            if canvas.coords(enemy.img)[1] < 500:
                canvas.move(enemy.img,0,5)
            else:
                enemy.destroy()
            try:
                for colliding_item in canvas.find_overlapping(*canvas.bbox(enemy.img)):
                    if "cannonball" in canvas.gettags(colliding_item) and enemy.type == "enemy":
                        cannon.score += 1
                        canvas.delete(enemy.img)
                        cls.enemy_list.remove(enemy)
                    elif "cannonball" in canvas.gettags(colliding_item) and enemy.type == "shield" or "cannonball" in canvas.gettags(colliding_item) and enemy.type == "health":
                        enemy.move()
                    
            except:
                pass
            
        root.after(1,cls.enemy_loop)

    
      
    def __init__(self):
        
        def clank():
            cannon_audio_file = "/Users/cisnerosa/documents/dcg/thunk.wav"
            boom = subprocess.call(["afplay", cannon_audio_file])
        clankclank = Process(target=clank)
        clankclank.start()
        
        
        d = random.randint(0,1)
        if d == 0:
            self.coords = [random.randint(80,400),0]
        else:
            self.coords = [random.randint(600,1200),0]
            
        self.img = canvas.create_image(*self.coords,image=level.tom,tags="enemy")
        self.type = "enemy"
        Enemy.enemy_list.append(self)
        
    def destroy(self):
        canvas.delete(self.img)
        Enemy.enemy_list.remove(self)
        if cannon.health >= 10:
            cannon.health -= 10
        def hitsound():
            audio_file = "/Users/cisnerosa/documents/dcg/blip.mp3"
            play = subprocess.call(["afplay", audio_file])
        hitsoundp = Process(target=hitsound)
        hitsoundp.start()


class Cannonball(object):
    def __init__(self,x,y,mouse,image):
        self.berg_shot = PhotoImage(file='bergeshot.gif')
        self.bug_shot = PhotoImage(file='doge.gif')
        
        if image == "circle":
            self.image = canvas.create_oval(cannon.x-22,cannon.y-22,cannon.x+22,cannon.y+22,fill="black",tags="cannonball")
        elif image == "evan_ball":
            self.image = canvas.create_image(x,y,image=self.berg_shot,tags="boomy")
        elif image == "june_ball":
            self.image = canvas.create_image(x,y,image=self.bug_shot,tags="boomy")
            
            
        
        self.mouse_vector = [x-mouse[0],y-mouse[1]]
        self.c2 = self.mouse_vector[0] **2 + self.mouse_vector[1] **2
        self.c = math.sqrt(self.c2)
        self.norm = [self.mouse_vector[0]/self.c,self.mouse_vector[1]/self.c]
        
        if image == "circle":
            self.norm[0] *= -15
            self.norm[1] *= -15
        elif image == "evan_ball":
            self.norm[0] *= -5
            self.norm[1] *= -5
        elif image == "june_ball":
            self.norm[0] *= -8
            self.norm[1] *= -8
        
        #max is about 40
        
        self.velocity = self.norm
        
        self.done = False

        
        
        
class Level(object):
    def __init__(self):
        self.gimg = PhotoImage(file="cannonbase.gif")
        self.tom = PhotoImage(file="thomas.gif")
        
        self.cannon_base = canvas.create_image(672,580,image=self.gimg,tags="cannon")
        self.ground = canvas.create_rectangle(0,580,1344,700,fill="brown")
        self.soundtrack()
        
        self.start_text = canvas.create_text(672,200,text="Press S to Start: \n -Click to fire. \n -Shoot Thomas or die! Each Thomas deals 10 damage! \n -Survive as long as you can! \n -Your score is shown in the gray circle. \n -Your health is the green bar, you've got 100 HP. \n -Shoot powerups for an advantage. \n -Use powerups at any time with the space bar. \nGood Luck!",font=("Courier","30") )
        self.begun = False
        
        flash_process = Process(target=self.screen_loop)
        flash_process.start()
        
        
    def soundtrack(self):
        def tunes():
            
            cannon_audio_file = "/Users/cisnerosa/documents/dcg/soundtrack/day %s.mp3" % random.randint(1,29)
            boom = subprocess.call(["afplay", cannon_audio_file])
            tunes()
            
            
            
        self.tunesp = Process(target=tunes)
        self.tunesp.start()
    def rip(self):
        self.ded = canvas.create_text(672,350,text="You Died!",font=("Courier","50"))
    def begin(self,event):
        if self.begun == False:
            self.begun = True
            canvas.delete(self.start_text)
            cannon.can_spawn = True
    def screen_loop(self):
        canvas.config(bg=random.sample(["red","orange","black","yellow","blue","green","pink"],1))
        root.after(200,self.screen_loop)
      
        
class Cannon(object):
    def __init__(self,x,y):
        self.amg = PhotoImage(file='arrow.gif')
        self.x = x
        self.y = y
        self.cannon = canvas.create_line(self.x,self.y,canvas.winfo_pointerx(),canvas.winfo_pointery(),width="50",fill="grey")
        
        
        self.ball_list = []
        self.score = 0
        
        self.scoreboard = canvas.create_text(self.x,self.y-80,text="%d"%self.score,font=("Courier","20"))
        self.health = 100
        self.alive = True
        self.healthbar_outline = canvas.create_rectangle(self.x-50,self.y+5,self.x+50,self.y+10)
        self.healthbar = canvas.create_rectangle(self.x-50,self.y+5,self.x-50+self.health,self.y+10,fill="green")
        
        self.boss = 0
        self.can_spawn = False
        self.round = 1
        
        self.powerup_container = canvas.create_rectangle(self.x+51,self.y,self.x+101,self.y+50,tags="container")
        self.powerup = "beans"
        self.powerup_2 = "beans"
        self.powerup_container_2 = canvas.create_rectangle(self.x+101,self.y,self.x+151,self.y+50)
        self.arrow_pointer = canvas.create_image(self.x+76,self.y+80,image=self.amg)
        
        
        self.update()
        self.cannonball_loop()
        self.spawn_loop()
    def update(self):
        if self.powerup_2 == "beans":
            canvas.coords(self.arrow_pointer,self.x+76,self.y+60)
        else:
            canvas.coords(self.arrow_pointer,self.x+126,self.y+60)
        
        self.mx,self.my = canvas.winfo_pointerxy()
        self.mx -= 7
        self.my -= 50
            
        
        mouse_vector = [self.x-self.mx,self.y-self.my]
        c2 = mouse_vector[0] **2 + mouse_vector[1] **2
        c = math.sqrt(c2)
        
    
        if self.alive:
            canvas.coords(self.cannon,self.x,self.y,self.x+(mouse_vector[0]/c)*-150,self.y+(mouse_vector[1]/c)*-150)
            canvas.tag_raise(level.cannon_base)
            canvas.tag_raise(level.ground)
            
        canvas.delete(self.scoreboard)
        self.scoreboard = canvas.create_text(self.x,self.y-35,text="%d"%self.score,font=("Courier","20"))
        canvas.tag_raise(self.scoreboard)
        
        canvas.delete(self.healthbar)
        self.healthbar = canvas.create_rectangle(self.x-50,self.y+5,self.x-50+self.health,self.y+10,fill="green")
        canvas.tag_raise(self.healthbar_outline)
        canvas.tag_raise(self.healthbar)
        canvas.tag_raise(self.powerup_container)
        canvas.tag_raise(self.powerup_container_2)
        canvas.tag_raise(self.arrow_pointer)
        if self.powerup != "beans":
            canvas.tag_raise(self.powerup.img)
        if self.powerup_2 != "beans":
            canvas.tag_raise(self.powerup_2.img)
            
        
        
        if self.health < 1 and self.alive:
            self.alive = False
            level.rip()
        
        if self.score >= 33 and self.boss == 0:
            self.boss = 1
            evan = Evan()
        if self.score >= 66 and self.boss == 1:
            self.boss = 2
            junebug = Junior()
            
            
        
        
        root.after(1,self.update)
    def fire(self,event):
        if self.alive:
            cannonball = Cannonball(x=canvas.coords(self.cannon)[0],y=canvas.coords(self.cannon)[1],mouse=[canvas.coords(self.cannon)[2],canvas.coords(self.cannon)[3]],image="circle")
            self.ball_list.append(cannonball)
        
            def boomboom():
                cannon_audio_file = "/Users/cisnerosa/documents/dcg/cannon_shot.mp3"
                bang = subprocess.call(["afplay", cannon_audio_file])
            shot_process = Process(target=boomboom)
            shot_process.start()
            
        
    def cannonball_loop(self):
        for ball in self.ball_list:
            canvas.tag_lower(ball.image)
            bc = canvas.coords(ball.image)
               
            
            
            ball.clist = []
            try:
                bbox = canvas.bbox(ball.image)
                overlapping = canvas.find_overlapping(*bbox)
                for colliding_item in overlapping:
                    if "enemy" in canvas.gettags(colliding_item):
                        ball.clist.append(colliding_item)
                    
                        
            except AttributeError:
                pass
                
            try:
                if len(ball.clist) < 1:
                    canvas.move(ball.image,ball.velocity[0],ball.velocity[1])
            
                
                if bc[1] < 0 or bc[0] < 0 or bc[0] > 1344 or bc[1] > 768:
                    canvas.delete(ball.image)
                    self.ball_list.remove(ball)
            except AttributeError:
                pass
        
            
            
            
        root.after(10,self.cannonball_loop)
    def spawn_loop(self):
        if self.round == 1:
            for i in range(random.randint(1,3)):
                if self.alive and self.can_spawn:
                    pass
                    baddie = Enemy()
        elif self.round == 2:
            for i in range(random.randint(2,4)):
                if self.alive and self.can_spawn:
                    pass
                    baddie = Enemy()
        elif self.round == 3:
            for i in range(random.randint(3,6)):
                if self.alive and self.can_spawn:
                    pass
                    baddie = Enemy()
      
        if random.randint(0,6) == 0 and self.can_spawn:
            up = Powerup([random.randint(44,1300),0])
        
        
        
        root.after(3000,self.spawn_loop)
    def use_powerup(self,event):
        if self.powerup != "beans" and self.powerup_2 == "beans" and self.powerup.type == "shield":
            print "1"
            canvas.delete(self.powerup.img)
            self.shield = canvas.create_oval(self.x-200,self.y-200,self.x+200,self.y+200,fill="",outline="green",tags="shield")
            self.powerup = "beans"
            root.after(5000,self.shield_off)
        elif self.powerup != "beans" and self.powerup_2 == "beans" and self.powerup.type == "health":
            print "2"
            canvas.delete(self.powerup.img)
            self.health = 100
            self.powerup = "beans"
        elif self.powerup != "beans" and self.powerup_2 != "beans" and self.powerup_2.type == "health":
            print "3"
            canvas.delete(self.powerup_2.img)
            self.health = 100
            self.powerup_2 = "beans"
        elif self.powerup != "beans" and self.powerup_2 != "beans" and self.powerup_2.type == "shield":
            print "4"
            canvas.delete(self.powerup_2.img)
            self.shield_2 = canvas.create_oval(self.x-200,self.y-200,self.x+200,self.y+200,fill="",outline="green",tags="shield")
            self.powerup_2 = "beans"
            root.after(5000,self.shield_2_off)
        
    def shield_off(self):
        canvas.delete(self.shield)
    def shield_2_off(self):
        canvas.delete(self.shield_2)
        




level = Level()
cannon = Cannon(x=canvas.coords(level.cannon_base)[0],y=canvas.coords(level.cannon_base)[1])
Enemy.enemy_loop()





root.bind("<Button-1>",cannon.fire)
root.bind("<space>",cannon.use_powerup)

root.bind("<s>",level.begin)
canvas.pack()
root.mainloop()