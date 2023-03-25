import os
import pygame
import subprocess
import keyboard
voice2 = 'en-IE-EmilyNeural'
voice3 = 'hi-IN-SwaraNeural'

def speak(data):
    voice = 'en-IE-EmilyNeural'
    filename = "data.mp3"

    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 1000
    chunks = [chunks[i:i + chunk_size]
              for i in range(0, len(chunks), chunk_size)]

    # Convert and play each chunk
    for chunk in chunks:
        text = ' '.join(chunk)
        command = f'edge-tts --voice "{voice}" --text "{text}"  --rate=+15%  --write-media "{filename}"'
        subprocess.run(command, shell=True)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")

        try:
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if keyboard.is_pressed('0'):
                    pygame.mixer.music.stop()
                    return False
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
    return True
