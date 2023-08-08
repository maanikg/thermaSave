# thermaSave

We wanted a way to help fellow Canadians decrease their carbon emission consumption and we thought we could create a model to do exactly that and use ML to optimize it!

It uses weather data from Toronto over the past 50 years and data from energy consumption for Toronto over the past 10 years to create a prediction for how the changing temperature could affect how buildings heating and cooling may have to operate. It allows users to look at a range of time in the future and have the program tell you how much to decrease/increase the temperature in your building to save a certain amount of energy based on the data found.

We used a weather API to create a dataset that we then used python's libraries including `pandas`, `numpy`, and most importantly a ML based Random Forest Regressor (via `scikit-learn`) to predict the weather in future years and how that might affect carbon emissions due to heating and cooling in buildings.

