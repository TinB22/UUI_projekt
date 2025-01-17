from collections import deque
from time import sleep

def pronadi_put_bfs(labirint, start, kraj):
    redovi, stupci = len(labirint), len(labirint[0])
    red = deque([(start, [start])])
    posjeceno = set()

    while red:
        (r, s), put = red.popleft()
        if (r, s) in posjeceno:
            continue
        posjeceno.add((r, s))
        if (r, s) == kraj:
            return put
        for dr, ds in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, ns = r + dr, s + ds
            if 0 <= nr < redovi and 0 <= ns < stupci and labirint[nr][ns] == 0:
                red.append(((nr, ns), put + [(nr, ns)]))
    return None

def animiraj_put(platno, put, velicina_polja, start, kraj):
    for r, s in put:
        if (r, s) == start or (r, s) == kraj:
            continue
        platno.create_rectangle(
            s * velicina_polja, r * velicina_polja,
            (s + 1) * velicina_polja, (r + 1) * velicina_polja,
            fill="blue", outline="gray"
        )
        platno.update()
        sleep(0.2)
