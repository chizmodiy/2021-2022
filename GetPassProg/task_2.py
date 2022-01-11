import re
MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    # replace this for solution
    x  = ()
    list_1 =[]
    code = re.sub(' {3}' , ' space ' , code)
    code =code.split( )
    text =[]
    for x in code:
        if x in MORSE:
             text.append(MORSE[f'{x}'])
        else:
            text.append('_space_')

    text = ''.join(text)
    text = re.sub('_space_',' ' , text)
    text = text.split()
    text_first_value  = text[0]
    for i in text[0]:
        list_1.append(i.lower())
    list_1[0] = list_1[0].upper()
    list_1 = ''.join(list_1)
    text[0] = list_1
    text = ' '.join(text)

    return text



if __name__ == "__main__":
    print(morse_decoder(".--- --- ... .- -.   .-.. --- ....")
          )