import argparse
import gzip
import pkg_resources
import sys

from .serializer import deserialize_digraph
from .phrasegenerator import GraphPhraseGenerator


CORPUS = {
    'dracula': 3,
}

PACKAGE = __name__.split('.', 1)[0]
CORPUS_PATH = ['data']


def script_phrase():
    parser = argparse.ArgumentParser()

    parser.add_argument('corpus', choices=CORPUS)

    args = parser.parse_args()

    corpus_path = '/'.join(CORPUS_PATH + ['{}.claptrap.gz'.format(args.corpus)])
    graph_dump = pkg_resources.resource_stream(PACKAGE, corpus_path)

    # gzip.GzipFile(fileobj=graph_dump, mode='rb')
    data = gzip.decompress(graph_dump.read())

    G = deserialize_digraph(data)
    phrase_gen = GraphPhraseGenerator(G)

    print(phrase_gen.phrase())
