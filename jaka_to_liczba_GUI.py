from tkinter import *
import random
class Application(Frame):
        """Stworzenie GUI do gry Jaka to liczba"""
        def __init__(self, master):
            super(Application, self).__init__(master)
            self.grid()
            self.create_widgets()
            self.correct_number = random.randint(1, 100)
            tries = 0
            self.tries = tries


        def create_widgets(self):
            Label(self, text="Wpisz liczbę z przedziału od 1 do 100:").grid(row=0, column=0, sticky=W)
            Label(self, text="Liczba prób:").grid(row=2, column=0, sticky=E)
            # Stworzenie oknna do wprowadzenia liczby z określonego zakresu
            self.input_number = Entry(self)
            self.input_number.grid(row=0, column=1, sticky=W)

            # Stworzenie okna odpowiedzi
            self.show_result = Text(self, width=26, height=1, wrap=WORD)
            self.show_result.grid(row=1, column=1, columnspan=1)

            # Stworzenie przycisku
            self.button = Button(self, text="Wyświetl wynik", command=self.root_algorytm,).grid(row=0, column=1, sticky=E)

            #Stworzenie okna z licznikiem prób
            self.count_tries= Text(self,width=26, height=1, wrap=WORD)
            self.count_tries.grid(row=2, column=1, columnspan=1)

        def root_algorytm(self):
            show = self.show_result
            the_number = self.correct_number
            input_number = int(self.input_number.get())
            if input_number == self.correct_number:
                show= "Gratulacje :)"
                self.tries += 1
            elif input_number > self.correct_number:
                show= "Za duża"
                self.tries += 1
            else:
                show= "Za mała"
                self.tries += 1


            self.show_result.delete(0.0,END)
            self.show_result.insert(0.0,show)
            self.count_tries.delete(0.0, END)
            self.count_tries.insert(0.0,"Liczba prób:" +str(self.tries))








root = Tk()
app=Application(root)
root.title("Jaka to liczba")
root.mainloop()

#Stworzenie paska postępu składającego się z 10 części, zmienia swój progress w zależności od bliskości do właściwej liczby