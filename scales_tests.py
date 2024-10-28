import serial
from serial import PARITY_EVEN

ser = serial.Serial("COM3", baudrate=4800, timeout=0.5, parity=PARITY_EVEN)
ser.write(b"\x4A")
data = ser.read(5)
print(data)
weight = int.from_bytes(data[2:4], byteorder="little", signed=True) / 100


import win32file
import win32event
import win32api

# Open the COM port
hComm = win32file.CreateFile(
    r'COM1',  # Change this to your COM port
    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
    0,  # No sharing
    None,  # No security
    win32file.OPEN_EXISTING,
    0,  # No special flags
    None  # No template
)

# Set the COM port parameters
dc = win32file.GetCommState(hComm)
dc.BaudRate = win32file.CBR_4800
dc.ByteSize = 8
dc.StopBits = win32file.ONESTOPBIT
dc.Parity = win32file.NOPARITY
win32file.SetCommState(hComm, dc)

# Write data to the COM port
win32file.WriteFile(hComm, b'\x45')

# Read data from the COM port
overlapped = win32file.OVERLAPPED()
data = win32file.ReadFile(hComm, 1024, overlapped)

# Close the COM port
win32file.CloseHandle(hComm)
