def gcdOfStrings(str1: str, str2: str) -> str:
    # start with the smaller string as initial divider
    if len(str1) < len(str2):
        divider = str1 
    else:
        divider = str2

    # shrink divider until it divides both
    while divider:
        if str1.replace(divider, "") == "" and str2.replace(divider, "") == "":
            return divider
        divider = divider[:-1]

    return ""