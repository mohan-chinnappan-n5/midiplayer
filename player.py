import streamlit as st
import pygame
import tempfile

# Initialize Pygame mixer
pygame.mixer.init()

def play_midi(file_path):
    """
    Play a MIDI file using pygame.

    Args:
        file_path (str): Path to the MIDI file.
    """
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    st.session_state.is_playing = True

def stop_midi():
    """
    Stop the MIDI playback using pygame.
    """
    pygame.mixer.music.stop()
    st.session_state.is_playing = False

def main():
    """
    Main function to create the Streamlit app for playing MIDI files.
    """
    # Initialize session state variables
    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False
    if 'volume' not in st.session_state:
        st.session_state.volume = 0.5

    st.title("MIDI Player")

    uploaded_file = st.file_uploader("Choose a MIDI file", type=["mid", "midi"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        # Display the audio player
        st.audio(uploaded_file, format='audio/midi')

        # Play button
        if st.button("Play"):
            play_midi(tmp_file_path)

        # Stop button
        if st.button("Stop"):
            stop_midi()

        # Volume slider
        if st.session_state.is_playing:
            st.slider("Volume", 0.0, 1.0, st.session_state.volume, key='volume', on_change=lambda: pygame.mixer.music.set_volume(st.session_state.volume))
            pygame.mixer.music.set_volume(st.session_state.volume)

if __name__ == "__main__":
    main()