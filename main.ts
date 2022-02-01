pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
let hra_zahajena = false
let nahodna_doba = 0
let vysledek_int = 0
let vysledek_str = "X"
let klic = false
let countA = 0
let countB = 0
function startovac() {
    
    countA = 0
    countB = 0
    vysledek_int = 0
    vysledek_str = "X"
    basic.clearScreen()
    klic = true
    soundExpression.happy.play()
    nahodna_doba = randint(3000, 10000)
    basic.pause(nahodna_doba)
    hra_zahajena = true
    music.playTone(Note.C, music.beat(1500))
}

control.inBackground(startovac)
basic.forever(function on_forever() {
    
    let is_pin1 = input.pinIsPressed(TouchPin.P1)
    let is_pin2 = input.pinIsPressed(TouchPin.P2)
    // console.log_value("Vysledek_int:", vysledek_int)
    // console.log_value("Vysledek_str:", vysledek_str)
    // console.log_value("Hra_zahajena:", hra_zahajena)
    // console.log_value("Klic:", klic)
    console.logValue("countA:", countA)
    console.logValue("countB:", countB)
    if (hra_zahajena && klic) {
        if (is_pin1 && is_pin2) {
            vysledek_str = "R"
            klic = false
        }
        
        if (is_pin1) {
            vysledek_int = 1
            klic = false
        }
        
        if (is_pin2) {
            vysledek_int = 2
            klic = false
        }
        
    }
    
    if (klic && hra_zahajena == false) {
        if (is_pin1) {
            countA = +1
        }
        
        if (is_pin2) {
            countB = +1
        }
        
    }
    
    vysledek()
})
function vysledek() {
    
    if (vysledek_str == "R") {
        basic.showString("R")
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    } else if (vysledek_int == 1) {
        basic.showNumber(1)
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    } else if (vysledek_int == 2) {
        basic.showNumber(2)
        basic.pause(3000)
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    } else if (countB > 0 && countA > 0 && hra_zahajena && klic) {
        basic.showString("C")
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    } else if (countB > 0 && countA == 0 && hra_zahajena && klic) {
        basic.showString("A")
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    } else if (countA > 0 && countB == 0 && hra_zahajena && klic) {
        basic.showString("B")
        basic.pause(3000)
        hra_zahajena = false
        startovac()
    }
    
}

