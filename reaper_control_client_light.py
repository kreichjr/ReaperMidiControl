# Client script to send data to the server to run commands to 
# control my DAW

import tkinter as tk
import socket
import sys

HOST = '127.0.0.1'    # The remote host
PORT = 6666              # The same port as used by the server

def stop_button_cmd(socket_src):
    cmd = "stop"
    socket_src.sendall(cmd.strip().encode())

def play_button_cmd(socket_src):
    cmd = "play"
    socket_src.sendall(cmd.strip().encode())

def record_button_cmd(socket_src):
    cmd = "record"
    socket_src.sendall(cmd.strip().encode())

def quit_button_cmd(socket_src):
    cmd = "endme"
    socket_src.sendall(cmd.strip().encode())
    sys.exit(1)
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    root = tk.Tk()

    #sw = root.winfo_screenwidth()*5//6
    #sh = root.winfo_screenheight()*5//6
    #button_width = sw // 3
    #button_height= sh // 3

    #root.title("Reaper Midi Control Client")
    #root.geometry("%dx%d+0+0" % (sw, sh))
    #root.resizable(0,0)
    root.config(bg="black")

    #title_frame = tk.Frame(root, bg="black", height=button_height)
    #title_frame.pack_propagate(0)
    #title_frame.pack(side=tk.TOP, fill=tk.X)

    title_label = tk.Label(root, bg="black", fg="red", text="Reaper Midi Control")#,font=("Comic Sans MS", (sh//12)))
    title_label.pack()



    quit_frame = tk.Frame(root, bg="black")#, width=button_width/2, height=button_height/2)
    #quit_frame.pack_propagate(0)
    quit_frame.pack()

    button_frame = tk.Frame(root, bg="black")
    #button_frame.pack_propagate(0)
    button_frame.pack()

    stop_frame = tk.Frame(button_frame)
    stop_frame.pack(side=tk.LEFT)

    play_frame = tk.Frame(button_frame)
    play_frame.pack(side=tk.LEFT)

    record_frame = tk.Frame(button_frame)
    record_frame.pack(side=tk.LEFT)


    stop_button = tk.Button(stop_frame, text="Stop", command=lambda x=s: stop_button_cmd(x))
    play_button = tk.Button(play_frame, text="Play", command=lambda x=s: play_button_cmd(x))
    record_button = tk.Button(record_frame, text="Record", command=lambda x=s: record_button_cmd(x))
    quit_button = tk.Button(quit_frame, text="Quit", command=lambda x=s: quit_button_cmd(x))

    quit_button.pack()
    stop_button.pack()
    play_button.pack()
    record_button.pack()
    
    root.mainloop()




    #while True:
    #    user_input = input("\nEnter your command:")
    #    s.sendall(user_input.strip().encode())
    #    data = s.recv(1024)
    #    command = data.strip().decode()
    #    if command == "endme":
    #        break

sys.exit(1)
