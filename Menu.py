

def GrabNumbers(Str):
    for s in Str:
        if s.isdigit():
            yield s

def StringToNums(Str):
    return int("".join(GrabNumbers(Str)))

def Settings():
    baseSettings = {"width":10,"fullscreen":0,"screenx":500,"screeny":500,"function":0}
    options = open("option.txt","r")
    options = [x.strip() for x in options.readlines()]
    for option in options:
        if "width" in option:
            baseSettings["width"] = StringToNums(option)
        if "fullscreen" in option:
            baseSettings["fullscreen"] = StringToNums(option)

        if "screenx" in option:
            baseSettings["screenx"] = StringToNums(option)

        if "screeny" in option:
            baseSettings["screeny"] = StringToNums(option)


        if "function" in option:
            baseSettings["function"] = StringToNums(option)

    return baseSettings

print(Settings())
