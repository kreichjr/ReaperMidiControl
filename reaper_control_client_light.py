# Client script to send data to the server to run commands to 
# control my DAW

import tkinter as tk
import socket
import sys

HOST = '192.168.0.69'    # The remote host
PORT = 6666              # The same port as used by the server

def retry_button_cmd(socket_src):
    cmd = "retry"
    socket_src.sendall(cmd.strip().encode())

def undo_button_cmd(socket_src):
    cmd = "undo"
    socket_src.sendall(cmd.strip().encode())

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

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    if sw > sh:
        button_width = sw // 3
        button_height= sh // 3
    else:
        button_width = sw // 3
        button_height= sh // 4

    root.config(bg="black")

    title_label = tk.Label(root, bg="black", fg="red", text="Reaper Midi Control")#,font=("Comic Sans MS", (sh//12)))
    title_label.pack()

    quit_frame = tk.Frame(root, bg="black")#, width=button_width/2, height=button_height/2)
    quit_frame.pack()

    button_frame = tk.Frame(root, bg="black")
    button_frame.pack(side=tk.BOTTOM, fill=tk.X)

    undo_frame = tk.Frame(root, width=button_width//2, height=button_height//2)
    undo_frame.pack_propagate(0)
    undo_frame.pack(side=tk.LEFT)

    retry_frame = tk.Frame(root, width=button_width//2, height=button_height//2)
    retry_frame.pack_propagate(0)
    retry_frame.pack(side=tk.RIGHT)
    
    stop_frame = tk.Frame(button_frame, width=button_width, height=button_height)
    stop_frame.pack_propagate(0)
    stop_frame.pack(side=tk.LEFT)

    play_frame = tk.Frame(button_frame, width=button_width, height=button_height)
    play_frame.pack_propagate(0) 
    play_frame.pack(side=tk.LEFT)

    record_frame = tk.Frame(button_frame, width=button_width, height=button_height)
    record_frame.pack_propagate(0)
    record_frame.pack(side=tk.LEFT)

    retry_button = tk.Button(retry_frame, text="Retry\nRecording", command=lambda x=s: retry_button_cmd(x))
    undo_button = tk.Button(undo_frame, text="Undo", command=lambda x=s: undo_button_cmd(x))
    stop_button = tk.Button(stop_frame, text="Stop", command=lambda x=s: stop_button_cmd(x))
    play_button = tk.Button(play_frame, text="Play", command=lambda x=s: play_button_cmd(x))
    record_button = tk.Button(record_frame, text="Record", command=lambda x=s: record_button_cmd(x))
    quit_button = tk.Button(quit_frame, text="Quit", command=lambda x=s: quit_button_cmd(x))

    quit_button.pack()
    retry_button.pack(fill=tk.BOTH, expand=1)
    undo_button.pack(fill=tk.BOTH, expand=1)
    stop_button.pack(fill=tk.BOTH, expand=1)
    play_button.pack(fill=tk.BOTH, expand=1)
    record_button.pack(fill=tk.BOTH, expand=1)
    
    root.mainloop()

sys.exit(1)