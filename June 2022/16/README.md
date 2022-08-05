# Check for Flights

In a country with ‘n’ cities, flight services are provided from some cities to
certain cities only. The presence of flight service is represented by a directed
graph as shown below. According to this graph, there are three flight services
from city 1 to city 2, city 3 and city 4. There is no flight service from city 6.

![route](./pic.jpeg)

Given the flight services available in a country and a source city ‘s’ and a
destination city ‘d’, write a C++ code to check if a person from city ‘s’ can reach
city ‘d’ using the flight services. If the person can reach then print 'Yes' and Print
‘No’ otherwise.

For example, if ‘s’ is 1 and ‘d’ is 6 then print Yes and if ‘s’ is 5 and d is 1 then
print No

#### Note:

The graph formed by the flight services is acyclic

#### Hint

One of the idea to solve the problem is using the concept of Breadth First
Search (BFS) of graphs. The steps involved using a queue are as follows:

1. Put the start city, s into a queue q
2. Repeat step 3 till either the queue becomes empty or destination city is found
3. Remove a city ‘c’ from q, if ‘c’ is ‘d’ then print Yes and stop otherwise find all
cities that can be reached from c and put it inside the queue

Vectors, map and queue of STL can be used to quickly solve this problem.
Queue is a data structure in which the element that is inserted first into the
queue is removed first.

To create a queue in STL `#include<queue>` and give as `queue<int> q;` to create
a queue of integers

Operations in queue of STL are

1. Push (e) – insert e into a queue at the end
2. front() - returns the first element in the queue
3. pop() - Remove the element in the front of the queue
4. Empty – Return true or false indicating if the queue is empty or not

#### Input Format

First line contains the number of cities in the country, n

Next ‘n’ lines contain the detail of flights to cities, each field in a line is
separated by a space. First field is the city name ‘c’, next is the number of cities
to which flight service is present from ‘c’, followed by the city names to which
flight service is from ‘c’

Next line contain the source city name from which the person wants to travel, s

Next line contain the destination city name to which the person wants to travel,
d

#### Output Format

Print Yes if there exists connecting flights between s and d and No otherwise