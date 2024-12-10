def addressVal(address):
    if "@" not in address or "." not in address:
        print("Invalid")
    elif address.index("@") > address.rindex("."):
        print("Invalid")
    elif address.count("@") > 1:
        print("Invalid")
    else:
        print("Valid")
      
