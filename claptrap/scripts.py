import argparse
import gzip
import pkg_resources
import random
import sys

from .canned import wub
from .phrasegenerator import GraphPhraseGenerator
from .serializer import deserialize_digraph


CANNED = "canned"
CORPUS = "corpus"

DRACULA = "dracula"
WUB = "wub"

DRAC_CHOICE = {"c": DRACULA, "min": 10, "max": 100}

CORPORA = {"d": DRAC_CHOICE, "drac": DRAC_CHOICE, "dracula": DRAC_CHOICE}
CANNED = {"wub": {"f": wub, "min": 3, "max": 30}}


def script_phrase():
    import cProfile

    p = cProfile.Profile()
    p.enable()
    _script_phrase()
    p.disable()
    p.dump_stats("profile.prof")


def _script_phrase():
    parser = argparse.ArgumentParser()

    parser.add_argument("corpus", choices=sorted(list(CORPORA) + list(CANNED)))
    parser.add_argument(
        "-l", "--length", help="Length or length range (delimit min-max)"
    )
    parser.add_argument(
        "-n",
        "--output-count",
        type=int,
        default=1,
        help="Number of phrases to generate",
    )

    args = parser.parse_args()

    if args.length:
        lenrange = [int(x) for x in args.length.split("-")]
        if len(lenrange) == 1:
            lenrange = lenrange * 2
        assert len(lenrange) == 2
    else:
        lenrange = None

    if args.corpus in CORPORA:
        corpus = CORPORA[args.corpus]
        phrase_gen = GraphPhraseGenerator.from_resource(corpus["c"])

        for _ in range(args.output_count):
            if lenrange is None:
                min_length = random.randint(corpus["min"], corpus["max"])
                max_length = corpus["max"]
            else:
                min_length = random.randint(*lenrange)
                max_length = lenrange[1]

            print(phrase_gen.phrase(length=(min_length, max_length)))

    elif args.corpus in CANNED:
        canned = CANNED[args.corpus]
        for _ in range(args.output_count):
            if lenrange is None:
                length = random.randint(*(canned[k] for k in ["min", "max"]))
            else:
                length = random.randint(*lenrange)

            print(canned["f"](length))
