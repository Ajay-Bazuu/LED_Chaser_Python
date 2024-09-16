import machine
import neopixel
import time
import random

# Define number of LEDs and data pin
NUM_LEDS = 15  # Number of LEDs in the strip
DATA_PIN = 12  # GPIO pin connected to the data line of the LED strip (D6 on ESP8266 corresponds to GPIO 12)

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_LEDS)

def custom_randint(min_val, max_val):
    # Use random.getrandbits() to get a random integer between min_val and max_val (inclusive)
    return min_val + (random.getrandbits(8) % (max_val - min_val + 1))

def get_random_color():
    # Generate a random color with RGB values
    return (custom_randint(0, 255), custom_randint(0, 255), custom_randint(0, 255))

def snake_pattern():
    while True:
        # Randomly choose the number of LEDs to light up (between 3 and 6)
        num_leds_to_glow = custom_randint(3, 6)
        
        # Randomly choose the starting LED index, ensuring enough space for the LEDs to glow
        start = 0

        # Generate a random color for this cycle
        color = get_random_color()

        print(f"Lighting {num_leds_to_glow} LEDs from {start} to {NUM_LEDS - 1} with color {color}")

        # Animate from start to end with the random color and number of LEDs
        for offset in range(NUM_LEDS - num_leds_to_glow + 1):
            # Set the selected range of LEDs to the random color
            for i in range(NUM_LEDS):
                if offset <= i < offset + num_leds_to_glow:
                    np[i] = color  # Set to the random color
                else:
                    np[i] = (0, 0, 0)  # Turn off the LED
            
            np.write()  # Send the data to the LED strip
            time.sleep(0.1)  # Adjust the delay for animation speed
        
        # Wait before starting the next pattern
        time.sleep(0.5)

def main():
    snake_pattern()

# Run the main loop
main()

