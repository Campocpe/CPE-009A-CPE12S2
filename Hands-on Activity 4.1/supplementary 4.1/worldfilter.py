def word_filter(sentence, bad_words):
    words = sentence.split()
    filtered_words = []
    
    for word in words:
        # Strip punctuation to check if the core word is "bad"
        clean_word = word.strip(".,!?").lower()
        if clean_word in [bw.lower() for bw in bad_words]:
            filtered_words.append("*" * len(word))
        else:
            filtered_words.append(word)
            
    return " ".join(filtered_words)