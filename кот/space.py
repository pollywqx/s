from pygame import * 
from random import randint 
init() 
 
 
mixer.music.load("музыка.mp3") 
mixer.music.play() 
 
img_back = "фон.jpg" 
img_hero = "перс.png" 
img_enemy = "ufo.png" 
img_bullet = "bullet.png" 
 
score = 0 
lost = 0 
 
f = font.Font(None, 36) 
 
win_width = 700 
win_height = 500 
win = display.set_mode((win_width, win_height)) 
display.set_caption("Shooter") 
 
background = transform.scale(image.load(img_back), (win_width, win_height)) 
 
class GameSprite(sprite.Sprite): # Клас батько для всіх класів, в ньому основкі властивості 
    def __init__(self, img, x, y, w, h, speed): 
        super().__init__() 
        self.image = transform.scale(image.load(img), (w, h)) 
 
        self.speed = speed 
 
        self.rect = self.image.get_rect() # створення хітбоксу 
        self.rect.x = x 
        self.rect.y = y 
 
    def reset(self): # метод малювання спрайту 
        win.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
class Player(GameSprite): 
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.reload = 0
        self.rate = 5

    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < win_width - 80: 
            self.rect.x += self.speed 
        if keys[K_SPACE]: 
            self.fire() 
 
    def fire(self): 
        bul = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, 15) 
        bullets.add(bul) 
 
 
class Enemy(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global lost 
        if self.rect.y > win_height: 
            self.rect.x = randint(80, win_width - 80) 
            self.rect.y = 0 
            lost += 1 
 
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y -= self.speed 
        if self.rect.y <= 0: 
            self.kill() 
 
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10) 
 
bullets = sprite.Group() 
monsters = sprite.Group() 
 
for i in range(5): 
    x = randint(80, win_width - 80) 
    speed = randint(1, 5) 
    monster = Enemy(img_enemy, x, -40, 80, 50, speed) 
    monsters.add(monster) 
 
finish = False 
run = True 
 
while run: 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
 
    if not finish: 
        win.blit(background, (0, 0)) 
 
        text = f.render(f"Рахунок: {score}", True, (255, 255, 255)) 
        win.blit(text, (10, 20)) 
 
        text_lose = f.render(f"Пропущено: {lost}", True, (255, 255, 255)) 
        win.blit(text_lose, (10, 50)) 
 
        ship.reset() 
        ship.update() 
        bullets.update() 
        monsters.update() 
 
        bullets.draw(win) 
        monsters.draw(win) 

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
                score += 1
                x = randint(80, win_width - 80) 
                speed = randint(1, 5) 
                monster = Enemy(img_enemy, x, -40, 80, 50, speed)
                monsters.add(monster)

        if sprite.spritecollide(ship, monsters, False) or lost >= 10:
            finish = True
            lose = f.render("YOU LOSE! HAHA", True, (200, 50, 50))     
            win.blit(lose, (200, 200))
        
        if score >= 50:
            finish = True
            w = f.render("YOU WIN!", True, (200, 255, 200))     
            win.blit(w, (200, 200))

        display.update() 
 
    time.delay(50)