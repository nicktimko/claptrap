from claptrap import PhraseGenerator


def test_phrasegen_fromdump():
    pg = PhraseGenerator.from_dump(file='dumps/markov-hockey.xz')

    assert len(pg.phrase(length=100)) == 100
    assert len(pg.phrase(length=10)) == 10
    for _ in range(20):
        assert 30 <= len(pg.phrase(length=(30, 40))) <= 40
