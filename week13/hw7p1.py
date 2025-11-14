# homework 7, problem 1
from nicegui import ui

ui.label("Simple hashing algorithm for HW7.").classes("text-lg")

def twistHash():
    inp = inputField.value
    h = 0x9E3779B1
    for c in inp:
        h = h ^ ord(c)
        h = h * 0x517CC1C7
        h = h & 0xFFFFFFFF
    h = h ^ len(inp)
    return int(h)

def displayHash():
    hashLabel.text = f"Hash value: {twistHash()}"

with ui.card().classes("w-66"):
    inputField = ui.input("Enter text to hash:")
    ui.button("GET HASH", color="green", on_click=displayHash)
    hashLabel = ui.label("Hash Value: ")

ui.run(title="Example of twistHash algorithm.")