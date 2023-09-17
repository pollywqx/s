import play
import pygame

pygame.init()

pygame.mixer.init()

play.set_backdrop('light green')

text1 = play.new_text(words = "Крутое пианинно, давай поиграем?", x = 0, y = 200)
text2 = play.new_text(words = 'Сыграй мелодию с помощью клавиш', x = 0, y = 150)

play_melody = play.new_box(color = 'light blue',
    border_color = 'aquamarine',
    border_width = 4,
    x = -100,
    y = -170,
    width = 160,
    height = 50)

play_melody_txt = play.new_text(words = 'Грати мелодію',
    x = -100, y = -170,
    font_size = 23)

clear_melody = play.new_box(color = 'light blue',
    border_color = 'aquamarine',
    border_width = 4,
    x = 100,
    y = -170,
    width = 160,
    height = 50)

clear_melody_txt = play.new_text(words = 'Очистити мелодію',
    x = 100, y = -170,
    font_size = 23)

piano_btn = play.new_circle(color = 'black',
    border_color = 'green',
    border_width = 4,
    radius = 12,
    x = -160, y = -100)

piano_txt = play.new_text(words = 'piano',
    font_size = 25, x = -120, y = -100)

flute_btn = play.new_circle(color = 'white',
    border_color = 'green',
    border_width = 4,
    radius = 12,
    x = -70, y = -100)

flute_txt = play.new_text(words = 'flute',
    font_size = 25, x = -30, y = -100)

guitar_btn = play.new_circle(color = 'white',
    border_color = 'green',
    border_width = 4,
    radius = 12,
    x = 20, y = -100)

guitar_txt = play.new_text(words = 'guitar',
    font_size = 25, x = 60, y = -100)

violin_btn = play.new_circle(color = 'white',
    border_color = 'green',
    border_width = 4,
    radius = 12,
    x = 110, y = -100)

violin_txt = play.new_text(words = 'violin',
    font_size = 25, x = 150, y = -100)

get_instrument = 1
keys = []
piano = []
flute = []
guitar = []
violin = []
melody = []
for i in range(8):
    key_x = -180 + i * 50
    key = play.new_box(color = 'white',
        border_color = 'black',
        border_width = 4,
        width = 40, height = 100,
        x = key_x, y = 0)
    keys.append(key)
    piano_snd = pygame.mixer.Sound(f"{i + 1}.ogg")
    piano.append(piano_snd)
    flute_snd = pygame.mixer.Sound(f"f{i + 1}.ogg")
    flute.append(flute_snd)
    guitar_snd = pygame.mixer.Sound(f"g{i + 1}.ogg")
    guitar.append(guitar_snd)
    violin_snd = pygame.mixer.Sound(f"v{i + 1}.ogg")
    violin.append(violin_snd)

@play.when_program_starts
def start():
    pass

@piano_btn.when_clicked
def piano_play():
    global get_instrument
    piano_btn.color = 'black'
    flute_btn.color = 'white'
    guitar_btn.color = 'white'
    violin_btn.color = 'white'
    get_instrument = 1

@flute_btn.when_clicked
def flute_play():
    global get_instrument
    piano_btn.color = 'white'
    flute_btn.color = 'black'
    guitar_btn.color = 'white'
    violin_btn.color = 'white'
    get_instrument = 2

@guitar_btn.when_clicked
def guitar_play():
    global get_instrument
    piano_btn.color = 'white'
    flute_btn.color = 'white'
    guitar_btn.color = 'black'
    violin_btn.color = 'white'
    get_instrument = 3

@violin_btn.when_clicked
def violin_play():
    global get_instrument
    piano_btn.color = 'white'
    flute_btn.color = 'white'
    guitar_btn.color = 'white'
    violin_btn.color = 'black'
    get_instrument = 4

@play_melody.when_clicked
async def play_mel():
    for mel in melody:
        mel.play()
        await play.timer(0.4)

@clear_melody.when_clicked
def clear_mel():
    melody.clear()
    clear_snd = pygame.mixer.Sound('clear_melody.wav')
    clear_snd.play

@play.repeat_forever
async def play_piano():
    for j in range(len(keys)):
        if keys[j].is_clicked and get_instrument == 1:
            keys[j].color = 'light green'
            piano[j].play()
            melody.append(piano[j])
            await play.timer(0.3)
            keys[j].color = 'white'

        if keys[j].is_clicked and get_instrument == 2:
            keys[j].color = 'light green'
            flute[j].play()
            melody.append(flute[j])
            await play.timer(0.3)
            keys[j].color = 'white'

        if keys[j].is_clicked and get_instrument == 3:
            keys[j].color = 'light green'
            guitar[j].play()
            melody.append(guitar[j])
            await play.timer(0.3)
            keys[j].color = 'white'

        if keys[j].is_clicked and get_instrument == 4:
            keys[j].color = 'light green'
            violin[j].play()
            melody.append(violin[j])
            await play.timer(0.3)
            keys[j].color = 'white'


play.start_program()
