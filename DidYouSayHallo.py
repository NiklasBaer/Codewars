def validate_hello(message):
    greetings = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for greeting in greetings:
        if greeting in message.lower():
            return True
    return False

