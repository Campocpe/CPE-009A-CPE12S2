import re

def word_filter(sentence, bad_words):
    filtered_sentence = sentence
    
    for word in bad_words:
        
        pattern = r'\b' + re.escape(word) + r'\b'
        filtered_sentence = re.sub(pattern, '*' * len(word), filtered_sentence, flags=re.IGNORECASE)
        
    return filtered_sentence


text = "you are stupid and an idiot "
blacklist = ["idiot", "stupid"]

print(word_filter(text, blacklist))