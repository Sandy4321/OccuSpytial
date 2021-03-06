import numpy as np
import pytest

from occuspytial.distributions import (
    DenseMultivariateNormal,
    GaussianMarkovRandomField,
    PolyaGamma,
)


def test_dense_mvnorm():
    d = DenseMultivariateNormal()
    mat = np.random.rand(5, 5)
    cov = mat.T @ mat
    mean = np.array([0.] * 5)

    cov_copy = cov.copy()
    arr = d.rvs(mean, cov_copy)

    assert isinstance(arr, np.ndarray)
    assert arr.ndim == 1
    assert arr.shape[0] == 5
    # check if input covariance was overwritten
    assert not np.allclose(cov, cov_copy)

    cov_copy = cov.copy()
    arr = d.rvs(mean, cov_copy, overwrite_cov=False)
    assert np.allclose(cov_copy, cov)


def test_gaussian_markov_random_field():
    d = GaussianMarkovRandomField()
    mat = np.random.rand(5, 5)
    prec_mat = np.linalg.inv(mat.T @ mat)
    mean = np.array([0.] * 5)

    prec_mat_copy = prec_mat.copy()
    arr = d.rvs(mean, prec_mat_copy)

    assert isinstance(arr, np.ndarray)
    assert arr.ndim == 1
    assert arr.shape[0] == 5
    # check if input precision matrix was overwritten
    assert not np.allclose(prec_mat, prec_mat_copy)

    prec_mat_copy = prec_mat.copy()
    arr = d.rvs(mean, prec_mat_copy, overwrite_prec=False)
    assert np.allclose(prec_mat_copy, prec_mat_copy)


def test_polyagamma():
    d = PolyaGamma()

    out = d.rvs(1, 1)
    assert isinstance(out, float)
    assert out > 0

    a = np.array([1.] * 5)
    b = np.array([2.] * 5)

    out = d.rvs(a, b)
    assert out.size == a.size == b.size

    c = b.copy()
    d.rvs(a, b, out=b)
    assert not np.allclose(c, b)

    with pytest.raises(ValueError, match="expected 'double' but got 'long'"):
        d.rvs(np.array([0] * 5), b)
