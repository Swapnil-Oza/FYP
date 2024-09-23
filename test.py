from audio import AudioPreProcessor
import whisper

# Initialize the audio processor
processor = AudioPreProcessor()

# Path to your original audio file
audio_file = "Recording.m4a"  # Update with your actual audio file path

# Pre-process the audio file (convert to .wav)
processor.process(audio_file)
if processor.error:
    print("Error occurred during audio processing:", processor.error)
else:
    print("Audio processing complete:", processor.output_path)

    # Load the Whisper model (consider using 'small' or 'tiny' for faster processing)
    model = whisper.load_model("medium")  # 'medium' model supports multiple languages

    # Transcribe and translate the pre-processed .wav file
    result = model.transcribe(processor.output_path, task='translate')  # Use 'translate' for translation

    # Print the transcription result
    print("Transcription:\n", result["text"])

# Clean up the temporary files
processor.cleanup()
