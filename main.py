# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
def read_file_content(filename):
    # [assignment] Add your code here
    lines = ""
    with open(filename) as f:
      lines = f.readlines()
    return lines

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    for str in text:
      words = str.split()
      for word in words:
        lower_case_word = word.lower()
        if lower_case_word in counts:
          counts[lower_case_word] += 1
        else:
          counts[lower_case_word] = 1
    return counts
print(count_words())









