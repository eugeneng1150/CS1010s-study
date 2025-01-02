def check(word):
    if len(word) >= 3:
        print("gg")
    if word[0] == word[-1]:
        print("cool")
    elif word[::2] == "cdc":
        print("nice")
    else:
        print("end?")
    if word[3::-1] == "edoc": ## this reverses the string
        print("not yet")
    else:
        print("end now")
    
check("codec")
# gg
# cool
# not yet
check("codecs")
# gg
# nice
# not yet
check("ar")
# end?
# end now