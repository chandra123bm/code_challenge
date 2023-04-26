What is data quality ?


In simple terms data quality can be defined as
" The degree to which the data meets the requirements of the purpose it was built for "

“As organizations accelerate their digital business efforts, poor data quality is a major contributor to a crisis in information trust and business value, negatively impacting financial performance.”

Ted Friedman, VP Analyst, Gartner

There is another was of describing it " data quality is the absense of defects in data which can not be tolerated"

here we need to accept the fact that we live in an imperfect world and so is the data . It cannot be complete free of defects and it is just fine.
there needs to be a threshold till which we can tolerate defects.


This makes the data quality very subjecive in nature  and its meaning differs for every organization depending on how they intend to use it.

3 examples here:

1.Banks and Insurance
2. Media and Advertizing
3. Retail - real time SOH


What are the impacts of having bad data quality practices:

1. data will be  deemed useless for business purposes 
2. Impacts the trust in the data teams by stakeholders
3. All the time and efforts an organization invests in capturing,storing and managing data assets will be wasted
4. Can lead to customer dissatifaction
5.Data teams spend more time debugging data issues than new feature developnent 

How to measure data quality.?

Before we start looking at how DQ is measure, lets understand how data asset  is set up at any given organization.

At the lowest level of data hierarchy, it always starts with a single data value. for example in real estate - its a property address, 
In a bank it is an account number.

Next, various data values which are related are grouped together as an entity or a data record. 
Multiple data records which are just many occurances of same type are grouped into a data set . 

And then we group these datasets into something called a data store. Depending on how we manage this we can these as data warehoues, data lakes , lake houses, data martes etc

<insert picture here>

 
 How do we say data that the data us fit for the need?
 There are key dimenions which help us to measure the quality of data in an organization.
 
 There are two types of metrics - Inherent DQ dimentions
 - structure of the data value, format and meaning
 1. Accuracy - 
 how well the data values depict the correctness .
 For example total sales in a day. To measure this we need to have a source we can compare to . This becomes complex if there are multiple sources of truth.
 
 2. Data Lineage : Having a valid source of data
 e.g. Sourcing a phone number from customer than from a public directory
 
 3. Meaning/Sematics : Are the data values are represent their meaning.
  Having a customer database with primary and mailing address. 
  
 4. Data format: Whether the data values have the specified format
 for example : Dates , yy/mm/dd or mm/dd/YYYY, or a 4 digit postcode
 
 
 
2. Context level data quality metrics

These evaluate the data at record revel, or data set level and focus on related data as well

like relations between Accounts and Customers
Business constomers must have ABNs and can not be blank 


Completeness - the degree to which data is filled annd not left blank
Like mandatory columns

required / optional/ inpplicable

Constistecy

Data need to be same accross departments. 
Like employee info in HR and Finance

Currency - does data represent the most upto date version

Timeliness - The time is takes to exttract the data is suitable for business needs

Uniqueness - Not having duplicates

How to build a case for data quality initiative :



To prove the importance of data quality we need to highlight how DQ problems increase business risks and impact effiecincy.
This may involve analyzing and mapping the DQ issues to the business risks.

For example a duplicate entry in the sales table can impact total sales metric
An outdated stocks table can impact wrong fulfilment decisions in retail company

A business uses its data as a fuel across all departments and functions. Not being able to trust the authenticity and accuracy of your data can be one of the biggest disasters in any data initiative

We need to analyze , and present how fixing data issues can benefit these major pillars of any organization:
business, 
finance, 
customer,
competition,
team and 
technology 

<speak one liners about all above >

Designing a data quality framework for DQ management 

Data quality framework is a systematic process that monitors the current state of data quality and ensures that it is maintained above defined thresholds.
It is usually designed in. 
Data quality framework is a systematic process that monitors the current state of data quality and ensures that it is maintained above defined thresholds.

It is usually designed in a cyclic manner in order to continuously assess and errors are corrected .

to begin with, the framework should include basic data integrity checks e.g. nullability , duplicates check etc and then more use case specific checks .


A simple framework can have 4 stages:


Assess ====> Design =====> Execute ====> Monitor


Assessment:
Where you define key DQ metrics 
Peform data profiling and find how potential gaps in the data
Define acceptable level of data quality.
This assessment requires you to understand how the dataset is used ? it is for runnning the business processess or to be analysed for desicison making
< sample data diagram>

Design :
 Decide the architecture of the framework
 Where are we placing the data validation checks .
 
 consider the factors like:
 Scalability
 
 Adaptability
 
 Reusability
 
Where to place the DQ processes:

A typical pipeline would look like this:

Source data ----> ETL ------>> Target datset

1. DQ at input 
2. as a part of ETL processes before loading it to the datastore 

 Execution :
 Here we decide how execute DQ checks.
 Factors to consider include:
 1. Frequecy of data checks
 2. Handling of errors
 3. Time to execute
 4. Thresholds 
 
 Monitoring :
 Here we see the results of executing data quality checks and observe anomalies.
 
As I indicated before this framework is an interative process.not a one stop destination.
It works as a continuus improvement model. 
We are going to find few errors which will need to be fixed and new quality rules added with new feature work.

Bulding a config driven DQ framework

Benefits :

1. Curate any dataset by placing the data quality rules as configurations. Since we do not need to build code everytime we had a DQ rule, it shortens build phase and promotes iterative development 
2. Even data analysts with SQL knowledge can configure the rules.This pushes the DQ responsibility to business domains rather than central data platform teams


Solution Overview:

![DQ](https://user-images.githubusercontent.com/69589496/234494547-d0980145-4658-4155-ba0e-77e6f37d0c0d.jpg)

