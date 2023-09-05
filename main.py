def on_button_pressed_a():
    global text_list
    text_list = ["ali", "basem", "charlie", "david", "55"]
    basic.show_string("" + str((text_list.index("david"))))
    basic.pause(100)
    basic.show_string("" + (text_list[0]))
    basic.show_string("" + (text_list[1]))
    basic.show_string("" + (text_list[2]))
    basic.show_string("" + (text_list[3]))
    basic.show_string("" + (text_list[4]))
    text_list.reverse()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global studies
    studies = ["arabic", "english", "Art"]
    basic.show_string("" + str((studies.index("arabic"))))
    basic.pause(500)
    basic.show_string("" + (studies[2]))
input.on_button_pressed(Button.B, on_button_pressed_b)

studies: List[str] = []
text_list: List[str] = []
movieSnacks = ["mints", "cola", "pretzel", "popcorn", "peanuts"]
basic.show_string("" + (movieSnacks[3]))