from nicegui import ui
from random import shuffle
# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
emojis = ["🤩", "🥵", "🤥", "🤡", "🙊", "🥺", "😭", "😫"] # ← Your task
emojis *= 2
shuffle(emojis)
buttons = []
opened = [] # indices of currently flipped cards
matched = [] # indices of solved cards
# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    def flip_back():
        for idx in (i, j):
            if idx not in matched:
                buttons[idx].text = "❓"
        opened.clear()
    ui.timer(0.5, lambda: flip_back(), once=True)
# TODO 3: Write click handler
def handle_click(idx: int) -> None:
    if idx in opened or idx in matched:
        return
    buttons[idx].text = emojis[idx]
    opened.append(idx)
    if len(opened) >= 2:
        i, j = opened
        if emojis[i] == emojis[j]:
            matched.append(i)
            matched.append(j)
            opened.clear()
            
            if len(matched) == 16:
                ui.notify("You win!", position="top")
        else:
            reset_pair(i, j)
# Build 4x4 grid
with ui.grid(columns=4):
# TODO 4: Create 16 buttons
    for i in range(0,16):
        item = ui.button("❓", on_click=lambda i=i: handle_click(i)).classes("w-40 h-40 text-lg")
        buttons.append(item)
ui.run(title='Memory Game')