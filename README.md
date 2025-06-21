# Graph Attack-Defense Game

![graphs_ml](https://github.com/user-attachments/assets/132f39a8-8065-47f8-9f38-ffc8105b2bdd)

This project uses the dataset [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html), the dataset records the traffic between servers. Benign traffic and cyberattacks.
All the traffics are modeled in flow level: fwd packages, bwr packages, flags, protocols, IPs, etc.

We are using Graphs + Machine Learning to model the dataset and find useful patterns:
* The central servers in the network.
* The most relevant servers in the network.
* The servers which handle more traffic.
* Servers communities (Community detection).
* Use Graph neural network to identify attackers.

## Prerequisites
* Install Python 3.11
* Install the libraries using requirements.txt.
```bash
pip install -r requirements.txt
```
* Add the traffic.csv dataset CSV file to the input data folder

## Usage
Explore the different notebooks, each one is focus on different tasks.

## External Resoruces
This project was built by the Medellín Machine Learning - Study Group (MML-SG) community. In the following [link](https://drive.google.com/drive/u/0/folders/1nPMtg6caIef5o9S_J8WyNEvyEt5sO1VH) you can find the meetings records about it:
* [20. Introducción a Grafos Machine Learning (GNN) (2024-08-21 19:09 GMT-5).mp4](https://drive.google.com/file/d/1SzNfLmjhO4XjaWiJ5L0xn7Tq0253wNWf/view?usp=drive_link)
* [21. Principios base de Grafos en Machine Learning (2024-08-28 19:09 GMT-5)](https://drive.google.com/file/d/1KNBXPZzWBubB34Zf8MVHDcH7WEKxAqiK/view?usp=drive_link)
* [22. Deep Learning en Grafos Introduccion (2024-09-04 19:09 GMT-5)](https://drive.google.com/file/d/1cGaGzXTNgP1yLGTu7oiZbFZMy4v1Crq5/view?usp=drive_link)
* [23. Graph Embeddings Introduccion y  Attack-Defend Game (2024-09-11 19:10 GMT-5))](https://drive.google.com/file/d/1dYvSuCeChagNAz2_2Ypdjr9WUZ-3PDt5/view?usp=drive_link)
* [24. Understanding Graph Embedding and Profiling Cyberattacks (2024/09/18 18:59 COT)](https://drive.google.com/file/d/1DiUVCeIDahVda_NrLfNaLl6Li2k70Qn4/view?usp=drive_link)
* [25. Graph Embeddings Introduction (2024-10-02 19:09 GMT-5)](https://drive.google.com/file/d/119DLsvif_7WrBcY4D8mKZf7f-sMwh7lM/view?usp=drive_link)
* [26. Community Detection Introduction (2024-10-09 19:09 GMT-5)](https://drive.google.com/file/d/1kFPWA1hspW-NUBONSSKKtXxLHxecEI23/view?usp=drive_link)
* [27. Hands on Graphs Community Detection and GNN– 2024/10/23 18:59 COT – Recording](https://drive.google.com/file/d/1ITCAzF6swWIKG1KmqgG8hih-iuJWiHot/view?usp=drive_link)
* [28. Build our first Graph Neural Network for Link Prediction  (2024-10-30 19:00 COT)](https://drive.google.com/file/d/19SrzOyMR-AB0CxXZNSBrJCmiggfl8Lah/view?usp=drive_link)
