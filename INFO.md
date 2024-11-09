# CDE-CAPSTONE

A travel Agency reached out to CDE, their business model involves recommending tourist location to their customers based on different data points, they want one of our graduates to build a Data Platform that will process the data from the Country rest API [HERE](https://restcountries.com/v3.1/all) into their cloud based Database/Data Warehouse for predictive analytics by their Data Science team.

## SOME CONSIDERATIONS TO BE AWARE

- The company needs some specific fields/attributes from the API data to enable downstream usage.
- However, you have to extract the entire raw data from the API into any `Cloud Based Object Storage`, which will serve as the Raw layer.
- The choice of file format when storing the data in Object Storage must be `Parquet` file considering its better for performance.
- We want to store the entire API data because, if the agency require more field/attribute in the future, we don't have to pull data from the API again, we simply pull from the one on the data lake.
- From the Data Lake, please extract the below attributes that is required for predictive analytics by the Travel Agency and write to a Cloud Database or Datawarehouse.
- Country name

- Independence

- United Nation members

- startOfWeek

- Official country name

- Common native name

- Currency Code e.g USD, EUR

- Currency name

- Currency symbol

- Country code ( idd ) . e.g Germany country code is +49

- you need to concatenate idd root and idd suffix from the response

- Capital

- Region

- Sub region

- Languages

- Area

- Population

- Continents

- Apache Airflow `MUST` be used for Orchestrating the entire workflow, which includes
- Extracting the data from the API
- Writing the extracted data to the Data Lake
- Extracting the final required attributes to the Database/Data Warehouse.
  
- CI/CD should be integrated to the Github Repository
- CI that carry out checks on code linting to ensure code written follow best practices.
- CD to carry out the Build and Push of the code that Extract and Write to object storage to a Cloud based Container Registry.
- Basically, you need to package the code that does the Extract of the raw data from API and the Code that write the data to Object storage into a Docker image and push the image to a Cloud Based Container Registry.

- All Cloud Infrastructures like IAM, Object storage, DB/DW resource provisioning has to be Terraformed with the Terraform State File backend managed in the cloud using an Object Storage.

- Lastly, please you `MUST` leverage DBT to model the data into Fact and Dimension tables.

### BONUS (NOT MANDATORY)

Derive any insights from the Data Set.

### SUBMISSION REQUIREMENTS

- A power point or something similar for presentation of the entire project covering the below
- The Data Architecture.
- The choice of tools 🛠️
- Well documented read me of the project in Github.
- Project submission will close on the 20th November, 2024.
- Github link should be submitted in the link [HERE](https://forms.gle/osnNmo7JyGkQeXnb8)
