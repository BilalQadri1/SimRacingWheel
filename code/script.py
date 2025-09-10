import serial
import vgamepad as vg
import time

# Set up serial communication with micro:bit
ser = serial.Serial('COM3', 115200, timeout=1)  #

# Create virtual Xbox controller
gamepad = vg.VX360Gamepad()

# Define button mapping
button_mapping = [
    vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
]

try:
    while True:
        # Read data from micro:bit
        data = ser.readline().decode('utf-8').strip()

        if data:
            try:
                values = list(map(int, data.split(',')))
                x_rotation, y_rotation = values[:2]
                pin_states = values[2:]

                # Map rotation values to joystick range (-32768 to 32767)
                x_axis = int(max(-32768, min(32767, x_rotation * 64)))
                y_axis = int(max(-32768, min(32767, y_rotation * 64)))

                # Update virtual controller joystick
                gamepad.left_joystick(x_value=x_axis, y_value=y_axis)

                # Update button states
                for i, state in enumerate(pin_states):
                    if i < len(button_mapping):
                        if state:
                            gamepad.press_button(button=button_mapping[i])
                        else:
                            gamepad.release_button(button=button_mapping[i])

                # Send updates to the virtual controller
                gamepad.update()

                print(f"X: {x_axis}, Y: {y_axis}, Pin states: {pin_states}")  # For debugging

            except ValueError:
                print("Invalid data received:", data)

        time.sleep(0.01)  # Small delay for stability

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()