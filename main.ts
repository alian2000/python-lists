input.onButtonPressed(Button.A, function () {
    text_list = [
    "ali",
    "basem",
    "charlie",
    "david",
    "55"
    ]
    basic.showString("" + (text_list.indexOf("david")))
    basic.pause(100)
    basic.showString("" + (text_list[0]))
    basic.showString("" + (text_list[1]))
    basic.showString("" + (text_list[2]))
    basic.showString("" + (text_list[3]))
    basic.showString("" + (text_list[4]))
    text_list.reverse()
})
input.onButtonPressed(Button.B, function () {
    studies = ["arabic", "english", "Art"]
    basic.showString("" + (studies.indexOf("arabic")))
    basic.pause(500)
    basic.showString("" + (studies[2]))
})
let studies: string[] = []
let text_list: string[] = []
let movieSnacks = [
"mints",
"cola",
"pretzel",
"popcorn",
"peanuts"
]
basic.showString("" + (movieSnacks[3]))
