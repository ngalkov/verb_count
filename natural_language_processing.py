"""Utils for process natural language"""


from nltk import pos_tag


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def filter_verbs(words_list):
    return [word for word in words_list if is_verb(word)]