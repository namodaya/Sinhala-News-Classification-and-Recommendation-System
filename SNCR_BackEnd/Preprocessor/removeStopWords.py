import io
infile = "/home/namo/My_Works/newsAggregator/Sinhala-News-Classification-and-Recommendation-System/SNCR_BackEnd/Preprocessor/stopWordList.txt"
fin = io.open(infile, "r", encoding='utf-8').read()

filename = "/home/namo/My_Works/newsAggregator/Sinhala-News-Classification-and-Recommendation-System/SNCR_BackEnd/Preprocessor/text"
try:
    text = io.open(filename, "r", encoding='utf-8').read()
except UnicodeDecodeError:
    text = io.open(filename, "r", encoding='latin-1').read()
text = text.lower()
words = text.split()
words.sort()


for word in words:
    if word in fin:
        text = text.replace(word,"")
        print text