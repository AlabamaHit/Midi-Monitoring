# Midi-Monitoring
This allows you to run anything inside built on python with your midi keyboard. It runs completely in the background and don't even show in the tray.

#########
# X button does "NOT" close the program. READ NEXT SECTION!!!
#########
# FIRST THING TO DO!!!!!!!
First thing is run the get_midi_names.py in console. It will list out your midi names.
Now open the keyboard.pyw and change the "self.device_name" to your midi name. Mine here in code is USB 0 for example.
I have it on key 94 which for me is last black key to call the function to open the gui back. You can see in code.
This can be any key you want, I just set it to that. On my keyboard the key numbers start 36 and goes up to 96 (working on tested below)
This makes it so you can close the program. Other wise, open task manager and end the task running in "Python". This will only happen if you don't close the program.

That is it. Run the program you will see
![Screenshot 2024-04-26 204330](https://github.com/AlabamaHit/Midi-Monitoring/assets/79298983/f35a3138-3a83-45a7-9541-2ef2114f1921)

Just press the X it will close the window. The Midi will still be monitoring.
As noted above (Read it Please) press that key, you will see same window. To stop it, click Close Program.
This will close everything out.

# WORKING AND Tested on!

I have tested it with my Yahama YPT-300. I used a MIDI to USB cable, to connect. The setting on my keyboard is "PC 2" in the functions on the keyboard. I am running Windows 10.
