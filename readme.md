
Program, który umożliwia przeprowadzenie analizy szeregów czasowych. 
Tworzy wykres z zakresu czasowego wybranego przez użytkownika, na którym przedstawione jest szereg czasowy oraz linia trendu i średnia krocząca. 


Dodatkowe moduły użyte w projekcie:
-tkinter (konsola z wyborem)
-yfinance
-pandas
-matplotlib
-numpy




1.	Opis: 
•	Program służy do pobierania danych z serwisu Yahoo Finance dotyczących cen nieruchomości, kryptowalut i surowców. Na podstawie pobranych danych program tworzy wykresy przedstawiające trendy cenowe w zadanym przedziale czasowym.
2.	Biblioteki:(dokładne wersje znajdują się w pliku requirements)
•	tkinter - biblioteka służąca do tworzenia GUI,
•	yfinance - biblioteka służąca do pobierania danych o cenach z serwisu Yahoo Finance,
•	pandas - biblioteka służąca do analizy danych,
•	matplotlib - biblioteka służąca do tworzenia wykresów,
•	numpy - biblioteka służąca do operacji na tablicach numerycznych.
3.	Interfejs graficzny:
•	Program posiada interfejs graficzny oparty na bibliotece tkinter.
•	Okno programu składa się z tytułu oraz przycisków, które służą do wybierania interesujących nas danych.
4.	Funkcjonalność: 
•	Po wybraniu danych program prosi o podanie daty początkowej i końcowej przedziału czasowego, dla którego chcemy zobaczyć trend cenowy. 
•	Następnie program pobiera dane z serwisu Yahoo Finance i tworzy wykres przedstawiający zmiany cen w danym przedziale czasowym. 
•	Wykres zawiera również średnią kroczącą oraz linię trendu.
5.Zakres działania:
• #nieruchomosci od 2013
• #wegiel od 2018
• #ropa od 2002
• #gaz od 2002
• #uran od 2010
• #btc od 2015
6.	Instrukcja obsługi:
•	Uruchomienie programu 
	należy uruchomić plik zawierający kod programu.
•	Wybór danych 
	 należy wybrać interesujące nas dane poprzez kliknięcie na odpowiedni przycisk.
•	Podanie daty 
	 po wyborze danych program poprosi o podanie daty początkowej i końcowej przedziału czasowego.
•	Wygenerowanie wykresu 
	 po podaniu dat program można wygenerować wykres poprzez kliknięcie na przycisk "Stwórz wykres".

Wyjaśnienie działania:
Funkcje “węgiel”; “gaz”; “ropa”; “uran”; “nier”; “btc” - Wykonują operacje na GUI (usuwają niepotrzebne przyciski i dodają nowe [tkinter]). 
Po ich uruchomieniu/wywołaniu użytkownik dostaje miejsce, w które powinien wpisać przedział czasowy, którym jest zainteresowany. 
Tuż pod, wygenerowany jest również przycisk ,,Stwórz wykres”, po naciśnięciu którego wywołamy inną już funkcję.

Pomocnicza funkcja “surowce” - operacje na GUI (usuwanie oraz dodawanie nowych przycisków [tkinter])

Głównymi funkcjami programu są:
“wegiel_uruchom”;
“gaz_uruchom”;
“ropa_uruchom”;
“uran_uruchom”;
“nier_uruchom”;
“btc_uruchom”
Powiązane z przyciskiem ,,Stwórz wykres”, które na podstawie zebranych danych od użytkownika oraz ‘yfinance’, przy pomocy bibliotek Pandas, Matplotlib oraz numpy, wykonują wszelkie obliczenia potrzebne do wytworzenia końcowego wykresu.


 
