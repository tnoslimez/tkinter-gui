from pygame import mixer
import random


# Starting the mixer
mixer.init()
# Loading the songs/sound effects
try:
    mixer.music.load("Media/Naruto OST 1 -Naruto Main Theme.mp3")
    sound = mixer.Sound('Media/click.mp3')  # load sound
    sound2 = mixer.Sound('Media/end.mp3')  # load sound
    sound3 = mixer.Sound('Media/Disappointed sound effect.mp3')  #load sound

except:
    print("couldn't load sound files")



def background_music():
    # Start playing the background music
    mixer.music.set_volume(0.1)
    mixer.music.play()


def sound_effect(sound):
    try:
        if "click" == sound:
            sound = mixer.Sound('media/click.mp3')
            sound.set_volume(0.6)
            sound.play()
        elif "end" == sound:
            sound = mixer.Sound('media/end.mp3')
            sound.set_volume(0.2)
            sound.play()
        elif "bruh" == sound:
            sound = mixer.Sound('media/Disappointed sound effect.mp3')  # load sound
            sound.set_volume(0.3)
            sound.play()
        else:
            print("ERROR WITH SOUND")
    except:
        raise(UserWarning, "could not play sound :-(")






#######################################################################

def quitScript():
    pygame.quit()
    sys.exit(0)
    quit()



if __name__ == '__main__':
	print ('The sound module is being run by itself')
else:
	print ('Pygame sound imported')
