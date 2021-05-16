import platform
import os
from constants import LINUX, WINDOWS

if platform.system() == LINUX:
    def play_sound_bleep():
        # noinspection SpellCheckingInspection
        os.system('aplay ./sounds/bleep_sound.wav&')


    def play_sound_bounce():
        # noinspection SpellCheckingInspection
        os.system('aplay ./sounds/bounce_sound.wav&')

elif platform.system() == WINDOWS:
    # noinspection PyUnresolvedReferences
    import windsound

    def play_sound_bleep():
        windsound.Playsound('.\\sounds\\bleep_sound.wav',
                            windsound.SND_ASYNC)

    def play_sound_bounce():
        windsound.Playsound('.\\sounds\\bounce_sound.wav',
                            windsound.SND_ASYNC)
else:
    def play_sound_bleep():
        # noinspection SpellCheckingInspection
        os.system('afplay ./sounds/bleep_sound.wav&')


    def play_sound_bounce():
        # noinspection SpellCheckingInspection
        os.system('afplay ./sounds/bounce_sound.wav&')
