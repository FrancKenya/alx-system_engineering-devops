**Title**
Postmortem: Debugging Project "0x12. Web Stack Debugging #2"

Date
June 14, 2024

**Incident Description**
This project involved addressing critical security and configuration issues in a web stack. The primary focus was on preventing unauthorized root access and ensuring Nginx runs under a non-root user.

**Impact**
Service Impact: Nginx service was potentially disrupted.
User Experience: Users experienced intermittent access issues and potential downtime.
Percentage Affected: Approximately 100% of the users were unable to access the page due to incorrect Nginx configurations.

**Duration of Outage**
Start Time: June 13, 2024, 14:00 EAT
End Time: June 13, 2024, 16:00 EAT

**Timeline**
14:00 EAT
: Issue detected via monitoring alerts indicating abnormal root access and Nginx process anomalies.
14:05 EAT
: On-call engineer received alert and began investigation.
14:15 EAT
: Initial diagnosis pointed to root login and Nginx running as root.
14:30 EAT
: Assumed root cause was improper user permissions.
14:45 EAT
: Investigation revealed incorrect Nginx configuration.
15:00 EAT
: Scripts developed to change root logging and configure Nginx.
15:30 EAT
: Misleading path explored by checking unrelated network configurations.
15:45 EAT
: Escalated to senior engineer for further analysis.
16:00 EAT
: Resolution implemented, Nginx reconfigured to run as nginx user.

**Root Cause**
Detailed Cause: The root cause was a misconfigured Nginx setup running under the root user, which posed security risks and led to process management issues. Additionally, improper user permissions allowed unrestricted root access.

**Resolution**
Detailed Fix: Developed Bash scripts to:
Reassign processes on port 80 and reassign any listening to another port.
Restart Nginx and ensure it runs under the nginx user.
Enabled UFW to restrict Nginx to port 80.
Adjusted file permissions to restrict access.
Corrective and Preventative Measures

**Improvements/Fixes:**
Enhanced user permission management.
Improved configuration testing and monitoring.
Regular audits of server configurations.

**Tasks:**
Patch Nginx server to prevent running as root.
Add monitoring on server memory and process management.
Develop and enforce a comprehensive testing protocol for configuration changes.
Conduct training sessions on user management and security best practices.

**Participants**
Lead Debugger: FRANCIS WAIHIGA
Team Members: JOHN WAMBUA, DAVID MUTISO
Reviewed By: [Supervisor/Manager's Name]