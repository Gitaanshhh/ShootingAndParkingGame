#ASSETS
import pygame as pyg
import os
import time
import random

WIDTH, HEIGHT = 900,500
window = pyg.display.set_mode((WIDTH,HEIGHT))


#colours
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
#characters

#blue car
blue_car_left = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'blue_car_left.png')),
                                    (140, 70))  # using os.path.join as diff os => diff directories
blue_car_right = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'blue_car_right.png')), (140, 70))
blue_car_up = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'blue_car_up.png')), (70, 140))
blue_car_down = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'blue_car_down.png')), (70, 140))

bc_rect = pyg.Rect(300, 100, 140, 70)
bc_rect_h = 140
bc_rect_w = 70

#char 1
char_left = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'char_left.png')), (70, 70))
char_right = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'char_right.png')), (70, 70))
char_up = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'char_up.png')), (70, 70))
char_down = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'char_down.png')), (70, 70))

char_rect = pyg.Rect(300, 100, 70, 70)
char_rect_h = 70
char_rect_w = 70

#bullet
bullet = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'Bullet.png')), (30, 30))

#targets
target_bot = pyg.transform.scale(pyg.image.load(os.path.join('Assets', 'target_bot.png')), (60, 70))
target_bot_rect = pyg.Rect(100, 100, 60, 70)
hit = []


#PLAYER INFO




class Game_info:
    def __init__(self, map):
        self.map = 0
        maps = 3
    def next_map(self):
        self.map += 1
        self.started = False
    def reset(self):
        self.map = 0
        self.started = False
    def start_map(self):
        self.started = True

game_info = Game_info(map)

class Parking:
    LEVELS = 3
    def __init__(self):
        self.level = 0
        self.status = False
        self.level_start_time = 0
    def next_level(self):
        self.level += 1
    def End(self):
        return self.level > self.LEVELS
    def reset(self):
        self.level = 0
        self.level_start_time = 0
    def start(self):
        self.status = True
    def get_time(self):
        if not self.status:
            return 0
        return round(time.time() - self.level_start_time, 0)
    def starttime(self):
        self.level_start_time = time.time()


parking = Parking()

class Shooter:
    LEVELS = 3
    def __init__(self):
        self.level = 0
        self.status = False
    def next_level(self):
        self.level += 1
    def End(self):
        return self.level > self.LEVELS
    def reset(self):
        self.level = 0
    def start(self):
        self.status = True

shooter = Shooter()

class player:
    def __init__(self, username):
        self.username = username
        #self.time = 100
        self.score = 0

    def register(self):
        f = open("Database.txt", "r+")
        database = f.readlines()
        for x in range(0, len(database)):
            line = database[x].split('-')
            if self.username == line[0]:
                print('Welcome back', self.username)
                break
        else:
            #f.write('\n')
            self.time = 100
            f.write(self.username + '-' +str(self.time) + '-' + str(self.score) + '\n')
            f.close

    def updatetime(self, time):
        self.time = time
        f = open("Database.txt", "r")
        database = f.readlines()
        f.close()
        for x in range(len(database)):
            line = database[x].split('-')
            if self.username == line[0]:
                line = self.username + '-' + str(self.time) + '-' + str(self.score) + '\n'
                database[x] = line
        f = open("Database.txt", "w")
        for x in range(len(database)):
            f.writelines(database[x])

    def order(self):
        f = open("Database.txt", "r")
        database = f.readlines()
        f.close()
        username = []
        time = []
        score = []
        for x in range(len(database)):
            line = database[x].split('-')
            time.append(float(line[1]))
        time.sort()
        for x in range(len(time)):
            for y in range(len(database)):
                line = database[y].split('-')
                if time[x] == float(line[1]) and line[0] not in username:
                    username.append(line[0])
                    break
        f = open("Leaderboard.txt", "w")
        for x in range(len(database)):
            line = username[x] + '-' + str(time[x]) + '-' + str(0) + '\n'
            database[x] = line
            f.writelines(database[x])


class Bullet:
    def __int__(self, rect):
        self.rect = rect



#BASIC FUNCTIONS
pyg.font.init()

def quit(event):
    if event.type == pyg.QUIT:
        pyg.quit()


def draw_window(window, colour):
    window.fill(colour)


def draw_window_obj(window, colour, obj, rect):
   window.fill(colour)
   window.blit(obj, (rect.x, rect.y))


def print_frontend(window, text, font, size, colour, x, y):
    font = pyg.font.SysFont(font, size)
    render = font.render(text, 1, colour)  # draw text on a new Surface -> render(text, antialias, color, background=None) -> Surface
    window.blit(render, (x, y))


def print_frontend_centre(window, text, font, colour):
    render = font.render(text, 1,
                         colour)  # draw text on a new Surface -> render(text, antialias, color, background=None) -> Surface
    window.blit(render, (window.get_width() / 2 - render.get_width() / 2, window.get_height() / 2 - render.get_height() / 2))


class Button:
    def __init__(self, text, bgcolour, fontcolour):
        font = pyg.font.SysFont("Arial", 20)
        self.text = font.render(text, 1, fontcolour)
        self.size = self.text.get_size()
        self.bgcolour = bgcolour
        self.fontcolour = fontcolour

    def squarebutton(self, window, x, y):
        self.x = x
        self.y = y
        self.shape = pyg.rect.Rect((self.x-10, self.y-10), (self.size[0]+20, self.size[1]+20))
        pyg.draw.rect(window, self.bgcolour, self.shape)

        window.blit(self.text, (self.x, self.y))

    def circlebutton(self, window, x, y):
        self.x = x
        self.y = y
        pyg.draw.circle(window, self.bgcolour, (self.x + self.size[0]/2, self.y + self.size[1]/2), self.size[0])
        #pyg.draw.circle(window, self.bgcolour, (self.x, self.y), self.size[0]+10)
        window.blit(self.text, (self.x, self.y))

    def Button_pressed(self, event, whilevar):
        self.status = False
        if event.type == pyg.MOUSEBUTTONDOWN:
            if pyg.mouse.get_pressed():
                pos = pyg.mouse.get_pos()
            if pos[0] in range(self.x, self.x + self.size[0] + 20) and pos[1] in range(self.y, self.y + self.size[1] + 20):
                self.status = 'pressed'
                #print('Pressed')
                return True
            else:
                return whilevar
        else:
            return whilevar

    def resetstatus(self):
        self.status = False

Map1 = Button('Map 1', (0, 255, 0), (255, 0, 0))
Map2 = Button('Map 2', (0, 255, 0), (255, 0, 0))
Leaderboard = Button('Leaderboard', (0, 255, 0), (255, 0, 0))

Menu = Button('Menu', (0, 0, 0), (255, 255, 255))
Resume = Button('Resume', (255, 0, 255), (0, 255, 0))

Start = Button('Start', (0, 255, 0), (255, 255, 255))

back_lob = Button('Back to lobby', (255, 0, 255), (0, 255, 0))

def return_lobby(window, event, lobby):
    if back_lob.Button_pressed(event, False) == True:
        game_info.reset()
        return False
    else:
        return True

MAIN_FONT = pyg.font.SysFont("comicsans", 44)
def get_input(window, typing, event):
        if event.type == pyg.KEYDOWN:
            if event.key == 13:                 #13 is the event code for 'Enter'
                typing = False
                return '', typing
            else:
                a = event.unicode
                return a, typing
        else:
            return '', typing



#MAIN FUCTIONS



def move(a, b, Speed, WIDTH, HEIGHT):
    key = pyg.key.get_pressed()
    if key[pyg.K_a] and a.x - Speed > 0 or key[pyg.K_LEFT] and a.x - Speed > 0:  # left
        a.x -= Speed
    elif key[pyg.K_d] and a.x + Speed + a.width < WIDTH or key[pyg.K_RIGHT] and a.x + Speed + a.width < WIDTH:  # right
        a.x += Speed
    elif key[pyg.K_w] and a.y - Speed > 0 or key[pyg.K_UP] and a.y - Speed > 0:  # right
        a.y -= Speed
    elif key[pyg.K_s] and a.y + Speed + a.height < HEIGHT or key[pyg.K_DOWN] and a.y + Speed + a.height < HEIGHT:  # right
        a.y += Speed
    return a


def direction(event, left, right, up, down, ori, rect, h, w, side):
    if event.type == pyg.KEYDOWN: #or event.type == 771:
        if event.key == pyg.K_a or event.key == pyg.K_LEFT:
            b = left
            rect = pyg.Rect(rect.x, rect.y, h, w)
            side = 'left'
        elif event.key == pyg.K_d or event.key == pyg.K_RIGHT:
            b = right
            rect = pyg.Rect(rect.x, rect.y, h, w)
            side = 'right'
        elif event.key == pyg.K_w or event.key == pyg.K_UP:
            b = up
            rect = pyg.Rect(rect.x, rect.y, w, h)
            side = 'up'
        elif event.key == pyg.K_s or event.key == pyg.K_DOWN:
            b = down
            rect = pyg.Rect(rect.x, rect.y, w, h)
            side = 'down'
        else:
            side = side
        #else:                #required for elif
            b = ori
    else:
        b = ori
    return b, rect, side

def resetpos(rect):
    rect.x = 0
    rect.y = 0

bullets = []
shooting = False


def shoot(side, char_rect):
    if side == 'left':
        x = char_rect.x - 18
        y = char_rect.y + char_rect_h/2 - 15
        velx = -5
        vely = 0
    elif side == 'right':
        x = char_rect.x + char_rect_w - 10
        y = char_rect.y + char_rect_h/2 - 15
        velx = 5
        vely = 0
    elif side == 'up':
        x = char_rect.x + 20
        y = char_rect.y - 18
        velx = 0
        vely = -5
    elif side == 'down':
        x = char_rect.x + 18
        y = char_rect.y + char_rect_h - 10
        velx = 0
        vely = 5
    bullet_rect = pyg.Rect(x, y, 30, 30)
    bullets.append((bullet_rect, velx, vely))
    return velx, vely, bullet_rect


def handle_bullet(info):  #info -> (rect, velx, vely)
    info[0].x += info[1]   #rect.x + velx
    info[0].y += info[2]   #vely.y + vely
    hit = []
    if target_bot_rect.colliderect(info[0]):
        bullets.remove(info)
        hit.append(True)
    elif info[0].x > WIDTH or info[0].x < 0:
        bullets.remove(info)
    elif info[0].y > HEIGHT or info[0].y < 0:
        bullets.remove(info)
    else:
        hit.append(False)
    if True in hit:
        return True
    else:
        return False


def in_box(char_rect, box):
    if char_rect.x in range(box.x, box.x+30) and char_rect.y in range(box.y, box.y+40):
        return 'completed'
    else:
        return False


#MAIN



WIDTH, HEIGHT = 900,500
window = pyg.display.set_mode((WIDTH,HEIGHT))
pyg.display.set_caption('Game')
FPS = 60
MAIN_FONT = pyg.font.SysFont("comicsans", 44)


def main():
    clock = pyg.time.Clock()
    run = False
    login = True
    loader = False
    lobby = False
    blue_car = blue_car_left
    bc_rect = pyg.Rect(300, 100, 140, 70)
    char = char_right
    char_rect = pyg.Rect(300, 100, 70, 70)
    sidecar = 'right'
    sidechar = 'right'
    Menuvar = False
    velx = 0
    vely = 0
    shooting = False

    while run != True:
        clock.tick(FPS)                               #Controls screen refresh speed/Fps
        for event in pyg.event.get():
            quit(event)
        if loader != True:
            draw_window(window, Black)
        while loader != True:
            print_frontend_centre(window, 'Press any key to begin!', MAIN_FONT, White)

            for event in pyg.event.get():
                quit(event)
                if event.type == pyg.KEYDOWN:
                    loader = True
                    break
            pyg.display.update()

        if login == True:
            for event in pyg.event.get():
                quit(event)
            typing = True
            username = ''
            while typing == True:
                window.fill(Black)
                print_frontend(window, 'Username', 'comicsans', 36, White, 90, 90)
                usernamebox = pyg.Rect(90, 150, 310, 80)
                pyg.draw.rect(window, White, usernamebox)
                for event in pyg.event.get():
                    quit(event)
                    user_text, typing = get_input(window, typing, event)
                    #if event.type == pyg.KEYDOWN:
                        #if event.key == pyg.K_BACKSPACE:
                            #username = username.rstrip(username[:-1])
                    username += user_text
                    text_surface = MAIN_FONT.render(username, 1, Red)
                    window.blit(text_surface, (100, 150))
                    pyg.display.update()
            user = player(username)
            user.register()
            print(username)
            login = False



        if lobby != True:
            draw_window(window, White)
            Map1.circlebutton(window, 100, 100)
            Map2.circlebutton(window, 250, 100)
            Leaderboard.squarebutton(window, 550, 100)
            pyg.display.update()
        while lobby != True:
            for event in pyg.event.get():
                quit(event)
                lobby = Map1.Button_pressed(event, lobby)
                lobby = Map2.Button_pressed(event, lobby)
                lobby = Leaderboard.Button_pressed(event, lobby)

                if lobby == True:
                    draw_window(window, White)

                    if Map1.status == 'pressed':
                        game_info.map = 1
                    if Map2.status == 'pressed':
                        game_info.map = 2
                    if Leaderboard.status == 'pressed':
                        game_info.map = 3
                    break

        if game_info.map == 2:
            Menu.squarebutton(window, 800, 50)
            window.blit(blue_car, (bc_rect.x, bc_rect.y))
            pyg.display.update()
            start = False
            parking.reset()
            resetpos(bc_rect)
            parking.start()

            while parking.status == True:
                clock.tick(FPS)
                for event in pyg.event.get():
                    quit(event)
                blue_car, bc_rect, sidecar = direction(event, blue_car_left, blue_car_right, blue_car_up, blue_car_down, blue_car, bc_rect, bc_rect_h, bc_rect_w, sidecar)
                draw_window_obj(window, White, blue_car, bc_rect)
                Menu.squarebutton(window, 800, 50)
                print_frontend(window, 'Level '+str(parking.level), "comicsans", 20, Black, 60, 60)
                print_frontend(window, 'Time '+str(parking.get_time()), "comicsans", 20, Black, 60, 80)
                while parking.level == 0:
                    for event in pyg.event.get():
                        quit(event)
                    window.fill(Black)
                    Start.circlebutton(window, 200, 100)
                    pyg.display.update()
                    start = Start.Button_pressed(event, start)
                    if start == True:
                        parking.level = 1
                        parking.starttime()
                if parking.level == 1:
                    Box = pyg.Rect(400, 80, 160, 90)
                    pyg.draw.rect(window, Red, Box)
                if parking.level == 2:
                    Box = pyg.Rect(400, 280, 140, 80)
                    pyg.draw.rect(window, Red, Box)
                if parking.level == 3:
                    Box = pyg.Rect(200, 180, 140, 80)
                    pyg.draw.rect(window, Red, Box)
                if parking.level == 4:
                    parking.End()
                    user.updatetime(parking.get_time())
                    lobby = False
                    parking.status = False
                pyg.display.update()
                bc_rect = move(bc_rect, blue_car, 5, WIDTH, HEIGHT)

                levelstatus = in_box(bc_rect, Box)
                if levelstatus == 'completed':
                    window.fill(Black)
                    print_frontend_centre(window, 'Level Cleared!!', MAIN_FONT, White)
                    pyg.display.update()
                    time.sleep(0.5)
                    resetpos(bc_rect)
                    parking.next_level()
                Menu.Button_pressed(event, parking.status)
                if Menu.status == 'pressed':
                    Menu.squarebutton(window, 800, 50)
                    pyg.display.update()
                    Menuvar = Menu.Button_pressed(event, Menuvar)
                    if Menuvar == True:
                        draw_window(window, Black)
                        back_lob.squarebutton(window, 650, 100)
                        Resume.squarebutton(window, 100, 100)
                        pyg.display.update()

                    while Menuvar:
                        for event in pyg.event.get():
                            quit(event)
                        if Resume.Button_pressed(event, False) == True:
                            Menuvar = False
                        lobby = return_lobby(window, event, lobby)
                        if lobby == False:
                            Menuvar = False
                            parking.status = False
                        else:
                            pass

        if game_info.map == 1:
            window.fill(White)
            Menu.squarebutton(window, 800, 50)
            window.blit(char, (char_rect.x, char_rect.y))
            pyg.display.update()
            shooter.start()

            while shooter.status == True:
                clock.tick(FPS)
                char, char_rect, sidechar = direction(event, char_left, char_right, char_up, char_down, char, char_rect,
                                                      char_rect_h, char_rect_w, sidechar)
                draw_window_obj(window, White, char, char_rect)
                Menu.squarebutton(window, 800, 50)
                char_rect = move(char_rect, char, 5, WIDTH, HEIGHT)
                for event in pyg.event.get():
                    quit(event)
                    if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_RCTRL and len(bullets) < 3 or event.key == pyg.K_RSHIFT and len(bullets) < 3:
                            bullet_rect, velx, vely = shoot(sidechar, char_rect)
                hit = []
                for x in bullets:
                    hit.append(handle_bullet(x))
                    window.blit(bullet, (x[0].x, x[0].y))
                if True in hit:
                    target_bot_rect.x = random.randint(10, 800)
                    target_bot_rect.y = random.randint(10, 400)

                window.blit(target_bot, (target_bot_rect.x, target_bot_rect.y))
                pyg.display.update()
                Menu.Button_pressed(event, shooter.status)
                if Menu.status == 'pressed':
                    Menu.squarebutton(window, 800, 50)
                    pyg.display.update()
                    Menuvar = Menu.Button_pressed(event, Menuvar)
                    if Menuvar == True:
                        draw_window(window, Black)
                        back_lob.squarebutton(window, 650, 100)
                        Resume.squarebutton(window, 100, 100)
                        pyg.display.update()

                    while Menuvar:
                        for event in pyg.event.get():
                            quit(event)
                        if Resume.Button_pressed(event, False) == True:
                            Menuvar = False
                        lobby = return_lobby(window, event, lobby)
                        if lobby == False:
                            Menuvar = False
                            shooter.status = False
                        else:
                            pass

        if game_info.map == 3:
            leaderboard = True
            if leaderboard == False:
                game_info.reset()
            window.fill(Black)
            print_frontend(window, 'RANK', 'comicsans', 20, Red, 40, 60)
            print_frontend(window, 'USERNAME', 'comicsans', 20, Red, 120, 60)
            print_frontend(window, 'TIME', 'comicsans', 20, Red, 390, 60)
            print_frontend(window, 'SCORE', 'comicsans', 20, Red, 540, 60)
            #pyg.display.update()
            user.order()

            f = open("Leaderboard.txt", "r")
            database = f.readlines()
            y = 100
            for x in range(len(database)):
                line = database[x].split('-')
                y += 40
                print_frontend(window, str(x+1),'comicsans', 20, White, 40, y)
                print_frontend(window, line[0],'comicsans', 20, White, 120, y)
                print_frontend(window, line[1],'comicsans', 20, White, 390, y)
                print_frontend(window, line[2],'comicsans', 20, White, 540, y)
            Menu.squarebutton(window, 800, 50)
            pyg.display.update()
            f.close()
            Menu.Button_pressed(event, leaderboard)
            if Menu.status == 'pressed':
                Menu.squarebutton(window, 800, 50)
                pyg.display.update()
                Menuvar = Menu.Button_pressed(event, Menuvar)
                if Menuvar == True:
                    draw_window(window, Black)
                    back_lob.squarebutton(window, 650, 100)
                    Resume.squarebutton(window, 100, 100)
                    pyg.display.update()

                while Menuvar:
                    for event in pyg.event.get():
                        quit(event)
                    if Resume.Button_pressed(event, False) == True:
                        Menuvar = False
                    lobby = return_lobby(window, event, lobby)
                    if lobby == False:
                        Menuvar = False
                        leaderboard = False
                    else:
                        pass
if __name__ == '__main__':
    main()
    #to open only when file is directly accessed
    #and not when imported

