from tkinter import *  # pobieramy biblioteke tkinter do tworzenia GUI
import yfinance as yf  # biblioteka yfinance z ktorej pobieramy dane o cenach
import pandas as pd  # biblioteka pandas sluzaca do analizy danych
import matplotlib.pyplot as plt  # biblioteka matplotlib sluzaca do tworzenia wykresow
import numpy as np
from tkinter import messagebox


root = Tk()  # tworzymy obiekt klasy tk
root.title("Trendy cen")  # nazwa aplikacji
root.geometry("800x400")  # rozmiar okienka

label = Label(root, text="Wybierz co cię interesuje :)", font=400, fg="red")  # tytul ktory wyswietli sie w srodku okienka
label.pack()  # ustala miejsce w ktorym wyswietli sie nasz tytul

def surowce():
    label.destroy()
    nier_przycisk.destroy()
    btc_przycisk.destroy()
    surowce_przycisk.destroy()

    wegiel_przycisk.place(relx=0.5, rely=0.3, anchor=CENTER)
    ropa_przycisk.place(relx=0.5, rely=0.4, anchor=CENTER)
    gaz_przycisk.place(relx=0.5, rely=0.5, anchor=CENTER)
    uran_przycisk.place(relx=0.5, rely=0.6, anchor=CENTER)


def wegiel():  # definiujemy funkcje "wegiel", ktorej uzyjemy potem
    label.destroy()
    wegiel_przycisk.destroy()
    ropa_przycisk.destroy()  # po wcisnieciu przycisku te komendy czyszcza nam wszystko w okienku
    gaz_przycisk.destroy()
    uran_przycisk.destroy()

    text1 = Label(root, text="Wprowadz date poczatkowa, a nastepnie date koncowa[YYYY-MM-DD]:",
                  font=60)  # wyswietli sie ten napis
    text1.pack()

    start_date_entry = Entry(root)  # wyswietli sie okienko, gdzie bedziemy wpisywac nasza date
    start_date_entry.pack()

    end_date_entry = Entry(root)# wyswietli sie okienko, gdzie bedziemy wpisywac nasza date
    end_date_entry.pack()

    def wegiel_uruchom():  # definiuje funkcje "wegiel_uruchom", ktora zostanie uzyta potem
        try:#funkcja sprawdza czy przy wpisanych przez uzytkownika danych program zadziala bez bledow, jesli nie - powie nam o tym
            end_date = end_date_entry.get()  # przypisujemy wczesniej wpisana w okienku date do zmiennej
            start_date = start_date_entry.get()  # przypisujemy wczesniej wpisana w okienku date do zmiennej
            coal_prices = yf.download('HCC', start=start_date, end=end_date) # uzywamy biblioteki yfinance, aby pobrac dane, z podanych wczesniej ram czasowych i przypisujemy je zmiennej
            df_coal = pd.DataFrame(coal_prices)#uzywamy biblioteki pandas, a dokladniej funkcji DataFrame, ktora uporzadkowuje podane dane w tabele
            rolling_mean_coal = df_coal['Close'].rolling(window=len(df_coal), min_periods=1).mean()# z podanych dancyh tworzymy srednia kroczaca, ktora bedzie przedstawiala nasz trend
            plt.plot(df_coal.index, df_coal['Close'])#uzywamy biblioteki matplotlib, ktora utworzy nam wykres cen na podstawie wczesniejszej tabeli, uporzadkowanej przez DataFrame
            plt.plot(df_coal.index, rolling_mean_coal,alpha=0.5, label='Średnia krocząca')#ponownie biblioteka matplotlib, ktora teraz na wykresie utworzy wczesniej obliczona srednia kroczaca i przypisze jej nazwe
            x = np.arange(len(df_coal))
            slope, intercept = np.polyfit(x, df_coal['Close'], 1) #tworzenie lini trendu
            trend_line = slope * x + intercept


            plt.plot(df_coal.index, trend_line,color="red", linewidth=3, linestyle="--", label='Trend')
            plt.title('Ceny wegla (HCC) na Yahoo Finance')#tytul wykresu
            plt.xlabel('Data')#legenda osi X
            plt.ylabel('Cena USD')#legenda osi Y
            plt.grid(True, axis='both', alpha=0.5)#utworzy nam siatke na wykresie, aby lepiej czytac ceny
            plt.legend()#utworzy legende
            root.destroy()  # powoduje zamkniecie calej aplikacji okienkowej
            plt.show()#tworzy caly wykres i wyswietla nam go
        except:#w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)


    save_button = Button(root, text="Stworz wykres", command=wegiel_uruchom)#pod wprowadzanymi datami wyswietli sie przycisk, ktory uruchamia funkcje powyzej
    save_button.pack()


def ropa():
    label.destroy()
    wegiel_przycisk.destroy()
    ropa_przycisk.destroy()
    gaz_przycisk.destroy()
    uran_przycisk.destroy()


    text1 = Label(root, text="Wprowadz date poczatkowa a nastepnie date koncowa[YYYY-MM-DD]:", font=60)
    text1.pack()
    start_date_entry = Entry(root)
    start_date_entry.pack()

    end_date_entry = Entry(root)
    end_date_entry.pack()


    def ropa_uruchom():
        try:
            end_date = end_date_entry.get()
            start_date = start_date_entry.get()

            oil_prices = yf.download('CL=F', start=start_date, end=end_date)
            df_oil = pd.DataFrame(oil_prices)
            rolling_mean_oil = df_oil['Close'].rolling(window=len(df_oil), min_periods=1).mean()
            x = np.arange(len(df_oil))
            slope, intercept = np.polyfit(x, df_oil['Close'], 1)
            trend_line = slope * x + intercept


            plt.plot(df_oil.index, df_oil['Close'])
            plt.plot(df_oil.index, rolling_mean_oil, label='Średnia krocząca')
            plt.plot(df_oil.index, trend_line, color="purple",linewidth=3,linestyle="--", label='Trend')
            plt.title('Ceny ropy naftowej (CL=F) na Yahoo Finance')
            plt.xlabel('Data')
            plt.ylabel('Cena USD')
            plt.grid(True, axis='both', alpha=0.5)
            root.destroy()
            plt.legend()
            plt.show()

        except:  # w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)

    save_button = Button(root, text="Stworz wykres", command=ropa_uruchom) 
    save_button.pack()


def gaz():
    label.destroy()
    wegiel_przycisk.destroy()
    ropa_przycisk.destroy()
    gaz_przycisk.destroy()
    uran_przycisk.destroy()


    text1 = Label(root, text="Wprowadz date poczatkowa a nastepnie date koncowa[YYYY-MM-DD]:", font=60)
    text1.pack()
    start_date_entry = Entry(root)
    start_date_entry.pack()

    end_date_entry = Entry(root)
    end_date_entry.pack()


    def gaz_uruchom():
        try:
            end_date = end_date_entry.get()
            start_date = start_date_entry.get()

            gaz_prices = yf.download('NG=F', start=start_date, end=end_date)
            df_gaz = pd.DataFrame(gaz_prices)
            rolling_mean_gaz = df_gaz['Close'].rolling(window=len(df_gaz), min_periods=1).mean()
            x = np.arange(len(df_gaz))
            slope, intercept = np.polyfit(x, df_gaz['Close'], 1)
            trend_line = slope * x + intercept

            plt.plot(df_gaz.index, trend_line, color="red",linewidth=3,linestyle="--", label='Trend')
            plt.plot(df_gaz.index, df_gaz['Close'])
            plt.plot(df_gaz.index, rolling_mean_gaz, label='Średnia krocząca',alpha=0.5)
            plt.title('Ceny gazu ziemnego (NG=F) na Yahoo Finance')
            plt.xlabel('Data')
            plt.ylabel('Cena USD')
            plt.grid(True, axis='both', alpha=0.5)
            root.destroy()
            plt.legend()
            plt.show()
        except:  # w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)


    save_button = Button(root, text="Stworz wykres", command=gaz_uruchom)
    save_button.pack()


def uran():
    label.destroy()
    wegiel_przycisk.destroy()
    ropa_przycisk.destroy()
    gaz_przycisk.destroy()
    uran_przycisk.destroy()


    text1 = Label(root, text="Wprowadz date poczatkowa a nastepnie date koncowa[YYYY-MM-DD]:", font=60)
    text1.pack()
    start_date_entry = Entry(root)
    start_date_entry.pack()

    end_date_entry = Entry(root)
    end_date_entry.pack()
    end_date = end_date_entry.get()

    def uran_uruchom():
        try:
            end_date = end_date_entry.get()
            start_date = start_date_entry.get()

            uran_prices = yf.download('URA', start=start_date, end=end_date)
            df_uran = pd.DataFrame(uran_prices)
            rolling_mean_gaz = df_uran['Close'].rolling(window=len(df_uran), min_periods=1).mean()
            x = np.arange(len(df_uran))
            slope, intercept = np.polyfit(x, df_uran['Close'], 1)
            trend_line = slope * x + intercept


            plt.plot(df_uran.index, trend_line,  label='Trend', color="red", linewidth=3, linestyle="--")
            plt.plot(df_uran.index, df_uran['Close'])
            plt.plot(df_uran.index, rolling_mean_gaz, label='Średnia krocząca',alpha=0.5)
            plt.title('Ceny uranu ETF (URA) na Yahoo Finance')
            plt.xlabel('Data')
            plt.ylabel('Cena USD')
            plt.grid(True, axis='both', alpha=0.5)
            root.destroy()
            plt.legend()
            plt.show()
        except:  # w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)

    save_button = Button(root, text="Stworz wykres", command=uran_uruchom)
    save_button.pack()


def nier():
    label.destroy()
    nier_przycisk.destroy()
    btc_przycisk.destroy()
    surowce_przycisk.destroy()


    text1 = Label(root, text="Wprowadz date poczatkowa a nastepnie date koncowa[YYYY-MM-DD]:", font=60)
    text1.pack()
    start_date_entry = Entry(root)
    start_date_entry.pack()

    end_date_entry = Entry(root)
    end_date_entry.pack()


    def nier_uruchom():
        try:
            end_date = end_date_entry.get()
            start_date = start_date_entry.get()

            estate_prices = yf.download('HOUS', start=start_date, end=end_date)
            df_estate = pd.DataFrame(estate_prices)
            rolling_mean_estate = df_estate['Close'].rolling(window=len(df_estate), min_periods=1).mean()
            x = np.arange(len(df_estate))
            slope, intercept = np.polyfit(x, df_estate['Close'], 1)
            trend_line = slope * x + intercept


            plt.plot(df_estate.index, df_estate['Close'])
            plt.plot(df_estate.index, rolling_mean_estate, label='Średnia krocząca')
            plt.plot(df_estate.index, trend_line, color="purple",linewidth=3,linestyle="--", label='Trend')
            plt.title('Ceny nieruchomosci (HOUS) na Yahoo Finance')
            plt.xlabel('Data')
            plt.ylabel('Cena USD')
            plt.grid(True, axis='both', alpha=0.5)
            root.destroy()
            plt.legend()
            plt.show()
        except:  # w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)

    save_button = Button(root, text="Stworz wykres", command=nier_uruchom) 
    save_button.pack()

def btc():
    label.destroy()
    nier_przycisk.destroy()
    btc_przycisk.destroy()
    surowce_przycisk.destroy()


    text1 = Label(root, text="Wprowadz date poczatkowa a nastepnie date koncowa[YYYY-MM-DD]:", font=60)
    text1.pack()
    start_date_entry = Entry(root)
    start_date_entry.pack()

    end_date_entry = Entry(root)
    end_date_entry.pack()


    def btc_uruchom():
        try:
            end_date = end_date_entry.get()
            start_date = start_date_entry.get()

            btc_prices = yf.download('BTC-USD', start=start_date, end=end_date)
            df_btc = pd.DataFrame(btc_prices)
            rolling_mean_btc = df_btc['Close'].rolling(window=len(df_btc), min_periods=1).mean()
            x = np.arange(len(df_btc))
            slope, intercept = np.polyfit(x, df_btc['Close'], 1)
            trend_line = slope * x + intercept


            plt.plot(df_btc.index, df_btc['Close'])
            plt.plot(df_btc.index, rolling_mean_btc, label='Średnia krocząca')
            plt.plot(df_btc.index, trend_line, color="purple",linewidth=3,linestyle="--", label='Trend')
            plt.title('Ceny BITCOINA (BTC-USD) na Yahoo Finance')
            plt.xlabel('Data')
            plt.ylabel('Cena USD')
            plt.grid(True, axis='both', alpha=0.5)
            root.destroy()
            plt.legend()
            plt.show()
        except:  # w momencie pojawienia sie bledu wyskoczy okienko z komunikatem
            messagebox.showerror('Bład', 'Niepoprawna data')
            end_date_entry.delete(0, END)
            start_date_entry.delete(0, END)

    save_button = Button(root, text="Stworz wykres", command=btc_uruchom) .pack()


wegiel_przycisk = Button(root, text="Wegiel", font=('Times', 12), height=1, width=10, command=wegiel) #wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
ropa_przycisk = Button(root, text="Ropa naftowa", font=('Times', 12), height=1, width=10, command=ropa)#wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
gaz_przycisk = Button(root, text="Gaz ziemny", font=('Times', 12), height=1, width=10,command=gaz)#wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
uran_przycisk = Button(root, text="Uran", font=('Times', 12), height=1, width=10, command=uran)#wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
nier_przycisk = Button(root, text="Nieruchomosci", font=('Arial Black', 12), height=1, width=13, command=nier)#wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
nier_przycisk.place(relx=0.5, rely=0.25, anchor=CENTER)
btc_przycisk = Button(root, text="BITCOIN", font=('Arial Black', 12), height=1, width=13, command=btc)#wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
btc_przycisk.place(relx=0.5, rely=0.4, anchor=CENTER)
surowce_przycisk = Button(root, text="Surowce", font=('Arial Black', 12), height=1, width=13, command=surowce) #wyswietla przycisk, ktory uruchamia funkcje zdefiniowana wyzej
surowce_przycisk.place(relx=0.5, rely=0.55, anchor=CENTER)
root.mainloop()#tworzy nasza aplikacje