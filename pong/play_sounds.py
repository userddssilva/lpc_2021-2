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
    import winsound


    def play_sound_bleep():
        winsound.PlaySound('.\\sounds\\bleep_sound.wav',
                           winsound.SND_ASYNC)


    def play_sound_bounce():
        winsound.PlaySound('.\\sounds\\bounce_sound.wav',
                           winsound.SND_ASYNC)
else:
    def play_sound_bleep():
        # noinspection SpellCheckingInspection
        os.system('afplay ./sounds/bleep_sound.wav&')


    def play_sound_bounce():
        # noinspection SpellCheckingInspection
        os.system('afplay ./sounds/bounce_sound.wav&')
