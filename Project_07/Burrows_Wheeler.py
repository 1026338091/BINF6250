import time
from collections import Counter
from pprint import pprint


def suffix_array(string: str) -> list[int]:

    if not string.endswith('$'):
        string += '$'
    # range(len(string)) generates positions list [0, 1, 2,3,4,5,6]
    # no suffix strings are stored only positions
    # key=lambda i: string[i:] creates each suffix only during comparison
    # once the comparison is done the suffix is immediately discarded
    # sorted() returns positions in lexicographical suffix order
    return sorted(range(len(string)), key=lambda i: string[i:])


def BWT_from_suffix_array(string: str, suffix_positions: list[int]) -> str:
    # ensure string ends with '$' before extracting BWT characters
    if not string.endswith('$'):
        string += '$'

    # for each sorted position i in suffix array
    # if i == 0 then suffix starts at beginning so there is no character before it
    # so take string[-1] last character
    # else take string[i-1] which is the character immediately before suffix eg. position 5 ,take character in position 4
    # joins all the characters into final BWT string and no list is stored for memory efficiency
    return "".join(string[-1] if i == 0 else string[i - 1]for i in suffix_positions)


def run_length_encode(bwt_string: str) -> str:
    # handle empty string edge case
    if not bwt_string:
        return ""

    # use a list to collect encoded pairs in BWT string
    result = []

    # Track with the first character and count
    current = bwt_string[0]
    count = 1

    # iterates starting at index 1 to full length of BWT string
    for i in range(1, len(bwt_string)):

        # if it is the same character increase count
        if bwt_string[i] == current:
            count += 1
        else:
            # if it is different character append to list
            result.append(f"{current}{count}")
            # reset tracker
            current = bwt_string[i]
            count = 1
    # append the final character as the loop ends without storing the final run
    result.append(f"{current}{count}")

    # join all the pairs in the list into one encoded string
    return "".join(result)


def cal_count(string: str) -> dict[str, int]:

    # count frequency of each character using Counter
    freq = Counter(string)

    # empty dict to store the final count for each character
    count_dict = {}
    # track the cumulative count of all characters seen so far
    total = 0

    # sorted(freq.keys()) gives characters in lexicographical order
    for char in sorted(freq.keys()):

        # record how many characters come before this one
        count_dict[char] = total
        # add this character's frequency to total
        total += freq[char]

    return count_dict


def cal_occur(bwt_string: str) -> dict[str, list[int]]:

    # counter counts frequency of each character in one pass
    # sorted () returns characters in lexicographical order
    unique_chars = sorted(Counter(bwt_string))

    # initialise both structures in one loop
    occurrence = {}
    running = {}
    for char in unique_chars:
        # occurrence stores cumulative count list for each character
        occurrence[char] = []
        # running stores current count of each character seen so far
        running[char] = 0

    # walk through BWT string building cumulative counts
    for char in bwt_string:
        # the running count for every character at this position
        running[char] += 1
        for c in unique_chars:
            # append current running count for every character at this position
            occurrence[c].append(running[c])

    return occurrence


def update_range(lower: int, upper: int, count: dict[str, int],
                 occur: dict[str, list[int]], a: str) -> tuple[int, int]:
    if lower == 0:
        occur_lower = 0
    else:
        occur_lower = occur[a][lower - 1]

    lower_new = count[a] + occur_lower

    occur_upper = occur[a][upper]
    upper_new = count[a] + occur_upper - 1

    return (lower_new, upper_new)


def find_match(query: str, reference: str) -> list[int]:

    # ensure reference string ends with '$'
    if not reference.endswith('$'):
        reference += '$'

    # build suffix array and BWT from reference
    positions = suffix_array(reference)
    bwt = BWT_from_suffix_array(reference, positions)

    # build count and occurrence dictionaries from BWT
    count = cal_count(bwt)
    occur = cal_occur(bwt)

    # initialise search range to cover all characters in BWT string
    lower, upper = 0, len(bwt) - 1

    # process query characters from right to left
    for char in reversed(query):

        # if char does not exist in reference
        if char not in count:
            return []

        # narrow the search range using LF mapping
        # update_range for getting count and occur to compute the new lower and upper
        lower, upper = update_range(lower, upper, count, occur, char)

        # if lower exceeds upper the range is empty
        if lower > upper:
            return []

    # positions[i] gives the actual starting position in the original string
    # sorted() returns positions in ascending order
    # generator expression for memory efficiency
    return sorted(positions[i] for i in range(lower, upper + 1))


def run_length_decode(encoded: str) -> str:

    # use a list to collect decoded
    result = []
    # track the walk through the encoded string
    i = 0

    # iterate till the end of the encoded string
    while i < len(encoded):

        # read current character
        char = encoded[i]
        # move one character forward
        i += 1

        # collect all digits that follow to get the count
        num = ""

        # Check if current is the end of the string to avoid index error and if the current is a digit
        while i < len(encoded) and encoded[i].isdigit():

            # concatenate each digit into num string and move one character forward
            num += encoded[i]
            i += 1

        # repeat character by the number of count and append it to list
        result.append(char * int(num))

    # join all decoded characters into one string
    return "".join(result)


if __name__ == "__main__":

    test = "ATTCTTGCT"

    # Encode
    start = time.time()

    positions = suffix_array(test)

    bwt = BWT_from_suffix_array(test, positions)

    encoded = run_length_encode(bwt)

    end = time.time()
    print("Encoded:",encoded)
    print(f"Time to encode: {end - start:.6f}s")
    print()

    # Decode
    start = time.time()
    decoded = run_length_decode(encoded)
    print("Decoded:", decoded)
    end = time.time()
    print(f"Time to decode: {end - start:.6f}s")
    print()


    start = time.time()
    count = cal_count(decoded)
    print("Counts:")
    pprint(count)
    print()
    print("Occurrences:")
    occur = cal_occur(decoded)
    pprint(occur)
    print()

    # start at row 0 which is the first row of the sorted matrix
    row = 0
    # empty string to collect recovered characters
    original_string = ""

    # iterate len(decoded) - 1 times
    for _ in range(len(decoded) - 1):

        # get the character at the current row in the BWT last column
        char = decoded[row]
        # prepend character to original_string
        original_string = char + original_string
        # jump to the corresponding row in the first column for LF mapping
        row = count[char] + occur[char][row] - 1

    # strip the '$' from the recovered string
    original_string = original_string.strip('$')
    end = time.time()
    print("Original string:", original_string)
    print(f"Time to recover: {end - start:.6f}s")

    print()
    query = "TCT"
    matches = find_match(query, test)
    print(f"Match position for '{query}':", matches)

###Encoded: T1$1G1T2C1T2A1C1
###Time to encode: 0.000008s

###Decoded: T$GTTCTTAC
###Time to decode: 0.000005s

###Counts:
###{'$': 0, 'A': 1, 'C': 2, 'G': 4, 'T': 5}

###Occurrences:
###{'$': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
###'A': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
###'C': [0, 0, 0, 0, 0, 1, 1, 1, 1, 2],
### 'G': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
###'T': [1, 1, 1, 2, 3, 3, 4, 5, 5, 5]}

###Original string: ATTCTTGCT
###Time to recover: 0.000114s

### Match position for 'TCT': [2]
