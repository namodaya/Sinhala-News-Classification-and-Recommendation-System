import io

class removeStopwords:
    def reoveStopWrds(self,text):
        infile = "stopWordList.txt"
        fin = io.open(infile, "r", encoding='utf-8').read()

        text = text.lower()
        words = text.split()
        words.sort()


        for word in words:
            if word in fin:
                text = text.replace(word,"")
                print text