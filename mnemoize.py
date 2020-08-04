#!/usr/bin/env python3
from __future__ import annotations
from typing import List
import os

__langs__ = {}


def get_words(lang: str = "english") -> List:
    global __langs__
    p = os.path.join(os.path.dirname(__file__), "bip-0039", lang + ".txt")
    if lang not in __langs__:
        if os.path.isfile(p):
            fulltext = [x.strip() for x in open(p, "r").readlines()]
            reverse = {}
            for num, word in enumerate(fulltext):
                reverse[word] = num
            __langs__[lang] = [fulltext, reverse]
    return __langs__[lang]


def pack(num: int, lang: str = "english") -> str:
    words = get_words(lang)[0]
    wnum = num
    res = []
    while wnum > 0:
        res.append(words[wnum & 2047])
        wnum = wnum >> 10
    return " ".join(res)


def unpack(text: str, lang: str = "english") -> int:
    words = get_words(lang)[1]
    wnum = 0
    for word in reversed(text.split(" ")):
        wnum = wnum << 10
        wnum = wnum | words[word]
    return wnum


if __name__ == "__main__":
    import random, uuid

    t = pack(uuid.uuid4().int, "russian")
    print(t)
    unpack(t, "russian")
