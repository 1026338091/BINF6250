# Introduction
This project uses the statistical method known as "markov chains" to to build a generative model for text. This model is flexible enough to handle inputs of selected types for this assignment, chiefly divided-by-line and continuous text files. Building this model gave us an opportunity to understand markov models and to work with nested python dicts as a data structure. It also allowed us to think through the considerations entailed by a generative model, specifically how to divide up the input to produce the output that we wanted (sentences).

Files:
- Please see project02.jypnb for the main project
- See test.py for test code
- build_model_2 is an alternate function for testing

# Pseudocode
```python

build_markov_model(markov_model, text, order):
    #handl date
    split text with"" to get wrod_list
    insert"*s*"(denpend on order)in the star and "*E*" in the end
    word_list = *s* * order + word + *E*


    #iterate data:
    for word in word_list 
        if order == 1
            current_state = word[i]
        else:
            current_state = tuple(word[i:i + order])

    get next_word: word[i + order]

    check if current_state in markov_model:
    if not:
        create key current_state in markov_model
      

    if next_word not in markov_model[current_state]:
        markov_model[current_state][next_word] = 0

    markov_model[current_state][next_word] += 1

    return markov_model



import numpy as np

def get_next_word(curren_word, makov_model, seed = 42):

    set a random seed (np.random.seed(seed))

    check current_word if in the markov_model ( return None if not)

    get the next_words(dic)
    next_words_dic = markov_model[current_word]

    extract the key(next_word) values(frenqucy)
    candidates = list(next_words_dict.key())
    counts = [next_words_dict[key] for key in next_words_dict]

    calculate total_count (sum(counts))

    caculate probobility : p(word) = count(word) / total_count
    probabilities = [count / total_count for count in counts]

    use np.random.choice to choose word
    choosen_word = np.random.choice(candidates, p = probabilities)

    return the output(choosen_word)


"""
generate text
"""
import numpy as np

def generate_random_text(markov_model, seed = 42):

    # Check model and get order
    check if markov_model is empty (return "" if empty)
    get the first key from model keys
    calculate order (order = len(first_key))

    # Set Seed (Important: Set only once outside loop)
    if seed is not None:
        set the random seed (np.random.seed(seed))

    # Initialize state
    initialize current_state with "*S*"
    current_state = tuple(["*S*"] * order)

    # Prepare container （sentence）
    create an empty list for sentence (sentence = [])

    # Start Generation Loop
    start a loop (while True):

        # Get the next word (Pass seed=None to keep randomness)
        next_word = get_next_word(current_state, markov_model, seed=None)

        # Check stop condition
        if next_word is "*E*" or None:
            break the looop

        # Save
        append next_word to sentence list

        # Update state (Sliding Window)
        drop the first word and add new word
        current_state = current_state[1:] + (next_word,)

    # Output
    return the joined sentence (" ".join(sentence))

"""
read fish book
"""

# Initialize
init empty model (markov_model = dict())

# try for safty（read file）
try:

    # Open and Read File
    open file in read mode (with open("data/one_fish_two_fish.txt", "r") as f)
    read all content string (text_content = f.read())

    # clean data
    replace newline with space (text_content.replace("\n", " "))

    # define punctuation list (punctuation_list = [",", ".", "!", ...])
    
    loop through punctuation (for p in punctuation_list)
        add space before and after p (replace(p, " " + p + " "))
        # "fish," to "fish , " for modle to split and regard as a variba;

    # 4. Train Model
    build the model with order 2 (build_markov_model(..., order=2))

    # 5. Generate and Output
    print header
    generate random text with seed (generate_random_text(..., seed=42))
    print the result (print(generated_text))

# Handle Error
missing file error (except FileNotFoundError):
    print error message ("error can't find")
```


# Successes
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Eric: It's interesting how varying the order of the model changes the determinism of the output. It would seem that as the order of the model approaches half the length of the input sequence, you basically get rote reproduction of the lines. Markov chains also seem inefficient from a complexity standpoint, where every possible combination of tokens is made as a separate key/vertex in the model. Cool little project.



# Generative AI Appendix
As per the syllabus
