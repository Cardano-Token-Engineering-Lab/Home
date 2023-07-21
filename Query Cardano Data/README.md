# Querying Cardano Native Tokens

There are a lot of various methods for pulling Cardano native token data.  This includes using APIs for various services and products that communicate and send data from a Cardano node. The method that will be used to start off the project will be Koios' Python API. There are multiple methods for querying data utilizing indexing solutions like db-sync, cardano-graphql, or Carp and as this repo progresses, different methods of pulling data will be demonstrated.

The documentation to the repo utilized can be found here [Koios-API-Python](https://github.com/cardano-apexpool/koios-api-python) and enables a simple Python library that connects and pulls data directly from the Koios network of nodes to a local machine.

This section will feature some basic files demonstrating how to utilize the API to begin pulling data into data frames for analysis.  When it comes to modeling the data, further manipulations may be done.

The test.py file in this directory is tied to the qADA by changing out the policy_id variable, with the applicable token's policy id.

# Future files that will be made are:
1. Holder Distribution Analysis - Understand the breakdown from whales to shrimps
2. Transaction Analysis - Swaps/price correlations over time
3. Alternative Querying Methods
