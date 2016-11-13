# encoding: utf-8
from csv import reader
import slob
import os

PLAIN_TEXT = 'text/plain; charset=utf-8'
LICENSE = 'Attribution-NonCommercial-ShareAlike 2.5 Generic'
CREATED_BY = 'powion'

langs = ['eng', 'fre', 'ger', 'ita', 'jap', 'kor', 'spa']

def make_dict(l1, l2):
    filename = 'dict/pokemon_' + langs[l1] + '_' + langs[l2] + '.slob'
    if os.path.exists(filename):
        os.remove(filename)
    with slob.create(filename) as dic:
        dic.tag('license', LICENSE)
        dic.tag('created-by', CREATED_BY)
        dic.tag('label', 'Pokémon ' + langs[l1].title() + '-' + langs[l2].title())
        with open('all_languages.csv', newline='') as csvfile:
            csvreader = reader(csvfile)
            for row in csvreader:
                input_terms(row[l1], row[l2], dic)
    print('Finished dic for ' + langs[l1] + ' ' + langs[l2])

def input_terms(w1, w2, dic):
    term1 = w1 + '  -  ' + w2
    term2 = w2 + '  -  ' + w1
    dic.add(w2.encode('utf-8'), term1, content_type=PLAIN_TEXT)
    dic.add(w1.encode('utf-8'), term2, content_type=PLAIN_TEXT)

def main():
    for i in range(0, len(langs)):
        for j in range(i+1, len(langs)):
            make_dict(i, j)
    print('Done!')

main()
