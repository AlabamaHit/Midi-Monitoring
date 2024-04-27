# Midi-Monitoring
This allows you to run anything with your midi keyboard built with python. It runs completely in the background and don't even show in the tray.

#########
# X button does "NOT" close the program. READ NEXT SECTION!!!
#########
# FIRST THING TO DO!!!!!!!
First thing is run the get_midi_names.py in console. It will list out your midi names.

Now open the keyboard.pyw and change the "self.device_name" to your midi name. Mine here in code is USB 0 for example.

I have it on key 94 which for me is last black key to call the function to open the gui back. You can see in code.

This can be set to any key you want, I just set it to that. On my keyboard the key numbers start 36 and goes up to 96 (working on tested below)

# Closing the Program:
Press the key you set above. The gui will come back up. Use the button Close Program, this will close it all the way out.
NOTE: If you press X it will just make the gui go away, to close the program you Must use the "Close Program" button.

That is it. Run the program you will see
![Screenshot 2024-04-26 204330](https://github.com/AlabamaHit/Midi-Monitoring/assets/79298983/f35a3138-3a83-45a7-9541-2ef2114f1921)

Just press the X it will close the window. The Midi will still be monitoring.

As noted above (Read it Please) press that key, you will see same window. To stop it, click Close Program.

This will close everything out.

Remember it runs 100% in the background, it will Not be in the system tray or taskbar. That is why you need to set that function to a key. I have it again, on 94 so in code 
you can see how to get it to call and set it to any key you want. 

# If you ever wonder if it's running? Click on the key you have for opening the gui back. If it does not open it's closed. You can verify in task manager if you want but not neccessary.

# WORKING AND Tested on!

I have tested it with my Yahama YPT-300. I used a MIDI to USB cable, to connect. The setting on my keyboard is "PC 2" in the functions on the keyboard. I am running Windows 10.

# I HOPE THIS HELPS SOMEONE OUT. I LOOKED FOR SO LONG FOR A SAFE WAY TO MAKE MY MIDI DO THIS
 I used to use HID macros, but I wanted something smaller because I only needed MIDI for running tasks. So, I set out to write this. 
 I'm sure this will work on any MIDI device; the only real changes you may need to make are the key numbers.

# PLEASE LET ME KNOW IF IT HELPED YOU OUT. I'M CURIOUS IF THIS REACHES SOMEONE THAT NEEDS A TOOL LIKE THIS.
 If you change the extension to .py instead of .pyw, the terminal window will remain visible on the screen. 
 The .pyw extension instructs the script to run without displaying the terminal window. This behavior is specific to Windows as far as I'm aware.
