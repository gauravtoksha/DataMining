#RediffDataset

The given dataset contains more than 14 lakh news articles from various newspapers in India for the year 2017, crawled on the Rediff Realtime News platform. Most of the major newspapers are covered in this dataset, and top news from most of these sites should be a part of the dataset.

The dataset contains the News source name, the time of crawl (which is a good approximation to the time of the news being published), the title of the news article, a summary and a derived description of the news article (first few lines). This data set is used for showing top news and for powering the news search on http://realtime.rediff.com - which is Rediff's attempt at automated news.

Tasks performed:<ol>
<li>Clean the data to remove erroneous characters, news paper name etc. from the title and subject line.</li>
<li>Extraction of Latent Variables such as Dates,Cities and States from the summaries</li>
<li>Identification of Entities such as person,organisation and location using various NER Frameworks available on the net</li>
<li>tokeninizing the summary using tf-idf for clustering of related articles</li>
<li>assigning categories to each cluster based on the token</li>
<li>finding out various trending people and categories and visualize them</li>
<li>using conditional probabilities to predict the likelihood of a news event</li>
<li>created a web crawler to crawl all those pages to get accurate date and the category---this was a failure due to the resources and time it takes to perform the job</li>
</ol>

<br>The above tasks are only performed on a subset of the entire dataset because of constraints of resources<br>
Currently we are trying to apply the logic on the entire dataset by using Apache Mahout scalable library on Hadoop architecture
