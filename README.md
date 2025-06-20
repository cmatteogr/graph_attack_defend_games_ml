# graph_attack_defend_games_ml

# Graph Attack-Defense Game



This project uses the dataset CIC-IDS2017, the dataset records the traffic between servers. Benign traffic and cyberattacks.
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
