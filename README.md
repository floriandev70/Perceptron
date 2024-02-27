# Perceptron
######################################################################################### 
bekommt Input/Output und passt Gewichte an, bis Fehler klein genug ODER Anzahl Epochen erreicht!

Perceptron(X,L)

Aktivierungsfunktion fa(x)=y
Gewichte W
Lernfunktion l
I. Learning

learn(features, labels, max_epochs, max_err) Solange Fehler zu groß ODER Max-Epochen nicht erreicht
X=features(i), L=labels(i)
perceptron.adjust_weights(X,L) X=Inputvektor, L=Outputlabelvektor
Falls Y <> L, dann passe Gewichte W an
II. Ausgabe

Gewichte
Lernkurve
Gradengleichung f(x)
Graph inkl. Grade f(x)
#########################################################################################
