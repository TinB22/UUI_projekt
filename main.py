import tkinter as tk
from labirint import generiraj_labirint, prikazi_labirint
from pronadi_put import pronadi_put_bfs, animiraj_put

class AplikacijaLabirint:
    def __init__(self, prozor):
        self.prozor = prozor
        self.prozor.title("AI Prolazak kroz Labirint")

        self.redovi = 21
        self.stupci = 21
        self.velicina_polja = 30

        self.labirint = generiraj_labirint(self.redovi, self.stupci)
        self.start = (1, 1)
        self.kraj = (self.redovi - 2, self.stupci - 2)
        self.labirint[self.start[0]][self.start[1]] = 0
        self.labirint[self.kraj[0]][self.kraj[1]] = 0

        self.platno = tk.Canvas(self.prozor, width=self.stupci * self.velicina_polja, height=self.redovi * self.velicina_polja)
        self.platno.pack()

        prikazi_labirint(self.platno, self.labirint, self.velicina_polja, self.start, self.kraj)

        tk.Button(self.prozor, text="Pokreni AI", command=self.pokreni_ai).pack(pady=10)

    def pokreni_ai(self):
        put = pronadi_put_bfs(self.labirint, self.start, self.kraj)
        if not put:
            tk.messagebox.showerror("Greška", "AI nije pronašao put!")
            return
        animiraj_put(self.platno, put, self.velicina_polja, self.start, self.kraj)

prozor = tk.Tk()
app = AplikacijaLabirint(prozor)
prozor.mainloop()
