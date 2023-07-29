# Querying Cardano Native Tokens

There are a lot of various methods for pulling Cardano native token data.  This includes using APIs for various services and products that communicate and send data from a Cardano node. The method that will be used to start off the project will be Blockfrost and Koios' Python API. There are multiple methods for querying data utilizing indexing solutions like db-sync, cardano-graphql, Koios, or Carp and as this repo progresses, different methods of pulling data will be demonstrated.

The documentation to the indexing solutions utilized can be found here [Koios-API-Python](https://github.com/cardano-apexpool/koios-api-python) and here [Blockfrost-Python](https://github.com/blockfrost/blockfrost-python/tree/master) they both enables a simple Python library that connects and pulls data directly from the Koios/Blockfrost to a local machine.

This section will feature some basic files demonstrating how to utilize the API to begin pulling data into data frames for analysis.  When it comes to modeling the data, further manipulations may be done.

# Future files that will be made are:
1. Holder Distribution Analysis - Understand the breakdown from whales to shrimps
2. Transaction Analysis - Swaps/price correlations over time
3. Alternative Querying/Indexing Methods for getting Cardano on-chain data
