# Secure Centralized Access System for Web Services with KDC
This project implements a Kerberos authentication system with Django, providing secure access control and ticket-based authentication for network services.

## Used Technologies:
> Python | Django | SQLite
## Main Subprojects:

- **KDC** - Represents the **Key Distribution Center (KDC)** system, responsible for ticket issuance.
- **Client** - Simulates the sending and receiving of messages by a service client.
- **Bus Kerberos** - Contains project-related files.

## KDC
The **KDC subproject** implements the logic for managing keys and tickets. It processes messages from the server and the client, analyzing incoming data, encrypting/decrypting it, and ultimately comparing it against database records.
## System Operation
To start the system, run the following command:

```bash
python manage.py runserver
```

Once the server is running, navigate to `127.0.0.1:8000/` in your web browser. You will be redirected to the login page, which contains fields for:

- **Username**
- **Password** 

## Authentication & Registration

- If the user does not exist, they can register through the registration page. The registration form requires the following information:
  - First Name
  - Last Name
  - Username
  - Password (hidden for security)

## Unauthorized Access

Attempts to access protected pages directly through the URL bar without authentication will fail, resulting in an error message.
If incorrect login credentials are provided, authentication will be denied.

## Ticket-Based Access
After a successful login, the user is redirected to the main page, which serves as a hub with links to available services. When clicking on a service link:

- The system issues a ticket.
- The ticket authenticates the user and server.
- The system verifies the connection.
- If validation is successful, the user is redirected to the service page.

## Ticket Expiry
Access to services is granted for a limited time, as defined by the timestamp attribute in the ticket. When the ticket expires, the client must re-authenticate using their password to obtain a new ticket.

## Sources:
 * http://web.mit.edu/kerberos/
 * https://www.ibm.com/docs/en/was-nd/8.5.5?topic=token-kerberos-usage-overview-web-services
 * https://docs.oracle.com/middleware/12212/owsm/concepts/GUID-199F1431-96C5-4765-8BC7-1F7C050DA2C0.htm#OWSMC2342
 * https://siddhivinayak-sk.medium.com/kerberos-based-user-authentication-and-sso-in-web-application-2d3f2a8c6bd1
