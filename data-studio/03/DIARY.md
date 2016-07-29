# Diary of Map the Fans

- The import of the data was straight forward. 
- It took me quite a while to merge them. 
- Since ZIP codes can not be clearly assigned to one community, I need to remove this column. Probably, I will reimport it later with the Shapefiles of the ZIP code areas.
- The data from SCB contained a number of rows for the same ZIP code. I grouped it, so that I have just one row per ZIP code area.  
- I took me quite a while to figure out how to merge the three datasets. 
- I tried to find correlations between the number of season cards and socia-demographic information. Since the values are not that extreme, I couldn't find any usable data.
- I did analyze the number of cards for both clubs and the number per capita. I finally made some plots. 

### Mapping part 

- I am generating a csv file of the necessary information out of Pandas. 
- The import of this file into 
- I was also trying to do that directly in javascript using the [Leaflet Library](http://leaflet.org). I could generate a map. To get it to work, I had to simplify the shapefile with [Ogr2](http://gdal.org/ogr2ogr.html). But still with a strong generalization the map reacted slow. Therefor I decided to stick with 'Carto'. 
