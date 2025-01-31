import math
import random
import struct
import io
import wave

from pydub import AudioSegment


def generate_tone(
        frequency=440,  # 周波数(Hz)
        duration_ms=500,  # 長さ(ミリ秒)
        volume_db=-10.0,  # 音量(dB)
        sample_rate=44100
) -> AudioSegment:
    """
    指定した周波数の単純なサイン波を生成し、pydubのAudioSegmentを返す。
    """

    # 総フレーム数 = サンプリング周波数 x 秒
    num_frames = int(sample_rate * (duration_ms / 1000.0))

    # dB を振幅に変換 (16bit=32767が振幅の最大値)
    amplitude = 32767 * (10 ** (volume_db / 20.0))

    # サンプル値を格納するリスト
    wave_data = []
    for i in range(num_frames):
        # サイン波 (2π × f × t)
        sample = amplitude * math.sin(2.0 * math.pi * frequency * (i / float(sample_rate)))
        wave_data.append(int(sample))

    # waveモジュールを使ってバイナリデータ(WAV)を一時的に作る
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wf:
        wf.setnchannels(1)  # モノラル
        wf.setsampwidth(2)  # 16ビット(2バイト)
        wf.setframerate(sample_rate)  # サンプリングレート
        # サンプル値(整数)を書き込む
        for sample in wave_data:
            wf.writeframesraw(struct.pack('<h', sample))

    # pydub で扱えるようにメモリ上のWAVをAudioSegmentに変換
    buf.seek(0)
    segment = AudioSegment.from_raw(
        buf,
        sample_width=2,
        frame_rate=sample_rate,
        channels=1
    )
    return segment


def generate_white_noise(duration_ms=200, volume_db=-10.0, sample_rate=44100):
    """
    指定した長さのホワイトノイズを生成し、pydubのAudioSegmentを返す。
    """
    num_frames = int(sample_rate * (duration_ms / 1000.0))
    amplitude = 32767 * (10 ** (volume_db / 20.0))

    # ノイズの場合、-1.0～1.0 の乱数に振幅を掛けてサンプル生成
    wave_data = []
    for _ in range(num_frames):
        sample_val = random.uniform(-1.0, 1.0) * amplitude
        wave_data.append(int(sample_val))

    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        for sample in wave_data:
            wf.writeframesraw(struct.pack('<h', sample))

    buf.seek(0)
    segment = AudioSegment.from_raw(
        buf,
        sample_width=2,
        frame_rate=sample_rate,
        channels=1
    )
    return segment


def create_simple_beep():
    """
    シンプルなビープ音
    """
    return generate_tone(frequency=800, duration_ms=300, volume_db=-5.0)


def create_door_knock():
    """
    ドアをノックするような音を2回鳴らす。
    - 短時間のノイズをフェードアウトし、間を空けてもう一度鳴らす。
    """
    knock1 = generate_white_noise(duration_ms=50, volume_db=-2.0)
    # フェードアウトで音が「スッ」と消えるように
    knock1 = knock1.fade_out(30)

    # 少し間を空ける
    silence = AudioSegment.silent(duration=100)

    knock2 = generate_white_noise(duration_ms=50, volume_db=-2.0)
    knock2 = knock2.fade_out(30)

    # 「コン」「コン」の2回を連結
    knocks = knock1 + silence + knock2
    return knocks


def create_success_sound():
    """
    成功をイメージした短いメロディ
    - 3つのサイン波を上昇させて連結
    """
    tone1 = generate_tone(frequency=600, duration_ms=150, volume_db=-5.0)
    tone2 = generate_tone(frequency=800, duration_ms=150, volume_db=-5.0)
    tone3 = generate_tone(frequency=1000, duration_ms=200, volume_db=-5.0)

    # 連続して再生
    success = tone1 + tone2 + tone3
    return success


def create_fail_sound():
    """
    失敗をイメージした短いメロディ
    - 3つのサイン波を下降させて連結
    """
    tone1 = generate_tone(frequency=600, duration_ms=200, volume_db=-5.0)
    tone2 = generate_tone(frequency=400, duration_ms=150, volume_db=-5.0)
    tone3 = generate_tone(frequency=200, duration_ms=150, volume_db=-5.0)

    fail = tone1 + tone2 + tone3
    return fail


def create_pinpon_sound():
    # ピン (少し高めの音)
    pin = generate_tone(frequency=880, duration_ms=200, volume_db=-5.0)
    # ポン (少し低めの音)
    pon = generate_tone(frequency=660, duration_ms=200, volume_db=-5.0)

    # 連結する (pydubでは + 演算子で連結できる)
    pinpon = pin + pon
    return pinpon


def create_bubuu_sound():
    # ブ (もっと低め)
    bu1 = generate_tone(frequency=200, duration_ms=200, volume_db=-3.0)
    # 間を少しだけ空ける(無音を作る)
    silence = AudioSegment.silent(duration=80)
    # ブー (さらに少し下げる)
    bu2 = generate_tone(frequency=160, duration_ms=300, volume_db=-3.0)

    # 連結する
    bubuu = bu1 + silence + bu2
    return bubuu


if __name__ == "__main__":
    # 各種効果音を生成
    beep_sound = create_simple_beep()
    knock_sound = create_door_knock()
    success_sound = create_success_sound()
    fail_sound = create_fail_sound()
    pinpon_sound = create_pinpon_sound()
    bubuu_sound = create_bubuu_sound()

    # 生成したサウンドをMP3として出力
    beep_sound.export("se/beep.mp3", format="mp3")
    knock_sound.export("se/door_knock.mp3", format="mp3")
    success_sound.export("se/success.mp3", format="mp3")
    fail_sound.export("se/fail.mp3", format="mp3")
    pinpon_sound.export("se/pinpon.mp3", format="mp3")
    bubuu_sound.export("se/bubuu.mp3", format="mp3")

    print("MP3ファイルが出力されました。")
