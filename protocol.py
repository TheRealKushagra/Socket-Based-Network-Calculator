
import json


def encode_message(message):
    """Convert a dictionary into a newline-delimited JSON message."""
    return (json.dumps(message) + "\n").encode("utf-8")


def decode_message(data):
    """Decode a newline-delimited JSON message into a dictionary."""
    message = data.split(b"\n", 1)[0]
    result = json.loads(message.decode("utf-8"))

    if not isinstance(result, dict):
        raise ValueError("The message must contain a JSON object.")

    return result
