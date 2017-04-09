# coding:utf-8
import mp3play

filename = r'Z:\1.mp3'
mp3 = mp3play.load(filename)

mp3.play()

# Let it play for up to 30 seconds, then stop it.
import time

time.sleep(min(mp3.seconds(), mp3.seconds()))
mp3.stop()
