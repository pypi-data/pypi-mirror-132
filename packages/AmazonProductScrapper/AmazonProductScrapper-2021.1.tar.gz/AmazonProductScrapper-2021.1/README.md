# Amazon Product Scrapper (Version 2021.1)

To install this python package, run this in terminal :  **`pip install AmazonProductScrapper`**

Check out the code here on GitHub. 

**GitHub Url** : [https://github.com/subhajit2001/AmazonProductScrapper](https://github.com/subhajit2001/AmazonProductScrapper "https://github.com/subhajit2001/AmazonProductScrapper")

Check out the published python package here on PyPi.

**PyPi Url** : [https://pypi.org/project/AmazonProductScrapper/](https://pypi.org/project/AmazonProductScrapper/ "https://pypi.org/project/AmazonProductScrapper/")

This package helps to extract product data for all the available products from a given keyword(E.g.: laptops, headphones etc.) This data is returned in the form of  a pandas dataframe.

The package can be loaded as:

```py
import AmazonProductScrapper as aps
```

Extract product data of all laptops which are available in realtime:

```py
df = aps.load_Amazon_product_data(“laptops”)
```

df is a Pandas Dataframe. We can view the dataframe as:

```py
print(df)
```
The maximum number of pages that can be loaded for a partcular keyword is 20 and that is the final limit.

The extracted pandas Dataframe contains the data about individual products:

1. ***Product_Name** (Product Name)*

2. ***Product_Price** (Price shown for the product)*

3. ***Actual_Product_Price** (Undiscounted Price)*

4. ***No._of_ratings** (Total number of ratings given by customers)*

5. ***Link** (Link of the respective product page)*

For extraction of reviews for a particular product, take the url of the product and no of pages of reviews you want to fetch. Each page contains 10 reviews approximately and the max pages that can be fetched is 500.

```py
df = aps.load_Amazon_product_review_data(“https://www.amazon.in/Boat-BassHeads-900-Wired-Headphone/dp/B074ZF7PVZ/ref=sr_1_3?crid=UPDZLG5ER2D3&keywords=headphones&qid=1640276178&sprefix=headphone%2Caps%2C647&sr=8-3”,500)
```

Provide 2 arguments to the function above, one is the url of the product and another is the number of pages to be loaded whose value has to be within 1 to 500.

```py
print(df)
```
The pandas Dataframe contains the data about an individual products:

1. ***Product** (Product Name)*

2. ***Title** (Title of the review given by the customer)*

3. ***Rating** (Rating given by customer)*

4. ***Review** (Review given by the customer)*

External Base packages required for making this library: Requests, bs4, Pandas

Credits for **progress bar**: 

* [https://stackoverflow.com/a/34325723](https://stackoverflow.com/a/34325723 "https://stackoverflow.com/a/34325723")

Do review the project and don’t forget to give your valuable suggestions to me here at: [subhajitsaha.formal@gmail.com](http://subhajitsaha.formal@gmail.com "http://subhajitsaha.formal@gmail.com")

Do submit a pull request if you want to.

Developer: Subhajit Saha. This project is licensed under `MIT License`.

`Copyright (c) 2021 Subhajit Saha` 
