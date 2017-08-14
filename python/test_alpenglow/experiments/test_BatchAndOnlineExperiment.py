import alpenglow as prs
import alpenglow.Getter as rs
import alpenglow.experiments
import pandas as pd
import math


class TestBatchAndOnlineExperiment:
    def test_batchAndOnlineExperiment(self):
        boModelExperiment = alpenglow.experiments.BatchAndOnlineExperiment(
            top_k=100,
            seed=254938879,
            dimension=10,
            period_length=1000,
            batch_learning_rate=0.07,
            batch_negative_rate=20,
            online_learning_rate=0.15,
            online_negative_rate=120,
            number_of_iterations=3,
            clear_model=True,
        )
        boRankings = boModelExperiment.run("python/test_alpenglow/test_data_4", experimentType="online_id", verbose=True)
        print(list(boRankings['rank'].fillna(101)))
        assert boRankings.top_k == 100
        desired_ranks = [101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 8.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 22.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 2.0, 101.0, 101.0, 101.0, 23.0, 14.0, 33.0, 101.0, 101.0, 35.0, 101.0, 41.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 15.0, 101.0, 4.0, 24.0, 5.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 29.0, 101.0, 4.0, 101.0, 37.0, 101.0, 101.0, 101.0, 6.0, 101.0, 101.0, 56.0, 101.0, 47.0, 51.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 57.0, 101.0, 10.0, 7.0, 101.0, 25.0, 32.0, 9.0, 36.0, 101.0, 101.0, 16.0, 101.0, 101.0, 101.0, 30.0, 2.0, 11.0, 50.0, 101.0, 19.0, 1.0, 101.0, 101.0, 18.0, 14.0, 101.0, 101.0, 101.0, 28.0, 52.0, 63.0, 101.0, 40.0, 34.0, 56.0, 48.0, 4.0, 69.0, 7.0, 101.0, 33.0, 101.0, 101.0, 67.0, 70.0, 64.0, 101.0, 74.0, 26.0, 20.0, 8.0, 56.0, 73.0, 101.0, 74.0, 101.0, 101.0, 56.0, 101.0, 44.0, 36.0, 101.0, 4.0, 21.0, 26.0, 4.0, 12.0, 101.0, 15.0, 101.0, 101.0, 49.0, 101.0, 101.0, 101.0, 101.0, 77.0, 101.0, 2.0, 16.0, 101.0, 101.0, 101.0, 101.0, 1.0, 16.0, 75.0, 101.0, 101.0, 62.0, 101.0, 23.0, 101.0, 56.0, 67.0, 31.0, 27.0, 101.0, 101.0, 53.0, 80.0, 101.0, 8.0, 33.0, 68.0, 15.0, 97.0, 5.0, 101.0, 101.0, 101.0, 101.0, 22.0, 101.0, 11.0, 101.0, 3.0, 101.0, 62.0, 8.0, 101.0, 101.0, 3.0, 17.0, 44.0, 82.0, 101.0, 101.0, 26.0, 63.0, 23.0, 1.0, 101.0, 6.0, 101.0, 23.0, 33.0, 68.0, 20.0, 24.0, 101.0, 30.0, 101.0, 101.0, 101.0, 101.0, 101.0, 28.0, 14.0, 101.0, 65.0, 8.0, 4.0, 5.0, 95.0, 101.0, 49.0, 38.0, 47.0, 10.0, 101.0, 101.0, 42.0, 101.0, 16.0, 9.0, 6.0, 101.0, 1.0, 19.0, 36.0, 5.0, 14.0, 9.0, 101.0, 32.0, 90.0, 101.0, 101.0, 101.0, 101.0, 27.0, 58.0, 1.0, 101.0, 101.0, 72.0, 101.0, 92.0, 68.0, 101.0, 87.0, 47.0, 47.0, 3.0, 12.0, 37.0, 101.0, 101.0, 101.0, 65.0, 101.0, 70.0, 1.0, 101.0, 77.0, 16.0, 101.0, 101.0, 101.0, 101.0, 1.0, 101.0, 101.0, 38.0, 10.0, 50.0, 40.0, 24.0, 101.0, 101.0, 101.0, 101.0, 30.0, 101.0, 8.0, 101.0, 93.0, 101.0, 11.0, 101.0, 101.0, 5.0, 95.0, 101.0, 96.0, 57.0, 24.0, 101.0, 18.0, 101.0, 92.0, 3.0, 101.0, 28.0, 101.0, 101.0, 8.0, 101.0, 13.0, 18.0, 101.0, 13.0, 21.0, 101.0, 4.0, 101.0, 10.0, 58.0, 79.0, 34.0, 54.0, 96.0, 9.0, 101.0, 1.0, 101.0, 101.0, 101.0, 23.0, 5.0, 57.0, 101.0, 101.0, 101.0, 101.0, 39.0, 37.0, 101.0, 2.0, 16.0, 101.0, 4.0, 36.0, 101.0, 7.0, 101.0, 41.0, 99.0, 101.0, 101.0, 7.0, 17.0, 101.0, 84.0, 59.0, 46.0, 55.0, 101.0, 101.0, 101.0, 101.0, 12.0, 27.0, 101.0, 101.0, 101.0, 100.0, 101.0, 101.0, 101.0, 19.0, 101.0, 101.0, 47.0, 1.0, 101.0, 25.0, 101.0, 101.0, 101.0, 101.0, 101.0, 32.0, 42.0, 16.0, 29.0, 4.0, 101.0, 80.0, 84.0, 35.0, 101.0, 101.0, 101.0, 6.0, 101.0, 45.0, 88.0, 9.0, 101.0, 101.0, 1.0, 101.0, 4.0, 32.0, 58.0, 67.0, 4.0, 55.0, 82.0, 18.0, 101.0, 1.0, 101.0, 31.0, 21.0, 69.0, 101.0, 80.0, 83.0, 64.0, 101.0, 58.0, 101.0, 101.0, 66.0, 3.0, 31.0, 15.0, 20.0, 98.0, 80.0, 49.0, 6.0, 101.0, 3.0, 5.0, 101.0, 1.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 93.0, 101.0, 101.0, 101.0, 101.0, 101.0, 101.0, 44.0, 93.0, 101.0, 61.0, 101.0, 56.0, 7.0, 46.0, 33.0, 101.0, 101.0, 43.0, 101.0, 101.0, 5.0, 46.0, 45.0, 41.0, 16.0, 29.0, 101.0, 78.0, 101.0, 2.0, 89.0, 35.0, 91.0, 101.0, 1.0, 101.0, 101.0, 4.0, 38.0, 70.0, 101.0, 29.0, 16.0, 101.0, 54.0, 91.0, 101.0, 101.0, 1.0, 101.0, 74.0, 39.0, 101.0, 9.0, 101.0, 101.0, 7.0, 19.0, 101.0, 29.0, 16.0, 67.0, 101.0, 101.0, 101.0, 59.0, 101.0, 1.0, 12.0, 101.0, 101.0, 15.0, 64.0, 101.0, 14.0, 22.0, 101.0, 17.0, 101.0, 101.0, 21.0, 101.0, 101.0, 101.0, 101.0, 101.0, 1.0, 101.0, 90.0, 101.0, 4.0, 1.0, 16.0, 22.0, 101.0, 101.0, 101.0, 47.0, 56.0, 101.0, 101.0, 5.0, 21.0, 101.0, 101.0, 17.0, 5.0, 67.0, 101.0, 101.0, 54.0, 18.0, 101.0, 9.0, 101.0, 16.0, 8.0, 19.0, 41.0, 62.0, 8.0, 27.0, 101.0, 4.0, 101.0, 45.0, 50.0, 62.0, 7.0, 15.0, 14.0, 101.0, 101.0, 101.0, 9.0, 101.0, 101.0, 101.0, 101.0, 11.0, 10.0, 101.0, 44.0, 101.0, 18.0, 2.0, 85.0, 101.0, 17.0, 101.0, 16.0, 101.0, 29.0, 21.0, 101.0, 101.0, 101.0, 20.0, 101.0, 101.0, 32.0, 101.0, 12.0, 23.0, 101.0, 101.0, 101.0, 31.0, 51.0, 42.0, 101.0, 101.0, 22.0, 75.0, 101.0, 2.0, 101.0, 48.0, 20.0, 8.0, 88.0, 5.0, 1.0, 30.0, 24.0, 2.0, 2.0, 101.0, 101.0, 26.0, 4.0, 101.0, 56.0, 28.0, 36.0, 101.0, 34.0, 4.0, 17.0, 101.0, 19.0, 24.0, 101.0, 16.0, 101.0, 101.0, 10.0, 80.0, 101.0, 101.0, 39.0, 47.0, 101.0, 9.0, 101.0, 101.0, 28.0, 101.0, 2.0, 101.0, 101.0, 23.0, 31.0, 101.0, 5.0, 101.0, 16.0, 101.0, 42.0, 5.0, 55.0, 3.0, 101.0, 38.0, 101.0, 101.0, 101.0, 11.0, 101.0, 101.0, 101.0, 25.0, 2.0, 7.0, 101.0, 7.0, 30.0, 15.0, 8.0, 42.0, 101.0, 5.0, 33.0, 38.0, 101.0, 101.0, 27.0, 88.0, 101.0, 82.0, 13.0, 101.0, 101.0, 62.0, 65.0, 51.0, 6.0, 7.0, 101.0, 28.0, 1.0, 101.0, 15.0, 10.0, 5.0, 1.0, 101.0, 101.0, 29.0, 12.0, 9.0, 1.0, 101.0, 84.0, 17.0, 101.0, 101.0, 6.0, 92.0, 11.0, 13.0, 45.0, 14.0, 101.0, 13.0, 13.0, 7.0, 32.0, 101.0, 40.0, 92.0, 101.0, 46.0, 101.0, 16.0, 4.0, 101.0, 93.0, 18.0, 1.0, 44.0, 9.0, 9.0, 101.0, 101.0, 38.0, 19.0, 48.0, 1.0, 15.0, 13.0, 11.0, 6.0, 101.0, 11.0, 5.0, 101.0, 1.0, 56.0, 24.0, 101.0, 1.0, 37.0, 101.0, 5.0, 20.0, 1.0, 101.0, 101.0, 96.0, 101.0, 101.0, 6.0, 16.0, 4.0, 101.0, 13.0, 8.0, 27.0, 11.0, 101.0, 1.0, 95.0, 27.0, 101.0, 50.0, 101.0, 101.0, 101.0, 3.0, 8.0, 21.0, 20.0, 101.0, 77.0, 30.0, 25.0, 21.0, 7.0, 5.0, 92.0, 19.0, 25.0, 35.0, 101.0, 101.0, 26.0, 101.0, 101.0, 20.0, 14.0, 92.0, 14.0, 26.0, 101.0, 2.0, 34.0, 57.0, 101.0, 22.0, 21.0, 7.0, 34.0, 39.0, 12.0, 12.0, 7.0, 52.0, 6.0, 4.0, 48.0, 25.0, 2.0, 13.0, 3.0, 101.0, 23.0, 10.0, 9.0, 101.0, 21.0, 19.0, 8.0, 22.0, 101.0, 58.0, 101.0, 21.0, 21.0, 22.0, 101.0, 96.0, 101.0, 101.0, 22.0, 22.0, 17.0, 19.0, 57.0, 101.0, 17.0, 101.0, 61.0, 77.0, 101.0, 101.0, 20.0, 25.0, 3.0, 101.0, 61.0, 5.0, 101.0, 94.0, 101.0, 11.0, 5.0, 34.0, 37.0, 95.0, 101.0, 26.0, 94.0, 101.0, 101.0, 19.0, 101.0, 4.0, 101.0, 10.0, 21.0, 5.0, 10.0, 4.0, 42.0, 1.0, 57.0, 101.0, 4.0, 96.0, 13.0, 15.0, 101.0, 8.0, 90.0, 101.0, 18.0, 4.0, 47.0, 1.0, 70.0, 101.0, 14.0, 8.0, 17.0, 72.0, 56.0, 101.0, 10.0, 1.0, 101.0, 4.0, 8.0, 24.0, 20.0, 101.0, 5.0, 2.0, 32.0, 96.0, 13.0, 1.0, 101.0, 1.0, 14.0, 55.0, 101.0, 3.0, 28.0, 31.0, 101.0, 101.0, 101.0, 101.0]
        assert list(boRankings["rank"].fillna(101)) == desired_ranks
