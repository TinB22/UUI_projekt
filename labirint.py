import random

def generiraj_labirint(redovi, stupci):
    labirint = [[1 for _ in range(stupci)] for _ in range(redovi)]

    def napravi_prolaz(x, y):
        smjerovi = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(smjerovi)
        for dx, dy in smjerovi:
            nx, ny = x + dx, y + dy
            if 0 <= nx < redovi and 0 <= ny < stupci and labirint[nx][ny] == 1:
                labirint[nx][ny] = 0
                labirint[x + dx // 2][y + dy // 2] = 0
                napravi_prolaz(nx, ny)

    labirint[1][1] = 0
    napravi_prolaz(1, 1)
    return labirint

def prikazi_labirint(platno, labirint, velicina_polja, start, kraj):
    redovi, stupci = len(labirint), len(labirint[0])
    platno.delete("all")
    for r in range(redovi):
        for s in range(stupci):
            if (r, s) == start:
                boja = "#3CB371"
            elif (r, s) == kraj:
                boja = "#FF6347"
            else:
                boja = "#2F4F4F" if labirint[r][s] == 1 else "#DCDCDC"
            rub_boja = "#A9A9A9" if labirint[r][s] == 0 else "#696969"
            platno.create_rectangle(
                s * velicina_polja, r * velicina_polja,
                (s + 1) * velicina_polja, (r + 1) * velicina_polja,
                fill=boja, outline=rub_boja, width=2
            )
