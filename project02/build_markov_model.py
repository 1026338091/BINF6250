
def build_markov_model(new_txt, markov_model={}, order=1):
    # lower case and split
    if isinstance(new_txt, str):
        words = new_txt.lower().split()
    else:
        words = new_txt

    #insert start and end
    start_token = ['*S*'] * order
    end_token = ['*E*']

    words = start_token + words + end_token

    #iterate though words
    for i in range(len(words) - order):

        current_state = tuple(words[i:i + order])
        
        # get next word
        next_word = words[i + order]

        #update markov model
        # if current state not in markov model
        if current_state not in markov_model:
            markov_model[current_state] = {}

        #if next word not in dic
        if next_word not in markov_model[current_state]:
            markov_model[current_state][next_word] = 0

        # count all frequencies
        markov_model[current_state][next_word] += 1

    return markov_model