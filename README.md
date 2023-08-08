# 🌎 thermaSave 

Check out the full project Devpost and video link here! ➡️ https://devpost.com/software/will

We wanted a way to help fellow Canadians decrease their carbon emission consumption and we thought we could create a model to do exactly that and use ML to optimize it!

About the project:
- Uses Toronto weather data and building energy consumption over the past 50 years to predict how changing temperatures could affect the heating and cooling operations of buildings
- Enables users to view a time range in the future and receive energy saving and management tips in response to estimated temperatures at the time

The process:
- Utilized a weather API to create a dataset that was then parsed using Python ML libraries (`pandas` and `numpy`)
- Implemented a ML-based Random Forest Regressor (via `scikit-learn`) to predict the weather in future years and how that might affect carbon emissions due to heating and cooling in buildings

----

### 💻 Tech Stack: 
<img src="https://img.shields.io/badge/-scikitLearn-3499cd?style=flat&logo=scikitlearn&logoColor=F7931E" height="30" alt = "SciKitLearn" /> <img src="https://img.shields.io/badge/-pandas-150458?style=flat&logo=pandas&logoColor=white" height="30" alt = "Pandas" />
<img src="https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=4dabcf" height="30" alt = "NumPy" />
