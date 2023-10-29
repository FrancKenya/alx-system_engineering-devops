Specifics About This Infrastructure:

Additional Server: Added an extra server for each component (web server, application server, and database server). This approach improves scalability, redundancy, and the overall resilience of the infrastructure.

Load Balancer Cluster: Configuring two HAProxy instances as a cluster ensures high availability. If one HAProxy node fails, the other can continue to balance the incoming traffic, reducing the risk of downtime.

Why Each Element is Added:

Additional Servers: Extra servers are introduced for component isolation, improving fault tolerance and providing the foundation for scaling the infrastructure horizontally. This approach ensures that if one server fails, the others can continue to serve traffic.

Load Balancer Cluster: The cluster provides load balancing to distribute incoming traffic evenly across web servers and application servers, enhancing performance and availability. In a cluster, if one load balancer fails, the other can take over the load-balancing duties.

Issues Addressed:

Redundancy and Fault Tolerance: By adding extra servers for web, application, and database components, the infrastructure is more resilient. Even if one server fails, others are available to maintain service
