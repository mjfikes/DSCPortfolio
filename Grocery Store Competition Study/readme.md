# Grocery store Competition Study

This project looks at two grocery store chains to see if it can be determined how they choose locations.


## Summary

The problem being addressed in my research is to answer two hypotheses about how the Wegmans grocery chain chooses locations. 
The first hypothesis is that Wegmans has a gentleman's agreement with another chain in the area called Price Chopper. A 2006 article checked with a spokesman, who discredited the story and said that they in fact compete in Western New York and Pennsylvania (Wegmans & Price chopper, 2008). Another article from February 2021 talks again about hesitation in expanding into the Capital region of New York and the gentleman's agreement is also mentioned (Springer, 2021). It seems that the myth persists to this day. I will use locations of both stores to see if there are any insights into the gentleman's agreement area the chains are splitting. 

The second hypothesis is that Wegmans will only open a store if the area is wealthy or populated enough to serve it. This would make sense from the standpoint of sales, as there need to be enough people shopping to support the cost associated with running a store. Census information should provide light for this hypothesis.


### Data Sources

Store addresses were obtained from their respective corporate website. They were geocoded via the geocod.io service.
All economic data is from the American Community Survey from the Census Bureau. 

### Required Libraries

* ggplot2
* ggmap
* geosphere
* ggbeeswarm
* ggpubr
* reshape2
* dplyr
* leaderCluster
* factoextra

### Files

* Grocery Study.pdf - Research paper with plotted visualizations

* Grocery Study.Rmd - R Markdown with code for report plots and analyses.

* geocode_PC.csv - geocoded store location data for Price Chopper

* geocode_Wegmans.csv - geocoded store location data for Wegmans


### References

Wegmans & Price chopper: The real deal. (2008, April 2). Retrieved March 02, 2021, from http://alloveralbany.com/archive/2008/04/02/wegmans-price-chopper-the-real-deal

Springer, J. (2021, February 12). Wegmans to ALBANY: Not now. Retrieved March 02, 2021, from https://www.winsightgrocerybusiness.com/retailers/wegmans-albany-not-now

Price Chopper Supermarkets. (2021, February 10). Retrieved March 02, 2021, from https://en.wikipedia.org/wiki/Price_Chopper_Supermarkets

## Author

[Matthew Fikes](https://www.linkedin.com/in/matthew-fikes-0ab91213/)

