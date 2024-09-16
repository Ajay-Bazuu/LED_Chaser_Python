import machine
import neopixel
import time

# Define number of LEDs and data pin
NUM_LEDS = 15  # Number of LEDs in the strip
DATA_PIN = 12  # GPIO pin connected to the data line of the LED strip (D6 on ESP8266 corresponds to GPIO 12)

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_LEDS)

def snake_pattern():
    for start in range(NUM_LEDS - 3):  # We stop 3 LEDs before the end since we're lighting 4 at a time
        print(f"Lighting LEDs from {start} to {start + 3}")

        # Set the next 4 LEDs to green
        for i in range(NUM_LEDS):
            if start <= i < start + 4:
                np[i] = (0, 255, 0)  # Set to green (RGB: 0, 255, 0)
            else:
                np[i] = (0, 0, 0)  # Turn off the LED
        
        np.write()  # Send the data to the LED strip
        time.sleep(0.5)  # Adjust the delay for animation speed

def main():
    while True:
        snake_pattern()

# Run the main loop
main()

