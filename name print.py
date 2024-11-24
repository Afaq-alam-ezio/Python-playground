import time
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_message(position):
    message = "Rakshu is pretty and beautiful"
    print(' ' * position + message)


def wave_print():
    max_width = 100  # Set a larger width for the console
    message_length = len("Rakshu is pretty and beautiful")

    while True:
        # Move message to the right
        for position in range(max_width - message_length):
            clear_console()
            print_message(position)
            time.sleep(0.05)  # Short delay for smoothness

        # Move message to the left
        for position in range(max_width - message_length, -1, -1):
            clear_console()
            print_message(position)
            time.sleep(0.05)  # Short delay for smoothness


if __name__ == "__main__":
    wave_print()
