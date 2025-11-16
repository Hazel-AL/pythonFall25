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
    # function necessary to run with ui.timer()
    def flip_back():
        # i and j are indeces, if they arent matched reset
        for idx in (i, j):
            if idx not in matched:
                buttons[idx].text = "❓"
        # and clear opened[]
        opened.clear()
    # delay for 0.5 sec, then run the actual function
    ui.timer(0.5, lambda: flip_back(), once=True)
# TODO 3: Write click handler
# takes the index of the card clicked 
def handle_click(idx: int) -> None:
    # exit function if the button is already opened
    if idx in opened or idx in matched:
        return
    # flip over the button, set the text to the matching emoji
    buttons[idx].text = emojis[idx]
    # add the button to opened[]
    opened.append(idx)
    # if 2 buttons are flipped:
    if len(opened) >= 2:
        # i, j makes code easier to read
        i, j = opened
        # if the same, add both to matched[] and clear opened[]
        if emojis[i] == emojis[j]:
            matched.append(i)
            matched.append(j)
            opened.clear()
            # if all are matched, notify user
            if len(matched) == 16:
                ui.notify("You win!", position="top")
        # otherwise reset
        else:
            reset_pair(i, j)
# Build 4x4 grid
with ui.grid(columns=4):
    # creates 16 buttons for the game
    for i in range(0,16):
        item = ui.button("❓", on_click=lambda i=i: handle_click(i)).classes("w-40 h-50 text-lg")
        buttons.append(item)
ui.run(title='Memory Game')