import numpy as np

# Loading & visualizing audio files
import librosa
import librosa.display

# saving files
import soundfile as sf


def read_audio_as_spec(filename: str, sample_size=2048, sample_rate=44100) -> np.ndarray:
    ''' Convert audio file to a spectrogram, contained in a numpy ndarray

    :param filename: location of audio file
    :return: the audio file as a spectrogram with the shape (1 + sample_size/2, x.shape[0] / hop_length)
    '''
    # Currently defaulting sample_rate to 44100, based off intel. Librosa default is 22050.

    hop_length = sample_size // 2

    x, sr = librosa.load(filename, sample_rate)
    X = librosa.stft(x, n_fft=sample_size, hop_length=hop_length)
    return X


def spectrogram_to_file(spectrogram: np.ndarray, output_file: str, sample_size=2048, sample_rate=44100) -> None:
    ''' Convert a spectrogram into audio, and write it to an audio file

    :param spectrogram: Numpy array that represents spectrogram
    :param output_file: Path for file to write to
    :return:
    '''
    # Currently defaulting sample_rate to 44100, based off intel. Librosa default is 22050.

    hop_length = sample_size // 2
    spectrogram = np.abs(spectrogram)
    spec_inv = librosa.griffinlim(spectrogram, hop_length=hop_length)
    sf.write(output_file, spec_inv, samplerate=sample_rate)
