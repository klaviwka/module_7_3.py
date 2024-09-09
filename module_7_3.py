class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', "'", '"', '-', '—']:
                    content = content.replace(punct, ' ')
                words = content.split()
                words = [word for word in words if word != 's']
                all_words[file_name] = words
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                results[name] = words.index(word.lower()) + 1
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            results[name] = words.count(word.lower())
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))
