input.onButtonPressed(Button.A, function () {
    strip.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(2000)
    strip.showColor(neopixel.colors(NeoPixelColors.White))
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)
strip.setBrightness(20)
basic.forever(function () {
	
})
