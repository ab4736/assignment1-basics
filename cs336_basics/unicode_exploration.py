import sys
# ## Understanding Basic Unicode

# print(ord('牛')) # this returns the "codepoint" integer representation
# print(chr(ord('牛'))) # this returns the character for the integer representation

# print(chr(0)) # seems to return nothing/a space
# print(repr(chr(0))) # this returns \x00, the repr of the character

# print("this is a test" + chr(0) + "string") # here it doesn't show up at all, so it's literally just a null value

# # TAKEAWAY: Unicode standard, shown above, converts characters to a codepoint integer, but how they're encoded into bytes is shown below


# ## Unicode Encodings, UTF-8 is the dominant encoding standard for the Iternet
# test_string = "whats up! 你好朋友" 
# utf_encoded = test_string.encode("utf-8")
# print(type(utf_encoded)) # this is of the type "bytes"
# print(sys.getsizeof(utf_encoded), "bytes") # this tells us the total size in bytes of the object, which is 55 bytes
# print(len(utf_encoded))  # this tells us how many bytes are being stored in our string, which is 22 bytes

# # Note: overhead in CPython for a bytestring is 33 bytes, which makes sense here

# print(list(utf_encoded)) # this turns the UTF encoding into a list
# print(len(test_string)) # 14
# print(len(utf_encoded)) # 22

# print(utf_encoded.decode("utf-8")) # this gives us back our original string

# # TAKEAWAY: One byte is not always one character, and this number depends on your encoding scheme, use .encode() and .decode() to encode and decode strings

## Different Unicode Encodings, Problem unicode2
test_string_chinese = "你好朋友"
test_string_english = "whats up! how are you doing?"
english_string_utf8 = test_string_english.encode("utf-8")
english_string_utf16 = test_string_english.encode("utf-16")
english_string_utf32 = test_string_english.encode("utf-32")
chinese_string_utf8 = test_string_chinese.encode("utf-8")
chinese_string_utf16 = test_string_chinese.encode("utf-16")
chinese_string_utf32 = test_string_chinese.encode("utf-32")

print("The UTF-8 length is:",len(list(english_string_utf8)),"while the english string length is", len(test_string_english) ) # 28 length, 28 * 1, no BOM because the encoding is "byte-sequential", there is no endianness involved
print("The UTF-16 length is:",len(list(english_string_utf16)),"while the english string length is", len(test_string_english) ) # 58 length, 28 * 2 + 2, because UTF-16 adds a 2 byte BOM (byte order mark) in the beginning
print("The UTF-32 length is:",len(list(english_string_utf32)),"while the english string length is", len(test_string_english) ) # 116 length, 28 * 4, but also adds a 4 byte BOM (byte order mark)

print("The UTF-8 length is:",len(list(chinese_string_utf8)),"while the chinese string length is", len(test_string_chinese) ) # 12 length for 4 characters, uses 3 per character
print("The UTF-16 length is:",len(list(chinese_string_utf16)),"while the chinese string length is", len(test_string_chinese) ) # 10 length, 4 * 2 + 2, note that ANY character in the basic multilingual plane (BMP) uses 2 bytes here, while emojis etc. use 4 bytes
print("The UTF-32 length is:",len(list(chinese_string_utf32)),"while the chinese string length is", len(test_string_chinese) ) # 20 length, 4 * 4 + 4, note that ANY character is still 4 bytes, and there's a 4-byte BOM as well

'''
Side tangent: Endianness

The word endianness comes from Gulliver's Travels (cool), where the people in the island
argue about whether to break a soft boiled egg on the big end or little end, becoming known
as little endians and big endians.

Little endian: putting the most significant LAST, like URDU

Big endian: putting the most significant bit FIRST, like ENGLISH

Example: in the number 512, 5 is the most significant, representing 500, while 215 would be little-endian.

Example: 
The letter 'A"
UTF-8: 41
UTF-16-LE: 41 00
UTF-16-BE: 00 41

The BOM in UTF-16 is FF FE for little-endian and FE FF for big-endian.

UTF-8 does not care about endianness because there's no ordering there, it's just a byte sequence
For UTF-16 and UTF-32, since characters are stored in groups of 2 and 4 bytes, they need an ordering (endianness), and have the BOM
'''
# # Playing around with an incorrect encoding function
# for b in test_string_chinese.encode("utf-8"):
#     print(b) # this prints the byte value

# print("Indexing bytestring directly", test_string_chinese.encode("utf-8")[1]) # this works!


def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring]) 

# This takes in a byestring, decodes every byte one by one, then appends them
try:
    print(decode_utf8_bytes_to_str_wrong("Working for English".encode("utf-8")))
except:
    print("This gave an error with the string: Working for English")

try:
    print(decode_utf8_bytes_to_str_wrong("你好".encode("utf-8")))
except:
    print("This gave an error with the string: 你好")

# The reason this doesn't work is that UTF-8 does NOT always mape one character to one byte, and only does so when it is an ASCII character

# Just to see, here are the first 100 UTF-8 characters, a lot of them are escape sequences (\n, \t, etc.), but the letters are consecutive with each other
for i in range(100):
    print(repr((bytes([i])).decode("utf-8")))

'''
Small tangent: UTF-8 continuation vs. start bytes

In UTF-8, since the size is flexible, you need to know how many bytes the token is going
to be, otherwise you might have some ambiguity. So, the first bit follows this pattern:
0xxxxxx --> 1-byte char (7 payload bits), payload means "information", so there are 127 possible ASCII characters stored here
110xxxxx --> 2-byte char (5 payload bits)
1110xxxx --> 3-byte char (4 payload bits)
11110xxx --> 4 byte char (3 payload bits)

Then, every byte after in the SAME character is in the form:
10xxxxxx --> continuation byte (6 payload bits)

Based on this, a 2 byte sequence that starts with 10xxxxxx would be illegal.
'''
try:
    print(repr((bytes([int("10111100", 2), int("10101010", 2)])).decode("utf-8"))) 
except:
    print("10111100, 10101010 cannot be decoded by UTF-8")

# Note: bytes is immutable, while bytearray is mutable, which means you can change bytearray
b = bytes([65, 66, 67])
ba = bytearray(b)

try:
    b[0] = 97
except:
    print("We can not change bytes elements") # this will print

try:
    ba[0] = 97

except:
    print("We can not change bytearray elements")

    