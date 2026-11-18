def add_user_message(messages, text):
    """Add a user message to the conversation history."""
    user_message = {
        "role": "user",
        "content": text
    }
    messages.append(user_message)


def chat(client, model, messages, system=None):
    """Send conversation history to Claude and return its response."""

    params = {
        "model" : model,
        "max_tokens" : 256,
        "messages" : messages,
    }

    if system: 
        params["system"] = system

    message = client.messages.create(**params)
        
    assistant_text = message.content[0].text

    add_assistant_message(messages, assistant_text)

    return assistant_text


def add_assistant_message(messages, text):
    """Add an assistant response to the conversation history."""
    assistant_message = {
        "role": "assistant",
        "content": text
    }
    messages.append(assistant_message)