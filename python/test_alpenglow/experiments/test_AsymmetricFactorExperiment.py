import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import alpenglow.evaluation
import pandas as pd
import math


class TestAsymmetricFactorExperiment:
    def test_AsymmetricFactorExperiment(self):
        experiment = alpenglow.experiments.AsymmetricFactorExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            learning_rate=0.1,
            negative_rate=10
        )
        rankings = experiment.run("python/test_alpenglow/test_data_4", experimentType="online_id", verbose=True, exclude_known=True)
        assert rankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 4.0, 101.0, 101.0, 3.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 15.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 34.0, 1.0, 13.0, 101.0, 101.0, 18.0, 101.0, 35.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 40.0, 101.0, 8.0, 30.0, 12.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 44.0, 101.0, 10.0, 101.0, 44.0, 101.0, 101.0, 101.0, 19.0, 101.0, 101.0, 42.0, 101.0, 20.0, 32.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 37.0, 101.0, 9.0, 63.0, 101.0, 17.0, 40.0, 7.0, 46.0, 101.0, 101.0, 47.0, 101.0, 101.0, 101.0, 7.0, 36.0, 18.0, 13.0, 101.0, 17.0, 40.0, 101.0, 101.0, 45.0, 15.0, 101.0, 101.0, 101.0, 37.0, 47.0, 7.0, 101.0, 48.0, 54.0, 42.0, 20.0, 8.0, 51.0, 8.0, 101.0, 8.0, 101.0, 101.0, 39.0, 69.0, 21.0, 101.0, 40.0, 47.0, 46.0, 28.0, 32.0, 27.0, 101.0, 23.0, 101.0, 101.0, 9.0, 101.0, 40.0, 60.0, 101.0, 8.0, 31.0, 34.0, 12.0, 13.0, 101.0, 8.0, 101.0, 101.0, 62.0, 101.0, 101.0, 101.0, 101.0, 56.0, 101.0, 3.0, 26.0, 101.0, 101.0, 101.0, 101.0, 7.0, 50.0, 15.0, 101.0, 101.0, 48.0, 101.0, 44.0, 101.0, 32.0, 4.0, 10.0, 8.0, 101.0, 101.0, 33.0, 64.0, 101.0, 23.0, 72.0, 41.0, 11.0, 41.0, 3.0, 101.0, 101.0, 101.0, 101.0, 25.0, 101.0, 25.0, 101.0, 7.0, 101.0, 3.0, 12.0, 101.0, 101.0, 41.0, 38.0, 31.0, 79.0, 101.0, 101.0, 78.0, 28.0, 78.0, 34.0, 101.0, 42.0, 101.0, 4.0, 37.0, 9.0, 4.0, 77.0, 38.0, 56.0, 101.0, 101.0, 101.0, 101.0, 101.0, 67.0, 39.0, 101.0, 67.0, 100.0, 2.0, 50.0, 60.0, 101.0, 62.0, 1.0, 70.0, 31.0, 101.0, 101.0, 67.0, 101.0, 53.0, 49.0, 71.0, 101.0, 2.0, 42.0, 63.0, 85.0, 10.0, 14.0, 101.0, 80.0, 8.0, 101.0, 101.0, 101.0, 101.0, 80.0, 53.0, 13.0, 101.0, 101.0, 66.0, 101.0, 54.0, 85.0, 101.0, 38.0, 91.0, 40.0, 20.0, 6.0, 65.0, 101.0, 101.0, 101.0, 25.0, 101.0, 24.0, 9.0, 101.0, 58.0, 56.0, 101.0, 101.0, 101.0, 101.0, 27.0, 9.0, 101.0, 25.0, 9.0, 2.0, 39.0, 51.0, 101.0, 101.0, 101.0, 101.0, 50.0, 101.0, 21.0, 101.0, 73.0, 101.0, 13.0, 101.0, 55.0, 4.0, 40.0, 101.0, 93.0, 20.0, 42.0, 63.0, 11.0, 101.0, 95.0, 16.0, 101.0, 55.0, 101.0, 52.0, 3.0, 24.0, 15.0, 9.0, 101.0, 3.0, 73.0, 101.0, 25.0, 101.0, 10.0, 49.0, 10.0, 67.0, 75.0, 17.0, 39.0, 101.0, 6.0, 69.0, 101.0, 101.0, 37.0, 1.0, 1.0, 72.0, 101.0, 101.0, 101.0, 5.0, 101.0, 101.0, 1.0, 101.0, 101.0, 4.0, 31.0, 101.0, 35.0, 101.0, 78.0, 74.0, 35.0, 21.0, 37.0, 7.0, 101.0, 90.0, 101.0, 61.0, 96.0, 69.0, 101.0, 101.0, 101.0, 45.0, 33.0, 101.0, 101.0, 101.0, 17.0, 101.0, 101.0, 87.0, 101.0, 101.0, 101.0, 28.0, 50.0, 101.0, 53.0, 101.0, 101.0, 101.0, 101.0, 101.0, 3.0, 40.0, 101.0, 44.0, 94.0, 101.0, 101.0, 61.0, 22.0, 101.0, 79.0, 101.0, 8.0, 101.0, 87.0, 101.0, 63.0, 101.0, 101.0, 10.0, 101.0, 4.0, 4.0, 26.0, 101.0, 7.0, 1.0, 26.0, 48.0, 1.0, 35.0, 4.0, 69.0, 30.0, 19.0, 101.0, 101.0, 49.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 29.0, 72.0, 101.0, 94.0, 52.0, 101.0, 2.0, 14.0, 1.0, 33.0, 101.0, 12.0, 101.0, 42.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 14.0, 101.0, 101.0, 16.0, 37.0, 82.0, 70.0, 101.0, 82.0, 20.0, 101.0, 36.0, 101.0, 101.0, 3.0, 101.0, 101.0, 88.0, 69.0, 77.0, 101.0, 8.0, 14.0, 101.0, 17.0, 101.0, 15.0, 60.0, 7.0, 101.0, 72.0, 3.0, 101.0, 74.0, 38.0, 81.0, 101.0, 101.0, 78.0, 12.0, 1.0, 36.0, 101.0, 101.0, 101.0, 6.0, 101.0, 61.0, 19.0, 101.0, 1.0, 101.0, 101.0, 46.0, 49.0, 101.0, 73.0, 100.0, 89.0, 101.0, 101.0, 101.0, 14.0, 17.0, 17.0, 6.0, 101.0, 1.0, 101.0, 21.0, 7.0, 99.0, 60.0, 101.0, 101.0, 18.0, 67.0, 67.0, 47.0, 5.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 9.0, 5.0, 37.0, 4.0, 101.0, 11.0, 101.0, 16.0, 95.0, 101.0, 101.0, 101.0, 101.0, 49.0, 101.0, 6.0, 69.0, 54.0, 101.0, 101.0, 101.0, 20.0, 101.0, 44.0, 101.0, 17.0, 37.0, 101.0, 101.0, 46.0, 8.0, 3.0, 101.0, 6.0, 101.0, 28.0, 98.0, 101.0, 21.0, 27.0, 5.0, 101.0, 58.0, 101.0, 85.0, 101.0, 101.0, 101.0, 59.0, 6.0, 101.0, 101.0, 87.0, 94.0, 101.0, 3.0, 11.0, 44.0, 64.0, 90.0, 101.0, 57.0, 64.0, 51.0, 2.0, 101.0, 101.0, 70.0, 101.0, 101.0, 48.0, 101.0, 32.0, 42.0, 101.0, 101.0, 101.0, 101.0, 49.0, 34.0, 95.0, 101.0, 12.0, 101.0, 101.0, 6.0, 101.0, 24.0, 27.0, 79.0, 30.0, 92.0, 14.0, 26.0, 35.0, 4.0, 51.0, 101.0, 101.0, 72.0, 3.0, 69.0, 2.0, 96.0, 2.0, 101.0, 101.0, 7.0, 7.0, 101.0, 101.0, 20.0, 101.0, 56.0, 101.0, 24.0, 1.0, 101.0, 41.0, 101.0, 101.0, 93.0, 5.0, 39.0, 101.0, 101.0, 20.0, 82.0, 35.0, 101.0, 101.0, 1.0, 10.0, 101.0, 5.0, 101.0, 16.0, 101.0, 10.0, 44.0, 19.0, 17.0, 6.0, 6.0, 101.0, 101.0, 30.0, 76.0, 14.0, 101.0, 101.0, 5.0, 3.0, 6.0, 101.0, 37.0, 20.0, 9.0, 18.0, 101.0, 101.0, 4.0, 75.0, 83.0, 85.0, 93.0, 36.0, 7.0, 101.0, 3.0, 1.0, 101.0, 101.0, 61.0, 48.0, 71.0, 8.0, 8.0, 101.0, 2.0, 4.0, 101.0, 18.0, 3.0, 80.0, 4.0, 101.0, 101.0, 68.0, 22.0, 12.0, 3.0, 101.0, 101.0, 83.0, 101.0, 101.0, 3.0, 71.0, 2.0, 101.0, 5.0, 7.0, 101.0, 4.0, 43.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 65.0, 101.0, 33.0, 6.0, 69.0, 101.0, 24.0, 6.0, 8.0, 82.0, 4.0, 101.0, 101.0, 57.0, 36.0, 3.0, 4.0, 9.0, 25.0, 13.0, 1.0, 57.0, 13.0, 6.0, 24.0, 1.0, 3.0, 101.0, 49.0, 2.0, 74.0, 36.0, 4.0, 14.0, 2.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 61.0, 61.0, 101.0, 6.0, 15.0, 40.0, 101.0, 101.0, 1.0, 101.0, 101.0, 101.0, 15.0, 65.0, 101.0, 101.0, 7.0, 61.0, 14.0, 51.0, 101.0, 32.0, 49.0, 80.0, 101.0, 14.0, 5.0, 101.0, 12.0, 3.0, 80.0, 101.0, 101.0, 101.0, 101.0, 101.0, 39.0, 74.0, 82.0, 84.0, 27.0, 101.0, 3.0, 12.0, 21.0, 101.0, 47.0, 16.0, 3.0, 28.0, 79.0, 10.0, 14.0, 12.0, 101.0, 9.0, 2.0, 95.0, 89.0, 2.0, 101.0, 4.0, 101.0, 95.0, 19.0, 6.0, 101.0, 22.0, 46.0, 11.0, 14.0, 101.0, 101.0, 101.0, 57.0, 14.0, 54.0, 101.0, 38.0, 101.0, 38.0, 101.0, 101.0, 50.0, 40.0, 10.0, 101.0, 3.0, 101.0, 101.0, 20.0, 101.0, 101.0, 25.0, 14.0, 101.0, 101.0, 78.0, 3.0, 101.0, 6.0, 101.0, 22.0, 14.0, 1.0, 49.0, 80.0, 101.0, 101.0, 58.0, 101.0, 101.0, 98.0, 101.0, 13.0, 101.0, 16.0, 20.0, 4.0, 30.0, 6.0, 44.0, 3.0, 101.0, 101.0, 1.0, 101.0, 21.0, 27.0, 101.0, 40.0, 58.0, 101.0, 19.0, 3.0, 41.0, 2.0, 29.0, 101.0, 99.0, 1.0, 101.0, 101.0, 19.0, 69.0, 53.0, 1.0, 64.0, 3.0, 57.0, 36.0, 18.0, 101.0, 3.0, 7.0, 19.0, 101.0, 19.0, 2.0, 101.0, 1.0, 4.0, 78.0, 75.0, 7.0, 12.0, 63.0, 35.0, 52.0, 101.0, 101.0]
        #print(list(rankings["rank"].fillna(101)))
        assert list(rankings["rank"].fillna(101)) == desired_ranks
