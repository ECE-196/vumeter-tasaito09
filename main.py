#print("Hello World!")

import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    initial_volume = []
    for _ in range(5):
        initial_volume.append(microphone.value)

    #leds[0].value = not leds[0].value
    #leds[1].value = not leds[0].value

    default_volume = sum(initial_volume) / len(initial_volume)
    led_step = 2000

    for index, led in enumerate(leds):
        index_volume = default_volume + (led_step*index)

        if volume >= index_volume:
            leds[index].value = 1
        else:
            leds[index].value = 0

    sleep(0.2)




    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
