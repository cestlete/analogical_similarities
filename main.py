
"""
# Welcome to Streamlit!

In the meantime, below is an example of what you can do with just a few lines of code:
"""
from openie import StanfordOpenIE
import os
import csv

properties = {
    'openie.affinity_probability_cap': 2 / 3,
}
# https://stanfordnlp.github.io/CoreNLP/openie.html#api
# Default value of openie.affinity_probability_cap was 1/3.


def process_document(txt, doc_name):
    with StanfordOpenIE(properties=properties) as client:
        # text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'
        # print('Text: %s.' % txt)
        # triple_list = client.annotate(txt)
        heading = [["NOUN", "VERB/PREP", "NOUN"]]
        with open(data_path + doc_name + ".OIE", 'w+', encoding="utf8") as resultFile:
            write = csv.writer(resultFile, lineterminator='\n')
            write.writerows(heading)
            for triple in client.annotate(txt):
                write.writerow([triple['subject'], triple['relation'], triple['object']])
                print(triple)
        resultFile.close()

process_document("Barack Obama was born in Hawaii. Richard Manning wrote this sentence.", "test1.txt")
