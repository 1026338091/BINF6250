# Introduction
Description of the project

# Pseudocode
Put pseudocodes in this box:

build_markov_model(markov_model, text, order):
#handl date
split text with"" to get wrod_list
insert"*s*"(denpend on order)in the star and "*E*" in the end
word_list = *s* * order + word + *E*


#iterate data:
  for word in word_list 
 if order == 1
    current_state = word[i]
 elif:
    current_state = tuple(word[i:i + order])

 get next_word: word[i + order]

 checck if current_state in markov_modle:
    if not:
      creat key current_state in markov_modle
      

 if next_word not in markov_model[current_state]:
    markov_model[current_state][next_word] = 0

 markov_molel[current_state][next_word] += 1

 return the output modle




import numpy as np

def get_next_word(curren_word, makov_model, seed = 42):



 





 
  
```
Some pseudocodes here
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
