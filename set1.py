# Challenges from https://cryptopals.com/sets/1

import codecs
import string

from collections import Counter

char_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
first_six = char_frequency[0:6]
last_six = char_frequency[-6:]

def hex_to_ascii(hex_string):
    return codecs.decode(hex_string, "hex")

def ascii_to_hex(ascii_string):
    return codecs.encode(ascii_string.encode(), "hex")

def hex_to_base64(hex_string):
    base64_string = codecs.encode(hex_to_ascii(hex_string), "base64")
    return base64_string.rstrip().decode("UTF-8")

def fixed_xor(arg1, arg2): 
    xor = hex(int(arg1, 16) ^ int(arg2, 16))
    return str(xor)[2:]

def xor_decode(hex_string):
    _outputs = {}

    for c in string.ascii_lowercase + string.ascii_uppercase + "0123456789":
        _xor = fixedXOR(((c * int(len(hex_string)/2)).encode().hex()), hex_string)
        ascii_string = hex_to_ascii(_xor)

        score = score_string(ascii_string)
        _outputs[ascii_string] = score


    sorted_scores = sorted(_outputs.items(), key=lambda kv: kv[1], reverse=True)
   
    max_strings = [] 
    max_score = None
    for e in sorted_scores:
        if not max_score:
            max_score = e[1]
            # print(f"Max Score: {max_score}")
            #print(e[0])
            max_strings.append(e[0].decode("UTF-8"))
        elif e[1] == max_score:
            max_strings.append(e[0].decode("UTF-8"))
            #print(e[0])

    return max_strings
        
        
# Score the string based on how likely it is English text
def score_string(ascii_string, expect_spaces=True): 
    score = 0
    counter = Counter(ascii_string.strip())
    i = 0

    if expect_spaces and ascii_string.find(b" ") == -1:
        return 0

    for c in counter:
        if i < 6:
            if chr(c).upper() in first_six:
                score += 1

        elif i >= (len(ascii_string) - 6):
            if chr(c).upper() in last_six:
                score += 1

        i += 1

    return score

if __name__ == "__main__":
    _input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    xor_decode(_input)
    #print(first_six, last_six)
