import serial
import binascii
import serial.tools.list_ports
import time

def find_cp210x_port():
    com_ports = serial.tools.list_ports.comports()
    for port, desc, hwid in com_ports:
        if "CP210x" in desc:
            return port
    return None

def display_ports_info():
    data = []
    com_ports = serial.tools.list_ports.comports()
    for port, desc, hwid in com_ports:
        temp = [port, desc]
        data.append(temp)
    
    headers = ["PORT", "Description"]
    make_table(headers, data)

def make_table(headers, data):
    max_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]
    header_row = "  |  ".join(f"{header:{width}}" for header, width in zip(headers, max_widths))
    print(header_row)
    print("-" * len(header_row))

    for row in data:
        row_str = "  |  ".join(f"{item:{width}}" for item, width in zip(row, max_widths))
        print(row_str)

def read_data_from_port(port):
    if not port:
        print('No CP210x port found')
        return

    try:
        ser = serial.Serial(port, 9600, timeout=1)
        command = b'\xB4\x05\x01\x01'
        ser.write(command)
        s = ser.read(100)
        ser.close()
        
        hex_data = binascii.hexlify(s).decode('utf-8')
        pairs = [hex_data[i:i+2] for i in range(0, len(hex_data), 2)]
        
        print(f'Received data: {s}')
        print(f'Hex data: {hex_data}')
        print(f'Pairs: {pairs}')
        print(f'Number of pairs: {len(pairs)}')

    except serial.SerialException as e:
        print(f"Error while reading from {port}: {e}")

def main():
    First_time = True
    display_ports_info()
    while True:
        live_port = find_cp210x_port()
        
        if live_port:
            time.sleep(0.1)
            if First_time:
                time.sleep(3)
                First_time = False
            read_data_from_port(live_port)
            input('Press Enter to continue...')
            print('')

        else:
            time.sleep(3)
            print('')
            print('No CP210x port found. Trying again in 3 second.')
            print('')
            display_ports_info()
            First_time = True


if _name_ == "_main_":
    main()
