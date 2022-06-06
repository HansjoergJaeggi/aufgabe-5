Zufallszahl = 0
"""

Aufgabe 5

Wenn der Zustand wahr ist, sollte eine zufällige Zahl durch 5 dividiert werden. Wenn diese zufällige Zahl teilbar ist, dann sollte ein Herz angezeigt werden.

"""
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
