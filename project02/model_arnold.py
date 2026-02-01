from collections import defaultdict

text = "one fish two fish red fish blue fish"


def build_mmodel(text, order=1):
    text_list = ["*S*" for k in range(order)] + text + ["*E*" for k in range(order)]

    model = defaultdict(lambda: defaultdict(int))
    for i in range(len(text_list) - order):
        segment = text_list[i: i + order + 1]
        antecedent = segment[:order]
        consequent = segment[-1]
        
        if "*E*" in antecedent:
            break

        model[tuple(antecedent)][consequent] += 1

    return model