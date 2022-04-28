let ASwitch = 0
let C = 0
let ABSwitch = 0

basic.forever(function () {
    if (ASwitch == 0 && input.buttonIsPressed(Button.A)) {
        ASwitch = 1
    }
    if (ABSwitch == 0 && input.buttonIsPressed(Button.AB)) {
    	ASwitch = 1
    }
})
basic.forever(function () {
    if (ASwitch == 1) {
        if (C >= 40) {
            music.playMelody("E C E C E C E C ", 120)
            basic.showString("" + C + "C")
            if (ABSwitch != 1) {
                basic.showString("kikendo" + "3")
            } else {
                basic.showString("3")
            }
            basic.clearScreen()
        } else if (C >= 35) {
            music.playMelody("F - F - F - F - ", 120)
            basic.showString("" + C + "C")
            if (ABSwitch != 1) {
                basic.showString("kikendo" + "2")
            } else {
                basic.showString("2")
            }
            basic.clearScreen()
        } else if (C >= 30) {
            music.playMelody("G - G - G - G - ", 120)
            basic.showString("" + C + "C")
            if (ABSwitch != 1) {
                basic.showString("kikendo" + "1")
            } else {
                basic.showString("1")
            }
            basic.clearScreen()
        } else {
            basic.showString("" + C + "C")
            basic.clearScreen()
        }
    } else {
        basic.showString("A")
        basic.pause(100)
        basic.showArrow(ArrowNames.West)
    }
})
basic.forever(function () {
    C = input.temperature() - 8
})
