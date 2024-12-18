import pyautogui as pg
import socket
import threading
import time
import keyboard

pg.FAILSAFE = False

host = input("host: ")
port = 12345

def handle_keyboard_event(client_socket):
    def on_key_event(event):
        # Capture and send keyboard events
        key_info = f"key:{event.name}:{event.event_type}"
        try:
            client_socket.send(key_info.encode())
        except:
            print("Connection error")
            keyboard.unhook_all()

    # Hook keyboard events
    keyboard.hook(on_key_event)
    keyboard.wait()

def setup_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Threads for different tasks
    keyboard_thread = threading.Thread(target=handle_keyboard_event, args=(client_socket,))
    server_command_thread = threading.Thread(target=process_server_commands, args=(client_socket,))

    keyboard_thread.start()
    server_command_thread.start()

    keyboard_thread.join()
    server_command_thread.join()

def process_server_commands(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()

            # Mouse and Click Events
            if data == "lc":
                pg.click()
            elif data == "rc":
                pg.click(button="right")
            elif data == "dc":
                pg.click(clicks=2)

            # Keyboard Special Actions
            elif data == "nl":
                pg.press("enter")
            elif data == "del":
                pg.press("backspace")
            
            # Text Input
            elif data.startswith("cde:"):
                text = data.replace("cde:", "")
                pg.write(text)
            
            # Keyboard Event Handling
            elif data.startswith("key:"):
                _, key, event_type = data.split(":")
                
                # Handle different keyboard event types
                if event_type == "down":
                    pg.keyDown(key)
                elif event_type == "up":
                    pg.keyUp(key)
            
            # Mouse Movement
            else:
                try:
                    x, y = map(int, data.split())
                    pg.moveTo(x, y)
                except ValueError:
                    print(f"Invalid data format: {data}")

        except Exception as e:
            print(f"Server command error: {e}")
            break

# Main execution
if __name__ == "__main__":
    setup_connection()
