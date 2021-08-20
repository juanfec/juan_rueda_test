# juan_rueda_test
 

## General Description

In this repository you will find my solution to the three problems proposed in the technical test

the language chosen was python because of his simplicity to solve algorithms


## A) Overlaps

this function gets two intervals as parameters and returns true if the intervals overlaps false if they dont

in the overlaps root folder you can test it like this 

```bash
python tests.py
```

## B) Versions

this function check to strings that represent version numbers and finds the greatest and returns it, or  'equals' if they are the same version 

in the versions root folder you can test it like this 

```bash
python tests.py
```

## C) Cache

this is a simple implementation of a cache using Redis, about the requirements here is how i solved them:


- `Simplicity`: the implementation is real simple, you just need the host url, the required ttl, the db name and the port used
- `Resilient ` as for the implementation i do recomend seting up the enviroment on AWS Elasticache, here i can set up a Multi Availability Zone with Auto-Failover architecture so a read replica can easily became the main node once the main node fails 
- `Near real time replication of data across Geolocation`, `Data consistency across regions` and `Locality of reference` those three can be implemented using Redis Global Datastore, a service also provided by AWS that allows me to have a implementation distributed across the world with near real time replication (less than 1 second delay replication),  the replication is all handled by the service and the latenci can be monitored, the locality of reference would be managed by the consumers, every cluster has an endpoint so the consumer should always point to the closest service.
  to what ever reason
- `Flexible Schema` Redis is a Key Value data store that allows to have a flexible schema
- `Cache can expire ` Redis has an expire time of its own so it can be easily implemented

This is a simple implementation of Redis, a more robust implementation can be developed having in count business rules, also a more specific architecture can be desinged, but in general i think redis would provide a robust solution for the problem given.

Also for a formal implementation the package should be publish so it can be available to the developers working with the tool.


