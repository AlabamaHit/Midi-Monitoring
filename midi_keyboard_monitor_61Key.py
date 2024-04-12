import webbrowser
import mido
import tkinter as tk
from tkinter import messagebox
import threading
import pystray
from PIL import Image

class MidiKeyboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MIDI Keyboard")
        self.root.iconbitmap('midi.ico')
        self.root.protocol("WM_DELETE_WINDOW", self.minimize_to_tray)  # Handle window close event
        self.icon = pystray.Icon("MIDI Keyboard", Image.open("midi.ico"), "MIDI Keyboard", self.create_menu())
        self.device_name = "USB Midi  0"  # Automatically connect to "USB Midi 0"
        try:
            self.inport = mido.open_input(self.device_name)
            self.keys = [self.create_key(i) for i in range(36, 97)]  # Adjusted range to cover all keys on your keyboard
            for i, key in enumerate(self.keys):
                key.grid(row=i//12, column=i%12, padx=2, pady=2)  # Add padding
            self.root.update()
        except OSError:
            messagebox.showerror("Error", f"Could not connect to MIDI device: {self.device_name}")

    def create_key(self, i):
        note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        octave = i // 12 - 1
        note = note_names[i % 12]
        color = 'black' if '#' in note else 'white'  # Different colors for black and white keys
        key = tk.Button(self.root, text=f"{note}{octave}", width=2, height=1, relief='groove', bg=color)
        return key

    def handle_key_press(self, i):
        print(f"Key {i} was pressed")
        self.keys[i-36].config(bg='red')  # Turn red
        # Call a different function based on the key that was pressed
        if i == 60:  # C2
            self.action_for_key_36()
        elif i == 62:  # C#2
            self.action_for_key_37()
        elif i == 38:  # D2
            self.action_for_key_38()
        # Add more elif statements here for more keys

    def handle_key_release(self, i):
        print(f"Key {i} was released")
        self.keys[i-36].config(bg='SystemButtonFace')  # Return to original color

    def action_for_key_36(self):
        webbrowser.open_new("hutton.in")

    def action_for_key_37(self):
        webbrowser.open("google.com")

    def action_for_key_38(self):
        print("Action for key 38")

    # Add more action methods here for more keys

    def run(self):
        threading.Thread(target=self.read_midi).start()
        self.root.mainloop()

    def read_midi(self):
        try:
            msg = next(self.inport.iter_pending())
            if msg.type == 'note_on':
                if msg.velocity > 0:
                    self.handle_key_press(msg.note)
                else:
                    self.handle_key_release(msg.note)
        except StopIteration:
            pass
        finally:
            self.root.after(1, self.read_midi)  # Check for new MIDI messages every 1ms

    def minimize_to_tray(self):
        self.root.withdraw()
        self.root.after(10, self.icon.run)  # Delay execution of self.icon.run

    def show_window(self, icon, item):
        self.icon.stop()
        self.root.deiconify()

    def exit(self, icon, item):
        self.inport()
        self.icon.stop()
        self.root.destroy()

    def create_menu(self):
        return (pystray.MenuItem("Open", self.show_window), pystray.MenuItem("Exit", self.exit))

keyboard = MidiKeyboard()
keyboard.run()
