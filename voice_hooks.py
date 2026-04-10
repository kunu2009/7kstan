"""Voice hook placeholders for Stan v1.

Keep this lightweight for Termux. Add real implementations later.
"""


def stt_available() -> bool:
    """Return whether speech-to-text is configured."""
    return False


def tts_available() -> bool:
    """Return whether text-to-speech is configured."""
    return False


def speech_to_text() -> str:
    """Capture speech and return text.

    Replace this stub with your chosen approach.
    """
    raise NotImplementedError("Speech-to-text not configured yet.")


def speak_text(text: str) -> None:
    """Speak text aloud.

    Replace this stub with your chosen approach.
    """
    raise NotImplementedError("Text-to-speech not configured yet.")
