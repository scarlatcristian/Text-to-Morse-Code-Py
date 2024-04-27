morse_code = {'A':'.-','B':'-...','C':'-.-.','D':'-..', 'E':'', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..','0': '-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..', '9':'----.'
}

text=input('Input a text to transform in morse code: ').upper()
words = text.split()
formatted_text = ''

for index, word in enumerate(words):
    for letter in word:
        formatted_text += morse_code[letter] + ' '
    if index < len(words) - 1:
        formatted_text += '/ '

print(formatted_text)