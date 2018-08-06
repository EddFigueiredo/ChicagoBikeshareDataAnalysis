# Chicago Bikeshare Data Analysis

Project #1 on Udacity's Fundamentals of Data Science 1

Clone the repo, and copy chicago.csv file available [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/March/5ab9668a_chicago-bikeshare-us/chicago-bikeshare-us.zip) to the root folder of the project.

Install the pependencies with pip:
- matplotlib

Run chicago_bikeshare.py

On Docker pull the image eddfigueiredo/bike-share-analysis:latest and run with:

docker run -ti --rm eddfigueiredo/bike-share-analysis:latest

Or build your own image with the Dockerfile on project root directory. Don't forget to add `chicago.csv` file.

For now running on docker doesn't show the graph with matplotlib. =- /
