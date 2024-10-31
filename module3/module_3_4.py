def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    is_root_words = lambda word1, word2: word1 in word2 or word2 in word1
    return [word for word in other_words if is_root_words(word.lower(), root_word)]


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
