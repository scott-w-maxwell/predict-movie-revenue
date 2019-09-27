import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Process
            I started with looking at the data I had with the  `head()`  &  `shape`  function. 
            The shape function returned (4803, 20) which means I have 4803 potential observations and 20 potential features.
            
            
            [See My Notebook Here]('https://colab.research.google.com/drive/1dLelDHNfJ_0-lVcQRZ17F2Byy5QRmpiN')
            ##### Data Cleaning & Exploration

            After taking a look at the data I noticed I would need to use the pandas function  `to_datetime`  on the release_date column. 
            After doing this I created a month and year feature out of the relase_date column. After creating these new features, I dropped the original column, since it is no longer needed.
            Then I continued on to create plotly scatter plots to discover that budget and release date (which was one of my suspicians) greatly effect the revenue. 
            The revenue column is what I wanted to be able to predict so naturally this is chosen to be my target. 

            ##### Baseline Prediction
            I created a mean baseline prediction dataframe out of creating a repeated list of the mean revenue. This allowed me to attempt a r^2 score with the average revenue and the actual revenue which returned 
            a very low score of -2.220e-16. I went on to get a mean_absolute_error using the average revenue which returned 96403855.60307099. I used  `r2_score`  and  `mean_absolute_error`  from the sklearn metrics library 

            ##### Split Train/Test/Validate Sets
            I wanted to predict the last year I had available to me in the dataset, so I isolated movies released in the year 2016 from the dataset, to use as my test set.
            Then I used `train_test_split` from the sklearn.model_selection python library to split 80 percent of my data into a training set and 20 percent into validation set.
            I then created datasets of just the features for both the train and validation sets, as well as target sets for both train and validation sets.
            
            ##### Wrangling Data (Engineering Features)
            To wrangle the data, I knew I needed to get rid of several different columns that would not normally be known to anyone before a movies release_date such as popularity, vote_count, etc.
            Another reason I got rid of other columns was because I knew I was going to `OneHotEncode`, and did not want any of the data with high cardinality to be used to create a mode, as this would
            likely do nothing or decrease the accuracy of the model. The columns such as title, id, homepage, etc. were dropped for this reason. Before I actually dropped these columns, I wanted to make use
            of a few other columns to engineer features. I created made_by_disney feature from the production_companies column. I also created length_of_title, production_countries_is_US, and a title_changed features out of 
            many of the columns I would later drop due to their high cardinality. To do all this I made a function to wrangle and engineer the features, and applied them to all my sets from the main dataframe.

            ##### Pipelines & models
            I tried 2 different types of regression models to fit to my data. I tried `LinearRegression` from sklearn.linear_model library and `RandomForestRegressor` from the sklern.ensemble library.
            I also wanted to use `SimpleImputer` from the sklearn.impute library to ensure any nan values were taken care of. In addition to SimpleImputer, I added `OneHotEncoder` to make columns that were
            not intially numbers into classifiers. I then fit both the models!

            ### Model Accuracy & Scores
            After fitting the model, I wanted to see if I had improved from my baseline, which given my r2_score from earlier, should not be hard to accomplish.

            These were the results for the linear regression model:

                    Validation set score: 0.5334596499306514
                    Test set score: 0.651236162536164
                    mean absolute error for linear regression model: 77165201.78057592
                    r2_score for linear regression: 0.651236162536164

            These were the results for the random forest regression model:

                Validation set score: 0.4281534348288621
                Test set score: 0.6027004661474664
                mean absolute error for random forest regression model 78246226.69903848
                r2_score for random forest regression: 0.6027004661474664

            ##### Conclusions

            The linear regression model worked better with a higher accuracy score for both the test and validation sets. Although this accuracy is not particularly accurate, it is much higher than our orginal
            mean baseline.

            """
        ),

    ],
)

layout = dbc.Row([column1])