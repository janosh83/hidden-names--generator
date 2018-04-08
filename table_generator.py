# coding=utf8

from random import randint

# word_list = ["prvni", "druhe", "treti", "ctvrte", "pate", "seste", "sedme", "osme", "devate"]
# word_set = set(word_list)
# width = 3
# length = 3

word_list = ["Kýbl",     "Jelito",  "Propiska", "Brokovnice", "Berle",   "Stan",
             "Nůše",     "Okurka",  "Dort",     "Mýdlo",      "Prsten",  "Karty",
             "Koruna",   "Brýle",   "Kožich",   "Vařečka",    "Deka",    "Míč",
             "Pádlo",    "Baterka", "Rum",      "Sandály",    "Obraz",   "Lopata",
             "Kružítko", "Paralen", "Peřina",   "Mucholapka", "Časopis", "Palačinky",
             "Termoska", "Víno",    "Sodovka",  "Topinkovač", "Trenky",  "Diář"]

word_set = set(word_list)
width = 6
length = 6

WORD_COUNT = len(word_list)
NUM_OF_HIDDEN_WORDS = 10
WOLF_INDEX = 13
LISTS_TO_GENERATE = 300

hidden_words = set()

if(width * length != len(word_list)):
    print("incorrect number of word in list found:", len(word_list), "expected ", width*length)

else:


    #print table
    filename = "hidden_names.html"

    with open(filename,"w") as f:

        f.write('<html><head> <meta charset="UTF-8"> <title>Hidden names</title>')
        f.write("<body>")

        for i in range(0, LISTS_TO_GENERATE):
            hidden_words = set()
            for j in range(0, NUM_OF_HIDDEN_WORDS):
                k = randint(0, WORD_COUNT - 1)
                w = word_list[k]
                # print(set([w]), hidden_words, set([w]) & hidden_words)

                while (w in hidden_words) or (w == word_list[WOLF_INDEX]):
                    # selected word has been already selected as hidden word or it is a wolf
                    k = randint(0, WORD_COUNT - 1)
                    w = word_list[k]
                    # print(set([w]), hidden_words, set([w]) & hidden_words)

                # print("adding",w)
                hidden_words.add(w)

            print(hidden_words)

            f.write("<h1>Map "+ str(i) + "</h1>")
            f.write('<table border="1" cellpadding="10">')

            for j in range(0, width):
                line = "<tr>"
                for k in range(0, length):
                    idx = j * width + k

                    line += "<td>"
                    if {word_list[idx]} & hidden_words:
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

            f.write("</table>")
            f.write("<br>")

        f.write("</body> </html>")
        f.close()



