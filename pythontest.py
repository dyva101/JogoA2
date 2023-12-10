import pygame as py

py.init()
py.mixer.init()

jump_fx = py.mixer.Sound("assets\\jumpland44100.mp3")
death_fx = py.mixer.Sound("assets\\deathsound.mp3")

# Test the sounds
jump_fx.play()
py.time.delay(1000)  # Wait for 1 second
death_fx.play()

# Wait for the sounds to finish
py.time.delay(5000)