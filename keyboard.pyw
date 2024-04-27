import mido
import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
import time
import subprocess
import ctypes

class MidiKeyboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MIDI Keyboard")
        self.root.resizable(False, False)  # Disable window resizing
        self.root.state('zoomed')  # Prevent window from being maximized
        self.device_name = "USB Midi  0"  # Automatically connect to "USB Midi 0"
        try:
            self.inport = mido.open_input(self.device_name)
            close_button = tk.Button(self.root, text="Close Program", command=self.close_program)
            close_button.pack(padx=20, pady=20)  # Add padding around the button
            self.root.protocol("WM_DELETE_WINDOW", self.hide_app)  # Handle close button to hide the app
            self.root.withdraw()  # Hide the app initially
            self.root.update_idletasks()  # Ensure all widgets are updated
            self.center_window()  # Center the window on the monitor
            self.root.deiconify()  # Show the window after centering
            self.last_key_press_time = time.time()
            self.debounce_time = 0.5  # Adjust debounce time as needed
        except OSError:
            messagebox.showerror("Error", f"Could not connect to MIDI device: {self.device_name}")

    def center_window(self):
        # Center the window on the monitor
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f'+{x}+{y}')

    def handle_key_press(self, i):
        current_time = time.time()
        if current_time - self.last_key_press_time > self.debounce_time:
            # Trigger action associated with MIDI key press
            print(f"Key {i} was pressed")
            if i == 36:  # MIDI note number 36
                webbrowser.open_new_tab("https://www.youtube.com")
            elif i == 38:  # MIDI note number 38
                webbrowser.open_new_tab("https://www.facebook.com/messages")
            elif i == 40:  # MIDI note number 40
                webbrowser.open_new_tab("https://www.instagram.com")
            elif i == 42:  # MIDI note number 42
                try:
                    # Replace "reaper.exe" with the actual executable name if necessary
                    subprocess.Popen(["C:\\Program Files\\REAPER (x64)\\reaper.exe"])
                except FileNotFoundError:
                    messagebox.showerror("Error", "Reaper executable not found.")

            elif i == 94:  # MIDI note number 94
                self.show_app()  # Bring up the GUI when note 94 is played

            self.last_key_press_time = current_time

    def run(self):
        threading.Thread(target=self.read_midi).start()
        self.root.mainloop()

    # Method to hide the application
    def hide_app(self):
        self.root.withdraw()

    # Method to bring the application back to the foreground
    def show_app(self):
        self.root.deiconify()

    # Method to close the program entirely
    def close_program(self):
        if hasattr(self, 'inport'):
            self.inport.close()
        self.root.destroy()

    # Reads the midi and reports to console??
    def read_midi(self):
        for msg in self.inport:
            if msg.type == 'note_on':
                self.handle_key_press(msg.note)

keyboard = MidiKeyboard()
keyboard.run()
