# -*- coding: utf-8 -*-
# This file as well as the whole tsfresh package are licenced under the MIT licence (see the LICENCE.txt)
# Maximilian Christ (maximilianchrist.com), Blue Yonder Gmbh, 2016

from unittest import TestCase
from contextlib import contextmanager
import warnings

import numpy as np
import pandas as pd


@contextmanager
def warning_free():
    """Small helper to surpress all warnings"""
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        yield


# todo: add test cases for float data
# todo: add test cases for nans, -infs, infs
# todo: add test cases with time series of length one


class DataTestCase(TestCase):
    def create_test_data_sample(self):
        cid = np.repeat([10, 500], 40)
        ckind = np.repeat(["a", "b", "a", "b"], 20)
        csort = [30, 53, 26, 35, 42, 25, 17, 67, 20, 68, 46, 12, 0, 74, 66, 31, 32,
                 2, 55, 59, 56, 60, 34, 69, 47, 15, 49, 8, 50, 73, 23, 62, 24, 33,
                 22, 70, 3, 38, 28, 75, 39, 36, 64, 13, 72, 52, 40, 16, 58, 29, 63,
                 79, 61, 78, 1, 10, 4, 6, 65, 44, 54, 48, 11, 14, 19, 43, 76, 7,
                 51, 9, 27, 21, 5, 71, 57, 77, 41, 18, 45, 37]
        cval = [11, 9, 67, 45, 30, 58, 62, 19, 56, 29, 0, 27, 36, 43, 33, 2, 24,
                71, 41, 28, 50, 40, 39, 7, 53, 23, 16, 37, 66, 38, 6, 47, 3, 61,
                44, 42, 78, 31, 21, 55, 15, 35, 25, 32, 69, 65, 70, 64, 51, 46, 5,
                77, 26, 73, 76, 75, 72, 74, 10, 57, 4, 14, 68, 22, 18, 52, 54, 60,
                79, 12, 49, 63, 8, 59, 1, 13, 20, 17, 48, 34]
        df = pd.DataFrame({"id": cid, "kind": ckind, "sort": csort, "val": cval})
        df = df.set_index("id", drop=False)
        df.index.name = None
        return df

    def create_test_data_sample_wide(self):
        rec = np.rec.array([
            (0, 10, 0, 11, 50),
            (1, 10, 1, 9, 40),
            (2, 10, 2, 67, 39),
            (3, 10, 3, 45, 7),
            (4, 10, 4, 30, 53),
            (5, 10, 5, 58, 23),
            (6, 10, 6, 62, 16),
            (7, 10, 7, 19, 37),
            (8, 10, 8, 56, 66),
            (9, 10, 9, 29, 38),
            (10, 10, 10, 0, 6),
            (11, 10, 11, 27, 47),
            (12, 10, 12, 36, 3),
            (13, 10, 13, 43, 61),
            (14, 10, 14, 33, 44),
            (15, 10, 15, 2, 42),
            (16, 10, 16, 24, 78),
            (17, 10, 17, 71, 31),
            (18, 10, 18, 41, 21),
            (19, 10, 19, 28, 55),
            (20, 500, 0, 15, 4),
            (21, 500, 1, 35, 14),
            (22, 500, 2, 25, 68),
            (23, 500, 3, 32, 22),
            (24, 500, 4, 69, 18),
            (25, 500, 5, 65, 52),
            (26, 500, 6, 70, 54),
            (27, 500, 7, 64, 60),
            (28, 500, 8, 51, 79),
            (29, 500, 9, 46, 12),
            (30, 500, 10, 5, 49),
            (31, 500, 11, 77, 63),
            (32, 500, 12, 26, 8),
            (33, 500, 13, 73, 59),
            (34, 500, 14, 76, 1),
            (35, 500, 15, 75, 13),
            (36, 500, 16, 72, 20),
            (37, 500, 17, 74, 17),
            (38, 500, 18, 10, 48),
            (39, 500, 19, 57, 34)],
            dtype=[('index', '<i8'), ('id', '<i8'), ('sort', '<i8'), ('a', '<i8'), ('b', '<i8')])
        df = pd.DataFrame.from_records(rec)
        df = df.set_index("index", drop=True)
        return df

    def create_test_data_sample_with_time_index(self):
        cid = np.repeat([10, 500], 40)
        ckind = np.repeat(["a", "b", "a", "b"], 20)
        csort = [30, 53, 26, 35, 42, 25, 17, 67, 20, 68, 46, 12, 0, 74, 66, 31, 32,
                 2, 55, 59, 56, 60, 34, 69, 47, 15, 49, 8, 50, 73, 23, 62, 24, 33,
                 22, 70, 3, 38, 28, 75, 39, 36, 64, 13, 72, 52, 40, 16, 58, 29, 63,
                 79, 61, 78, 1, 10, 4, 6, 65, 44, 54, 48, 11, 14, 19, 43, 76, 7,
                 51, 9, 27, 21, 5, 71, 57, 77, 41, 18, 45, 37]
        cval = [11, 9, 67, 45, 30, 58, 62, 19, 56, 29, 0, 27, 36, 43, 33, 2, 24,
                71, 41, 28, 50, 40, 39, 7, 53, 23, 16, 37, 66, 38, 6, 47, 3, 61,
                44, 42, 78, 31, 21, 55, 15, 35, 25, 32, 69, 65, 70, 64, 51, 46, 5,
                77, 26, 73, 76, 75, 72, 74, 10, 57, 4, 14, 68, 22, 18, 52, 54, 60,
                79, 12, 49, 63, 8, 59, 1, 13, 20, 17, 48, 34]
        time = pd.date_range(start='2018-01-01', freq='1D', periods=80)
        df = pd.DataFrame({"time": time, "id": cid, "kind": ckind, "sort": csort, "val": cval})
        df = df.set_index("time", drop=False)
        df.index.name = None
        return df

    def create_test_data_nearly_numerical_indices(self):
        cid = "99999_9999_" + pd.Series(np.repeat([10, 500], 40)).astype(str)
        ckind = np.repeat(["a", "b", "a", "b"], 20)
        csort = [30, 53, 26, 35, 42, 25, 17, 67, 20, 68, 46, 12, 0, 74, 66, 31, 32,
                 2, 55, 59, 56, 60, 34, 69, 47, 15, 49, 8, 50, 73, 23, 62, 24, 33,
                 22, 70, 3, 38, 28, 75, 39, 36, 64, 13, 72, 52, 40, 16, 58, 29, 63,
                 79, 61, 78, 1, 10, 4, 6, 65, 44, 54, 48, 11, 14, 19, 43, 76, 7,
                 51, 9, 27, 21, 5, 71, 57, 77, 41, 18, 45, 37]
        cval = [11, 9, 67, 45, 30, 58, 62, 19, 56, 29, 0, 27, 36, 43, 33, 2, 24,
                71, 41, 28, 50, 40, 39, 7, 53, 23, 16, 37, 66, 38, 6, 47, 3, 61,
                44, 42, 78, 31, 21, 55, 15, 35, 25, 32, 69, 65, 70, 64, 51, 46, 5,
                77, 26, 73, 76, 75, 72, 74, 10, 57, 4, 14, 68, 22, 18, 52, 54, 60,
                79, 12, 49, 63, 8, 59, 1, 13, 20, 17, 48, 34]
        df = pd.DataFrame({"id": cid, "kind": ckind, "sort": csort, "val": cval})
        df = df.set_index("id", drop=False)
        df.index.name = None
        return df

    def create_one_valued_time_series(self):
        cid = [1, 2, 2]
        ckind = ["a", "a", "a"]
        csort = [1, 1, 2]
        cval = [1.0, 5.0, 6.0]
        df = pd.DataFrame({"id": cid, "kind": ckind, "sort": csort, "val": cval})
        return df

    def create_test_data_sample_with_target(self):
        """
        Small test data set with target.
        :return: timeseries df
        :return: target y which is the mean of each sample's timeseries
        """
        cid = np.repeat(range(50), 3)
        csort = list(range(3)) * 50
        cval = [1, 2, 3] * 30 + [4, 5, 6] * 20
        df = pd.DataFrame({'id': cid, 'kind': 'a', 'sort': csort, 'val': cval})
        y = pd.Series([2] * 30 + [5] * 20)
        return df, y
