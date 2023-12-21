with open("a.bin", "rb") as file:
    with open("a.png", "wb") as out:
        while mbytes := file.read(4):
            out.write(bytes(reversed(mbytes)))
