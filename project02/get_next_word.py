import numpy as np

def get_next_word(current_word, markov_model, seed=42):
    
    if seed is not None:
        np.random.seed(seed)

    #check current_word if in the markov_model
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
        
        chosen_word = str(np.random.choice(candidates, p=probabilities))
        
        # return chosen word
        return chosen_word
        
    else:
        # cuurent_word not in markov_mopdel
        return None