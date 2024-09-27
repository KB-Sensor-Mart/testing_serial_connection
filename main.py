import serial
import time

# Configure the serial port
port = 'COM2'
baud_rate = 115200

try:
    # Attempt to open the serial port
    print(f"Attempting to open port {port} at baud rate {baud_rate}...")
    ser = serial.Serial(port, baud_rate, timeout=1)

    # Check if the port is open
    if ser.is_open:
        print(f"Successfully opened {port}")
    else:
        print(f"Failed to open {port}")
    
    # Give some time for the connection to establish
    time.sleep(2)
    
    print(f"Listening on {port} at {baud_rate} baud rate...")

    while True:
        # Check if there's any data waiting in the serial buffer
        if ser.in_waiting > 0:
            print(f"Data available: {ser.in_waiting} bytes")  # Debugging: Shows the number of bytes available
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received: {data}")
        else:
            print("No data available.")  # Debugging: No data received from the port

        # Additional debug: Check if data is available on a byte-by-byte level
        raw_data = ser.read(ser.in_waiting or 1)
        if raw_data:
            print(f"Raw data bytes: {raw_data}")

        # Pause briefly to avoid spamming the console
        time.sleep(1)

except serial.SerialException as e:
    print(f"Serial exception occurred: {e}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
