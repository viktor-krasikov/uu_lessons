class WordsFinder:
    path = ''

    def __init__(self, *file_names):
        self.file_names = file_names

    def __remove_punctuation(self, text):
        for sym in ['\n', ',', '.', '=', '!', '?', ';', ':', ' - ']:
            text = text.replace(sym, ' ')
        return text

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(self.path + file_name, 'r', encoding='utf-8') as file:
                all_words[file_name] = self.__remove_punctuation(file.read().lower()).split()
        return all_words

    def find(self, word):
        word = word.lower()
        return {file_name: (words.index(word) + 1)
                for file_name, words in self.get_all_words().items() if word in words}

    def count(self, word):
        word = word.lower()
        return {file_name: words.count(word) for file_name, words in self.get_all_words().items()}


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
