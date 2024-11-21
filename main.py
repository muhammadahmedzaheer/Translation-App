import os
from google.cloud import speech, translate_v2 as translate
import time
from google.cloud import texttospeech
from pydub import AudioSegment

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'agile-sanctum-442220-v0-546e65f56962.json'

# Initialize clients for speech recognition, translation, and text-to-speech
speech_client = speech.SpeechClient()
translate_client = translate.Client()
tts_client = texttospeech.TextToSpeechClient()

# Set the GCS URI for the audio file (replace with your actual URI)
audio_uri = "gs://audiofilesbuckethahaha/OSR_in_000_0062_16k.wav"

# Audio configuration for speech recognition
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # Audio encoding type
    sample_rate_hertz=16000,  # The sample rate of the audio file
    language_code="hi-IN",  # Language code for Hindi
)

# Audio object with the GCS URI
audio = speech.RecognitionAudio(uri=audio_uri)

# Start speech-to-text processing
print("Starting audio processing...")

try:
    # Request LongRunning speech recognition from Google Cloud (for audio longer than 1 minute)
    operation = speech_client.long_running_recognize(config=config, audio=audio)

    print("Processing... Please wait.")
    
    # Wait for the operation to complete
    response = operation.result(timeout=90)  # Set a timeout value if needed

    # Process the recognition results and print them
    transcript = ""
    for result in response.results:
        sentence = result.alternatives[0].transcript
        print("Original Transcript: ", sentence)
        transcript += sentence + ". "  # Combine all sentences

    # Save original transcript to a text file
    with open("original_transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)
    print("Original transcript saved as 'original_transcript.txt'.")

    # Translate the text to English
    translation = translate_client.translate(transcript, target_language='en')
    translated_text = translation['translatedText']
    print("Translated Text: ", translated_text)

    # Save translated transcript to a text file
    with open("translated_transcript.txt", "w", encoding="utf-8") as f:
        f.write(translated_text)
    print("Translated transcript saved as 'translated_transcript.txt'.")

    # Google Text-to-Speech: Convert translated text to speech
    synthesis_input = texttospeech.SynthesisInput(text=translated_text)

    # Set voice parameters for TTS
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Audio configuration for output
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the TTS request
    response = tts_client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # Save the translated audio as an MP3 file
    with open("translated_audio.mp3", "wb") as out:
        out.write(response.audio_content)
    print("Generated audio saved as 'translated_audio.mp3'.")

    # OPTIONAL: Add pauses between sentences (optional) for clarity
    # Load the MP3 file using pydub
    audio = AudioSegment.from_mp3("translated_audio.mp3")

    # Optionally, add silence between each sentence to improve clarity
    silence = AudioSegment.silent(duration=1000)  # 1 second of silence
    final_audio = AudioSegment.empty()

    for sentence in translated_text.split(". "):
        # Append each sentence with a 1-second silence in between
        sentence_audio = AudioSegment.from_mp3("translated_audio.mp3")
        final_audio += sentence_audio + silence

    # Save the final audio with pauses
    final_audio.export("final_translated_audio.mp3", format="mp3")
    print("Generated final audio with pauses as 'final_translated_audio.mp3'.")

except Exception as e:
    print(f"Error occurred: {e}")
