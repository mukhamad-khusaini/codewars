def validate_hello(greetings):
    greetWords=["hello","ciao","salut","hallo","hola","ahoj","czesc"]

    return True if True in [i in greetings.lower() for i in greetWords] else False