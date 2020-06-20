# mnemoize

Use mnemonic code instead of bytes or passwords.

The whole idea and even wordlists based on BIP-0039.
All wordlists licensed with MIT License (MIT) by Pavol Rusnak
Russian wordlist is from github.com/abdk-consulting/bips

Usage of mnemoize is simple, there are only two public methods:

- `pack(int, language=english)` is used to convert int of any size to a list of words. These words are uniquely and definitely can be converted back to int with
- `unpack(words, language=english)` which is used to reverse words (as one string) back to the corresponding number.

The default value for language is 'english' but you can change it to any from this list:

- chinese_simplified
- chinese_traditional
- english
- french
- italian
- japanese
- korean
- russian
- spanish

Be careful, wordlist will load into memory on the first call of  `pack` or `unpack` methods, once per language.

``` python
>>> import mnemoize
>>> mnemoize.pack(2439857293485792857)
'sleep upon canvas piano lonely auction able'

>>> mnemoize.unpack('sleep upon canvas piano lonely auction able')
2439857293485792857


>>> mnemoize.pack(133713371337133713371337, 'russian')
'вирус казино мрамор разбить месяц хорошо прибыть бригада'
```
