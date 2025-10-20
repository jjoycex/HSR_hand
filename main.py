import ASR
import llm

def main():
    """
    Main function to record audio, transcribe it, and then query the llm.
    """
    audio_filename = "recorded_audio.wav"
    
    # Record audio
    ASR.record_audio_to_file(audio_filename, 5)
    
    # Transcribe audio
    transcribed_text = ASR.transcribe_audio_with_whisper(audio_filename)
    print(f"Transcribed text: {transcribed_text}")
    
    # Query the llm with the transcribed text
    if transcribed_text:
        llm.query_ollama(transcribed_text)

main()
