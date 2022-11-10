#imports for DeepSpeech
import time, logging
from datetime import datetime
import threading, collections, queue, os, os.path
import deepspeech
import numpy as np
import pyaudio
import wave
import webrtcvad
from halo import Halo
from scipy import signal

#imports for this project
import subprocess
import duckduck
import weather_update
import pyttsx3
import al_jazeera_news
import crypto_update
import tell_time
import lcd_display
import joke_machine
import play_music
from pygame import mixer
import fact_machine
import led_controls
import note_taking
import chromecast_controls
import light_temp_sensor
import set_timer
import read_notes



#function which sends text to the tts engine to be spoken
def jarvis_speak(text):
    #execute bash command to mute the microphone so that
    #tts output doesn't cause a feedback loop
    turn_off_mic = subprocess.run(["amixer", "-c", "1", "set", "Mic", "nocap"], capture_output=True)

    #turn on leds
    led_thread = threading.Thread(target=led_controls.led_sequence, args=())
    led_thread.start()

    #convert the text to speech and read it
    tts_engine.say(text)
    tts_engine.runAndWait()

    #led remains on only for duration of speech
    led_controls.led_loop = False

    #turn microphone back on
    turn_on_mic = subprocess.run(["amixer", "-c", "1", "set", "Mic", "cap"], capture_output=True)


#The function which processes speech input from user
#if a command is detected then the corresponding program will run
def process_speech(text):

    #searches duckduckgo for the term following the word 'search'
    if "search" in text:
        word_loc = text.find("search") + 6
        if len(text[word_loc:]) > 1:
            search_res = duckduck.searchforterm(text[word_loc:])
            jarvis_speak(search_res)

    #starts a timer for given amount of time
    elif "timer" in text:
        timer_loc = text.find("timer") + 6
        timer_text = text[timer_loc:]

        timer_list = set_timer.check_timer_valid(timer_text)

        #set timer if first value in list is true
        if timer_list[0]:
            timer_thread = threading.Thread(target=set_timer.new_timer, args=([timer_list[1]]))
            timer_thread.start()
            jarvis_speak("Timer Set")
        else:
            timer_thread = threading.Thread(target=set_timer.play_error_tone, args=())
            timer_thread.start()
            jarvis_speak("Error setting timer")

    #searches for current weather forecast in given location
    elif "weather" in text or "whether" in text:
        word_loc = text.find("weather") + 8
        if word_loc < 0:
            word_loc = text.find("whether") + 8
        if len(text[word_loc+1:]) > 0:
            weather_report = weather_update.get_forecast_report(text[(word_loc+1):].strip())
            jarvis_speak(weather_report)

    #reads the reminders given input via the note command
    elif "reminders" in text:
        notes_text = read_notes.process_notes("./notes")
        jarvis_speak(notes_text)

    #checks al-jazeera for current top stories
    elif "news" in text:
        jarvis_speak("Generating news report")
        news_report = al_jazeera_news.get_news_report()
        jarvis_speak(news_report)

    #checks for current value of given crypto values
    elif "stocks" in text:
        crypto_values = crypto_update.get_crypto_data("USD")
        for crypto_value in crypto_values:
            lcd_display.write_new_message(crypto_value.replace(":", "\n$"))
            jarvis_speak(crypto_value + " Dollars")
            time.sleep(2)
        lcd_display.clear_screen()

    #reads out current time and displays clock on the lcd screen
    elif "clock" in text:
        time_thread = threading.Thread(target=show_time, args=())
        time_thread.start()

    #prints ip address of pi to the lcd screen
    elif "ip address" in text:
        ip_thread = threading.Thread(target=lcd_display.display_ip, args=())
        ip_thread.start()

    #reads the setup and punchline of a joke
    elif "joke" in text:
        jarvis_jka, jarvis_jkb = joke_machine.gen_joke()
        jarvis_speak(jarvis_jka)
        time.sleep(1)
        jarvis_speak(jarvis_jkb)

    #plays random song from the music/ directory
    elif "play music" in text:
        current_song = play_music.choose_rand_song("./music/")
        mixer.pre_init()
        mixer.init(buffer=1024)
        mixer.music.load(current_song)
        mixer.music.play()

    #stops music if it is currently playing
    elif "stop music" in text:
        mixer.music.pause()

    #reads a random fact
    elif "fact" in text:
        jarvis_fact = fact_machine.gen_fact()
        jarvis_speak(jarvis_fact)

    #writes a new note to the notes/ directory
    elif "note " in text:
        note_loc = text.find("note ")
        note_content = text[note_loc+5:]
        note_taking.write_note(note_content)
        jarvis_speak("Note written")

    #casts a random video from a given playlist to a nearby chromecast
    elif "cast video" in text:
        jarvis_speak("Casting video")
        vid_id = chromecast_controls.get_video_from_playlist("PLNXV9Mb7egjGE5GigSZ9gSDETb8ib64W7")
        chromecast_controls.cast_to_device("Living Room TV", vid_id)

    #if no command recognised
    else:
        jarvis_speak("I'm sorry, I didn't understand that...")



#function to process the time from another program and
#print it to lcd screen while saying it via tts
def show_time():
    current_time = tell_time.time_now()
    lcd_display.write_new_message(str(current_time[0:2]) + ":" + str(current_time[2:4]) + ":" + str(current_time[4:6]) + " " + str(current_time[6:8]))
    jarvis_speak(str(current_time[0:2]) + ":" + str(current_time[2:4]) + " " + str(current_time[6:8]))

    #time remains on screen for ~20 seconds
    for i in range(20):
        #format the time correctly to be printed on screen
        time_string = str(current_time[0:2]) + ":" + str(current_time[2:4]) + ":" + str(current_time[4:6]) + " " + str(current_time[6:8])
        lcd_display.write_new_message(time_string)
        time.sleep(1)
        current_time = tell_time.time_now()

    lcd_display.clear_screen()







#
#setup before running the main function
#


logging.basicConfig(level=20)

#initialise the tts engine
tts_engine = pyttsx3.init()

#read the voice configuration from the file and alter the voice accordingly
with open("config/voiceconfig.csv") as config_file:
    voice_data = config_file.readline()

#split the data at each comma
voice_data = voice_data.split(",")

#update each of the properties accordingly
tts_engine.setProperty("voice", voice_data[0])
tts_engine.setProperty("rate", int(voice_data[1]))
tts_engine.setProperty("volume", voice_data[2])
tts_engine.runAndWait()

#ensure that the microphone is set to capture
subprocess.run(["amixer", "-c", "1", "set", "Mic", "cap"])

#ensure that lcd screen is clear
lcd_display.clear_screen()

#start the arduino sensors program in a different thread
sensor_thread = threading.Thread(target=light_temp_sensor.read_sensors, args=())
sensor_thread.start()


#greet the user with their custom name
jarvis_speak("Hello, " + voice_data[3])




class Audio(object):
    """Streams raw audio from microphone. Data is received in a separate thread, and stored in a buffer, to be read from."""

    FORMAT = pyaudio.paInt16
    # Network/VAD rate-space
    RATE_PROCESS = 16000
    CHANNELS = 1
    BLOCKS_PER_SECOND = 50

    def __init__(self, callback=None, device=None, input_rate=RATE_PROCESS, file=None):
        def proxy_callback(in_data, frame_count, time_info, status):
            #pylint: disable=unused-argument
            if self.chunk is not None:
                in_data = self.wf.readframes(self.chunk)
            callback(in_data)
            return (None, pyaudio.paContinue)
        if callback is None: callback = lambda in_data: self.buffer_queue.put(in_data)
        self.buffer_queue = queue.Queue()
        self.device = device
        self.input_rate = input_rate
        self.sample_rate = self.RATE_PROCESS
        self.block_size = int(self.RATE_PROCESS / float(self.BLOCKS_PER_SECOND))
        self.block_size_input = int(self.input_rate / float(self.BLOCKS_PER_SECOND))
        self.pa = pyaudio.PyAudio()

        kwargs = {
            'format': self.FORMAT,
            'channels': self.CHANNELS,
            'rate': self.input_rate,
            'input': True,
            'frames_per_buffer': self.block_size_input,
            'stream_callback': proxy_callback,
        }

        self.chunk = None
        # if not default device
        if self.device:
            kwargs['input_device_index'] = self.device
        elif file is not None:
            self.chunk = 320
            self.wf = wave.open(file, 'rb')

        self.stream = self.pa.open(**kwargs)
        self.stream.start_stream()

    def resample(self, data, input_rate):
        """
        Microphone may not support our native processing sampling rate, so
        resample from input_rate to RATE_PROCESS here for webrtcvad and
        deepspeech

        Args:
            data (binary): Input audio stream
            input_rate (int): Input audio rate to resample from
        """
        data16 = np.fromstring(string=data, dtype=np.int16)
        resample_size = int(len(data16) / self.input_rate * self.RATE_PROCESS)
        resample = signal.resample(data16, resample_size)
        resample16 = np.array(resample, dtype=np.int16)
        return resample16.tostring()

    def read_resampled(self):
        """Return a block of audio data resampled to 16000hz, blocking if necessary."""
        return self.resample(data=self.buffer_queue.get(),
                             input_rate=self.input_rate)

    def read(self):
        """Return a block of audio data, blocking if necessary."""
        return self.buffer_queue.get()

    def destroy(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

    frame_duration_ms = property(lambda self: 1000 * self.block_size // self.sample_rate)

    def write_wav(self, filename, data):
        logging.info("write wav %s", filename)
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        # wf.setsampwidth(self.pa.get_sample_size(FORMAT))
        assert self.FORMAT == pyaudio.paInt16
        wf.setsampwidth(2)
        wf.setframerate(self.sample_rate)
        wf.writeframes(data)
        wf.close()


class VADAudio(Audio):
    """Filter & segment audio with voice activity detection."""

    def __init__(self, aggressiveness=3, device=None, input_rate=None, file=None):
        super().__init__(device=device, input_rate=input_rate, file=file)
        self.vad = webrtcvad.Vad(aggressiveness)

    def frame_generator(self):
        """Generator that yields all audio frames from microphone."""
        if self.input_rate == self.RATE_PROCESS:
            while True:
                yield self.read()
        else:
            while True:
                yield self.read_resampled()

    def vad_collector(self, padding_ms=300, ratio=0.75, frames=None):
        """Generator that yields series of consecutive audio frames comprising each utterence, separated by yielding a single None.
            Determines voice activity by ratio of frames in padding_ms. Uses a buffer to include padding_ms prior to being triggered.
            Example: (frame, ..., frame, None, frame, ..., frame, None, ...)
                      |---utterence---|        |---utterence---|
        """
        if frames is None: frames = self.frame_generator()
        num_padding_frames = padding_ms // self.frame_duration_ms
        ring_buffer = collections.deque(maxlen=num_padding_frames)
        triggered = False

        for frame in frames:
            if len(frame) < 640:
                return

            is_speech = self.vad.is_speech(frame, self.sample_rate)

            if not triggered:
                ring_buffer.append((frame, is_speech))
                num_voiced = len([f for f, speech in ring_buffer if speech])
                if num_voiced > ratio * ring_buffer.maxlen:
                    triggered = True
                    for f, s in ring_buffer:
                        yield f
                    ring_buffer.clear()

            else:
                yield frame
                ring_buffer.append((frame, is_speech))
                num_unvoiced = len([f for f, speech in ring_buffer if not speech])
                if num_unvoiced > ratio * ring_buffer.maxlen:
                    triggered = False
                    yield None
                    ring_buffer.clear()

def main(ARGS):
    # Load DeepSpeech model
    if os.path.isdir(ARGS.model):
        model_dir = ARGS.model
        ARGS.model = os.path.join(model_dir, 'output_graph.pb')
        ARGS.scorer = os.path.join(model_dir, ARGS.scorer)

    print('Initializing model...')
    logging.info("ARGS.model: %s", ARGS.model)
    model = deepspeech.Model(ARGS.model)
    if ARGS.scorer:
        logging.info("ARGS.scorer: %s", ARGS.scorer)
        model.enableExternalScorer(ARGS.scorer)

    # Start audio with VAD
    vad_audio = VADAudio(aggressiveness=ARGS.vad_aggressiveness,
                         device=ARGS.device,
                         input_rate=ARGS.rate,
                         file=ARGS.file)
    print("Listening (ctrl-C to exit)...")
    frames = vad_audio.vad_collector()

    # Stream from microphone to DeepSpeech using VAD
    spinner = None
    if not ARGS.nospinner:
        spinner = Halo(spinner='line')
    stream_context = model.createStream()
    wav_data = bytearray()
    for frame in frames:
        if frame is not None:
            if spinner: spinner.start()
            logging.debug("streaming frame")
            stream_context.feedAudioContent(np.frombuffer(frame, np.int16))
            if ARGS.savewav: wav_data.extend(frame)
        else:
            if spinner: spinner.stop()
            logging.debug("end utterence")
            if ARGS.savewav:
                vad_audio.write_wav(os.path.join(ARGS.savewav, datetime.now().strftime("savewav_%Y-%m-%d_%H-%M-%S_%f.wav")), wav_data)
                wav_data = bytearray()
            text = stream_context.finishStream()

            print(text)

            #check for the presence of the wakeword
            if "computer" in text:
                process_speech(text[8:])


            stream_context = model.createStream()











if __name__ == '__main__':
    DEFAULT_SAMPLE_RATE = 16000

    import argparse
    parser = argparse.ArgumentParser(description="Stream from microphone to DeepSpeech using VAD")

    parser.add_argument('-v', '--vad_aggressiveness', type=int, default=3,
                        help="Set aggressiveness of VAD: an integer between 0 and 3, 0 being the least aggressive about filtering out non-speech, 3 the most aggressive. Default: 3")
    parser.add_argument('--nospinner', action='store_true',
                        help="Disable spinner")
    parser.add_argument('-w', '--savewav',
                        help="Save .wav files of utterences to given directory")
    parser.add_argument('-f', '--file',
                        help="Read from .wav file instead of microphone")

    parser.add_argument('-m', '--model', required=True,
                        help="Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)")
    parser.add_argument('-s', '--scorer',
                        help="Path to the external scorer file.")
    parser.add_argument('-d', '--device', type=int, default=None,
                        help="Device input index (Int) as listed by pyaudio.PyAudio.get_device_info_by_index(). If not provided, falls back to PyAudio.get_default_device().")
    parser.add_argument('-r', '--rate', type=int, default=DEFAULT_SAMPLE_RATE,
                        help=f"Input device sample rate. Default: {DEFAULT_SAMPLE_RATE}. Your device may require 44100.")

    ARGS = parser.parse_args()
    if ARGS.savewav: os.makedirs(ARGS.savewav, exist_ok=True)
    main(ARGS)

