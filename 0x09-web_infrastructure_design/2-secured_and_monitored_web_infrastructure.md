Specifics About This Infrastructure:

Firewalls: Firewalls are added for security. They control and monitor incoming and outgoing network traffic, providing an additional layer of protection for the infrastructure.

HTTPS intercepts are encrypted and cannot be read

SSL Termination: Terminating SSL at the Load Balancer is more efficient because it reduces the processing load on individual web and application servers, making it easier to manage SSL certificates.

Monitoring: Monitoring is used to track the performance, security, and health of the infrastructure. Monitoring tools collect data about server and application performance, security threats, and more.

Monitoring Data Collection: Monitoring tools collect data through agents or clients installed on servers. The data collected may include server performance metrics, logs, security events, and more.

Monitoring QPS: To monitor web server query per second (QPS), you'd configure your monitoring tool to track the number of incoming requests to the web servers. If the QPS exceeds a specified threshold, it triggeSr alerts.

Issues with This Infrastructure:

Terminating SSL at the Load Balancer: While efficient, terminating SSL at the Load Balancer means that traffic between the Load Balancer and web servers is unencrypted. If the internal network is not secure, this could be a vulnerability.

Single MySQL Server Accepting Writes: Relying on a single MySQL server for write operations creates a single point of failure. If that server becomes unavailable, it can lead to data loss or service disruption.

Homogeneous Servers: Using servers with the same components (database, web server, and application server) may result in a lack of redundancy. A failure in one component can affect all servers, potentially causing downtime.
