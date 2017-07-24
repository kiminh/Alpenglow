import alpenglow as prs
import alpenglow.Getter as rs
import pandas as pd
import numpy as np
import unittest


class TestOfflineModel(unittest.TestCase):
    def test_rmse(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        model = prs.OfflineModel()
        model.fit(data)

        def predict(model, user, item):
            rd = rs.RecDat()
            rd.user = user
            rd.item = item
            return model.prediction(rd)

        errors = [(1 - predict(model.model, u, i))**2 for (u, i) in data[['user', 'item']].values]
        rmse = np.sqrt(pd.Series(errors)).mean()
        self.assertAlmostEqual(0.31307693145764515, rmse)

    def test_ranking(self):
        data = pd.read_csv(
            "python/test_alpenglow/test_data_4",
            sep=' ',
            header=None,
            names=['time', 'user', 'item', 'id', 'score', 'eval']
        )
        exp = prs.OfflineModel()
        exp.fit(data)
        preds = exp.recommend()

        assert preds['item'].tolist() == [94, 30, 166, 225, 300, 299, 442, 196, 455, 337, 372, 462, 250, 256, 427, 204, 38, 247, 429, 62, 36, 338, 496, 215, 177, 293, 255, 128, 40, 156, 165, 86, 375, 102, 483, 371, 444, 211, 383, 450, 266, 292, 108, 25, 120, 468, 251, 97, 497, 282, 414, 4, 168, 69, 491, 298, 197, 277, 452, 181, 479, 81, 325, 16, 421, 263, 330, 54, 161, 434, 295, 271, 99, 464, 351, 400, 395, 5, 458, 348, 245, 22, 216, 118, 105, 236, 221, 377, 440, 191, 425, 17, 436, 205, 127, 278, 265, 77, 80, 284, 197, 300, 16, 427, 86, 116, 165, 440, 29, 6, 491, 234, 204, 215, 403, 318, 356, 436, 139, 181, 99, 452, 296, 425, 58, 295, 468, 95, 108, 266, 281, 483, 271, 78, 351, 299, 112, 429, 419, 250, 12, 434, 478, 284, 192, 93, 127, 362, 254, 488, 205, 105, 330, 178, 142, 15, 445, 206, 302, 409, 497, 260, 390, 273, 481, 111, 450, 152, 72, 63, 294, 146, 19, 45, 232, 237, 65, 48, 276, 426, 7, 252, 380, 185, 268, 136, 228, 406, 144, 446, 381, 122, 459, 270, 35, 27, 349, 441, 49, 87, 166, 225, 30, 38, 196, 299, 177, 293, 442, 250, 247, 256, 483, 292, 337, 36, 25, 156, 444, 211, 450, 215, 108, 266, 414, 491, 204, 330, 375, 181, 351, 282, 251, 348, 62, 102, 86, 128, 271, 4, 165, 97, 40, 69, 96, 298, 146, 174, 16, 277, 99, 197, 120, 421, 168, 325, 454, 245, 425, 284, 161, 221, 236, 216, 383, 205, 54, 127, 22, 464, 233, 400, 81, 80, 118, 112, 78, 278, 191, 403, 479, 5, 436, 478, 318, 377, 356, 17, 234, 458, 6, 419, 265, 58, 95, 77, 289, 122, 139, 296, 30, 225, 166, 94, 299, 300, 372, 337, 98, 462, 196, 215, 36, 496, 250, 40, 338, 62, 455, 256, 429, 444, 204, 120, 255, 38, 247, 293, 211, 383, 292, 434, 165, 427, 128, 156, 25, 483, 263, 97, 177, 491, 81, 251, 86, 102, 181, 452, 414, 497, 400, 168, 375, 99, 4, 271, 395, 295, 450, 371, 277, 325, 108, 479, 266, 188, 351, 197, 421, 298, 464, 246, 195, 69, 162, 440, 494, 498, 53, 206, 330, 418, 410, 447, 425, 23, 281, 205, 127, 54, 192, 161, 5, 93, 348, 314, 12, 78, 105, 112, 94, 225, 30, 166, 300, 442, 299, 98, 337, 250, 62, 372, 496, 40, 215, 462, 204, 293, 255, 429, 427, 38, 36, 455, 247, 165, 128, 338, 25, 444, 156, 292, 86, 256, 266, 450, 177, 108, 371, 375, 251, 483, 97, 497, 211, 120, 383, 434, 491, 102, 468, 263, 81, 181, 400, 395, 99, 4, 452, 414, 271, 421, 325, 464, 277, 22, 245, 216, 298, 295, 351, 168, 118, 127, 191, 425, 197, 195, 479, 221, 236, 16, 330, 54, 206, 69, 278, 188, 282, 80, 161, 436, 478, 146, 440, 5, 162, 246, 377, 78, 204, 225, 166, 30, 196, 337, 247, 98, 62, 375, 250, 462, 102, 299, 497, 256, 40, 372, 429, 468, 156, 427, 266, 108, 450, 496, 395, 38, 455, 452, 251, 371, 177, 483, 282, 263, 255, 168, 215, 298, 245, 118, 16, 197, 325, 338, 216, 81, 22, 97, 69, 464, 54, 188, 191, 236, 161, 479, 278, 36, 80, 221, 25, 458, 211, 400, 5, 195, 277, 246, 162, 53, 292, 498, 410, 418, 414, 23, 494, 447, 116, 29, 284, 377, 434, 17, 77, 4, 440, 403, 289, 265, 120, 318, 488, 58, 6, 296, 397, 234, 94, 225, 30, 166, 442, 299, 98, 337, 204, 372, 250, 62, 247, 128, 40, 496, 455, 256, 215, 86, 429, 36, 383, 427, 38, 102, 338, 293, 375, 255, 156, 497, 177, 251, 483, 452, 371, 211, 266, 450, 108, 292, 263, 395, 25, 468, 444, 81, 120, 97, 400, 434, 168, 414, 282, 69, 298, 197, 421, 188, 277, 325, 479, 4, 54, 464, 16, 491, 161, 195, 246, 245, 162, 118, 5, 22, 498, 53, 216, 418, 181, 410, 236, 494, 458, 271, 221, 23, 447, 191, 278, 99, 80, 295, 436, 330, 377, 440, 116, 17, 225, 166, 94, 442, 300, 98, 337, 372, 215, 196, 462, 250, 36, 40, 496, 62, 338, 455, 429, 204, 256, 255, 444, 120, 38, 427, 247, 292, 165, 293, 483, 383, 434, 211, 97, 128, 414, 25, 156, 251, 452, 86, 81, 497, 177, 263, 491, 181, 102, 400, 298, 371, 450, 395, 325, 99, 271, 375, 266, 168, 295, 108, 4, 421, 188, 464, 330, 351, 197, 498, 246, 205, 162, 348, 479, 494, 53, 440, 195, 410, 418, 277, 281, 447, 23, 206, 425, 69, 192, 314, 127, 93, 468, 12, 105, 78, 245, 22, 112, 353, 166, 442, 300, 215, 337, 196, 250, 462, 372, 496, 36, 429, 165, 247, 455, 256, 338, 383, 128, 452, 86, 255, 497, 251, 434, 483, 292, 395, 427, 414, 38, 263, 444, 102, 120, 188, 293, 400, 97, 298, 25, 211, 246, 410, 162, 53, 494, 418, 371, 447, 23, 156, 181, 195, 450, 325, 491, 421, 375, 266, 108, 271, 464, 348, 99, 278, 295, 236, 330, 351, 221, 468, 168, 197, 205, 80, 245, 22, 118, 105, 216, 206, 281, 191, 101, 440, 488, 69, 479, 78, 93, 314, 192, 112, 96, 174, 12, 454, 353, 127, 166, 30, 94, 225, 462, 455, 337, 442, 98, 102, 177, 300, 36, 299, 247, 168, 211, 69, 282, 196, 204, 128, 215, 375, 479, 197, 86, 120, 429, 161, 156, 38, 5, 165, 54, 452, 277, 458, 444, 427, 483, 4, 263, 250, 16, 62, 17, 77, 81, 377, 265, 289, 496, 330, 497, 397, 440, 40, 132, 29, 414, 116, 293, 113, 205, 251, 371, 295, 357, 400, 6, 403, 454, 348, 234, 468, 233, 281, 318, 436, 356, 12, 271, 488, 58, 192, 188, 93, 95, 491, 434, 296, 314, 255, 298, 139, 146, 195, 362, 353, 166, 225, 94, 442, 98, 462, 337, 256, 36, 196, 215, 338, 250, 204, 429, 496, 247, 40, 427, 62, 38, 177, 383, 211, 102, 444, 255, 120, 483, 128, 156, 165, 293, 414, 86, 292, 375, 168, 452, 371, 69, 282, 251, 298, 97, 81, 181, 197, 497, 25, 4, 479, 263, 491, 434, 277, 450, 348, 330, 295, 266, 400, 351, 271, 108, 161, 54, 5, 395, 105, 188, 99, 325, 205, 468, 458, 440, 421, 16, 498, 162, 246, 96, 418, 494, 53, 78, 357, 174, 410, 454, 112, 464, 281, 23, 17, 447, 377, 139, 265, 30, 225, 94, 299, 337, 372, 215, 98, 62, 40, 250, 496, 204, 36, 165, 247, 128, 383, 429, 338, 86, 256, 263, 455, 434, 293, 444, 255, 497, 452, 81, 292, 102, 251, 120, 38, 211, 188, 25, 427, 156, 483, 375, 246, 498, 177, 162, 181, 53, 410, 97, 494, 418, 23, 447, 414, 195, 491, 168, 108, 266, 99, 271, 450, 371, 298, 277, 421, 479, 325, 4, 197, 351, 464, 468, 69, 278, 236, 54, 221, 206, 161, 295, 5, 80, 22, 78, 118, 458, 105, 245, 112, 216, 348, 191, 488, 440, 127, 425, 281, 166, 94, 300, 40, 98, 250, 496, 215, 372, 36, 462, 204, 338, 255, 429, 292, 444, 120, 293, 434, 165, 38, 97, 25, 455, 427, 128, 247, 156, 395, 256, 414, 497, 181, 483, 251, 86, 263, 450, 383, 211, 491, 81, 452, 266, 298, 108, 400, 99, 325, 188, 464, 246, 421, 498, 162, 375, 494, 271, 53, 351, 410, 447, 418, 371, 23, 4, 278, 221, 236, 102, 195, 78, 112, 80, 295, 177, 127, 22, 206, 168, 425, 245, 216, 419, 118, 281, 191, 440, 468, 192, 277, 93, 314, 105, 348, 12, 205, 353, 478, 414, 53, 348, 181, 447, 246, 292, 494, 78, 410, 174, 139, 351, 96, 278, 101, 236, 162, 23, 498, 369, 188, 357, 105, 395, 221, 80, 419, 418, 298, 112, 94, 30, 225, 166, 299, 98, 442, 196, 337, 250, 204, 372, 62, 462, 455, 496, 247, 40, 165, 429, 427, 215, 128, 256, 38, 36, 86, 293, 255, 338, 156, 177, 102, 375, 383, 483, 450, 371, 266, 497, 108, 292, 25, 251, 444, 211, 468, 97, 452, 120, 414, 81, 395, 298, 263, 434, 421, 491, 400, 325, 282, 168, 4, 197, 464, 277, 69, 181, 245, 22, 99, 216, 118, 16, 271, 479, 191, 236, 221, 295, 188, 54, 278, 330, 161, 80, 351, 195, 5, 436, 127, 162, 458, 246, 498, 440, 425, 348, 53, 205, 225, 166, 94, 299, 442, 300, 372, 98, 337, 462, 196, 215, 36, 455, 250, 338, 496, 256, 40, 62, 204, 429, 247, 444, 255, 38, 427, 383, 120, 211, 165, 128, 293, 483, 177, 102, 156, 292, 86, 434, 414, 452, 251, 97, 81, 25, 497, 263, 375, 168, 491, 371, 400, 181, 4, 450, 298, 69, 197, 271, 479, 295, 395, 325, 266, 99, 277, 108, 330, 282, 421, 188, 351, 464, 205, 440, 348, 54, 161, 468, 246, 498, 5, 195, 162, 281, 494, 53, 418, 410, 458, 447, 314, 192, 206, 23, 425, 105, 93, 12, 94, 165, 86, 102, 455, 225, 30, 462, 375, 196, 337, 177, 372, 427, 468, 69, 429, 156, 497, 371, 452, 38, 16, 197, 62, 266, 442, 168, 161, 450, 483, 54, 108, 250, 5, 458, 479, 251, 298, 299, 395, 293, 277, 211, 29, 81, 188, 116, 236, 284, 377, 263, 421, 221, 80, 17, 338, 77, 118, 245, 278, 289, 265, 436, 216, 191, 36, 357, 414, 22, 418, 498, 53, 4, 410, 403, 397, 162, 6, 23, 246, 318, 494, 325, 234, 447, 330, 356, 348, 454, 113, 464, 58, 139, 195, 101, 132, 233, 296, 488, 94, 225, 30, 166, 300, 299, 442, 337, 250, 62, 372, 455, 165, 247, 462, 427, 128, 429, 40, 496, 86, 38, 256, 293, 215, 255, 36, 156, 375, 102, 450, 371, 266, 177, 338, 108, 483, 383, 497, 468, 251, 25, 292, 97, 452, 211, 298, 395, 444, 414, 81, 282, 421, 120, 325, 263, 464, 197, 400, 245, 22, 434, 216, 16, 69, 118, 168, 4, 491, 236, 221, 277, 191, 278, 80, 188, 181, 479, 54, 99, 161, 271, 330, 295, 436, 5, 351, 195, 284, 498, 162, 458, 246, 348, 127, 53, 410, 418, 447, 494, 166, 442, 196, 337, 215, 40, 372, 496, 429, 462, 427, 256, 247, 165, 255, 38, 86, 483, 338, 128, 414, 292, 293, 371, 251, 497, 156, 97, 383, 266, 102, 25, 108, 177, 395, 81, 444, 120, 375, 468, 211, 434, 325, 421, 181, 188, 400, 464, 348, 278, 221, 236, 498, 330, 491, 263, 80, 245, 351, 162, 246, 22, 197, 53, 118, 410, 216, 494, 418, 295, 447, 99, 282, 271, 205, 105, 191, 23, 112, 78, 195, 454, 16, 69, 96, 168, 4, 101, 440, 419, 281, 174, 233, 127, 314, 369, 192, 425, 488, 436, 300, 442, 372, 250, 256, 196, 429, 462, 36, 38, 204, 338, 215, 496, 40, 255, 62, 156, 483, 414, 247, 292, 293, 177, 371, 450, 97, 120, 444, 165, 266, 128, 375, 211, 86, 25, 108, 102, 181, 251, 468, 325, 348, 383, 351, 497, 168, 282, 491, 4, 330, 421, 236, 221, 295, 464, 197, 105, 278, 80, 395, 452, 69, 112, 78, 99, 271, 205, 96, 434, 419, 245, 479, 440, 174, 81, 277, 139, 216, 369, 22, 118, 16, 454, 101, 191, 281, 314, 127, 425, 233, 357, 192, 436, 403, 400, 498, 162, 188, 12, 284, 16, 436, 455, 102, 127, 215, 99, 177, 112, 78, 434, 452, 318, 403, 58, 195, 188, 419, 425, 162, 254, 491, 296, 478, 400, 498, 447, 246, 122, 351, 95, 362, 356, 53, 410, 440, 314, 81, 494, 15, 4, 234, 418, 197, 6, 499, 181, 369, 105, 23, 1, 256, 129, 228, 270, 481, 290, 407, 361, 52, 273, 282, 336, 35, 90, 281, 485, 227, 305, 493, 232, 139, 7, 230, 50, 268, 404, 48, 171, 473, 231, 460, 79, 19, 408, 131, 206, 72, 459, 150, 186, 136, 183, 474, 381, 164, 210, 43, 426, 225, 166, 299, 300, 442, 196, 98, 250, 337, 496, 40, 215, 62, 372, 204, 462, 429, 36, 247, 427, 128, 86, 293, 38, 455, 251, 338, 483, 292, 497, 256, 25, 383, 444, 371, 414, 434, 97, 452, 395, 400, 211, 156, 102, 263, 450, 108, 266, 120, 375, 177, 491, 325, 468, 298, 421, 181, 188, 271, 464, 195, 295, 99, 245, 498, 22, 330, 246, 216, 118, 162, 494, 410, 53, 191, 418, 447, 278, 23, 236, 221, 351, 348, 80, 168, 197, 206, 205, 105, 440, 146, 4, 314, 436, 127, 281, 488, 425, 479, 69, 429, 98, 256, 483, 488, 421, 211, 206, 278, 116, 118, 101, 191, 414, 22, 245, 271, 29, 325, 298, 197, 254, 464, 338, 216, 93, 236, 80, 292, 221, 69, 479, 375, 353, 5, 25, 281, 205, 12, 54, 255, 161, 192, 436, 468, 314, 168, 19, 231, 458, 1, 114, 120, 79, 461, 227, 302, 493, 83, 378, 35, 323, 294, 104, 27, 276, 388, 125, 232, 347, 485, 228, 361, 49, 390, 0, 404, 481, 144, 268, 57, 63, 222, 290, 131, 136, 408, 405, 406, 155, 142, 441, 460, 444, 270, 237, 283, 152, 7, 134, 30, 225, 299, 442, 455, 337, 372, 38, 300, 36, 156, 250, 429, 483, 496, 444, 462, 215, 293, 196, 292, 371, 177, 450, 375, 25, 168, 266, 298, 62, 108, 295, 4, 464, 491, 421, 440, 204, 468, 205, 247, 479, 197, 271, 99, 181, 281, 69, 192, 245, 12, 93, 277, 216, 251, 348, 351, 436, 454, 403, 118, 22, 425, 318, 353, 191, 233, 127, 86, 128, 6, 165, 356, 234, 58, 95, 105, 362, 102, 146, 296, 478, 434, 236, 54, 221, 497, 17, 161, 16, 80, 278, 206, 132, 458, 377, 397, 5, 499, 29, 30, 94, 166, 300, 204, 337, 442, 462, 196, 247, 86, 98, 256, 102, 250, 40, 215, 452, 429, 455, 497, 36, 496, 375, 263, 81, 395, 251, 338, 177, 188, 483, 156, 282, 168, 427, 69, 211, 38, 468, 400, 197, 498, 479, 410, 246, 53, 418, 293, 195, 162, 494, 23, 266, 434, 371, 54, 161, 447, 298, 450, 108, 5, 16, 458, 421, 255, 414, 120, 277, 325, 97, 464, 116, 118, 29, 245, 236, 278, 191, 22, 216, 436, 377, 221, 77, 444, 80, 440, 17, 488, 292, 25, 265, 289, 4, 397, 205, 403, 281, 98, 300, 211, 338, 204, 337, 452, 81, 38, 197, 168, 295, 105, 479, 196, 161, 250, 444, 400, 16, 5, 146, 128, 96, 271, 54, 174, 458, 165, 496, 375, 29, 255, 116, 298, 351, 497, 440, 491, 277, 263, 289, 6, 17, 265, 403, 181, 488, 314, 77, 377, 362, 356, 188, 318, 101, 234, 120, 95, 397, 58, 139, 113, 15, 281, 122, 4, 12, 357, 93, 132, 369, 192, 436, 296, 284, 498, 353, 418, 468, 494, 53, 156, 308, 134, 410, 380, 200, 23, 157, 65, 273, 70, 162, 445, 441, 144, 406, 39, 246, 94, 166, 30, 225, 462, 442, 98, 372, 337, 299, 196, 204, 256, 455, 247, 165, 128, 102, 250, 86, 36, 62, 215, 429, 338, 177, 427, 496, 40, 375, 38, 452, 497, 211, 156, 483, 282, 293, 251, 69, 168, 371, 255, 81, 263, 197, 468, 444, 479, 266, 120, 450, 161, 108, 54, 400, 277, 5, 16, 395, 414, 458, 25, 4, 298, 188, 97, 434, 292, 421, 330, 325, 195, 377, 17, 116, 29, 77, 464, 265, 295, 440, 498, 246, 289, 162, 418, 271, 53, 436, 491, 205, 410, 494, 245, 118, 23, 397, 447, 348, 225, 94, 98, 300, 462, 196, 338, 36, 215, 256, 250, 496, 40, 62, 444, 38, 120, 429, 427, 177, 255, 211, 204, 247, 156, 292, 383, 102, 375, 168, 483, 25, 181, 165, 97, 434, 491, 414, 263, 277, 86, 479, 450, 69, 99, 251, 351, 266, 371, 452, 197, 108, 497, 81, 271, 298, 295, 282, 400, 54, 161, 5, 395, 325, 348, 78, 458, 112, 105, 440, 330, 425, 357, 188, 421, 17, 419, 464, 377, 246, 127, 77, 162, 265, 468, 205, 132, 96, 494, 281, 498, 397, 53, 418, 289, 206, 447, 410, 174, 23, 225, 166, 94, 442, 300, 98, 372, 337, 215, 462, 36, 196, 250, 40, 496, 338, 455, 256, 62, 429, 204, 255, 444, 120, 38, 247, 427, 383, 483, 211, 292, 165, 293, 414, 434, 97, 128, 156, 177, 452, 251, 25, 86, 102, 81, 497, 263, 491, 181, 298, 168, 400, 371, 375, 325, 450, 295, 271, 99, 4, 395, 330, 266, 197, 188, 421, 479, 108, 351, 205, 464, 69, 348, 440, 277, 498, 246, 281, 162, 494, 53, 418, 410, 192, 195, 314, 447, 23, 93, 206, 425, 282, 12, 105, 127, 78, 454, 353, 112, 468, 94, 30, 225, 166, 299, 98, 442, 196, 337, 372, 250, 204, 462, 455, 62, 247, 496, 429, 215, 40, 165, 427, 256, 36, 128, 38, 86, 255, 338, 293, 156, 177, 383, 102, 483, 375, 371, 497, 450, 292, 251, 266, 25, 444, 211, 108, 468, 97, 452, 120, 414, 81, 395, 263, 298, 434, 282, 400, 168, 491, 421, 325, 197, 69, 4, 464, 277, 181, 271, 479, 16, 245, 99, 22, 330, 295, 118, 216, 54, 188, 161, 191, 236, 221, 351, 278, 5, 80, 195, 348, 458, 436, 440, 162, 246, 205, 498, 105, 127, 53, 30, 225, 166, 299, 94, 196, 98, 337, 250, 215, 40, 372, 62, 36, 462, 255, 429, 338, 204, 293, 292, 444, 38, 427, 455, 25, 165, 434, 247, 120, 97, 128, 251, 256, 483, 491, 156, 211, 181, 497, 86, 414, 81, 263, 383, 400, 395, 450, 108, 266, 371, 99, 452, 271, 177, 325, 351, 298, 421, 375, 464, 295, 188, 102, 4, 246, 162, 195, 498, 494, 53, 127, 447, 410, 206, 425, 418, 22, 468, 23, 245, 216, 278, 221, 277, 118, 330, 78, 168, 236, 105, 112, 191, 348, 80, 281, 440, 205, 192, 419, 166, 225, 30, 300, 98, 256, 247, 455, 337, 165, 196, 462, 128, 86, 372, 299, 442, 102, 427, 383, 375, 429, 177, 250, 62, 38, 156, 371, 483, 468, 497, 36, 452, 266, 69, 338, 450, 40, 251, 108, 293, 215, 168, 496, 197, 211, 16, 255, 298, 161, 479, 54, 81, 414, 5, 395, 458, 421, 263, 277, 325, 245, 97, 118, 464, 330, 216, 29, 4, 22, 191, 400, 116, 436, 25, 236, 188, 377, 284, 17, 221, 77, 278, 80, 440, 289, 265, 403, 454, 120, 318, 6, 195, 205, 292, 356, 233, 348, 234, 397, 299, 30, 166, 94, 442, 300, 196, 250, 496, 337, 98, 215, 204, 372, 36, 429, 462, 255, 165, 338, 292, 293, 434, 25, 427, 444, 38, 97, 247, 128, 251, 497, 120, 86, 483, 395, 81, 455, 450, 156, 452, 414, 263, 400, 266, 108, 383, 256, 491, 325, 181, 371, 211, 298, 464, 421, 99, 188, 271, 195, 375, 498, 22, 246, 162, 245, 216, 410, 494, 53, 118, 447, 468, 102, 418, 295, 278, 191, 23, 221, 206, 236, 351, 127, 80, 425, 177, 4, 281, 314, 440, 192, 93, 205, 330, 78, 112, 12, 353, 488, 30, 300, 299, 442, 196, 337, 372, 455, 462, 38, 429, 496, 255, 256, 36, 62, 215, 293, 338, 204, 247, 40, 177, 292, 156, 444, 371, 128, 483, 165, 25, 211, 450, 375, 414, 86, 266, 108, 102, 120, 97, 181, 251, 491, 298, 383, 468, 351, 4, 497, 168, 282, 348, 271, 295, 105, 395, 99, 325, 277, 330, 434, 197, 69, 421, 81, 236, 221, 464, 278, 400, 80, 96, 78, 479, 112, 452, 16, 263, 174, 245, 419, 22, 216, 54, 161, 425, 127, 118, 440, 191, 139, 205, 5, 146, 357, 436, 162, 188, 458, 94, 166, 225, 300, 98, 299, 337, 442, 427, 247, 250, 256, 372, 462, 165, 128, 38, 62, 429, 86, 177, 156, 375, 293, 102, 40, 496, 255, 371, 450, 36, 338, 483, 215, 108, 468, 383, 497, 282, 251, 298, 292, 25, 211, 97, 414, 452, 69, 197, 16, 444, 168, 421, 395, 4, 325, 120, 277, 464, 245, 81, 236, 479, 54, 161, 216, 118, 22, 221, 278, 80, 191, 5, 263, 330, 458, 491, 284, 400, 348, 436, 295, 181, 351, 99, 377, 105, 29, 271, 17, 403, 188, 440, 434, 205, 454, 116, 318, 265, 77, 166, 299, 462, 98, 300, 36, 256, 215, 455, 196, 496, 250, 40, 444, 120, 383, 211, 62, 177, 247, 38, 102, 204, 168, 427, 255, 414, 483, 292, 156, 128, 293, 434, 263, 181, 165, 452, 375, 479, 69, 81, 4, 491, 86, 97, 197, 277, 251, 400, 25, 295, 282, 271, 497, 351, 348, 188, 161, 5, 54, 330, 298, 99, 440, 246, 395, 162, 494, 458, 418, 53, 105, 498, 410, 23, 371, 357, 205, 447, 325, 96, 281, 174, 139, 78, 17, 77, 112, 265, 377, 192, 93, 289, 132, 314, 12, 101, 397, 206, 419, 215, 444, 196, 177, 496, 168, 250, 40, 383, 429, 427, 414, 483, 102, 62, 4, 255, 479, 375, 97, 69, 247, 292, 204, 197, 293, 277, 181, 282, 491, 434, 295, 440, 128, 161, 5, 54, 458, 452, 263, 205, 330, 351, 99, 348, 25, 325, 271, 281, 357, 192, 17, 12, 78, 314, 93, 139, 112, 77, 265, 377, 105, 132, 289, 86, 397, 419, 450, 165, 425, 371, 81, 454, 403, 353, 113, 6, 369, 464, 96, 101, 233, 497, 251, 234, 174, 266, 356, 16, 318, 29, 127, 400, 206, 436, 116, 108, 95, 58, 478, 337, 255, 483, 166, 225, 298, 497, 236, 221, 245, 80, 216, 22, 118, 25, 278, 30, 69, 191, 197, 421, 251, 54, 161, 464, 277, 292, 395, 4, 458, 325, 5, 383, 436, 97, 377, 403, 29, 168, 318, 414, 479, 234, 372, 356, 116, 58, 6, 17, 105, 296, 77, 95, 265, 289, 462, 139, 357, 362, 348, 112, 330, 397, 211, 419, 351, 78, 127, 454, 96, 113, 254, 442, 478, 233, 132, 146, 174, 122, 290, 268, 252, 228, 1, 369, 144, 183, 15, 390, 90, 445, 388, 499, 230, 484, 425, 72, 273, 237, 70, 338, 40, 337, 99, 62, 256, 434, 4, 425, 120, 205, 454, 127, 206, 233, 97, 108, 78, 112, 478, 450, 362, 156, 419, 263, 277, 266, 102, 383, 69, 282, 122, 314, 284, 468, 497, 15, 369, 132, 403, 488, 268, 356, 101, 139, 308, 204, 237, 35, 65, 445, 144, 484, 48, 361, 157, 353, 318, 437, 265, 323, 347, 404, 200, 302, 95, 0, 70, 231, 446, 294, 113, 407, 16, 7, 473, 129, 43, 45, 485, 136, 298, 134, 409, 499, 59, 39, 344, 104, 145, 331, 276, 406, 290, 283, 252, 125, 130, 1, 405, 94, 30, 225, 166, 299, 196, 442, 337, 204, 250, 372, 455, 462, 62, 427, 247, 429, 165, 496, 256, 38, 40, 128, 215, 36, 293, 255, 86, 338, 156, 177, 375, 102, 371, 450, 483, 266, 383, 108, 292, 25, 497, 251, 444, 468, 211, 97, 414, 120, 452, 298, 395, 282, 81, 263, 491, 421, 4, 168, 325, 434, 197, 69, 400, 181, 277, 464, 16, 245, 22, 216, 236, 99, 118, 479, 221, 271, 278, 54, 351, 191, 80, 295, 330, 161, 188, 5, 348, 105, 458, 436, 127, 162, 246, 440, 195, 498, 284, 425, 377, 166, 225, 299, 372, 98, 462, 196, 256, 36, 215, 455, 250, 40, 62, 496, 204, 247, 429, 383, 128, 120, 165, 38, 444, 156, 211, 102, 293, 427, 177, 255, 375, 86, 292, 168, 483, 414, 263, 97, 434, 497, 452, 395, 25, 4, 479, 251, 181, 277, 81, 298, 69, 197, 450, 266, 108, 188, 491, 400, 282, 54, 371, 325, 161, 246, 162, 5, 494, 53, 418, 498, 99, 421, 410, 458, 23, 351, 447, 271, 468, 440, 464, 295, 357, 236, 78, 221, 112, 348, 278, 17, 80, 377, 195, 77, 105, 139, 281, 419, 265, 30, 94, 166, 299, 300, 442, 98, 196, 337, 250, 372, 40, 496, 215, 462, 204, 36, 429, 165, 455, 255, 247, 427, 338, 38, 128, 293, 256, 86, 292, 444, 483, 156, 25, 383, 251, 497, 97, 120, 450, 434, 371, 102, 211, 177, 266, 108, 375, 81, 452, 414, 395, 263, 400, 491, 298, 468, 325, 181, 421, 464, 99, 271, 188, 4, 168, 295, 22, 245, 195, 216, 118, 197, 498, 351, 246, 277, 162, 191, 330, 236, 53, 494, 278, 410, 221, 418, 447, 479, 23, 69, 127, 80, 425, 206, 440, 282, 205, 348, 16, 225, 166, 94, 299, 442, 300, 372, 98, 337, 462, 196, 215, 36, 455, 250, 256, 338, 496, 40, 62, 204, 429, 247, 383, 444, 38, 120, 255, 427, 165, 211, 128, 177, 293, 483, 102, 156, 86, 292, 452, 434, 414, 97, 375, 251, 263, 81, 497, 168, 25, 491, 400, 181, 371, 4, 298, 69, 479, 450, 197, 395, 266, 277, 271, 325, 295, 99, 108, 282, 188, 330, 421, 440, 464, 351, 205, 161, 54, 246, 498, 5, 348, 162, 494, 53, 468, 418, 195, 410, 281, 447, 23, 458, 192, 206, 425, 314, 93, 12, 105, 36, 38, 97, 351, 400, 455, 427, 4, 295, 81, 414, 425, 251, 127, 156, 78, 112, 483, 105, 395, 419, 478, 277, 177, 246, 96, 162, 174, 146, 195, 108, 325, 447, 494, 348, 464, 188, 498, 53, 281, 410, 450, 330, 23, 192, 418, 93, 266, 353, 314, 497, 440, 12, 383, 421, 205, 132, 371, 247, 168, 452, 256, 397, 488, 22, 113, 265, 357, 362, 481, 122, 19, 63, 17, 77, 323, 268, 232, 136, 237, 408, 221, 302, 499, 446, 409, 48, 87, 0, 473, 347, 361, 7, 479, 276, 142, 426, 65, 405, 260, 372, 337, 462, 250, 98, 300, 255, 196, 211, 491, 181, 429, 99, 25, 263, 271, 295, 400, 455, 483, 81, 325, 293, 281, 206, 192, 4, 38, 440, 93, 12, 351, 425, 452, 156, 383, 464, 127, 251, 246, 195, 494, 479, 78, 162, 330, 421, 188, 498, 112, 53, 410, 478, 418, 447, 23, 298, 395, 419, 277, 497, 122, 488, 15, 348, 146, 132, 427, 454, 105, 233, 369, 174, 481, 499, 7, 408, 460, 96, 380, 473, 441, 301, 150, 52, 19, 273, 63, 171, 232, 361, 48, 349, 1, 406, 185, 260, 65, 134, 393, 30, 225, 94, 442, 299, 372, 462, 98, 300, 337, 455, 196, 256, 36, 215, 338, 250, 496, 40, 62, 204, 247, 429, 383, 444, 177, 211, 38, 102, 128, 120, 427, 165, 255, 293, 156, 483, 86, 168, 375, 452, 263, 292, 434, 81, 414, 69, 251, 497, 479, 4, 97, 25, 197, 282, 277, 491, 400, 181, 371, 161, 54, 5, 271, 295, 298, 450, 395, 458, 330, 99, 266, 188, 108, 325, 440, 351, 348, 205, 421, 17, 246, 77, 377, 162, 468, 498, 16, 265, 494, 53, 418, 195, 410, 281, 289, 464, 23, 132, 397, 98, 128, 247, 338, 282, 383, 69, 468, 429, 293, 299, 479, 371, 62, 161, 54, 277, 16, 458, 5, 36, 120, 497, 255, 298, 97, 377, 17, 444, 77, 414, 325, 421, 265, 289, 40, 29, 397, 464, 452, 284, 116, 357, 132, 496, 236, 251, 245, 113, 25, 118, 221, 216, 80, 292, 22, 191, 215, 263, 278, 330, 395, 454, 205, 281, 295, 233, 362, 192, 12, 348, 122, 15, 254, 314, 488, 93, 78, 112, 425, 419, 105, 369, 127, 101, 491, 273, 99, 499, 478, 441, 252, 178, 408, 72, 380, 445, 481, 268, 260, 442, 372, 196, 62, 383, 165, 338, 86, 427, 128, 81, 251, 255, 414, 177, 211, 371, 298, 444, 292, 400, 263, 188, 120, 434, 293, 395, 330, 348, 156, 498, 282, 25, 375, 97, 69, 197, 246, 53, 410, 162, 418, 494, 181, 23, 168, 447, 295, 205, 450, 271, 491, 325, 195, 421, 105, 468, 351, 266, 454, 479, 108, 233, 96, 464, 16, 174, 99, 440, 101, 488, 278, 281, 236, 146, 314, 221, 161, 192, 93, 29, 12, 5, 277, 245, 4, 54, 116, 118, 80, 206, 353, 369, 139, 436, 22, 191, 78, 216, 403, 166, 30, 225, 94, 372, 442, 299, 337, 98, 455, 300, 256, 36, 338, 215, 196, 383, 247, 177, 211, 250, 496, 429, 444, 102, 204, 40, 62, 120, 38, 128, 168, 427, 69, 483, 263, 165, 293, 452, 255, 156, 86, 375, 81, 479, 282, 277, 4, 197, 434, 251, 491, 400, 161, 5, 54, 414, 292, 497, 181, 458, 271, 330, 295, 25, 371, 97, 99, 17, 77, 377, 348, 265, 440, 205, 289, 188, 397, 132, 16, 351, 113, 195, 105, 116, 146, 29, 281, 246, 454, 162, 494, 418, 357, 53, 498, 206, 395, 410, 23, 225, 94, 372, 337, 36, 98, 338, 455, 496, 40, 250, 62, 383, 429, 204, 444, 120, 247, 211, 434, 452, 102, 255, 263, 38, 292, 81, 177, 165, 128, 483, 414, 181, 293, 427, 168, 251, 400, 86, 188, 497, 491, 156, 97, 25, 395, 246, 498, 162, 479, 271, 69, 494, 53, 418, 410, 4, 23, 197, 447, 298, 351, 99, 295, 348, 375, 277, 330, 195, 205, 105, 440, 5, 161, 282, 54, 371, 325, 281, 78, 96, 206, 174, 112, 101, 357, 192, 458, 93, 421, 12, 314, 419, 425, 139, 488, 17, 353, 265, 464, 30, 98, 300, 299, 455, 196, 462, 337, 256, 250, 247, 204, 38, 36, 177, 215, 338, 165, 62, 496, 102, 86, 255, 293, 40, 483, 156, 383, 375, 211, 292, 414, 444, 251, 282, 450, 266, 108, 25, 497, 468, 168, 69, 298, 120, 452, 81, 197, 97, 181, 348, 4, 330, 491, 395, 479, 277, 351, 16, 105, 400, 263, 295, 161, 54, 271, 5, 325, 421, 236, 221, 96, 458, 188, 278, 80, 174, 434, 464, 99, 162, 205, 245, 440, 246, 357, 498, 494, 139, 418, 53, 377, 436, 410, 17, 118, 146, 78, 447, 454, 30, 166, 225, 94, 442, 372, 98, 337, 300, 215, 36, 462, 496, 196, 40, 455, 250, 256, 444, 120, 62, 429, 255, 38, 211, 427, 293, 204, 434, 292, 97, 156, 483, 383, 177, 247, 491, 25, 414, 168, 181, 4, 263, 99, 452, 81, 271, 128, 102, 295, 251, 165, 400, 375, 325, 479, 277, 497, 450, 197, 330, 440, 86, 371, 205, 69, 298, 351, 281, 425, 464, 266, 421, 108, 192, 206, 127, 314, 93, 12, 353, 348, 54, 161, 5, 478, 195, 454, 17, 132, 395, 78, 265, 146, 233, 77, 458, 488, 112, 397, 299, 442, 372, 300, 98, 337, 462, 196, 215, 455, 256, 36, 338, 250, 496, 40, 204, 62, 429, 247, 383, 38, 427, 165, 128, 444, 211, 120, 102, 177, 255, 483, 86, 156, 414, 293, 292, 452, 375, 168, 251, 497, 81, 263, 434, 97, 25, 298, 371, 181, 69, 479, 197, 400, 395, 282, 4, 491, 188, 277, 450, 348, 295, 325, 330, 271, 266, 246, 498, 108, 351, 162, 494, 53, 418, 161, 410, 54, 99, 5, 421, 23, 447, 440, 205, 105, 468, 458, 464, 281, 195, 96, 357, 16, 78, 236, 174, 112, 17, 192, 196, 156, 211, 442, 377, 77, 17, 289, 263, 427, 38, 265, 4, 483, 357, 397, 429, 113, 132, 371, 36, 266, 6, 188, 436, 403, 234, 284, 440, 318, 81, 108, 62, 298, 356, 395, 251, 58, 450, 139, 418, 296, 53, 23, 95, 410, 454, 488, 494, 246, 162, 498, 233, 101, 421, 195, 447, 330, 254, 205, 236, 120, 362, 293, 118, 80, 15, 281, 348, 12, 191, 221, 369, 245, 273, 122, 178, 445, 294, 72, 142, 400, 186, 1, 144, 252, 48, 390, 409, 406, 380, 441, 134, 231, 35, 228, 260, 270, 152, 185, 299, 372, 247, 337, 102, 128, 36, 62, 497, 40, 250, 496, 251, 98, 400, 455, 395, 498, 410, 53, 418, 246, 23, 494, 162, 195, 447, 69, 338, 483, 282, 434, 168, 197, 177, 375, 479, 161, 5, 54, 414, 458, 116, 29, 16, 298, 330, 348, 205, 454, 421, 371, 468, 233, 77, 120, 440, 277, 289, 377, 17, 265, 93, 281, 436, 254, 12, 271, 357, 314, 192, 353, 325, 397, 206, 278, 6, 146, 174, 113, 118, 295, 444, 132, 105, 139, 403, 96, 318, 58, 236, 1, 231, 95, 356, 191, 369, 19, 114, 294, 300, 455, 62, 211, 196, 434, 255, 292, 383, 38, 4, 263, 491, 181, 99, 314, 25, 293, 277, 205, 197, 271, 452, 427, 177, 298, 353, 421, 204, 206, 69, 425, 81, 400, 102, 127, 5, 497, 132, 54, 330, 17, 458, 161, 397, 77, 78, 351, 128, 122, 403, 265, 436, 6, 15, 112, 251, 289, 246, 478, 318, 377, 488, 494, 113, 356, 95, 195, 165, 162, 234, 139, 419, 58, 454, 247, 296, 53, 233, 395, 188, 418, 357, 369, 498, 450, 410, 23, 447, 499, 481, 29, 254, 408, 380, 7, 273, 441, 301, 473, 94, 225, 30, 166, 300, 299, 442, 98, 337, 250, 62, 496, 372, 40, 204, 215, 462, 293, 255, 429, 36, 38, 427, 455, 165, 247, 128, 338, 25, 156, 444, 86, 292, 256, 450, 266, 108, 177, 97, 497, 251, 375, 371, 483, 120, 383, 434, 211, 491, 102, 263, 468, 81, 400, 395, 452, 99, 181, 4, 421, 325, 271, 464, 414, 277, 22, 216, 245, 118, 298, 168, 295, 127, 191, 425, 197, 351, 195, 479, 206, 16, 54, 188, 221, 236, 69, 330, 278, 436, 161, 282, 478, 80, 440, 5, 377, 162, 246, 146, 281, 166, 225, 94, 299, 442, 300, 372, 98, 337, 462, 196, 215, 36, 455, 338, 250, 256, 496, 40, 62, 204, 429, 247, 444, 38, 120, 383, 255, 427, 211, 177, 128, 165, 293, 156, 483, 102, 292, 86, 434, 414, 97, 375, 452, 168, 25, 251, 263, 81, 497, 491, 4, 181, 371, 400, 69, 479, 450, 197, 277, 298, 271, 266, 295, 99, 108, 325, 282, 395, 330, 421, 351, 188, 54, 161, 440, 5, 464, 205, 348, 468, 458, 281, 246, 498, 162, 195, 494, 53, 425, 418, 410, 192, 206, 17, 314, 105, 447, 93, 23, 30, 166, 442, 300, 98, 196, 337, 250, 215, 372, 496, 40, 36, 62, 462, 429, 455, 204, 427, 338, 38, 292, 256, 293, 247, 444, 165, 483, 414, 25, 97, 120, 128, 251, 156, 371, 86, 211, 434, 450, 177, 497, 181, 491, 266, 298, 81, 383, 108, 395, 452, 400, 325, 102, 375, 271, 351, 295, 99, 263, 421, 464, 330, 468, 348, 4, 188, 105, 278, 221, 236, 245, 168, 498, 22, 246, 162, 80, 216, 205, 494, 118, 53, 410, 447, 418, 197, 96, 78, 127, 191, 112, 425, 440, 174, 23, 206, 195, 281, 314, 94, 30, 166, 225, 300, 299, 442, 196, 337, 372, 455, 250, 462, 204, 427, 256, 38, 62, 247, 429, 36, 496, 338, 215, 293, 40, 255, 128, 165, 177, 156, 86, 375, 102, 483, 371, 444, 450, 383, 266, 292, 211, 108, 25, 120, 97, 251, 468, 497, 414, 282, 4, 168, 298, 491, 69, 452, 197, 277, 181, 81, 325, 421, 263, 434, 479, 395, 16, 464, 99, 271, 400, 295, 330, 54, 161, 351, 245, 5, 22, 216, 348, 236, 118, 458, 221, 191, 105, 278, 80, 440, 425, 436, 127, 377, 17, 205, 77, 265, 284, 30, 225, 94, 300, 442, 98, 196, 337, 250, 372, 496, 215, 462, 40, 62, 204, 36, 429, 455, 427, 38, 338, 256, 293, 165, 292, 128, 483, 444, 86, 25, 156, 251, 371, 177, 414, 97, 211, 120, 383, 497, 450, 266, 108, 102, 434, 81, 375, 491, 452, 181, 298, 395, 400, 263, 468, 325, 271, 421, 99, 295, 464, 351, 330, 4, 348, 188, 168, 245, 22, 197, 216, 236, 221, 278, 118, 105, 498, 277, 246, 162, 191, 80, 195, 494, 205, 69, 53, 127, 282, 410, 447, 418, 425, 479, 440, 23, 206, 96, 78, 30, 225, 300, 299, 442, 337, 372, 196, 462, 455, 256, 250, 204, 247, 36, 62, 215, 429, 427, 338, 496, 38, 40, 128, 165, 177, 293, 255, 86, 102, 383, 156, 375, 483, 211, 444, 292, 371, 120, 414, 497, 251, 450, 25, 266, 108, 168, 97, 282, 452, 468, 298, 69, 81, 4, 263, 197, 395, 181, 277, 479, 491, 434, 400, 325, 54, 161, 421, 351, 348, 330, 16, 295, 5, 271, 188, 464, 458, 99, 105, 236, 221, 278, 80, 162, 246, 498, 440, 245, 494, 53, 418, 410, 377, 205, 17, 447, 118, 22, 96, 30, 225, 94, 299, 442, 300, 98, 372, 337, 462, 196, 455, 215, 36, 250, 256, 338, 496, 40, 62, 204, 429, 247, 38, 427, 444, 383, 255, 128, 177, 211, 165, 293, 120, 102, 156, 483, 86, 292, 375, 25, 251, 168, 434, 452, 414, 263, 97, 497, 81, 371, 491, 4, 181, 400, 69, 450, 479, 277, 197, 266, 108, 282, 271, 295, 395, 99, 298, 325, 330, 54, 161, 351, 5, 421, 468, 188, 440, 464, 458, 348, 205, 246, 162, 498, 195, 16, 494, 53, 105, 17, 281, 418, 425, 377, 410, 77, 265, 447, 23, 94, 98, 442, 337, 372, 462, 256, 250, 215, 36, 62, 247, 429, 40, 496, 165, 427, 338, 128, 86, 38, 383, 102, 483, 255, 177, 156, 375, 452, 293, 414, 298, 497, 371, 211, 450, 251, 120, 292, 266, 97, 444, 282, 108, 81, 468, 395, 168, 25, 69, 263, 325, 434, 421, 188, 479, 400, 348, 4, 464, 330, 181, 16, 498, 236, 277, 221, 278, 162, 246, 418, 53, 205, 410, 161, 491, 494, 295, 80, 54, 447, 245, 23, 351, 5, 440, 118, 105, 99, 22, 271, 216, 454, 191, 458, 281, 195, 101, 78, 112, 429, 211, 271, 462, 371, 295, 414, 483, 206, 464, 325, 375, 105, 22, 421, 263, 96, 221, 400, 216, 132, 146, 174, 251, 236, 245, 80, 281, 168, 191, 397, 468, 298, 278, 192, 440, 118, 265, 377, 17, 256, 357, 113, 348, 77, 247, 353, 128, 395, 330, 403, 93, 362, 436, 314, 12, 356, 479, 234, 318, 289, 95, 139, 296, 6, 284, 481, 87, 268, 122, 323, 409, 408, 63, 142, 499, 19, 446, 237, 441, 473, 48, 45, 0, 232, 136, 390, 228, 150, 65, 111, 276, 260, 58, 331, 405, 90, 344, 178, 461]

        preds2 = exp.recommend(users=[1,2], exclude_known=False)
        assert preds2['user'].unique().tolist() == [1,2]

        preds = exp.recommend(exclude_known=True)
        joined_preds = preds.join(
            data.set_index(['user','item']), 
            on=['user','item'], how='inner'
        )
        assert len(joined_preds) == 0