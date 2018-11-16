import re
with open("input_text.txt", "r") as test_file:
    u = test_file.read()


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


with open("cleaned_output_text.txt", "w") as z:
    bersih = cleanhtml(u)
    print(bersih, file=z)
