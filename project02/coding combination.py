import numpy as np

def build_markov_model(markov_model, new_txt, order=1):
    # lower case and split
    words = new_txt.lower().split()

    # insert star and end
    start_token = ['*S*'] * order
    end_token = ['*e*']

    words = start_token + words + end_token

    # iterate though words
    for i in range(len(words) - order):

        # get current state
        current_state = tuple(words[i:i + order])

        # get next word
        next_word = words[i + order]

        # update markov model
        # if current state not in markov model
        if current_state not in markov_model:
            markov_model[current_state] = {}

        # if next word not in dic
        if next_word not in markov_model[current_state]:
            markov_model[current_state][next_word] = 0

        # count all frequencies
        markov_model[current_state][next_word] += 1

    return markov_model

import numpy as np


def get_next_word(current_word, markov_model, seed=42):
    if seed is not None:
        np.random.seed(seed)

    # check current_word if in the markov_model
    if current_word in markov_model:

        # get next_words (dic)

        next_words_dict = markov_model[current_word]

        # exact the key(next_word) values(frenqucy)
        candidates = list(next_words_dict.keys())
        counts = list(next_words_dict.values())

        # caculate total_count
        total_count = sum(counts)

        # caculate probobilitys for each word
        # P(word) = count(word) / total_count
        probabilities = [count / total_count for count in counts]

        # np.random.choice to choosen next word randomly based on probobilitys

        chosen_word = np.random.choice(candidates, p=probabilities)

        # return chosen word
        return chosen_word

    else:
        # cuurent_word not in markov_mopdel
        return None

import numpy as np

new_txt = "one fish two fish red fish blue fish"
def generate_random_text(markov_model, seed= 42):
    """
    generate text depend on markov_modle
    """
    # check order
    # keys [('one', 'fish'), ('fish', 'two')] -> order = 2
    if not markov_model:
        return ""

    first_key = list(markov_model.keys())[0]
    order = len(first_key)

    # set random seed
    if seed is not None:
        np.random.seed(seed)

    # 2. set current_state
    current_state = tuple(["*S*"] * order)

    # 3. set a sentence
    sentence = []

    # 4. generate next_word and combine
    while True:
        # use the get_next_word we made
        next_word = get_next_word(current_state, markov_model, seed=None)

        # check the end and None
        if next_word == "*e*" or next_word is None:
            break

        # c.  append next_word to sentence
        sentence.append(next_word)

        # Sliding Window to remove old variable and add the new
        # transform next word to tuple
        current_state = current_state[1:] + (next_word,)

    # 5. combine the sentence with ""
    return " ".join(sentence)


markov_model = dict()

# open file
try:
    with open("one_fish_two_fish.txt", "r") as f:

        # 2. read all line
        text_content = f.read()

        # clean data
        text_content = text_content.replace("\n", " ")

        # define punctuation
        punctuation_list = [",", ".", "!", "?", "\"", ";", ":"]

        for p in punctuation_list:
            #  "," transform to " , " for split in markov_modle
            text_content = text_content.replace(p, " " + p + " ")

        #repacle "." , "?", "!"
        end_sign = [".", "?", "!"]
        for p in end_sign:
            text_content = text_content.replace(p, " " + p + " *e*")
        # for example "fish," -> "fish , "

        # train model
        markov_model = build_markov_model(markov_model, text_content, order=2)

    # spawn and print output
    print("output")
    generated_text = generate_random_text(markov_model, seed = 42)
    print(generated_text)

except FileNotFoundError:
      print("error: can't find the file 'one_fish_two_fish.txt' exist?")

import numpy as np

# new dic
sonet_markov_model = dict()
sonet = ""  # save t temporary

try:
    with open("sonnets.txt", "r") as f:
        # iterate lines
        for line in f:
            # strip
            line = line.strip()

            # to check""(the end fo a sonet)
            if line == "":
                # when sonet not empty
                if len(sonet) > 0:

                    # punctuation deine
                    for p in [",", ".", "!", "?", ":", ";", "'"]:
                        sonet = sonet.replace(p, " " + p + " ")

                    # train modle with one of sonet
                    sonet_markov_model = build_markov_model(sonet_markov_model, sonet, order=2)

                    # empty sonet for next sonet
                    sonet = ""

            else:
                # cumulate

                sonet = sonet + " " + line

    # when loop end handle the last sonet
    if len(sonet) > 0:
        # punttuation
        for p in [",", ".", "!", "?", ":", ";", "'"]:
            sonet = sonet.replace(p, " " + p + " ")

        sonet_markov_model = build_markov_model(sonet_markov_model, sonet, order=2)

    # generate shakespeare style
    print("sharke style")

    print(generate_random_text(sonet_markov_model, seed=42))

except FileNotFoundError:
    print("erro : can't findsonnets.txt")

if __name__ == "__main__":
    pass
