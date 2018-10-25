# The goal is to write server software that listens for input from custom client software
# to remotely control the DAW Reaper via Midi Signals

# Helpful notes:
# get_device_info(an_id) -> (interf, name, input, output, opened)
# Midi Note 69 = Undo
# Midi Note 70 = Stop
# Midi Note 72 = Play
# Midi Note 74 = Record

import pygame
import pygame.midi
import socket
import time
import sys

HOST = ""
PORT = 6666

class ReaperControlServer:

    def __init__(self):
        #initialize midi
        pygame.midi.init()
        
        self.port_input  = -1
        self.port_output = -1
        
        #prints midi device info
        for id in range(pygame.midi.get_count()):
            test_port = pygame.midi.get_device_info(id)[1].decode("UTF-8")
            if test_port == "KReichJr's Port":
                if pygame.midi.get_device_info(id)[2] == 1:
                    self.port_input = id
                elif pygame.midi.get_device_info(id)[3] == 1:
                    self.port_output = id
                
        if self.port_input < 0 or self.port_output < 0:
            print("Missing required ports!")
            sys.exit(1)

        self.midi_out = pygame.midi.Output(self.port_output)
        self.midi_in  = pygame.midi.Input(self.port_input)

        self.midi_out.set_instrument(0)

    def undoEdit(self):
        self.midi_out.note_on(69,127)
        self.midi_out.note_off(69,127)
    
    def stopSong(self):
        self.midi_out.note_on(70,127)
        self.midi_out.note_off(70,127)
    
    def playSong(self):
        self.midi_out.note_on(72,127)
        self.midi_out.note_off(72,127)
    
    def recordSong(self):
        self.midi_out.note_on(74,127)
        self.midi_out.note_off(74,127)

    def endMidi(self):
        self.midi_in.close()
        self.midi_out.close()
        pygame.midi.quit()

main_program = ReaperControlServer()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    print("\n\nListening for client connections...\n")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            command = data.strip().decode()
            print(command)
            if command == "stop":
                main_program.stopSong()
            elif command == "play":
                main_program.playSong()
            elif command == "record":
                main_program.recordSong()
            elif command == "undo":
                main_program.undoEdit()
            elif command == "endme":
                main_program.endMidi()
                sys.exit(1)
            else:
                continue
            if not data: break
            conn.sendall(data)

main_program.endMidi()
sys.exit(1)

#while True:
#    command = input("\nEnter your command. Choices are 'stop' or 'play' or 'record' or 'endme': ")
#    if command == "stop":
#        main_program.stopSong()
#    elif command == "play":
#        main_program.playSong()
#    elif command == "record":
#        main_program.recordSong()
#    elif command == "endme":
#        main_program.endMidi()
#        sys.exit(1)
#    else:
#        continue
