# Cardano Token Engineering Lab

![CTEL Logo](./Asset%20Design/CTEL_Logo.png)

Cardano Token Engineering resources for developing, understanding, and modeling design mechanisms in the Cardano ecosystem.

For more information on the project please visit: [The Token Lab](https://thetokenlab.xyz)

# Background
This GitHub repo is intended to be the home for token engineering where content will be created for a wide variety of users, from those who aspire to learn data analytics and modeling, to those with existing analytics backgrounds, and for researchers and academics to participate and contribute to ongoing research about projects in the Cardano Ecosystem.

Token engineering is one of the newest forms of engineering and consists of a blend of economics, computer science, game theory, and sociologic principles all intertwined to form the basis of token economies.  A token economy can be thought of as a system built around the tokenization of an item that is designed with programmatic incentive mechanisms to encourage certain behaviors.  From a blockchain perspective, this could include the design parameters of a token on how it should be created, distributed, and utilized.  Understanding the desired behaviors that a token should illicit from a user would then lead to the steering of the programming of how the incentive mechanisms work.  

The goal of the Cardano Token Engineering Lab is to help:
1. Understand the nuances of the eUTXO account model that enables or restricts certain design patterns in token engineering
2. Help give Cardano-based projects a starting place to understand, contribute, and leverage information derived from the Lab
3. Build a community of like-minded thinkers, engineers, analysts, and theorists to grow this area and help make the Cardano Ecosystem stronger
4. Provide a background and starting place for aspiring token engineers of a variety of backgrounds to be able to contribute

# Suggested Readings/Videos to get Started
Here are a list of books that are great resources and will likely have reviews of main concepts presented here.
1. [Token Economy: Money, NFT, DeFI by Shermin Voshgmir](https://github.com/sherminvo/TokenEconomyBook)
    A great non-technical book that goes on to explain the hows and whys of token economies, such as the function of money, the evolution of currency and the birth of tokenization as well as use cases for token, NFTs and how DeFi works.  Overall, a great read to help understand the importance around how token engineering and token economies are more than just the combination of computer science, game theory, and economics and how the social aspects is just as critical
2. [Modeling and Simulation in Python by Allen B. Downey](https://allendowney.github.io/ModSimPy/)
    An excellent open source book that can be read online for free that goes through the basics on Python modeling and is built using Jupyter Notebooks.  This gives a super easy Python interface to work from a browser that doesn't require a local install of any software to work.  Having a good basic understanding of Python will be core for the skills and direction of this project, although much of the modeling can be done in most programming langauges.
3. [Introduction to the Modeling and Analysis of Complex Systems by Hiroki Sayama](https://open.umn.edu/opentextbooks/textbooks/233)
    A classic, college-level modeling and analysis book that is open-source and available for free. The author goes through the principles of modeling systems and builds complexity with topics and models throughout the book.  The key takeaway of this book is that modeling complex systems, as with most engineering fundamentals, focuses on starting with small, simple models and slowly building off that.  This book will presume that the reader already has a firm understanding of Python.
4. [Algorithmic Game Theory (Stanford CS364A) - Tim Roughgarden](https://youtube.com/playlist?list=PLEGCF-WLh2RJBqmxvZ0_ie-mleCFhi2N4)
    An older academic course, but it helps to set the stage of the roots of token engineering by bridging concepts that split between computer science and game theory.  Tim Roughgarden is a PhD, with a lot of experience and research on Mechanism Design which is foundation of Token Engineering.
5. [Tokenomics: Mastering the Art of Token Design by Stefan Piech](https://www.amazon.com/Tokenomics-Mastering-Art-Token-Design/dp/B0C646FPYQ)
    A new book that was recently released on token design. I'm currently reading this and will put a more descriptive summary, but published in Q1 of 2023.

# Modeling and Analysis
A majority of the analysis will be primarily using the Python programming language, where there are some open-source Python libraries designed to model complex, dynamic systems such as token economies and design mechanisms.  Resources will be created here to help anyone get started with learning Python, utilizing the modeling libraries available, and being able to start to contribute to the Lab.

A major helper in this space will be leveraging cadCAD, an open source dynamic systems modeling library created in Python.  This open source library is designed to help model complex and adaptive systems, much like those we commonly see in token engineering and mechanism design.  You can read more at the cadCAD GitHub Repo: [cadCAD GitHub Repo](https://github.com/cadCAD-org/cadCAD)

# Data Querying
As this project progresses the aim is to share methods and ways to pull on-chain data for modeling.  Right now we have some basic scripts demonstrating how to pull data utilizing Blockfrosts REST API endpoints.  We further have plans on demonstrating similar data extraction leveraging KOIOS gREST API, ran and operated by the Cardano Operators Guild.  A link to the data querying repo can be found here:  [Query Cardano Data](https://github.com/Cardano-Token-Engineering-Lab/Query-Cardano-Data)