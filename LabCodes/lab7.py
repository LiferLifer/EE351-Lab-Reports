import RPi.GPIO as GPIO
import time

buzzer_pin = 18

notes = {
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,
    'A#4': 466.16,
    'B4': 493.88,
    'C5': 523.25,
    'C#5': 554.37,
    'D5': 587.33,
    'D#5': 622.25,
    'E5': 659.25,
    'F5': 698.46,
    'F#5': 739.99,
    'G5': 783.99,
    'G#5': 830.61,
    'A5': 880.00,
    'A#5': 932.33,
    'B5': 987.77
}


# 从音符序列文件中读取音符和持续时间
def read_music_sequence(filename):
    with open(filename, 'r') as file:
        music_sequence = file.read().split()
    return music_sequence

def play_tone(note, duration):
    if note == 'P':
        time.sleep(duration)
        return
    p = GPIO.PWM(buzzer_pin, notes[note])
    p.start(50)
    time.sleep(duration)
    p.stop()
    time.sleep(0.01)

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

# 从音符序列文件中读取音符和持续时间
music_sequence = read_music_sequence('musicsq.txt')

# 播放音乐
for note_duration in music_sequence:
    note, duration = note_duration.split(':')
    duration = float(duration)
    play_tone(note, duration)

# 清理GPIO设置
GPIO.cleanup()
