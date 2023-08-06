# Amazon Product Scrapper (Version 0)

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

If this is the output on your screen then the function has executed successfully:

![](https://github.com/subhajit2001/AmazonProductScrapper/blob/main/exec1.png)

The pandas Dataframe looks like this:

![](https://github.com/subhajit2001/AmazonProductScrapper/blob/main/exec2%20(2).png)

The pandas Dataframe contains the data about an individual products:

1. ***Product_Name** (Product Name)*

2. ***Product_Price** (Price shown for the product)*

3. ***Actual_Product_Price** (Undiscounted Price)*

4. ***No._of_ratings** (Total number of ratings given by customers)*

5. ***Link** (Link of the respective product page)*

External Base packages required for making this library: Requests, bs4, Pandas

Credits for **progress bar**: 

* [https://stackoverflow.com/a/34325723](https://stackoverflow.com/a/34325723 "https://stackoverflow.com/a/34325723")

Do review the project and don’t forget to give your valuable suggestions to me here at: [subhajitsaha.formal@gmail.com](http://subhajitsaha.formal@gmail.com "http://subhajitsaha.formal@gmail.com")

Do submit a pull request if you want to.

Developer: Subhajit Saha. This project is licensed under `MIT License`.

`Copyright (c) 2021 Subhajit Saha`
