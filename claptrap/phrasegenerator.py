import collections
import random

from .munging import (
    mat_to_sparse,
    matgen,
    phrase,
    sparse_dump,
    sparse_load,
    word_gen,
)


IGNORE = {'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'chapter', 'gutenberg'}


class PhraseGenerator:
    @classmethod
    def from_corpus(cls, corpus, threshold=1000):
        counter = collections.Counter(corpus)
        words = [
            word
            for word, count
            in counter.most_common(threshold)
            if word.lower() not in IGNORE
        ]
        sparse = mat_to_sparse(matgen(words, corpus))
        return cls(words, sparse)

    @staticmethod
    def _load_file(path):
        with open(path, 'rb') as f:
            if f.read(5) == b'\xfd7zXZ':
                f.seek(0)
                return f.read()
        with open(path, 'r') as f:
            return f.read()

    @classmethod
    def from_dump(cls, *, file=None, data=None):
        if file is not None:
            if isinstance(file, str):
                data = cls._load_file(file)
            else:
                data = file.read()

        sparse, words = sparse_load(data)
        return cls(words, sparse)

    def __init__(self, words, matrix):
        self.words = words
        self.matrix = matrix
        self.gen = word_gen(words, matrix)

    def phrase(self, length=[100, 120]):
        return phrase(self.gen, length)

    def to_file(self, path):
        with open(path, 'wb') as f:
            f.write(sparse_dump(self.matrix, self.words))


def pick_random_node(G):
    index = random.randrange(len(G))
    for n, node in enumerate(G.nodes()):
        if n == index:
            return node


def weighted_next(G, source):
    if not len(G[source]):
        return pick_random_node(G)
    nodes, weights = zip(*((e['id'], e['weight']) for e in G[source].values()))
    return random.choices(nodes, weights)[0]


class GraphPhraseGenerator:
    def __init__(self, digraph):
        self.digraph = digraph
        self._walker = self._walk()

    def _walk(self):
        node = pick_random_node(self.digraph)
        while True:
            yield node
            node = weighted_next(self.digraph, node)

    def phrase(self, length=(60, 100)):
        try:
            min_len, max_len = length
        except TypeError:
            min_len = max_len = length
        if min_len > max_len:
            raise ValueError('Minimum length must be smaller than the maximum length')
        if min_len < 1:
            raise ValueError('Length must be positive')

        accum = ''
        while not accum.isalpha():
            accum = next(self._walker).title()

        term = False
        while len(accum) < min_len:
            word = next(self._walker)
            if word in set('.!?;,:'):
                accum += word
                if word in set('.!?'):
                    term = True
            else:
                if term:
                    word = word.title()
                    term = False
                accum += ' ' + word

        accum = accum[:max_len]
        if accum[-1] == ' ':
            return accum[:-1] + random.choice('.!?s')
        return accum
