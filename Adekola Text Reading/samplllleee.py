import collections

file_name = "Story"

def read_file_content(file_name):
    s = open('story.txt').read()
    return (s)
read_file_content(file_name)

s = open('story.txt').read()
def count_words():
    
    s_list = s.split()
    print(s_list)
    s_count = collections.Counter(s_list)
    print(s_count)


print(count_words())