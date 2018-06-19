import collections
import sys

import networkx as nx

from claptrap.munging import gen_words
from claptrap.dumps import dump_word_digraph


def main():
    start_marker = '*** START OF THIS PROJECT GUTENBERG EBOOK DRACULA ***'
    end_marker = '*** END OF THIS PROJECT GUTENBERG EBOOK DRACULA ***'

    try:
        with open('dracula.txt', 'r') as f:
            dracula = f.read()
    except IOError:
        import requests
        dracula = requests.get('http://www.gutenberg.org/cache/epub/345/pg345.txt').text

    dracula = dracula[dracula.find(start_marker) + len(start_marker):dracula.find(end_marker)]

    drac_corpus = list(gen_words(text=dracula))[231:]
    drac_counter = collections.Counter(drac_corpus)

    per_line = 7
    for n, (block, count) in enumerate(drac_counter.most_common(98)):
        print('{:>4d} {:<8s}'.format(count, block), end='')
        if n % per_line == per_line - 1:
            print()

    iwords = iter(drac_corpus)
    prev = next(iwords)
    G = nx.DiGraph()
    for word in iwords:
        if G.has_edge(prev, word):
            G[prev][word]['weight'] += 1
        else:
            G.add_edge(prev, word, weight=1)
        prev = word

    dump_word_digraph(G, '../claptrap/data/dracula.claptrap.gz')


if __name__ == '__main__':
    sys.exit(main())
