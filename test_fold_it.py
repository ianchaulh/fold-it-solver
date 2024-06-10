import unittest   # The test framework
from fold_it import dfs, BOARD


class TestDFS(unittest.TestCase):
    def test_one_item_path_found(self):
        for i in range(1,17):
            self.assertTrue(dfs(BOARD, BOARD, {i}))

    def test_two_item_path_found(self):
        two_item = [{1,4}, {13,16}, {5,9}, {10,2}, {4,16}, {8,12},
                    {15,3}]
        for two_item_set in two_item:
            self.assertTrue(dfs(BOARD, BOARD, two_item_set))

    def test_three_item_path_found(self):
        three_item = [{9,10,11}, {8,5,6}, {8,12,16}, {1,3,2},
                      {1,5,13}, {3,11,15}]
        for three_item_set in three_item:
            self.assertTrue(dfs(BOARD, BOARD, three_item_set))

    def test_four_item_path_found(self):
        four_item = [{2,3,15,14}, {5,12,8,9}, {11,9,15,13}, {14,13,9,10}]
        for four_item_set in four_item:
            self.assertTrue(dfs(BOARD, BOARD, four_item_set))

    def test_six_item_path_found(self):
        six_item = [{1,2,3,5,6,7}, {1,3,2,13,14,15}, {5,7,9,11,15,13}]
        for six_item_set in six_item:
            self.assertTrue(dfs(BOARD, BOARD, six_item_set))

    def test_eight_item_path_found(self):
        eight_item = [{1,2,3,4,5,6,7,8}, {1,2,3,4,13,14,15,16}]
        for eight_item_set in eight_item:
            self.assertTrue(dfs(BOARD, BOARD, eight_item_set))

    def test_nine_item_path_found(self):
        nine_item = [{1,2,3,5,6,7,9,10,11}, {2,3,4,6,7,8,14,15,16}]
        for nine_item_set in nine_item:
            self.assertTrue(dfs(BOARD, BOARD, nine_item_set))

    def test_twelve_item_path_found(self):
        twelve_item = [{1,5,9,13,2,3,6,7,10,11,14,15}]
        for twelve_item_set in twelve_item:
            self.assertTrue(dfs(BOARD, BOARD, twelve_item_set))

    def test_all_item_path_found(self):
        all_item_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
        self.assertTrue(dfs(BOARD, BOARD, all_item_set))

    def test_two_item_no_path_found(self):
        two_item = [{1,6}]
        for two_item_set in two_item:
            self.assertFalse(dfs(BOARD, BOARD, two_item_set))  

    def test_three_item_no_path_found(self):
        three_item = [{1,7,2}, {1,6,11}]
        for three_item_set in three_item:
            self.assertFalse(dfs(BOARD, BOARD, three_item_set)) 

    def test_four_item_no_path_found(self):
        four_item = []
        for four_item_set in four_item:
            self.assertFalse(dfs(BOARD, BOARD, four_item_set))

    def test_five_item_no_path_found(self):
        five_item = [{1,2,3,4,5}]
        for five_item_set in five_item:
            self.assertFalse(dfs(BOARD, BOARD, five_item_set))

    def test_six_item_no_path_found(self):
        six_item = []
        for six_item_set in six_item:
            self.assertFalse(dfs(BOARD, BOARD, six_item_set))

    def test_seven_item_no_path_found(self):
        seven_item = []
        for seven_item_set in seven_item:
            self.assertFalse(dfs(BOARD, BOARD, seven_item_set))

    def test_eight_item_no_path_found(self):
        eight__item = []
        for eight_item_set in eight__item:
            self.assertFalse(dfs(BOARD, BOARD, eight_item_set))

    def test_nine_item_no_path_found(self):
        nine_item = []
        for nine_item_set in nine_item:
            self.assertFalse(dfs(BOARD, BOARD, nine_item_set))

    def test_ten_item_no_path_found(self):
        ten_item = []
        for ten_item_set in ten_item:
            self.assertFalse(dfs(BOARD, BOARD, ten_item_set))

    def test_eleven_item_no_path_found(self):
        eleven_item = []
        for eleven_item_set in eleven_item:
            self.assertFalse(dfs(BOARD, BOARD, eleven_item_set))

    def test_twelve_item_no_path_found(self):
        twelve_item = []
        for twelve_item_set in twelve_item:
            self.assertFalse(dfs(BOARD, BOARD, twelve_item_set))

    def test_thirteen_item_no_path_found(self):
        thirteen_item = []
        for thirteen_item_set in thirteen_item:
            self.assertFalse(dfs(BOARD, BOARD, thirteen_item_set))

    def test_fourteen_item_no_path_found(self):
        fourteen_item = []
        for fourteen_item_set in fourteen_item:
            self.assertFalse(dfs(BOARD, BOARD, fourteen_item_set))

    def test_fifteen_item_no_path_found(self):
        fifteen_item = []
        for fifteen_item_set in fifteen_item:
            self.assertFalse(dfs(BOARD, BOARD, fifteen_item_set))
            
if __name__ == '__main__':
    unittest.main()
