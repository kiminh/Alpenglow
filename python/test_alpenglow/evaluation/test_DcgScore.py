import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.evaluation
import pandas as pd
import math
import unittest


class TestDcgScore(unittest.TestCase):
    def test_dcgScore(self):
        ranks = [102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 65, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 100, 102, 102, 18, 102, 102, 100, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 100, 100, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 100, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 67, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 100, 102, 102, 102, 102, 100, 102, 100, 102, 102, 102, 102, 58, 100, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 102, 102, 102, 102, 102, 100, 100, 102, 102, 100, 102, 102, 102, 100, 100, 100, 102, 102, 100, 102, 102, 102, 102, 100, 102, 102, 102, 47, 102, 102, 102, 100, 100, 102, 102, 102, 100, 102, 100, 102, 102, 102, 102, 102, 100, 100, 102, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 100, 102, 54, 100, 102, 100, 100, 102, 102, 100, 100, 102, 100, 102, 102, 102, 102, 102, 102, 102, 102, 102, 102, 100, 100, 102, 100, 102, 102, 102, 102, 100, 102, 102, 102, 100, 102, 100, 100, 47, 102, 100, 102, 102, 102, 100, 102, 102, 100, 100, 102, 102, 100, 100, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 100, 102, 102, 102, 102, 102, 100, 102, 102, 100, 100, 100, 100, 100, 102, 100, 102, 102, 100, 102, 102, 100, 100, 37, 100, 102, 102, 102, 102, 102, 100, 102, 100, 102, 102, 102, 55, 102, 102, 100, 102, 102, 102, 102, 102, 102, 100, 100, 102, 102, 102, 102, 100, 102, 102, 102, 102, 102, 22, 102, 100, 100, 100, 102, 102, 102, 102, 102, 100, 102, 100, 102, 100, 102, 102, 102, 102, 102, 100, 102, 102, 102, 100, 102, 102, 100, 102, 100, 100, 102, 100, 102, 102, 100, 100, 100, 102, 102, 100, 100, 100, 102, 102, 100, 102, 102, 102, 102, 102, 102, 102, 100, 102, 102, 100, 100, 102, 102, 102, 102, 100, 102, 102, 102, 102, 100, 102, 102, 102, 21, 100, 102, 100, 102, 100, 102, 102, 102, 100, 100, 102, 102, 100, 102, 102, 102, 100, 102, 102, 100, 102, 102, 102, 102, 100, 102, 102, 102, 100, 100, 102, 102, 102, 100, 102, 102, 102, 100, 102, 102, 100, 102, 102, 102, 100, 102, 100, 102, 100, 100, 102, 100, 102, 100, 100, 100, 102, 102, 102, 102, 102, 100, 102, 100, 102, 102, 100, 102, 102, 102, 100, 102, 100, 102, 102, 102, 100, 102, 102, 102, 102, 102, 100, 102, 100, 100, 100, 102, 100, 102, 100, 102, 102, 100, 100, 100, 100, 100, 100, 102, 88, 102, 102, 102, 100, 102, 100, 100, 102, 100, 102, 102, 100, 102, 102, 102, 102, 102, 102, 100, 102, 102, 102, 100, 100, 100, 100, 102, 100, 100, 102, 102, 100, 102, 100, 102, 102, 102, 100, 102, 102, 100, 102, 14, 102, 100, 102, 102, 102, 102, 100, 102, 100, 100, 100, 102, 100, 102, 100, 102, 102, 102, 102, 102, 100, 100, 100, 100, 102, 102, 102, 102, 102, 102, 100, 102, 100, 100, 102, 100, 100, 102, 102, 100, 100, 100, 102, 100, 102, 102, 102, 102, 102, 102, 102, 100, 100, 102, 102, 100, 102, 102, 100, 100, 102, 102, 100, 102, 100, 102, 102, 100]
        facRankings = pd.DataFrame.from_records(
            [
                (i, i, 0, r + 1 if r < 100 else None)
                for i, r in enumerate(ranks)
            ],
            columns=["id", "time", "prediction", "rank"]
        ).set_index("id")
        facRankings.top_k = 100
        dcg = alpenglow.evaluation.DcgScore(facRankings).mean()
        dcgs = [math.log(2) / math.log(r + 2) if r < 100 else 0 for r in ranks]
        self.assertAlmostEqual(dcg, sum(dcgs) / len(dcgs))
