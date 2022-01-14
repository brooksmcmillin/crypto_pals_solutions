# Challenges from https://cryptopals.com/sets/1

import codecs
import string

from collections import Counter

char_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
first_six = char_frequency[0:6]
last_six = char_frequency[-6:]

def hex_to_ascii(hex_string):

    # If the hex_string has an odd number of characters, prepend a 0 at the beginning
    if (len(hex_string) % 2) == 1:
        hex_string = '0' + hex_string

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
        _xor = fixed_xor(((c * int(len(hex_string)/2)).encode().hex()), hex_string)
        ascii_string = hex_to_ascii(_xor)

        score = score_string(ascii_string)
        _outputs[ascii_string] = score


    sorted_scores = sorted(_outputs.items(), key=lambda kv: kv[1], reverse=True)
   
    max_strings = [] 
    max_score = None
    for e in sorted_scores:
        try:
            if not max_score:
                max_score = e[1]
                max_strings.append(e[0].decode("UTF-8"))
            elif e[1] == max_score:
                max_strings.append(e[0].decode("UTF-8"))
        except UnicodeDecodeError:
            pass

    return max_strings
        
        
# Score the string based on how likely it is English text
def score_string(ascii_string, expect_spaces=True, no_symbols=True): 
    score = 0
    counter = Counter(ascii_string.strip())
    i = 0

    # If there should be spaces, but there arne't any return 0
    if expect_spaces and ascii_string.find(b" ") == -1:
        return 0

    # If especting normal english w/o symbol, return 0 on symbols
    if no_symbols and not all(
        chr(x).isalpha() 
        or chr(x).isspace() 
        or chr(x) in "'\""
        for x in ascii_string):
        
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

# CHALLENGE 4 START
# Find one string that has been single character XORd from list of strings
def file_xor_decode(file_name):
    max_score = None
    max_strings = [] 

    with open(file_name, 'r') as f:
        lines = f.readlines()

        for line in lines:
            #line = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
            output = xor_decode(line)
            if len(output) > 0:
                score = score_string(output[0].encode('UTF-8'))
                #print(f"{output[0]} - {score}")
                if (not max_score) or (score > max_score):
                    max_score = score
                    max_strings = [output[0]]
                elif score == max_score:
                    max_strings.append((line, output[0]))

    return max_strings[0]


if __name__ == "__main__":
    _input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    xor_decode(_input)
