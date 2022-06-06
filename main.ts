let Zufallszahl = 0
/**
 * Aufgabe 5
 * 
 * Wenn der Zustand wahr ist, sollte eine zufällige Zahl durch 5 dividiert werden. Wenn diese zufällige Zahl teilbar ist, dann sollte ein Herz angezeigt werden.
 */
// Rest von "Zufallszahl" /5=0
// 
// ist nicht direkt verfügbar. Wird in Python Zufallszahl % 5 == 0: geschrieben, wird der Block "Rest von Zufallszahl gebildet.
basic.forever(function () {
    Zufallszahl = randint(0, 19)
    basic.showNumber(Zufallszahl)
    if (Zufallszahl % 5 == 0) {
        basic.showIcon(IconNames.Heart)
    }
})
