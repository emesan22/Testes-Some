動作 = 0
非表示 = 0
ondo = 0

def on_button_pressed_a():
    global 動作
    動作 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global 動作
    動作 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 非表示
    if 非表示 == 0:
        非表示 = 1
    elif 非表示 == 1:
        非表示 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    if 動作 == 1:
        if ondo >= 40:
            music.play_melody("E C E C E C E C ", 120)
            basic.show_string("" + str(ondo) + "C")
            if 非表示 == 1:
                basic.show_string("kikendo" + "3")
            else:
                basic.show_string("3")
            basic.clear_screen()
        elif ondo >= 35:
            music.play_melody("F - F - F - F - ", 120)
            basic.show_string("" + str(ondo) + "C")
            if 非表示 == 1:
                basic.show_string("kikendo" + "2")
            else:
                basic.show_string("2")
            basic.clear_screen()
        elif ondo >= 30:
            music.play_melody("G - G - G - G - ", 120)
            basic.show_string("" + str(ondo) + "C")
            if 非表示 == 1:
                basic.show_string("kikendo" + "1")
            else:
                basic.show_string("1")
            basic.clear_screen()
        else:
            basic.show_string("" + str(ondo) + "C")
            basic.clear_screen()
    else:
        basic.show_string("A")
        basic.pause(100)
        basic.show_arrow(ArrowNames.WEST)
basic.forever(on_forever)

def on_forever2():
    global ondo
    ondo = input.temperature() - 8
basic.forever(on_forever2)
