

def text_file(text,positive,negative):
    pcnt = 0
    ncnt = 0
    neut_cnt = 0
    P=[]
    N=[]
    with open(text,'r',errors='ignore') as f:
        text = f.read()
        text = text.replace("\n",' ')
        text = text.replace('?','.')
        text = text.replace('!', '.')
        text = text.replace(':', '')
        text = text.replace('-', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace(',','')
        text = text.lower()
    with open(positive,"r") as f1:
        for i in f1:
            i = i.replace("\n","")
            P.append(i)
    with open(negative, "r") as f2:
        for i in f2:
                i = i.replace("\n", "")
                N.append(i)

    sentences=text.split(".")

    for sentence in sentences:
        words = sentence.split(" ")
        words = set(words)
        positive_words = set(P)
        negative_words = (set(N))

        if len(positive_words.intersection(words)) > len(negative_words.intersection(words)):
           pcnt+= 1


        elif len(positive_words.intersection(words)) < len(negative_words.intersection(words)):
             ncnt+= 1
        else:
             neut_cnt+= 1
    print("Positive Words: ",pcnt)
    print("Negative Words : ",ncnt)
    print("Nuetral Words: ", neut_cnt)
def main():
    negative = "negativesentimentwords.txt"
    text = 'thehoundofthebaskervilles.txt'
    positive = "positivesentimentwords.txt"
    text_file(text,positive,negative)

main()
