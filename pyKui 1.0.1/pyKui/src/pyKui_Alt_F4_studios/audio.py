from pyKui_Alt_F4_studios.imports import *
from pyKui_Alt_F4_studios.errors import *
from pyKui_Alt_F4_studios.variables import *

class audio:
    def init():
        ### Init the audio module

        global initedAudio

        pygame.mixer.init()
        
        initedAudio = True

    def uninit():
        ### Uninit the audio module
        
        global initedAudio

        initedAudio = False

    def preInit(frequency = 44100, size = -16, channels=2, buffer=512, devicename = None, allowedchanges = AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE):
        global initedAudio

        pygame.mixer.init()
        
        initedAudio = True
        
    class musicPlayer:
        def play(audioPath = "", loops = 0, start = 0.0, fade_ms = 0):
            ### Load audio of the given path
            
            if initedAudio:
                print("Playing")
                pygame.mixer.music.load(audioPath)
                pygame.mixer.music.play(loops, start, fade_ms)
            
            else:
                raise pyKuiAudioNotInit(audioNotInitErrorMessage)

        def stop():
            ### Stop musicPlayer

            pygame.mixer.stop()

        def pause():
            ### Pause audio

            pygame.mixer.pause()
            
        def unpause():
            pygame.mixer.unpause()

        def fadeout(time):
            pygame.mixer.fadeout(time)
