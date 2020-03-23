from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file(
    "file-location", "wav"
)  #   audio source location and type of audio.
chunk_length_ms = 2000  #   length of parts
chunks = make_chunks(myaudio, chunk_length_ms)

for i, chunk in enumerate(chunks):
    chunk_name = "file-name-format{i}".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")
