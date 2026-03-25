def clean_text(text):
    #standardize to lowercase
    text = text.lower()
  
    # List of punctuation to treat as separate tokens
    #exclude the single quote 
    punctuation = [",", ".", "!", "?", "\"", ";", ":", "(", ")", "—"]
    for p in punctuation:
        text = text.replace(p, f" {p} ")
    return text
