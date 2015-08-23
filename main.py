from Tkinter import *
import sys
import math
from numpy import deg2rad
from time import sleep
import random

root = Tk()
root.geometry("1350x650+0+0")
root.title("Leap of Faith")
canvas = Canvas()
canvas.config(width=1366,height=670,bg="light blue")

root.wm_attributes("-topmost", 1)
root.focus_force()

#27x13

level_dict = {
    "1":"Level1",
    "2":"Level2",
    "3":"Level3",
    "4":"Level4",
    "5":"Level5",
    "6":"Level6",
    "7":"Level7",
    "8":"Level8",
    "9":"Level9",
    "10":"Level10" 
}


class Enemy(object):
    def __init__(self,avatar):
        self.avatar = avatar
        self.health = 100
        self.alive = True
        
    
        
        
        
class Bullet(object):
    def __init__(self,obj,start,length,width,color,make):
        self.make = make
        if make == "bullet":
            self.speed = 20
            self.length = length
            obj = obj[0],obj[1]-50
        
            mouse_vector = [obj[0] - start[0],obj[1] - start[1]]
            m1 = mouse_vector[0] ** 2
            m2 = mouse_vector[1] ** 2
            mouse_mag = math.sqrt(m1 + m2)
            self.norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
            self.len = [self.norm[0] * length,self.norm[1] * length]
            self.bullet = canvas.create_line(start,[start[0]+self.len[0],start[1]+self.len[1]],fill=color,width=width,tags='bullet')
            self.deleted = False
        elif make == "wave":
            self.speed = 15
            self.length = length
            obj = obj[0],obj[1]-50
        
            mouse_vector = [obj[0] - start[0],obj[1] - start[1]]
            m1 = mouse_vector[0] ** 2
            m2 = mouse_vector[1] ** 2
            mouse_mag = math.sqrt(m1 + m2)
            self.norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
            self.len = [self.norm[0] * length,self.norm[1] * length]
            
            left_theta = deg2rad(10)
            right_theta = deg2rad(-10)
            
            left_cos = math.cos(left_theta)
            left_sin = math.sin(left_theta)
            
            right_cos = math.cos(right_theta)
            right_sin = math.sin(right_theta)
            
            
            
            left_x = self.norm[0] * left_cos - self.norm[1] * left_sin
            left_y = self.norm[0] * left_sin + self.norm[1] * left_cos            
            
            right_x = self.norm[0] * right_cos - self.norm[1] * right_sin
            right_y = self.norm[0] * right_sin + self.norm[1] * right_cos
            
            
            
            
            
            
            
            self.bullet = canvas.create_polygon(start[0]+right_x*40,start[1]+right_y*40,start[0]+left_x*40,start[1]+left_y*40,start[0]+self.len[0]*1.2,start[1]+self.len[1]*1.2,fill=color,outline="black",tags="bullet")
            
            self.deleted = False
    
        elif make == "circle":
            self.speed = 5
            self.length = length
            obj = obj[0],obj[1]-50
        
            mouse_vector = [obj[0] - start[0],obj[1] - start[1]]
            m1 = mouse_vector[0] ** 2
            m2 = mouse_vector[1] ** 2
            mouse_mag = math.sqrt(m1 + m2)
            self.norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
            self.len = [self.norm[0] * length,self.norm[1] * length]
            self.bullet = canvas.create_oval(start[0]-5,start[1]-5,start[0]+5,start[1]+5,fill=color,tags='bullet')
            self.deleted = False
            
            
        elif make == "turret_round":
            self.speed = 10
            self.length = length
            obj = obj[0],obj[1]
        
            mouse_vector = [obj[0] - start[0],obj[1] - start[1]]
            m1 = mouse_vector[0] ** 2
            m2 = mouse_vector[1] ** 2
            mouse_mag = math.sqrt(m1 + m2)
            self.norm = [mouse_vector[0] / mouse_mag,mouse_vector[1] / mouse_mag]
            self.len = [self.norm[0] * length,self.norm[1] * length]
            self.bullet = canvas.create_line(start,[start[0]+self.len[0],start[1]+self.len[1]],fill=color,width=width,tags="enemy_bullet")
            self.deleted = False
        
        
        
        player.bullet_list.append(self)
        
            
        
        
class Level(object):
    def __init__(self):
        self.dirt_block = PhotoImage(file='dirt.gif') 
        self.grass_block = PhotoImage(file='grass.gif')
        self.teleporter = PhotoImage(file='teleporter.gif')
        self.ladder = PhotoImage(file='ladder.gif')
        self.goal = PhotoImage(file='goal.gif')
        self.spawn = PhotoImage(file='spawn.gif')
        self.steel = PhotoImage(file='steel.gif')
        self.turret_ud = PhotoImage(file='turret_ud.gif')
        
    
        
        
        
        with open('choice.txt','r') as selection:
            self.level_to_read = selection.read()
        level_to_read = level_dict[self.level_to_read]
        
        
        coords = [25,25]
        self.tile_list = []
        self.turret_list = []
        self.bullet_list = []
        
        with open('%s.txt' % level_to_read,'r') as level:
            while True:
                c = (level.read(1))
                if not c:
                    break
                
           
           
                if c == """\n""":
                    coords[1] += 50
                    coords[0] = 25
                    make = False
               
                elif c == '0':
                    make = True
                elif c == '1':
                    tileimg = self.dirt_block
                    make = True
                elif c =='2':
                    tileimg = self.grass_block
                    make = True
                elif c == 'a':
                    tileimg = self.teleporter
                    make = True
                elif c == 'b':
                   tileimg = self.teleporter
                   make = True
                elif c == 'l':
                    tileimg = self.ladder
                    make = True
                elif c == 'g':
                    tileimg = self.goal
                    make = True 
                elif c == 's':
                    tileimg = self.spawn
                    make = True
                elif c == 'm':
                    tileimg = self.steel
                    make = True
                elif c == 'u':
                    #u is for upside-down, specifies a turret orientation
                    tileimg = self.turret_ud
                    make = True
                  
            
                if make == True:
                    if c != '0':
                        tile = canvas.create_image(*coords,image=tileimg)
                    
                        if c == '1':
                            canvas.itemconfig(tile,tags="player_collide")
                            self.tile_list.append(tile)
                        elif c == '2':
                            canvas.itemconfig(tile,tags="player_collide")
                            self.tile_list.append(tile)
                        elif c == 'a':
                            canvas.itemconfig(tile,tags="teleporter_a")
                            self.tile_list.append(tile)
                        elif c == 'b':
                            canvas.itemconfig(tile,tags="teleporter_b")
                            self.tile_list.append(tile)
                        elif c == 'l':
                            canvas.itemconfig(tile,tags="ladder")
                            self.tile_list.append(tile)
                        elif c == 'g':
                            canvas.itemconfig(tile,tags="goal")
                            self.tile_list.append(tile)
                        elif c == 's':
                            canvas.itemconfig(tile,tags="spawn")
                            self.tile_list.append(tile)
                        elif c == 'm':
                            canvas.itemconfig(tile,tags="player_collide")
                            self.tile_list.append(tile)
                        elif c == 'u':
                            canvas.itemconfig(tile,tags=("enemy","turret"))
                            self.tile_list.append(tile)
                    
                    
                
                
                    
        
                    coords[0] += 50
        
        
        
        

        
        
        #spawn enemies
        for tile in self.tile_list:
            if "turret" in canvas.gettags(tile):
                enemy = Enemy(avatar=tile)
                self.turret_list.append(enemy)
        



    def turret_loop(self):
        for en in self.turret_list:
            if en.alive:
                try:
                    canvas.delete(en.laser_pointer)
                except AttributeError:
                    pass
                en.laser_pointer = canvas.create_line(canvas.coords(en.avatar)[0],canvas.coords(en.avatar)[1],canvas.coords(player.avatar)[0],canvas.coords(player.avatar)[1],fill="")
            
            
            
                en.overlapping = canvas.find_overlapping(*canvas.bbox(en.avatar))
                for i in en.overlapping:
                    if "bullet" in canvas.gettags(i) and en.alive:
                        en.alive = False
                        canvas.delete(en.avatar)
                        self.turret_list.remove(en)
                    
            
                
                if player.alive and en.alive:
                    bul = Bullet(obj=[canvas.coords(en.laser_pointer)[2],canvas.coords(en.laser_pointer)[3]],start=[canvas.coords(en.avatar)[0],canvas.coords(en.avatar)[1]],length=50,width=1,color="red",make="turret_round")
                    self.bullet_list.append(bul)
            
            
            
        root.after(500,self.turret_loop)
    def bullet_loop(self):
        for bullet in self.bullet_list:
            canvas.move(bullet.bullet,bullet.norm[0],bullet.norm[1])
        
        root.after(10,self.bullet_loop)

class Player(object): 
    def __init__(self):
        self.coords = [100,585]
        
        
        for i in level.tile_list:
            if "spawn" in canvas.gettags(i):
                self.coords = canvas.coords(i)
        self.arrow = PhotoImage(file='arrow.gif')
        self.pointer = canvas.create_image(70,575,image=self.arrow)
        self.exp = PhotoImage(file='explosion.gif')
          
        self.velocity = [0,0]
        self.anim_stage = 0
        self.animated = False
        self.right = True
        self.gravitational_constant = 0
        self.climbing = False
        self.won = False
        self.jump_height = 100
        self.bullet_list = []
        self.mode = "rifle"
        self.explosion_list = []
        
        self.ball_ammo = 25
        self.stick_ammo = 35
        self.laser_ammo = 45
        self.health = 100
        self.alive = True
        
        self.health_bar_outline = canvas.create_rectangle(50,610,150,630,fill="",outline="black")
        self.health_bar = canvas.create_rectangle(50,611,50+self.health,630,fill="green",outline="")
        
        self.circle_disp = canvas.create_text(100,525,text="%d"%self.ball_ammo,font=("DIN","20"),fill="blue")
        self.stick_disp = canvas.create_text(100,550,text="%d"%self.stick_ammo,font=("DIN","20"),fill="grey")
        self.laser_disp = canvas.create_text(100,575,text="%d"%self.laser_ammo,font=("DIN","20"),fill="red")
                
        
        
        left_0 = left_sprites.images[0]
        left_1 = left_sprites.images[1]
        left_2 = left_sprites.images[2]
        left_3 = left_sprites.images[3]
        
        right_0 = right_sprites.images[0]
        right_1 = right_sprites.images[1]
        right_2 = right_sprites.images[2]
        right_3 = right_sprites.images[3]
       
        
    
        self.left_animation_dict = {
            0:left_0,
            1:left_1,
            2:left_2,
            3:left_3,
        }
        
        self.right_animation_dict = {
            0:right_0,
            1:right_1,
            2:right_2,
            3:right_3,
        }
        
        
        
        
        
        self.avatar = canvas.create_image(*self.coords,image=self.right_animation_dict[0])
        
        
        
        
        
         
        with open('settings.txt','r') as settings:
            self.right_button = settings.readline()
            self.left_button = settings.readline()
            self.jump_button = settings.readline()
            self.shoot_button = settings.readline()
            self.switch_button = settings.readline()
        
        
        
        
        self.update_loop()
        self.animation_loop()
        self.bullet_loop()
        
    def update_loop(self):
        canvas.delete(self.health_bar)
        
        self.health_bar = canvas.create_rectangle(50,611,50+self.health,630,fill="green",outline="")

        
        self.coords = canvas.coords(self.avatar)
        
        self.bbox = canvas.bbox(self.avatar)
        self.overlapping = canvas.find_overlapping(*self.bbox)
        
        
        
        self.collision_list = []
        

        for i in self.overlapping:
            if "teleporter_a" in canvas.gettags(i):
                for tile in level.tile_list:
                    if "teleporter_b" in canvas.gettags(tile):
                        to_tp = canvas.coords(tile)
                        canvas.coords(self.avatar,to_tp[0],to_tp[1]+10)
            if "player_collide" in canvas.gettags(i):
                self.collision_list.append(canvas.gettags(i))
            elif "ladder" in canvas.gettags(i):
                self.collision_list.append(canvas.gettags(i))
            elif "goal" in canvas.gettags(i) and self.won == False:
                root.after(500,self.victory)
                self.won = True
            elif "enemy_bullet" in canvas.gettags(i) and self.alive == True:
                self.health -= 1
                
        if self.health < 1:
            self.alive = False
                
        if ("player_collide",) not in self.collision_list and ("ladder",) not in self.collision_list:
            canvas.move(self.avatar,0,self.gravitational_constant)
            self.gravitational_constant += .4
            if self.gravitational_constant > 15:
                self.gravitational_constant = 15
                
        else:
            self.gravitational_constant = 0
          
    
    
        
        
    
           
                
            
            
        
        #side collision
        self.left_list = []
        self.right_list = []
        self.bottom_list = []
        self.top_list = []
        
        
        self.left_block = canvas.find_overlapping(self.coords[0]-23,self.coords[1]-20,self.coords[0]-22,self.coords[1]+20)
        self.right_block = canvas.find_overlapping(self.coords[0]+23,self.coords[1]-20,self.coords[0]+22,self.coords[1]+20)
        self.bottom_block = canvas.find_overlapping(self.coords[0]-15,self.coords[1]+21,self.coords[0]+15,self.coords[1]+21)
        self.top_block = canvas.find_overlapping(self.coords[0]-15,self.coords[1]-26,self.coords[0]+15,self.coords[1]-27)
        
        
        for i in self.left_block:
            if "player_collide" in canvas.gettags(i):
                self.left_list.append(canvas.gettags(i))  
        for i in self.right_block:
            if "player_collide" in canvas.gettags(i):
                self.right_list.append(canvas.gettags(i))
        for i in self.bottom_block:
            if "player_collide" in canvas.gettags(i):
                self.bottom_list.append(canvas.gettags(i))
        for i in self.top_block:
            if "player_collide" in canvas.gettags(i):
                self.top_list.append(canvas.gettags(i))
                
        if ("player_collide",) in self.bottom_list:
            canvas.move(self.avatar,0,-1)
        if ("player_collide",) in self.top_list:
            canvas.move(self.avatar,0,1)
            
            
        if self.velocity[0] < 0:
            if ('player_collide',) not in self.left_list:
                canvas.move(self.avatar,self.velocity[0],0)           
        elif self.velocity[0] > 0:
            if ('player_collide',) not in self.right_list:
                canvas.move(self.avatar,self.velocity[0],0)
        
        if self.climbing == True and ("player_collide",) not in self.top_list:
            canvas.move(self.avatar,0,-3)
        #side collision
        
        
        
        
        root.after(10,self.update_loop)
    def animation_loop(self):
        if self.animated == True and self.alive:
            if self.anim_stage != 3:
                self.anim_stage += 1
            else:
                self.anim_stage = 0
        elif self.alive:
            self.anim_stage = 0
      
                
                
        canvas.delete(self.avatar)
        if self.right == True:
            self.avatar = canvas.create_image(self.coords[0],self.coords[1],image=self.right_animation_dict[self.anim_stage])
        elif self.right == False:
            self.avatar = canvas.create_image(self.coords[0],self.coords[1],image=self.left_animation_dict[self.anim_stage])
            
        
        root.after(100,self.animation_loop)
        
    def victory(self):
        
        #lock out controls
        
        root.bind("<%s>"%player.right_button,self.dummy)
        root.bind("<%s>"%player.left_button,self.dummy)

        root.bind("<%s>"%player.jump_button,self.dummy)
        root.bind("<%s>"%player.shoot_button,self.dummy)
        
        root.bind("<KeyRelease-%s>"%player.right_button,self.dummy)
        root.bind("<KeyRelease-%s>"%player.left_button,self.dummy)
        root.bind("<KeyRelease-%s>"%player.jump_button,self.dummy)
        
        self.animated = False
        self.velocity[0] = 0
        
        #lock out controls
        
        
        v = Toplevel()
        
        v.wm_attributes("-topmost", 1)
        v.focus_force()
        
        
        v.geometry("800x500+283+50")
        v.title("Level Cleared!")
        
        def save():
            with open('progress.txt','w') as progress:
                progress.write("%s"%level.level_to_read)
        def close():
            sys.exit()
                
        save_button = Button(v,text="Save",command=save)
        close_button = Button(v,text="Close Level",command = close)
        
        close_button.pack()
        save_button.pack()
        
    
    
    def move_right(self,event):
        if self.alive:
            self.velocity[0] = 4
            self.animated = True
            self.right = True
    def move_left(self,event):
        if self.alive:
            self.velocity[0] = -4
            self.animated = True
            self.right = False
    def up(self,event):
        self.ladder_list = []
       
        
        
        for i in self.overlapping:
            if "ladder" in canvas.gettags(i):
                self.ladder_list.append(canvas.gettags(i))
        
        
                
        if ("ladder",) in self.ladder_list and self.alive:
            self.climbing = True
            
            
    
        
        
            
            
            
        
        
    def stop(self,event):
        self.animated = False
        self.velocity[0] = 0
    def vel_stop(self,event):
        self.climbing = False
   
        
        
        
    def dummy(self,event):
        pass
    def fire(self,event):
        
        if self.mode == "shotgun" and self.ball_ammo > 0 and self.alive:
            
            self.ball_ammo -= 1
            boolet = Bullet(obj=[canvas.winfo_pointerxy()[0]-5,canvas.winfo_pointerxy()[1]],start=[canvas.coords(self.avatar)[0],canvas.coords(self.avatar)[1]],length=15,width=1,color="blue",make="circle")
        elif self.mode == "rifle" and self.laser_ammo > 0 and self.alive:
            self.laser_ammo -= 1
            boolet = Bullet(obj=[canvas.winfo_pointerxy()[0]-5,canvas.winfo_pointerxy()[1]],start=[canvas.coords(self.avatar)[0],canvas.coords(self.avatar)[1]],length=50,width=1,color="red",make="bullet")
        elif self.mode == "wavegun" and self.stick_ammo > 0 and self.alive:
            self.stick_ammo -= 1
            boolet = Bullet(obj=[canvas.winfo_pointerxy()[0]-5,canvas.winfo_pointerxy()[1]],start=[canvas.coords(self.avatar)[0],canvas.coords(self.avatar)[1]],length=50,width=1,color="grey",make="wave")
        self.stats_update()
        
        
    def bullet_loop(self):
        for i in self.bullet_list:
            canvas.move(i.bullet,i.norm[0]*i.speed,i.norm[1]*i.speed)
            
            
            
                
                
           
            bbox = canvas.bbox(i.bullet)
            overlapping = canvas.find_overlapping(*bbox)   
             

            for block in overlapping:
                if "teleporter_a" in canvas.gettags(block):
                    for tile in level.tile_list:
                        if "teleporter_b" in canvas.gettags(tile):
                            
                            if i.make == "bullet":
                                to_tp = canvas.coords(tile)
                                canvas.coords(i.bullet,to_tp[0],to_tp[1],to_tp[0]+i.norm[0]*i.length,to_tp[1]+i.norm[1]*i.length) 
    
    
                        
                        
                                
                elif "player_collide" in canvas.gettags(block) and i.make == "circle":
                    try:
                        self.bullet_list.remove(i)
                        
                    except (ValueError,AttributeError):
                        
                        pass
                elif i.make == "wave" and "player_collide" in canvas.gettags(block):
                    try:
                        
                        
                        bc = canvas.coords(i.bullet)
                        explosion = canvas.create_image(bc[0],bc[1],image=self.exp,tags="bullet")
                        self.explosion_list.append(explosion)
                        root.after(500,self.delete)
                        
                        
            
                        canvas.delete(i.bullet)
                        self.bullet_list.remove(i)
                        
                        
                    except (ValueError,AttributeError,IndexError):
                        pass
            
                               
            
            
        
       
            
                    
                
                
            
            
                
            
                elif "player_collide" in canvas.gettags(block):
                    try:
                        self.bullet_list.remove(i)
                        canvas.delete(i.bullet)
                        
                    except (ValueError,AttributeError):
                        
                        pass
        
        root.after(1,self.bullet_loop)
        


    def switch(self,event):
        if self.mode == "shotgun" and self.alive:
            #laser
            canvas.delete(self.pointer)
            self.pointer = canvas.create_image(70,575,image=self.arrow)
            self.mode = "rifle"
        elif self.mode == "rifle" and self.alive:
            #stick 
            canvas.delete(self.pointer)
            self.pointer = canvas.create_image(70,550,image=self.arrow)
            self.mode = "wavegun"
        elif self.mode == "wavegun" and self.alive:
            #circle
            canvas.delete(self.pointer)
            self.pointer = canvas.create_image(70,525,image=self.arrow)
            self.mode = "shotgun"
        

    def stats_update(self):
        canvas.delete(self.stick_disp)
        canvas.delete(self.circle_disp)
        canvas.delete(self.laser_disp)
        
        
        self.circle_disp = canvas.create_text(100,525,text="%d"%self.ball_ammo,font=("DIN","20"),fill="blue")
        self.stick_disp = canvas.create_text(100,550,text="%d"%self.stick_ammo,font=("DIN","20"),fill="grey")
        self.laser_disp = canvas.create_text(100,575,text="%d"%self.laser_ammo,font=("DIN","20"),fill="red")
        
        
    def delete(self):
        to_del = self.explosion_list.pop()
        canvas.delete(to_del)
        

class Left_Spritesheet(object):
    def __init__(self):

        self.spritesheet = PhotoImage(file="spritesheet.gif")
        self.num_sprintes = 4
        self.last_img = None
        self.images = [self.subimage(32*i, 0, 32*(i+1), 48) for i in range(self.num_sprintes)]
    

    def subimage(self, l, t, r, b):
        dst = PhotoImage()
        root.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst
class Right_Spritesheet(object):
    def __init__(self):
        self.spritesheet = PhotoImage(file="spritesheet.gif")
        self.num_sprintes = 4
        self.last_img = None
        self.images = [self.subimage(32*i, 48, 32*(i+1), 96) for i in range(self.num_sprintes)]
    

    def subimage(self, l, t, r, b):
        dst = PhotoImage()
        root.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst





level = Level()
left_sprites = Left_Spritesheet()
right_sprites = Right_Spritesheet()
player = Player()

level.turret_loop()

root.bind("<%s>"%player.right_button,player.move_right)
root.bind("<%s>"%player.left_button,player.move_left)

root.bind("<%s>"%player.jump_button,player.up)
root.bind("<%s>"%player.shoot_button,player.fire)
root.bind("<%s>"%player.switch_button,player.switch)
        
root.bind("<KeyRelease-%s>"%player.right_button,player.stop)
root.bind("<KeyRelease-%s>"%player.left_button,player.stop)
root.bind("<KeyRelease-%s>"%player.jump_button,player.vel_stop)




canvas.pack()
root.mainloop()
        
        