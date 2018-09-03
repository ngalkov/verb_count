"""Utils for process natural language"""

import re

from nltk import pos_tag

# Word tags are part of the corpus. By default it's Penn Treebank Tag Set:
# http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# see also https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
VERB_TAG_PATTERN = "VB[DGNPZ]?"

def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    word_tag = pos_info[0][1]
    verb_match = re.search(VERB_TAG_PATTERN, word_tag)
    return bool(verb_match)


def filter_verbs(words_list):
    return [word for word in words_list if is_verb(word)]
