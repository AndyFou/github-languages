# Github Network Analysis on Greek Users

![Language Graph](graph.png)
Format: ![Alt Text](url)

## Description
This is a university project about the analysis of the languages used by the github community and some sub-communities discriminated by location.

## Data
500 users since the beginning of Github & ~150000 users from 2012 to 2013 (narrowed down to ~40.000 that stated their location)

## Procedure
Collection of locations (as giver by the user), languages (of user's public repos) & other features (nof public_repos, nof followers)
* modelling languages (connections via users (pairs of languages)) & detect communities using association rules
* applying the same on some particular locations (UK, USA - SF, Australia, Germany, Brazil, Greece) - ίσως τα τοπ μερη; ή οι μεγαλύτερες/πολυπληθέστερες χώρες στον κόσμο; - ίσως αναλογικά αυτό
* applying the same only for highly influential users (meaning with many followers and/or many public_repos)

## Challenges
* locations issues: empty loc, not all same structure, some are not real, special characters not recognized by encoding (ex mxico, so paolo/paulo, zrich, montral, malm, florianpolis,dsseldorf)
* languages issues: access denied on repositories, only public repos (no forks or private)

## Ideas
* Get lang graph for locations
* Get lang graph for influential users
* Association Rules for Community Detection
* Get graph of users: nodes-users edges-common langs

* Get top countries for developers by a source (eg http://goo.gl/vBF6BE or https://goo.gl/bwxcoZ)

**Descriptive Statistics**
users per location (top pie / top barchart), langs and bytes  

### Notes
* το cluster του web το βγαζει πολυ καλα σε σχεση με αλλα (λογικο απο τη φυση των δεδομενων, το github παιζει πολυ με web devs)
* results-loc: some places have too many users (SF) and most have too little (powerlaw)

#### Dependencies
* [PyGithub](https://github.com/PyGithub/PyGithub) (pip install PiGithub) 
