def on_button_pressed_a():
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(2000)
    strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
input.on_button_pressed(Button.A, on_button_pressed_a)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB)
strip.set_brightness(20)

def on_forever():
    pass
basic.forever(on_forever)
