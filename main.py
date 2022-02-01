pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)

hra_zahajena = False
nahodna_doba = 0
vysledek_int = 0
vysledek_str = "X"
klic = False
countA = 0
countB = 0

def startovac():
    global hra_zahajena, nahodna_doba, klic, countA, countB, vysledek_str, vysledek_int
    countA = 0
    countB = 0
    vysledek_int = 0
    vysledek_str = "X"
    basic.clear_screen()
    klic = True
    soundExpression.happy.play()
    nahodna_doba = randint(3000, 10000)
    basic.pause(nahodna_doba)
    hra_zahajena = True
    music.play_tone(Note.C, music.beat(1500))
control.in_background(startovac)

def on_forever():
    global hra_zahajena, vysledek_int, vysledek_str, klic, countA, countB
    is_pin1 = input.pin_is_pressed(TouchPin.P1)
    is_pin2 = input.pin_is_pressed(TouchPin.P2)

    #console.log_value("Vysledek_int:", vysledek_int)
    #console.log_value("Vysledek_str:", vysledek_str)
    #console.log_value("Hra_zahajena:", hra_zahajena)
    #console.log_value("Klic:", klic)

    console.log_value("countA:", countA)
    console.log_value("countB:", countB)


    if hra_zahajena and klic:
        if is_pin1 and is_pin2:
            vysledek_str = "R"
            klic = False
        if is_pin1:
            vysledek_int = 1
            klic = False
        if is_pin2:
            vysledek_int = 2
            klic = False

    if klic and hra_zahajena == False:
        if is_pin1:
            countA =+ 1
        if is_pin2:
            countB =+ 1
    vysledek()
basic.forever(on_forever)

def vysledek():
    global hra_zahajena, klic, vysledek_int, vysledek_str, countA, countB

    if vysledek_str == "R":
        basic.show_string("R")
        basic.pause(3000)
        hra_zahajena = False
        startovac()

    elif vysledek_int == 1:
        basic.show_number(1)
        basic.pause(3000)
        hra_zahajena = False
        startovac()

    elif vysledek_int == 2:
        basic.show_number(2)
        basic.pause(3000)
        basic.pause(3000)
        hra_zahajena = False
        startovac()

    elif countB > 0 and countA > 0 and hra_zahajena and klic:
        basic.show_string("C")
        basic.pause(3000)
        hra_zahajena = False
        startovac()

    elif countB > 0 and countA == 0 and hra_zahajena and klic:
        basic.show_string("A")
        basic.pause(3000)
        hra_zahajena = False
        startovac()

    elif countA > 0 and countB == 0 and hra_zahajena and klic:
        basic.show_string("B")
        basic.pause(3000)
        hra_zahajena = False
        startovac()

