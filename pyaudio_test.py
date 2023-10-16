#例：pyaudioのライトコード
#pip install pyaudio
import pyaudio
import wave#wavファイルを扱うためのライブラリ
def record():
    CHUNK = 1024
    filename = "./output.wav"
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    record_seconds = 5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print("録音開始…")
    frames = []
    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("録音終了")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def play():
    CHUNK = 1024
    filename = "./output.wav"
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
    data = wf.readframes(CHUNK)
    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    record()
    play()