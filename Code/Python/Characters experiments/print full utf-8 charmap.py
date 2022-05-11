import unicodedata
charmap = open("fullcharmap", "w", encoding="utf-8")
charmap_no_ctrl = open("fullcharmap_no_ctrl", "w", encoding="utf-8")


for a in range(0, 0x10ffff):
    try:
        if unicodedata.category(chr(a))[0] != "C":
            charmap_no_ctrl.write(chr(a))
        charmap.write(chr(a))
    except UnicodeEncodeError:
        pass

charmap.close()
charmap_no_ctrl.close()