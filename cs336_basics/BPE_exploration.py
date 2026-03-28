## This entire file is going to be a "playground" for implementing BPE
import regex as re

PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
print(re.findall(PAT, "some text that I'm trying to pretokenize right now! 10000 1000"))
# output: ['some', ' text', ' that', ' I', "'m", ' trying', ' to', ' pretokenize', ' right', ' now', '!', ' 10000', ' 1000']

'''
This tokenizer looks at:
'(?:[sdmt]|ll|ve|re) --> this is to separate contractions with these endings
| ?\p{L}+ --> this matches optional space followed by one or more letters
| ?[^\s\p{L}\p{N}]+ --> matches optional space followed by one or more digits
|\s+(?!\S) --> matches optional space followed by one or more punctuation symbols
|\s+ --> this matches whitespace characters that are not followed by non-whitespace, could indicate trailing whitespace ata end of line

This is the GPT-2 pre-tokenizer that splits text into meaningful chunks.

Notes:
" text" and "text" are DIFFERENT tokens, which means that we are looking at the fact that it's not the first word in a sentence '''
iterator = re.finditer(PAT, "some text that I'm trying to pretokenize right now! 10000 1000")
print(next(iterator))
print(next(iterator))
'''
These return regex.Match functions, which have the functions:
.group(): returns the matched string
.start(): returns the start position in the text
.end(): returns the end position in the text
.span(): tuple of the (start,end)

Also, an iterator is a list that doesn't store everything in memory at once. You call
next(iterator) to get the next element. You can also do [for i in iterator] similarly
'''
print(max([("A", "B"), ("A", "C"), ("B", "ZZ"), ("BA", "A")])) # max() lets you find the lexographical maximum of anything, including pairs of tokens

'''
Regex basics:
Regex is a pattern-matching language that describes text patterns. You can search for, match, and change
strings based on patterns. Here are the metacharacters:
.: any single character --> a.c matches "abc", "adc", "a?c"
*: 0 or more of previous --> ab*c matches "ac", "abbbbc"
+: 1 or more of previous --> ab+c matches "abc, "abbc", NOT "ac"
?: 0 or 1 of previous --> ab?c matches "ac, "abc"
|: or --> cat|dog matches "cat", "dog"
^: start of string --> ^hello matches "hello darkness my old friend"
$: end of string --> $world matches "hello world
\: escape character --> \. matches the literal dot, this stops confusion between $3 and end of word
[]: character classes --> [aeiou] matches any letter in the list, [0-9], [a-z], [^0-9] is anything NOT in the list, ^ inside [] is NOT
{#}: repetitions --> a{3} matches "aaa", a{2,4} is 2-4, a{3,} is 3 and up

There are also shortcuts
\d: any digit [0-9]
\D: any non-digit [^0-9]
\w: any word character [a-zA-Z0-9_]
\W: any non word character
\s: any whitespace (space, tab, newline)
\S: any non-whitespace

Regex functions:
re.search(regex, text): find first match --> match object
re.match(regex, text): find match ONLY if it's at the start --> match object
re.findall(regex, text): find all matches --> list(match)
re.finditer(regex, text): find all matches --> iterator(match)
re.sub(regex, replacement, text): replace any valid regex with the replacement text --> strin
re.fullmatch(regex, text): returns True if whole string matches, False if not 
re.split(regex, text): return text split on the characters inputted --> list(string)'''
# I'm going to play around with it a little bit, here are two implementations of an email regex, first is more rigid than the second
email_reg = r"([a-z]|[A-Z])+\.([a-z]|[A-Z])+@(yahoo|gmail|hotmail)\.com"
print(re.fullmatch(email_reg, "akash.bhowmick@hotmail.com"))

email_reg_compressed = r"[A-Za-z0-9\.]+@(yahoo|gmail|hotmail)\.com"
print(re.fullmatch(email_reg_compressed, "akabho23@gmail.com"))


