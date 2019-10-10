# ORG.com Informational System

Django based CRUD webapp with product, issues and metrics as models

## Getting Started
Setting up a Dev Environment
This webapp is a Python 3.6 application.

1. On GitHub, fork the repo by clicking the Fork button in the GitHub UI.
2. Open your terminal, run command **mkdir epam_task**
3. **cd epam_task**
4. Install Virtualenv in your local by running the command **pip install virtualenv**
5. Run the command **virtualenv epam_env**, this will set up the virtual environment with python 3.6, pip and other essential tools.
6. Activate env with **. epam_env/bin/activate**
7. Clone the repo on your local machine with **git clone git@github.com:cheran0308/epam.git** and **cd org_com**
8. Now install the dependencies like django and django rest framework with **pip install -r requirements.txt**
9. Open **orm_com/settings.py** and change the database settings according to yours.
10. Run **python manage.py migrate** and then **python manage.py runserver** to run the web application.
11. Go to localhost:8000 in your browser.

## Tech Stack
This web application uses:

* Ubuntu 18.04 LTS (OS)
* Python 3.6
* Django and Django rest framework
* Mysql as a Database (mysqlclient)

### Why Django Rest Framework 
Django rest framework is a powerful framework for building rest based API's as it is inbuilt with serialization, authentication and support for unit testing.

## Django specific packages and modules used

* Rest_framework : 
    * viewsets 
    * decorators.action
    * views.APIview
    * response.Response, 
    * test.APITestCase
    * test.APIRequestFactory
    * serializers
    * db.models

## DataBase Structure

* Product :
    * Title - String
    * Description - String

* Issue : 
    * Title - String
    * Category - String
    
* Metric : 
    * Title - String
    * Description - String
    
* PIMRelation :
    * product - ForeignKey(Product)
    * metric - ForeignKey(Metric)
    * issue - ForeignKey(Issue)
    
## API Endpoints

Base_url = http://localhost:8000

* **/** -> Navigates to the Index Page with Hello World Message
* **/products/** -> 
    * Get : Gets the list of all the products
    * Post : Use the below json to insert a new product : 
    
             
             {
                "product" : {
                  "title" : "title1",
                  "description" : "description for title1"
                }
             }
     
     * Put : This is used to update the existing product information. To update pass the id of the product. For example if you have to update product with id=1, then use the url `/product/1`
     
            {
                "product" : {
                  "title" : "product_updated"
                }
            }
     
     * delete : This is used to delete a product. Use `/product/1` to delete the product with id=1
     
* **/metrics/** -> 
    * Get : Gets the list of all the metrics
    * Post : Use the below json to insert a new metric : 
    
             
             {
                "metric" : {
                  "title" : "title1",
                  "description" : "description for title1"
                }
             }
     
     * Put : This is used to update the existing metric information. To update pass the id of the metric. For example if you have to update metric with id=1, then use the url `/metric/1`
     
            {
                "metric" : {
                  "title" : "metric_updated"
                }
            }
     
     * delete : This is used to delete a metric. Use `/metric/1` to delete the metric with id=1
     
* **/issues/** -> 
    * Get : Gets the list of all the issues
    * Post : Use the below json to insert a new issue : 
    
             
             {
                "issue" : {
                  "title" : "title1",
                  "category" : "cat for title1"
                }
             }
     
     * Put : This is used to update the existing issue information. To update pass the id of the issue. For example if you have to update issue with id=1, then use the url `/issue/1`
     
            {
                "issue" : {
                  "title" : "title_updated"
                }
            }
     
     * delete : This is used to delete a issue. Use `/issue/1` to delete the issue with id=1
     
* **Get /product_issues/** : gets the list of all the product and issues
* **Get /product_metrics/** : gets the list of all the product and metrics
* **Get /metric_issues/** : gets the list of all the metrics and issues
* **Post /set_product_issues/** : Maps a product to issue
    
           {
              "product_issue" : {
                  "product" : 1,
                  "issue" : 1
              }
           }
           
* **Post /set_product_metrics/** : Maps a product to metric
    
           {
              "product_metric" : {
                  "product" : 1,
                  "metric" : 1
              }
           }
           
* **Post /set_metric_issues/** : Maps a metric to issue
    
           {
              "metric_issue" : {
                  "metric" : 1,
                  "issue" : 1
              }
           }
           
* **Delete /pim_relation/<id> : Deletes a particular PIMRelation row
* **Get /get_issue_by_product/<product_id>** : Get all the issues for a particular product
* **Get /get_metric_by_product/<product_id>** : Get all the metrics for a particular product
* **Get /get_issue_by_metric/<metric_id>** : Get all the issues for a particular metric

## Test
This web application makes use of rest_framework.test. To run the test, Run the command `python manage.py test` in the command line.
