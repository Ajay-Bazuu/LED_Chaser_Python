import machine
import neopixel
import time

# Define number of LEDs and data pin
NUM_LEDS = 15  # Number of LEDs in the strip
DATA_PIN = 12  # GPIO pin connected to the data line of the LED strip (D6 on ESP8266 corresponds to GPIO 12)

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_LEDS)

def set_all_leds(color):
    for i in range(NUM_LEDS):
        np[i] = color  # Set each LED to the given color
    np.write()  # Send the data to the LED strip

def main():
    while True:
        print("Turning all LEDs green")
        set_all_leds((0, 255, 0))  # Set all LEDs to green (RGB: 0, 255, 0)
        time.sleep(5)  # Wait for 5 seconds

        print("Turning off all LEDs")
        set_all_leds((0, 0, 0))  # Turn off all LEDs
        time.sleep(2)  # Wait for 2 seconds

# Run the main loop
main()

