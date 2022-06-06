Zufallszahl = 0
# Rest von "Zufallszahl" /5=0
# 
# ist nicht direkt verfügbar. Wird in Python Zufallszahl % 5 == 0: geschrieben, wird der Block "Rest von Zufallszahl gebildet.

def on_forever():
    global Zufallszahl
    Zufallszahl = randint(0, 19)
    basic.show_number(Zufallszahl)
    if Zufallszahl % 5 == 0:
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
