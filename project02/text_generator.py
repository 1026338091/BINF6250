from pathlib import Path
from model_arnold import build_mmodel
from build_markov_model import build_markov_model
from get_next_word import get_next_word
from pprint import pprint

def generate_text(filename, order=1, split_punct=False, max_line_len=128, n_lines=64, seed=None):
    
    def check_punct(entry):
        output = [[]]
        j = 0
        for i in range(len(entry)):
            if ord(entry[i]) in range(33, 64) or entry[i] == "\n":
                output.append([entry[i]])
                if i < len(entry) - 1:
                    output.append([])
                    j += 2
            else:
                output[j].append(entry[i])
        return ["".join(entry) for entry in output if len(entry) > 0]
    
    def format_output(text):
        for i in range(len(text) - 1, -1, -1):
            if text[i] in {"*S*", "*E*"}:
                text.pop(i)
            elif len(text[i]) == 1:
                if ord(text[i]) in range(33, 64):
                    text[i - 1] += text[i]
                    if i < len(text) - 1:
                        if text[i] in {"!", ".", "?"}:
                            text[i + 1] = text[i + 1][0].capitalize() + text[i + 1][1:]
                    text.pop(i)
                elif text[i] == "i":
                    text[i] = text[i].capitalize()
        output = " ".join(text)
        output = output[0].capitalize() + output[1:]
        return output



    path = Path(__file__).parent / "data" / f"{filename}.txt"

    with open(path, "r", encoding="utf8") as f:
        lines = f.readlines()
    
    model = {}
    for line in lines:
        word_list = line.split(" ")
        word_list = [word.lower() for word in word_list]
        if split_punct:
            clean_words = []
            for word in word_list:
                clean_words.extend(check_punct(word))
            word_list = clean_words
        # check = build_mmodel(word_list, order=order)
        seq_model = build_markov_model(word_list, markov_model={}, order=order)
        # if seq_model != check:
        #     print("ERROR")
        for key in seq_model:
            if key in model:
                for sub_key in seq_model[key]:
                    if sub_key in model[key]:
                        model[key][sub_key] += seq_model[key][sub_key]
                    else:
                        model[key][sub_key] = seq_model[key][sub_key]
            else:
                model[key] = seq_model[key]

    output = []
    for i in range(n_lines):
        j = order
        line_out = ["*S*" for _ in range(order)]
        while j < max_line_len:
            tok = get_next_word(tuple(line_out[j - order:j]), markov_model=model, seed=seed)
            if tok is not None:
                line_out.append(tok)
            j += 1
        line_out_clean = format_output(line_out)
        print(line_out_clean)
        input()

generate_text("one_fish_two_fish", split_punct=True, order=5)