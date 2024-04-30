def how_much_i_love_you(nb_petals):
    phrase=["I love you","a little","a lot","passionately","madly","not at all"]
    if(nb_petals>6):
        c=nb_petals%6
        return phrase[c-1]
    
    return phrase[nb_petals-1]