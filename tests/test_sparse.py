from claptrap.munging import mat_to_sparse, sparse_dump, sparse_load


def test_sparse_serialdeserial():
    mat = [[1, 0, 2], [0, 3, 100], [10, 4, 5]]
    smat = mat_to_sparse(mat)
    words = ['a', 'b', 'c']
    assert sparse_load(sparse_dump(smat, words)) == (smat, words)
    assert sparse_load(sparse_dump(smat, words, compress=False)) == (smat, words)
