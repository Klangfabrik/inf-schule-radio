def show_emoticon():
    if emfang == 1:
        basic.show_icon(IconNames.HEART)
    elif emfang == 2:
        basic.show_icon(IconNames.SMALL_HEART)
    elif emfang == 3:
        basic.show_icon(IconNames.DUCK)
    else:
        basic.show_icon(IconNames.NO)
        basic.show_number(emfang, 250)

def on_received_number(receivedNumber):
    global emfang
    emfang = receivedNumber
    show_emoticon()
radio.on_received_number(on_received_number)

def on_button_a():
    global Zahl
    if Zahl <= 9:
        Zahl += 1
    else:
        Zahl = 0
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    radio.send_number(Zahl)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

emfang = 0
Zahl = 0
Funkkanal = 42
radio.set_group(Funkkanal)
basic.show_number(Funkkanal)
Zahl = 0

def on_forever():
    basic.show_number(Zahl)
basic.forever(on_forever)
