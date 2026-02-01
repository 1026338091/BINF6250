# Introduction
Description of the project

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

```


# Successes
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Other members' reflections on the project

# Generative AI Appendix
As per the syllabus
