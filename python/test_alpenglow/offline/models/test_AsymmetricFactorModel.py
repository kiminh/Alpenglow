import alpenglow as prs
from alpenglow.offline.models import AsymmetricFactorModel
from alpenglow.offline.evaluation import NdcgScore
import alpenglow.Getter as rs
import pandas as pd
import numpy as np
import unittest
import pytest
import sys
import alpenglow.cpp
compiler = alpenglow.cpp.__compiler
stdlib = alpenglow.cpp.__stdlib


class TestAsymmetricFactorModel(unittest.TestCase):
    def test_rmse(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        model = AsymmetricFactorModel(
            negative_rate=9,
            number_of_iterations=20,
        )
        model.fit(data)

        def predict(model, user, item):
            rd = rs.RecDat()
            rd.user = user
            rd.item = item
            return model.prediction(rd)

        errors = [(1 - predict(model.model, u, i))**2 for (u, i) in data[['user', 'item']].values]
        rmse = np.sqrt(pd.Series(errors)).mean()
        assert rmse == pytest.approx(0.2693938783455279, abs=5*1e-2)

    def test_ranking(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        exp = AsymmetricFactorModel(
            negative_rate=9,
            number_of_iterations=20,
        )
        exp.fit(data)
        preds = exp.recommend(exclude_known=False, k=20)
        if(compiler == "gcc" and stdlib == "libstdc++"):
            #print(preds['item'].tolist() )
            assert preds['item'].tolist() ==  \
                 [98, 94, 427, 255, 338, 414, 429, 282, 38, 371, 247, 97, 250, 455, 166, 468, 496, 40, 325, 298, 256, 372, 166, 338, 94, 455, 337, 30, 225, 383, 177, 168, 462, 282, 102, 120, 375, 479, 128, 277, 98, 300, 429, 427, 94, 455, 255, 371, 462, 496, 38, 338, 250, 372, 166, 483, 295, 497, 247, 256, 442, 30, 372, 225, 166, 215, 337, 196, 462, 299, 444, 496, 300, 292, 94, 211, 263, 293, 434, 120, 196, 300, 442, 30, 204, 266, 165, 250, 86, 450, 455, 108, 38, 337, 225, 299, 293, 62, 4, 292, 165, 300, 128, 86, 383, 204, 94, 442, 196, 462, 247, 102, 166, 497, 337, 62, 225, 395, 429, 452, 300, 196, 462, 204, 165, 30, 86, 442, 455, 383, 102, 128, 94, 452, 337, 166, 250, 497, 429, 400, 299, 30, 225, 215, 166, 36, 442, 337, 196, 462, 40, 496, 444, 434, 81, 372, 263, 452, 62, 94, 299, 225, 94, 30, 62, 166, 204, 40, 98, 250, 196, 337, 247, 452, 496, 36, 81, 215, 300, 128, 256, 338, 372, 462, 383, 166, 94, 282, 168, 479, 120, 69, 102, 30, 36, 455, 337, 54, 211, 5, 30, 462, 455, 300, 299, 372, 215, 442, 196, 166, 337, 225, 36, 94, 177, 491, 102, 211, 256, 496, 300, 442, 30, 462, 196, 166, 299, 225, 215, 372, 337, 94, 165, 455, 86, 383, 250, 429, 496, 204, 30, 225, 299, 442, 196, 166, 337, 62, 215, 94, 40, 250, 372, 263, 36, 300, 434, 496, 444, 292, 168, 444, 4, 338, 97, 442, 156, 277, 86, 255, 165, 120, 372, 196, 263, 293, 375, 40, 483, 6, 300, 462, 455, 196, 429, 204, 497, 86, 165, 400, 452, 371, 442, 30, 105, 250, 496, 215, 81, 383, 30, 299, 225, 215, 442, 462, 166, 196, 337, 455, 372, 36, 300, 94, 263, 81, 452, 444, 204, 434, 94, 256, 98, 247, 128, 204, 383, 282, 166, 102, 300, 455, 462, 497, 86, 165, 375, 177, 452, 468, 204, 300, 98, 94, 196, 250, 427, 455, 247, 38, 165, 266, 450, 86, 108, 128, 497, 166, 429, 299, 299, 30, 94, 204, 300, 225, 98, 166, 196, 250, 455, 247, 62, 337, 452, 40, 496, 497, 462, 429, 94, 98, 30, 166, 299, 225, 455, 250, 337, 300, 372, 196, 36, 338, 255, 427, 38, 256, 496, 40, 94, 250, 98, 427, 196, 300, 204, 62, 255, 225, 429, 166, 38, 165, 450, 266, 496, 299, 40, 108, 299, 225, 30, 94, 300, 166, 196, 204, 442, 250, 62, 165, 215, 40, 496, 337, 462, 86, 81, 429, 30, 225, 299, 300, 204, 166, 94, 442, 165, 462, 196, 383, 215, 62, 452, 337, 81, 128, 86, 263, 98, 338, 94, 120, 255, 166, 97, 414, 40, 427, 256, 282, 429, 325, 225, 496, 36, 372, 444, 168, 225, 166, 94, 62, 128, 383, 30, 165, 204, 337, 299, 442, 247, 40, 86, 256, 102, 263, 452, 462, 94, 462, 166, 30, 256, 372, 455, 225, 338, 98, 337, 300, 442, 383, 102, 36, 299, 247, 429, 177, 300, 462, 383, 165, 452, 204, 86, 128, 102, 497, 30, 247, 455, 256, 372, 94, 81, 400, 442, 166, 30, 442, 166, 372, 225, 337, 455, 94, 299, 462, 196, 215, 338, 300, 444, 36, 177, 4, 256, 120, 299, 30, 225, 215, 166, 36, 442, 337, 196, 462, 40, 496, 444, 434, 81, 372, 263, 452, 62, 94, 300, 462, 455, 196, 429, 204, 497, 86, 165, 400, 452, 371, 442, 30, 105, 250, 496, 215, 81, 383, 300, 442, 462, 496, 30, 215, 196, 299, 429, 166, 250, 372, 94, 225, 292, 491, 337, 400, 25, 255, 204, 94, 98, 247, 128, 256, 282, 165, 86, 102, 166, 427, 375, 497, 455, 383, 468, 300, 225, 177, 62, 225, 40, 299, 94, 166, 30, 97, 250, 337, 204, 496, 442, 128, 434, 98, 36, 120, 498, 196, 98, 94, 166, 225, 427, 250, 255, 299, 429, 40, 496, 30, 38, 300, 414, 62, 247, 338, 97, 292, 196, 300, 455, 204, 30, 250, 266, 38, 86, 165, 177, 450, 299, 225, 337, 94, 102, 462, 166, 108, 30, 166, 442, 225, 372, 94, 299, 462, 337, 338, 215, 36, 120, 256, 444, 496, 455, 211, 196, 300, 166, 30, 372, 94, 455, 338, 462, 225, 442, 256, 299, 337, 98, 36, 215, 120, 300, 444, 211, 177, 427, 204, 98, 94, 38, 455, 300, 266, 86, 128, 247, 375, 450, 165, 250, 196, 108, 468, 371, 177, 300, 299, 30, 442, 94, 166, 496, 98, 429, 250, 196, 225, 455, 372, 255, 215, 462, 427, 38, 292, 300, 98, 427, 94, 455, 429, 255, 371, 250, 497, 38, 247, 496, 204, 462, 468, 105, 166, 483, 299, 30, 442, 166, 462, 372, 225, 299, 94, 300, 215, 337, 455, 338, 196, 36, 496, 256, 444, 383, 211, 62, 225, 299, 40, 166, 94, 30, 337, 204, 128, 165, 196, 442, 250, 97, 498, 434, 263, 36, 120, 30, 299, 225, 215, 442, 462, 166, 196, 337, 455, 372, 36, 300, 94, 263, 81, 452, 444, 204, 434, 299, 442, 30, 225, 166, 94, 215, 496, 372, 337, 444, 300, 255, 250, 40, 196, 338, 292, 36, 120, 299, 225, 166, 338, 30, 120, 40, 94, 215, 442, 36, 372, 444, 496, 337, 62, 97, 98, 255, 414, 166, 94, 225, 30, 299, 442, 372, 338, 337, 98, 256, 462, 36, 120, 215, 40, 62, 455, 383, 444, 455, 196, 300, 30, 442, 94, 38, 177, 166, 86, 337, 462, 204, 102, 266, 165, 427, 372, 225, 375, 94, 30, 299, 300, 166, 225, 98, 462, 455, 204, 247, 250, 429, 372, 215, 196, 337, 256, 496, 36, 462, 30, 372, 300, 455, 383, 256, 215, 442, 166, 102, 337, 338, 94, 36, 452, 211, 225, 400, 299, 30, 462, 442, 299, 300, 215, 225, 166, 372, 337, 196, 455, 94, 36, 383, 496, 263, 400, 211, 81, 94, 166, 442, 98, 225, 429, 372, 427, 300, 30, 337, 250, 338, 256, 462, 38, 196, 496, 293, 128, 338, 299, 120, 30, 36, 225, 215, 166, 372, 444, 40, 98, 496, 94, 97, 442, 337, 255, 434, 414, 30, 225, 166, 299, 94, 337, 442, 372, 215, 462, 36, 62, 40, 196, 98, 256, 338, 250, 300, 455, 256, 94, 383, 455, 102, 462, 166, 128, 282, 247, 372, 177, 204, 98, 30, 375, 337, 225, 338, 86, 30, 300, 462, 225, 383, 166, 94, 204, 442, 165, 196, 299, 86, 452, 337, 215, 128, 102, 81, 372, 166, 338, 94, 225, 299, 30, 372, 98, 120, 442, 36, 215, 496, 40, 444, 337, 256, 462, 255, 97, 196, 300, 442, 30, 204, 266, 165, 250, 86, 450, 455, 108, 38, 337, 225, 299, 293, 62, 4, 292, 30, 299, 225, 215, 442, 462, 166, 196, 337, 455, 372, 36, 300, 94, 263, 81, 452, 444, 204, 434, 299, 225, 94, 166, 40, 98, 30, 496, 62, 250, 255, 215, 36, 97, 442, 292, 414, 337, 120, 338, 98, 94, 427, 255, 338, 414, 429, 282, 38, 371, 247, 97, 250, 455, 166, 468, 496, 40, 325, 298, 299, 94, 98, 225, 166, 30, 40, 496, 255, 250, 62, 338, 36, 215, 337, 442, 300, 429, 120, 97, 98, 94, 166, 338, 225, 427, 255, 299, 256, 429, 40, 247, 414, 250, 496, 30, 455, 282, 372, 120, 166, 94, 225, 30, 299, 442, 372, 338, 337, 98, 256, 462, 36, 120, 215, 40, 62, 455, 383, 444, 30, 300, 196, 299, 455, 204, 225, 166, 462, 94, 337, 442, 250, 215, 102, 165, 452, 86, 247, 372, 299, 442, 30, 166, 225, 94, 196, 250, 98, 496, 255, 337, 292, 372, 444, 293, 25, 120, 38, 300]

        assert NdcgScore(data, preds, top_k=20) == pytest.approx(0.9211200538533627, abs=1e-2)

        preds2 = exp.recommend(users = [1, 2], exclude_known=False)
        assert preds2['user'].unique().tolist() == [1,2]

        preds = exp.recommend(exclude_known=True)
        joined_preds = preds.join(
            data.set_index(['user', 'item']),
            on=['user','item'], how='inner', rsuffix="_right"
        )
        assert len(joined_preds) == 0
