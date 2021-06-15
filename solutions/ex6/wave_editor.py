"""
AUTHOR: fam
This file will edit your wav (type of audio file) file,
the way that you want it to.
ENJOY!
"""
from wave_helper import *
from os import system, name
import math

print("Welcome!")
WAVE_LIST = []
SAMPLE_RATE = 2000  # it depends if the file exist or not
audio = []  # same
AUDIO_DATA_REVERSED = []
AUDIO_DATA_REMOVED = []
AUDIO_DATA_SPEED_UP = []
AUDIO_DATA_SPEED_DOWN = []
VOLUME_UP = []
VOLUME_DOWN = []
MAXIMUM_VOLUME = 32767
LOWEST_VOLUME = -32768
AUDIO_DATA_REVERB = []
PI = math.pi
FREQUENCIES_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Q']
FREQUENCIES = [440, 494, 523, 587, 659, 698, 784, 0]
DEFAULT_WAVES_SAMPLES = 125


def opening_menu():
    print("""
Please choose one of the options below: 
1. Edit WAV file.
2. Compose a tune with the right format for a WAV file.
3. Exit the program.
    """)
    open_input = 0
    while open_input not in [1, 2, 3]:
        open_input = int(input())
        if open_input in [1, 2, 3]:
            break
        print("[!] PLEASE SELECT ONE OF THE OPTIONS ABOVE")
    return open_input


def edit_wav_menu():
    """
    this func will print and check if the input that the user have input
    is right, otherwise it will print an error.
    :return: the input after been checked
    """
    print("""
What do you want to change in your WAV file?
1. Reverse.
2. Removing audio.
3. Speed up.
4. Speed down.
5. Volume up.
6. Volume down.
7. Reverb filter.
8. Exit to the end menu.
    """)
    wav_input = 0
    while wav_input not in [1, 2, 3, 4, 5, 6, 7, 8]:
        wav_input = int(input())
        if wav_input in [1, 2, 3, 4, 5, 6, 7, 8]:
            break
        print("[!] PLEASE SELECT ONE OF THE OPTIONS ABOVE")
    return wav_input


def wave_load_file(filename):
    """
    this func will load the wav file, as an audio data format, example:
    [[1,2], [3,4] [5,6]]
    :param filename: the name of the wav file
    :return: 1 if the func successfully loaded the wav file
    """
    global WAVE_LIST, audio, SAMPLE_RATE
    if filename[-4:] == '.wav':  # not must to specify the extension
        pass
    else:
        filename += '.wav'
    if load_wave(filename) == -1:
        print("There was a problem with the file you selected."
              " Please try again.")
        exit()
    else:
        WAVE_LIST = load_wave(filename)
        SAMPLE_RATE = WAVE_LIST[0]
        audio = WAVE_LIST[1]
    return 1


def reverse_audio(audio_data):
    """
    this func will reverse the audio data, by just reversing the values in the audio_data list
    :param audio_data: the data with the audio values in
    :return: the final list after being reversed
    """
    global AUDIO_DATA_REVERSED
    AUDIO_DATA_REVERSED = []  # so if he want to do the same request, it will reset this list
    AUDIO_DATA_REVERSED = [audio_data[-i] for i in range(1, len(audio_data))]  # just flip the list
    AUDIO_DATA_REVERSED.append(audio_data[0])  # -0 is 0, so first one won't be the last one, and its not right
    # if we want to reverse it.
    return AUDIO_DATA_REVERSED


def remove_audio(audio_data):  # TODO fix remove audio
    """
    this func will remove the audio of a wav file
    :param audio_data: the data with the audio values in
    :return: the final list after the audio has been removed
    """
    global AUDIO_DATA_REMOVED
    AUDIO_DATA_REMOVED = []  # so if he want to do the same request, it will reset this list
    for i in audio_data:
        tmp = []
        for j in i:  # 1 index is the audio_data index
            if j > 0:
                tmp_data = j * -1
                if tmp_data < LOWEST_VOLUME:
                    tmp_data = LOWEST_VOLUME
            else:
                tmp_data = j
            tmp.append(tmp_data)
        AUDIO_DATA_REMOVED.append(tmp)
    return AUDIO_DATA_REMOVED


def speed_up(audio_data):
    """
    this func will speed the audio by 2.
    :param audio_data: the file with all numbers representing the audio
    :return: the final list after the audio has been speed up
    """
    global AUDIO_DATA_SPEED_UP
    AUDIO_DATA_SPEED_UP = []  # so if he want to do the same request, it will reset this list
    for i in range(len(audio_data)):
        if i % 2 == 0:  # don't forget, 'i' is starting from index 0
            AUDIO_DATA_SPEED_UP.append(audio_data[i])
        else:
            continue
    return AUDIO_DATA_SPEED_UP


def speed_down(audio_data):
    """
    this func will speed down the audio, and make it slower.
    :param audio_data: the data with the audio values in
    :return: the final list after the audio has been speed down
    """
    global AUDIO_DATA_SPEED_DOWN
    AUDIO_DATA_SPEED_DOWN = []  # so if he want to do the same request, it will reset this list
    prev_audio_data = []
    for _ in audio_data:  # if i would do prev_audio_data = AUDIO_DATA, from some reason
        # prev_audio_data would get updated after i insert down below.
        prev_audio_data.append(_)
    for i in range(len(audio_data) - 1):
        tmp = []
        for j in range(2):  # two channels (right side - left side)
            avg = (audio_data[i][j] + audio_data[i + 1][j]) / 2
            tmp.append(int(avg))
        AUDIO_DATA_SPEED_DOWN.append(tmp)
    for x in range(len(prev_audio_data)):  # index error if not -1, nothing is added after last index in AUDIO_DATA
        data = audio_data[x]
        AUDIO_DATA_SPEED_DOWN.insert(x + x, data)
    return AUDIO_DATA_SPEED_DOWN


def if_up_down_max_low_volume_up(data1, data2):
    """
    this func will multiply by 1.2 every data in one audio data,
    and check if it passed the maximum volume, or the lowest volume
    :param data1: first data in one audio data
    :param data2: second data in one audio data
    :return: the two audio data after being multiplied, and if they have been changed or not
    """
    changed_1 = False
    changed_2 = False
    if data1 * 1.2 > MAXIMUM_VOLUME:
        data1 = MAXIMUM_VOLUME
        changed_1 = True
    elif data1 * 1.2 < LOWEST_VOLUME:
        data1 = LOWEST_VOLUME
        changed_1 = True
    elif data2 * 1.2 > MAXIMUM_VOLUME:
        data2 = MAXIMUM_VOLUME
        changed_2 = True
    elif data2 * 1.2 < LOWEST_VOLUME:
        data2 = LOWEST_VOLUME
        changed_2 = True
    return data1, data2, changed_1, changed_2


def volume_up(audio_data):
    """
    this func will make multiply each data in a audio data by 1.2;
    the func will also call the function 'if_up_down_max_low_volume_up',
    and check if the data's in one audio data, have crossed the maximum volume
    or the lowest volume.
    :param audio_data: the data with the audio values in
    :return: the final list after it been volumed up
    """
    global VOLUME_UP
    VOLUME_UP = []  # so if he want to do the same request, it will reset this list
    for i in audio_data:
        data = if_up_down_max_low_volume_up(i[0], i[1])
        if data[2]:
            data1 = data[0]  # one channel
        else:
            data1 = int(data[0] * 1.2)
        if data[3]:
            data2 = data[1]  # second channel
        else:
            data2 = int(data[1] * 1.2)
        final = [data1, data2]
        VOLUME_UP.append(final)
    return VOLUME_UP


def volume_down(audio_data):
    """
    this func will volume down, with dividing by 1.2.
    :param audio_data: the data with the audio values in
    :return: the final list after it been volumed down
    """
    global VOLUME_DOWN
    VOLUME_DOWN = []  # so if he want to do the same request, it will reset this list
    for i in audio_data:
        data1 = int(i[0] / 1.2)  # one channel
        data2 = int(i[1] / 1.2)  # second channel
        final = [data1, data2]
        VOLUME_DOWN.append(final)
    return VOLUME_DOWN


def reverb(audio_data):
    """
    this func will make a reverb effect for the audio.
    :param audio_data: the data with the audio values in
    :return: the final list after it been revered.
    """
    global AUDIO_DATA_REVERB
    AUDIO_DATA_REVERB = []  # so if he want to same request, it will reset this list
    for i in range(0, len(audio_data)):
        data = audio_data[i]  # we will always use it, even if its first audio data or last
        if i == 0:  # if we are on the first audio data
            data1 = audio_data[i + 1]
            first_audio_data_num = int((data[0] + data1[0]) / 2)
            second_audio_data_num = int((data[1] + data1[1]) / 2)  # just for the other next audio data
        else:
            if i != len(audio_data) - 1:
                data1 = audio_data[i + 1]  # i does not equal 0 or -1
                data2 = audio_data[i - 1]
                first_audio_data_num = int((data[0] + data1[0] + data2[0]) / 3)
                second_audio_data_num = int((data[1] + data1[1] + data2[1]) / 3)
            else:  # i is len(audio_data)
                data2 = audio_data[i - 1]
                first_audio_data_num = int((data[0] + data2[0]) / 2)
                second_audio_data_num = int((data[1] + data2[1]) / 2)
        AUDIO_DATA_REVERB.append([first_audio_data_num, second_audio_data_num])
    return AUDIO_DATA_REVERB


def if_one(option):
    """
    this func will be executed the the user have chose the option 1
    in the starting menu.
    :param option: what option the user chose
    :return:
    """
    global audio
    if option == 1:
        filename_wav = input("Please input the name of the wav file: ")
        wave_load_file(filename_wav)
    else:
        pass
    wav_input_final = 0
    while wav_input_final != 8:
        wav_input_final = edit_wav_menu()
        if wav_input_final == 1:
            audio = reverse_audio(audio)
        elif wav_input_final == 2:
            audio = remove_audio(audio)
        elif wav_input_final == 3:
            audio = speed_up(audio)
        elif wav_input_final == 4:
            audio = speed_down(audio)
        elif wav_input_final == 5:
            audio = volume_up(audio)
        elif wav_input_final == 6:
            audio = volume_down(audio)
        else:
            audio = reverb(audio)
        print("Successfully changed!")
    save_file = input("What name do you want to save the results to? ")
    save_wave(SAMPLE_RATE, audio, save_file)
    return


def make_music():
    """
    this func will make music for you by an instruction file.
    :return: the final list with the audio data's in
    """
    filename = input("Please input the instructions file: ")
    try:
        with open(filename, 'r') as FILE:
            pattern = FILE.readline().split()  # TODO add an option for multiple lines
            for char in pattern:
                index = pattern.index(char)
                if char.isalpha():  # to see if its not the 'time' to play the tune
                    index1 = FREQUENCIES_CHARS.index(char)
                    seconds = int(pattern[index + 1])  # the seconds, its always the second
                    frequency = FREQUENCIES[index1]
                    if char == 'Q':  # 'Q' is silence, so just zero for 'seconds' seconds
                        for i in range(1, seconds + 1):
                            audio.append([0, 0])
                        continue
                    samples_per_cycle = 2000/frequency  # this is the equations
                    for i in range(1, (seconds + 1)*DEFAULT_WAVES_SAMPLES):  # 1/16 second is 125 samples,
                        # so 2000 samples is one second.
                        equations = int(MAXIMUM_VOLUME * math.sin(PI * 2 * i/samples_per_cycle))  # also the equation
                        audio.append([equations, equations])
        return audio
    except FileNotFoundError:
        print("Instructions file have not been found.")


def main():
    """
    main function, it will clear cmd/terminal and execute functions.
    :return: exit the script
    """
    open_input = 0
    while open_input != 3:  # 3 is to exit
        open_input = opening_menu()
        if name == 'nt':  # for windows
            clear_command = 'cls'
        else:  # for linux
            clear_command = 'clear'
        if open_input == 1:  # edit a wav file
            system(clear_command)  # clear the terminal/cmd
            if_one(1)
            print("\nSuccessfully saved the file!")
        elif open_input == 2:  # make a music from text file
            system(clear_command)
            make_music()
            system(clear_command)
            if_one(2)
            print("\nSuccessfully saved the file!")
    print("Goodbye!")
    return exit()


if __name__ == '__main__':
    main()
