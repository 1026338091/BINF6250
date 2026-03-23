# Introduction
This project is the implementation of the Burrows-Wheeler Transformation. A transformed string can be used for encoding to reduce storage size, or to be quickly searched using the unique Last First property of the Barrows-Wheeler Transformation. 

# Pseudocode

```
# this function makes the BWT the memory-intensive way
def BWT(string: str) -> str:
    if no "$" add to end of string
    matrix = string rotated 1 left each row
    sort by 1st column
    return last column

# create suffix array
def suffix_array(string: str) -> list[int]:
    if no "$" add to end of string
    for each row i, matrix = string[i:]
    order = list 1:len(string)
    zip matrix, order
    sort zip
    unzip
    return order

# create the BWT using the suffix array
def BWT_from_suffix_array(
  text: str, 
  suffix_positions: list[int]
  ) -> str:
    if no "$" add to end of string
    for each suffix position:
        if pos == 0:
            bwt_string = text[-1] # go back around
        bwt_string = text[pos-1]
    return bwt_string

# counts chars lexicographically smaller than each char
def cal_count(string: str) -> dict[str, int]:
    for each unique char in string:
        dict[char] = count
        increment count
    return count dict

# calculate occurences of each char up to each position
def cal_occur(bwt_string: str) -> dict[str, list[int]]:
    for unique char in string:
        for each char in bwt_string:
            if char == key:
                count char
            append count to dict
    return count dict

# update range given char 
def update_range(
  lower: int, 
  upper: int, 
  count: dict[str, int], 
  occur: dict[str, list[int]], 
  char: str,
  bwt_string: str) -> tuple[int, int]:
      (summarized)
    lower = count[char] + occur[char][lower]
    upper = count[char] + occur[char][upper]
    return lower, upper

# search string for query using BWT
def find_match(query: str, reference: str) -> list[int]:
    for char in reversed query:
        if lower > upper:
            return
        lower, upper = update_range()
    return matches in range(lower, upper)

# encode a BWT string
def run_length_encode(bwt_string: str) -> str:
    for char in bwt_string:
        if char == last char:
            count +1
        else:
            encoded = encoded + char + count
    return encoded

# decode an encoded BWT string
def run_length_decode(encoded: str) -> str:
    for symbol in encoded:
        if symbol is alpha:
            if last char was numeric:
                decoded = char * num
                char, num = ""
        if symbol is num:
            num += symbol
    decoded = char * num # last iteration
    return decoded

# recover_string
def recover_string(bwt_string: str, 
  count: dict[str:int],
  occur: dict[str:int]) -> str:
    row = 0, recovered = "$"
    while bwt_string[row] != "$":
        recovered = bwt_string[row] + recovered
        row = count[char] + occur[char][row]
    return recovered  
  
```

# Successes
Description of the team's learning points

# Struggles
We struggled a little trying to understand how the program should use all the functions in one flow. 
We also struggled a lot with indexing, but being able to visualize the trace with the matrix really helped. 

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Victoria Van Berlo
This project was a lot of fun and also frustrating. Our group met a bit late to start so I was able to spend some extra time in the beginning getting comfortable with the easier functions before we met up to discuss the more tricky parts. The indexing tripped me up a lot and I did a lot of printing out matrices to visually track the index progression. Following the provided outline of the functions was also very helpful for creating modular functions that didn't rely on the others to work. I also created the recover_string() function because I felt like it was lacking from run_length_decode().

# Generative AI Appendix
As per the syllabus
