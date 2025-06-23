#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr
import ans

tk = TkDrawer()
try:
    for name in ["ccc", "custom_yes", "cube", "box", "king", "cow"]:
        ans.ans = 0
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        Polyedr(f"data/{name}.geom").draw(tk)
        delta_time = time() - start_time
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print("=============================================================")
        print(ans.ans, "= сумма площадей")
        print("=============================================================")
        tk.canvas.create_text(
            890, 10,
            text=str(ans.ans),
            anchor='ne',
            font=('Arial', 14),
            fill='red'
        )
        tk.root.update()
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
