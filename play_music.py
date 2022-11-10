import os
import random


#selects a song randomly from a given directory
def choose_rand_song(music_dir):
    file_list = os.listdir(music_dir)
    rnd_file = random.choice(file_list)
    return (music_dir + rnd_file)
