import numpy as np


def generate_random_text(markov_model, seed=42):
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
        if next_word == "*E*" or next_word is None:
            break

        # c.  append next_word to sentence
        sentence.append(next_word)

        # Sliding Window to remove old variable and add the new
        # transform next word to tuple
        current_state = current_state[1:] + (next_word,)

    # 5. combine the sentence with ""
    return " ".join(sentence)

"""
main progrem
"""
"""
read the fish book
"""
markov_model = dict()

# open file
try:
    with open("data/one_fish_two_fish.txt", "r") as f:

        # 2. read all line
        text_content = f.read()

        # clean data
        text_content = text_content.replace("\n", " ")

        # define punctuation
        punctuation_list = [",", ".", "!", "?", "\"", ";", ":"]

        for p in punctuation_list:
            #  "," transform to " , " for split in markov_modle
            text_content = text_content.replace(p, " " + p + " ")

        # for example "fish," -> "fish , "

        # train model
        markov_model = build_markov_model(markov_model, text_content, order=2)

    # spawn and print output
    print("output")
    generated_text = generate_random_text(markov_model, seed=42)
    print(generated_text)

except FileNotFoundError:
    print("error: can't find the file 'one_fish_two_fish.txt' exist?")