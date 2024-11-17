import speech_recognition as sr

def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        transcription = recognizer.recognize_google(audio, language="kn-IN")  # Kannada language
        print(f"Transcription: {transcription}")
        return transcription
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        print("There was an issue with the speech recognition service.")
        return ""

def process_wav_content(wav_file_path):
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Load the WAV file and process the audio
    with sr.AudioFile(wav_file_path) as source:
        print(f"Processing WAV file: {wav_file_path}")
        audio = recognizer.record(source)  # Record the audio from the file

    try:
        # Transcribe the WAV file content using Google's API
        wav_content = recognizer.recognize_google(audio, language="kn-IN")  # Kannada language
        print(f"Transcribed WAV Content: {wav_content}")
        return wav_content
    except sr.UnknownValueError:
        print("Sorry, the audio in the WAV file could not be understood.")
        return ""
    except sr.RequestError:
        print("There was an issue with the speech recognition service.")
        return ""

def answer_based_on_content(question, content):
    # Matching based on content in the transcription
    if "ಲೈಲಾ" in question and "ಲೀಲಾ" in content:  # Check for "Laila" and context of the story in the content
        return "ಲೀಲಾ ಎಂಬ ಹುಡುಗಿ ಗಡಿಯಾರವನ್ನು ನೋಡಿ ತನ್ನ ಭಾವನೆಗಳನ್ನು ಹಂಚಿಕೊಂಡಳು."  # "Laila is a girl who saw a watch and shared her feelings."
    if "ಗಡಿಯಾರ" in question and "ಗಡಿಯಾರ" in content:  # Check for "watch"
        return "ಗಡಿಯಾರವು ಸಮಯವನ್ನು ಮಾತ್ರ ತೋರಿಸುವುದಿಲ್ಲ, ಅದು ನಿನ್ನ ಸಮಯವನ್ನು ತೋರಿಸುತ್ತದೆ."  # "The watch doesn't just show time, it shows your time."
    return "ಕ್ಷಮಿಸಿ, ನಾನು ಇದಕ್ಕೆ ಉತ್ತರಿಸಬಲ್ಲವನು ಅಲ್ಲ."  # "Sorry, I cannot answer that."

def get_input():
    input_type = input("Do you want to enter text manually or use voice input? (text/voice): ").strip().lower()
    if input_type == "text":
        text = input("Enter text: ")
        return text
    elif input_type == "voice":
        return listen_to_voice()
    else:
        print("Invalid input type. Please enter 'text' or 'voice'.")
        return get_input()

def process_text(text):
    # For now, we just return the text as is, but this is where you can process the text
    return text

if __name__ == "__main__":
    # Path to your WAV file
    wav_file_path = r"C:\Users\sivas\OneDrive\Pictures\New folder\kan.wav"

    # Load and process the content from the WAV file
    wav_content = process_wav_content(wav_file_path)

    # Get input (text or voice)
    input_text = get_input()
    processed_text = process_text(input_text)
    print(f"Processed Text: {processed_text}")

    # Answer the question based on the content of the WAV file
    answer = answer_based_on_content(processed_text, wav_content)
    print(f"Answer: {answer}")
