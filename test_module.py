import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot(self):
        # Call the function to draw the plot
        ax = draw_plot()

        # Check that the plot has the correct labels
        self.assertEqual(ax.get_xlabel(), 'Year')
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')

        # Check that there are two lines on the plot (one for each line of best fit)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 2)

if __name__ == "__main__":
    unittest.main()
