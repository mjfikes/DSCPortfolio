# College Retention Prediction

This study looks at ways to predict Fall to Spring retention at a community college based on available student data.


## Summary

The model is fairly accurate, although false positives are more common than false negatives. An accuracy rate of ~80%
might be sufficient for identifying students that need additional assistance. The features identified make sense in both
sets. HEH and EDUCATION_GOAL relate to how long a student has been in school and how long they plan to stay. High
school grade based on GPA and mother and father’s highest level of education are also features with some value in the
early data. Several of these variables indicate academic readiness to be an important component in predicting retention.
The important features in the early set are joined with information about grades and credits in the full set. Both high and
low grades have an impact on retention, and the amount of credits obtained may indicate the anticipated graduation
terms of students as they reach their credit requirements.
I recommend checking the model against real‐world data early in the semester to identify possible at‐risk students so
advisors can keep an eye on their individual needs. This early intervention may lead to decreased attrition and outcomes
can later be tested against baseline predictions for accuracy.

### Data Sources

* Student data system

* High school transcripts

* Free Application for Federal Student Aid (FAFSA) Application data


### Files

* Retention Case Study Notebook.ipynb - a Jupyter notebook containing the code running the prediction modeling. Predictions were attempted with logicistic classification, multilayer perceptron, and random forest classification models.

* Retention Case Study Report.pdf - Written report of project results and analysis. 

* retention_output.csv - data with features converted to one-hot encoding for machine models



## Author

[Matthew Fikes](https://www.linkedin.com/in/matthew-fikes-0ab91213/)

