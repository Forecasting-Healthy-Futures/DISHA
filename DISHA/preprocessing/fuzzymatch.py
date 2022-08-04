import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class fuzzymatch:

    def __init__(self, df, std_cols, min_score=0):
        """This fuction takes a dataframe and a list of standard column names. 
           It gives the fuzzy match of given column against the standard column names.

        Args:
            df (pandas series): A pandas column for which the name fuzzy match is to be performed
            std_cols (list): A list of standard column names
            min_score (int, optional): This minimum threshold of matching to be performed. Defaults to 0.
        """
        df = self.df
        std_cols = self.std_cols
        min_score = self.min_score

    def match_names(self):
        """This function takes a string and a list of standard column names.

        Returns:
            tuple: a tuple of the matched column name and the score of the match
        """
        max_score = -1
        max_name = ''
        for x in self.std_cols:
            score = fuzz.ratio(self.df, x)
            if (score > self.min_score) & (score > max_score):
                max_name = x
                max_score = score
        return (max_name, max_score)

    def fuzzy_match(self):
        """_summary_: This function takes a dataframe and a list of standard column names.

        Returns:
            dictionary: a dictionary of the matched column name and the score of the match
        """
        names = []
        input_col = input_col.dropna()
        input_names = list(input_col.unique())

        for x in input_names:
            match = self.match_names(x.upper(), self.std_cols, self.min_score)
            if match[1] >= self.min_score:
                name = (str(x), str(match[0]))
                names.append(name)

        name_dict = dict(names)
        crosswalk = pd.DataFrame.from_dict(name_dict, orient='index')
        crosswalk.reset_index(level=0, inplace=True)
        crosswalk.columns = ['Wrong_Name', 'Correct_name']
        return {'dictionary': name_dict, 'crosswalk': crosswalk}