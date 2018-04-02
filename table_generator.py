from random import randint

word_list = ["prvni", "druhe", "treti", "ctvrte", "pate", "seste", "sedme", "osme", "devate"]
word_set = set(word_list)
width = 3
length = 3

WORD_COUNT = len(word_list)
NUM_OF_HIDDEN_WORDS = 3
WOLF_INDEX = 4

hidden_words = set()

if(width * length != len(word_list)):
    print("incorrect number of word in list found:", len(word_list), "expected ", width*length)

else:
    for i in range(0,NUM_OF_HIDDEN_WORDS):
        j = randint(0,WORD_COUNT-1)
        w = word_list[j]
        #print(set([w]), hidden_words, set([w]) & hidden_words)

        while(set([w]) & hidden_words) or (w == word_list[WOLF_INDEX]):
            # selected word has been already selected as hidden word or it is a wolf
            j = randint(0, WORD_COUNT - 1)
            w = word_list[j]
            #print(set([w]), hidden_words, set([w]) & hidden_words)

        #print("adding",w)
        hidden_words.add(w)

    print(hidden_words)

    #print table
    with open("file.html","w") as f:

        f.write("<html><body>")
        f.write("<table>")

        for i in range(0,width):
            line = "<tr>"
            for j in range(0,length):
                idx = i*width + j

                line += "<td>"
                if set([word_list[idx]]) & hidden_words:
                    # hidden word
                    line += "<u>" + word_list[idx] + "</u>"
                elif word_list[idx] == word_list[WOLF_INDEX]:
                    # wolf
                    line += "<b><i>" + word_list[idx] + "</i></b>"
                else:
                    # normal word
                    line += word_list[idx] + " "
                line += "</td>"

            line += "</tr>"
            f.write(line)

        f.write("</table> </body> </html>")
        f.close()



