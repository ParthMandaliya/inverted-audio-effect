import numpy as np
import time

# If VLC player is already installed
# python -m pip install python-vlc
# Other wise install the VLC player first
import vlc

from matplotlib import pyplot as plt
from multiprocessing import Process
from pydub import AudioSegment

# Load the original audio file
original_sound = AudioSegment.from_file("original_sound.wav")

# Invert the phase of the original sound
opposite_phase_sound = original_sound.invert_phase()

# Mix the two sounds together
mixed_sound = original_sound * opposite_phase_sound

# Export the opposite phase sound to a new file
opposite_phase_sound.export("opposite_phase_sound.wav", format="wav")

# Export the opposite phase sound to a new file
mixed_sound.export("mixed_sound.wav", format="wav")


def plot_waveform(titles, *audio_segments):
    plt.figure(figsize=(10, 4))

    for i, audio_segment in enumerate(audio_segments):
        samples = np.array(audio_segment.get_array_of_samples())
        time_ = np.linspace(
            0, len(samples) / audio_segment.frame_rate, num=len(samples)
        )
        label = titles[i] if titles else f"Sound {i + 1}"

        plt.plot(time_, samples, label=label)

    plt.title("Overlayed Waveforms")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()


def play_sound(file_path: str):
    player = vlc.MediaPlayer(file_path)
    print(f"'{file_path}' Playing started...")
    player.play()


print("Close the plot to start playing both audios")
plot_waveform(
    ["Original Sound", "Opposite Phase Sound", "Mixed Sound"],
    original_sound, opposite_phase_sound, mixed_sound
)


p1 = Process(target=play_sound, args=("./original_sound.wav",))
p2 = Process(target=play_sound, args=("./opposite_phase_sound.wav",))

p1.start()
p2.start()

time.sleep(60)
