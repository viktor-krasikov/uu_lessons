def all_variants(text):
    for substring_length in range(1, len(text) + 1):
        for start_index in range(0, len(text) - substring_length + 1):
            yield text[start_index:start_index + substring_length]


a = all_variants("abc")
for i in a:
    print(i)
