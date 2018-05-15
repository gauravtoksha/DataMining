#RediffDataset

The given dataset contains more than 14 lakh news articles from various newspapers in India for the year 2017, crawled by the Rediff Realtime News platform. Most of the major newspapers are covered in this dataset, and top news from most of these sites should be a part of the dataset.

The dataset contains the News source name, the time of crawl (which is a good approximation to the time of the news being published), the title of the news article, a summary and a derived description of the news article (first few lines). This data set is used for showing top news and for powering the news search on http://realtime.rediff.com - which is Rediff's attempt at automated news.

Tasks performed:
1)Clean the data to remove erroneous characters, news paper name etc. from the title and subject line.
2)Extraction of Latent Variables such as Dates,Cities and States from the summaries
3)Identification of Entities such as person,organisation and location using various NER Frameworks available on the net.
4)tokeninizing the summary using tf-idf for clustering of related articles
5)assigning categories to each cluster based on the token
6)finding out various trending people and categories and visualize them
7)using conditional probabilities to predict the likelihood of a news event
8)created a web crawler to crawl all those pages to get accurate date and the category---this was a failure due to the resources and time it takes to perform the job
