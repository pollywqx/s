import play

# спрайт (по умолчанию улыбается)
player = play.new_image(image='1.png', x=0, y=0, size = 100)
speech = play.new_text(words=None, x = 0, y = -play.screen.height/2 + 20) # Наш текст для гравця. Який ми потім змінюємо


@play.when_program_starts
def start():
    # Тут ми робимо стартові дії. Наприклад напис з управлінням:

    tutorial = play.new_text(words="п - подарить кольцо, к - сделать комплимент, о - обнять, н - накормить, д - отправить в Дубаи", x= 0, y= 230, font_size= 25)
    speech.words = "привет"



@play.repeat_forever
async def do ():
    # Тут цикл в якому перевіряємо нажаті клавіші
    if play.key_is_pressed('п') or play.key_is_pressed('П'): # Дві умови бо може бути ввімкнен капс лок(Також можно додати ямову для анг. мови)
        player.image = '2.png'
        speech.words = 'спасибочки'
        await play.timer(seconds = 2.0)
        player.image = '1.png'
        speech.words = 'Это всё? А можно ещё?..'

    if play.key_is_pressed('к') or play.key_is_pressed('К'):
        player.image = '3.png'
        player.size = 25
        speech.words = 'мне приятно)'
        await play.timer(seconds = 2.0)
        player.image = '1.png'
        player.size = 100
        speech.words = 'хочу что то ещё!'

    if play.key_is_pressed('о') or play.key_is_pressed('О'):
        player.image = '4.png'
        player.size = 80
        speech.words = 'Уиии'
        await play.timer(seconds = 2.0)
        player.image = '1.png'
        speech.words = ':)'

    if play.key_is_pressed('н') or play.key_is_pressed('Н'):
        player.image = '5.jpg'
        player.size = 100
        speech.words = 'ням ням'
        await play.timer(seconds = 2.0)
        player.image = '1.png'
        speech.words = 'я наелась'
        

    if play.key_is_pressed('д') or play.key_is_pressed('Д'):
       player.image = '6.jpg' 
       player.size = 100
       speech.words = 'всё, я поехала'
       await play.timer(seconds= 3.0)
       exit() 

play.start_program()
