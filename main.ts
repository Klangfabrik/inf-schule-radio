function show_emoticon () {
    if (emfang == 1) {
        basic.showIcon(IconNames.Heart)
    } else if (emfang == 2) {
        basic.showIcon(IconNames.SmallHeart)
    } else if (emfang == 3) {
        basic.showIcon(IconNames.Duck)
    } else {
        basic.showIcon(IconNames.No)
        basic.showNumber(emfang, 250)
    }
}
radio.onReceivedNumber(function (receivedNumber) {
    emfang = receivedNumber
    show_emoticon()
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    if (Zahl <= 9) {
        Zahl += 1
    } else {
        Zahl = 0
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    radio.sendNumber(Zahl)
})
let emfang = 0
let Zahl = 0
let Funkkanal = 42
radio.setGroup(Funkkanal)
basic.showNumber(Funkkanal)
Zahl = 0
basic.forever(function () {
    basic.showNumber(Zahl)
})
