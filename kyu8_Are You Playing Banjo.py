def are_you_playing_banjo(name):
    return name + " plays banjo"  if name[:1]=='r'or name[:1]=='R' else name + " does not play banjo"

print(are_you_playing_banjo('sigit'))