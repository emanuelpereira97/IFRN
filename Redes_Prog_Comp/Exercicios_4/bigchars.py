caracteres = {
    "A": [
        "  A  ",
        " A A ",
        "A   A",
        "AAAAA",
        "A   A",
        "A   A"
    ],
    "B": [
        "BBBB ",
        "B   B",
        "BBBB ",
        "B   B",
        "B   B",
        "BBBB "
    ],
    "C": [
        " CCC ",
        "C   C",
        "C    ",
        "C    ",
        "C   C",
        " CCC "
    ],
    "D": [
        "DDDD ",
        "D   D",
        "D   D",
        "D   D",
        "D   D",
        "DDDD "
    ],
    "E": [
        "EEEEE",
        "E    ",
        "EEE  ",
        "E    ",
        "EEEEE"
    ],
    "F": [
        "FFFFF",
        "F    ",
        "FFF  ",
        "F    ",
        "F    ",
        "F    "
    ],
    "G": [
        " GGG ",
        "G    ",
        "G  GG",
        "G   G",
        "G   G",
        " GGG "
    ],
    "H": [
        "H   H",
        "H   H",
        "HHHHH",
        "H   H",
        "H   H",
        "H   H"
    ],
    "I": [
        " III ",
        "  I  ",
        "  I  ",
        "  I  ",
        "  I  ",
        " III "
    ],
    "J": [
        "JJJJJ",
        "    J",
        "    J",
        "    J",
        "J   J",
        " JJJ "
    ],
    "K": [
        "K   K",
        "K  K ",
        "KKK  ",
        "K  K ",
        "K   K",
        "K   K"
    ],
    "L": [
        "L    ",
        "L    ",
        "L    ",
        "L    ",
        "L    ",
        "LLLLL"
    ],
    "M": [
        "M   M",
        "MM MM",
        "M M M",
        "M   M",
        "M   M",
        "M   M"
    ],
    "N": [
        "N   N",
        "NN  N",
        "N N N",
        "N  NN",
        "N   N",
        "N   N"
    ],
    "O": [
        " OOO ",
        "O   O",
        "O   O",
        "O   O",
        "O   O",
        " OOO "
    ],
    "P": [
        "PPPP ",
        "P   P",
        "PPPP ",
        "P    ",
        "P    ",
        "P    "
    ],
    "Q": [
        " QQQ ",
        "Q   Q",
        "Q   Q",
        "Q   Q",
        "Q  Q ",
        " QQ Q"
    ],
    "R": [
        "RRRR ",
        "R   R",
        "RRRR ",
        "R R  ",
        "R  R ",
        "R   R"
    ],
    "S": [
        " SSS ",
        "S   S",
        "S    ",
        " SSS ",
        "    S",
        "SSSS "
    ],
    "T": [
        "TTTTT",
        "  T  ",
        "  T  ",
        "  T  ",
        "  T  ",
        "  T  "
    ],
    "U": [
        "U   U",
        "U   U",
        "U   U",
        "U   U",
        "U   U",
        " UUU "
    ],
    "V": [
        "V   V",
        "V   V",
        "V   V",
        " V V ",
        " V V ",
        "  V  "
    ],
    "W": [
        "W   W",
        "W   W",
        "W   W",
        "W W W",
        "WW WW",
        "W   W"
    ],
    "X": [
        "X   X",
        " X X ",
        "  X  ",
        "  X  ",
        " X X ",
        "X   X"
    ],
    "Y": [
        "Y   Y",
        " Y Y ",
        "  Y  ",
        "  Y  ",
        "  Y  ",
        "  Y  "
    ],
    "Z": [
        "ZZZZZ",
        "    Z",
        "   Z ",
        "  Z  ",
        " Z   ",
        "ZZZZZ"
    ],
    "0": [
        " OOO ",
        "O   O",
        "O  OO",
        "O O O",
        "OO  O",
        " OOO "
    ],
    "1": [
        "  1  ",
        " 11  ",
        "  1  ",
        "  1  ",
        "  1  ",
        "11111"
    ],
    "2": [
        " 222 ",
        "2   2",
        "    2",
        "   2 ",
        "  2  ",
        "22222"
    ],
    "3": [
        " 333 ",
        "3   3",
        "    3",
        "  33 ",
        "    3",
        "3333 "
    ],
    "4": [
        "   4 ",
        "  44 ",
        " 4 4 ",
        "4  4 ",
        "44444",
        "   4 "
    ],
    "5": [
        "55555",
        "5    ",
        "5555 ",
        "    5",
        "5   5",
        " 555 "
    ],
    "6": [
        " 666 ",
        "6    ",
        "6666 ",
        "6   6",
        "6   6",
        " 666 "
    ],
    "7": [
        "77777",
        "    7",
        "   7 ",
        "  7  ",
        " 7   ",
        "7    "
    ],
    "8": [
        " 888 ",
        "8   8",
        " 888 ",
        "8   8",
        "8   8",
        " 888 "
    ],
    "9": [
        " 999 ",
        "9   9",
        "9   9",
        " 9999",
        "    9",
        " 999 "
    ]
}


nome = input ("Digite seu nome: ").upper()

nome_digitado = ['']

for letra in nome:
   if letra in caracteres:
      nome_digitado += caracteres[letra]
for linha in nome_digitado:
    print(linha)