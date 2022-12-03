# Disease-prediction-using-entity-extraction

## Apache Fuseki
1. Run the Apache Fuseki service by following the installation steps at https://jena.apache.org/documentation/fuseki2/
2. Open web browser and navigate to localhost:3030
3. Click on "manage" then "new dataset"
4. Name the new dataset "Medical" and click "Persisent (TDB2)" then "Create dataset"
5. Click on "datasets" and "add data" next to "Medical"
6. Select the seed.owl file in project directory and upload


## Prequisites for running the web application
* Node.js
* Java with Apache Jena library. Get the Apache Jena library here: https://jena.apache.org/download/index.cgi
* Python
* Run these commands to install spacey library:
    `pip install spacey`
    `python -m spacy download en`

## Running the web application
1. Open diseases-server.js and change path_to_project value to project directory (line 4)
2. Change path_to_jena value to location of Apache Jena library (line 5)
3. Navigate to project directory
4. Run following command:
    `node diseases-server.js`
5. Open browser and navigate to localhost:8080
6. Try performing some queries against seed data
7. Copy and paste text from "dataset.txt" and click submit to extract entities from featured data
8. Try performing the same queries and notice the changes in results