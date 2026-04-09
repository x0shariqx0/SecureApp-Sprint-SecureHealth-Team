
Protection Needs Elicitation (PNE) Report

Project: Secure Patient Record & Appointment Portal


1.Introduction:

This Protection Needs Elicitation (PNE) report is for the Secure Patient Record & Appointment Portal project. The goal of this report is to find the system's valuable assets, the threats that could harm them, and the security measures that are needed to keep the application safe. The system needs strong security to keep unauthorised users from getting in, leaking data, and using it in ways that aren't allowed because it handles private patient records, appointment information, doctor details, and user credentials.

2.System Overview:

The Secure Patient Record & Appointment Portal is a web-based tool that helps keep patient medical records and appointment scheduling safe. Patients, doctors, and administrators should all be able to use the system. Patients can sign up, log in, see their own information, and make appointments. Doctors can look at the medical history of assigned patients, update treatment-related information, and look at their records. Administrators can keep an eye on the portal's overall operation, manage users, and keep an eye on appointments. Security is very important because the system stores and processes private health information.

3.Stakeholders:

a.Patients: who use the portal to view their information and manage appointments.

b.Doctors: who access patient records and update medical details.

c.Administrators: who manage users, appointments, and system operations.

d.Hospital or Clinic Management: who depend on the system for secure and reliable healthcare service delivery.

e.Development and Security Team: responsible for maintaining, updating, and securing the system.


4.Assets Identification:
| Asset | Description | Importance |
|---|---|---|
| Patient Personal Data | Includes patient name, age, gender, contact details, and profile information | Sensitive personal information that must remain private |
| Patient Medical Records | Includes diagnosis, prescriptions, treatment history, test results, and medical notes | Highly confidential healthcare data |
| Appointment Data | Includes booking details, doctor assignment, dates, and appointment status | Important for service continuity and scheduling |
| Doctor Information | Includes doctor profiles, specialization, availability, and assigned appointments | Necessary for operational use of the portal |
| User Credentials | Includes email addresses, usernames, and passwords | Critical for secure authentication |
| Session Tokens | Used to maintain logged-in user sessions | Can allow unauthorized access if stolen |
| Audit Logs | Record user actions such as login, updates, and booking activity | Important for accountability and monitoring |
| Backend Database | Stores all patient, doctor, and appointment data | Core system asset containing sensitive information |
| Web Application and API | The portal interface and backend services used by all users | Main platform through which the system operates |


5.Threat Identification:
| Threat | Affected Asset | Possible Impact |
|---|---|---|
| Unauthorized Access | Patient records, doctor data, appointments | Sensitive data may be viewed by unauthorized users |
| Data Leakage | Patient personal data and medical records | Private healthcare information may be exposed |
| Data Tampering | Medical records, appointment data | Incorrect or malicious changes may affect treatment or scheduling |
| Credential Theft | User credentials | Attackers may log in as valid users |
| Session Hijacking | Session tokens | Attackers may take over active user sessions |
| Privilege Escalation | Admin and doctor functions | A low-level user may gain higher-level access |
| Insider Misuse | All sensitive data | Authorized users may misuse the system intentionally |
| Repudiation | Audit logs and update history | Users may deny actions if proper logs are not maintained |
| Service Disruption | Portal, API, database | Users may be unable to access records or appointments |
| Malicious Request Manipulation | Records and appointment endpoints | Attackers may abuse weak request validation to access or modify data improperly |


6.Protection Needs:

The following protection needs are derived from the sensitivity of healthcare data and the identified threats.
| Protection Need | Description |
|---|---|
| Authentication | Only valid users should be able to log in and access the system |
| Authorization | Users should only access the data and functions permitted by their role |
| Confidentiality | Sensitive patient and doctor information must be protected from unauthorized disclosure |
| Integrity | Patient records and appointment data must not be changed without authorization |
| Availability | The system should remain accessible for legitimate users when needed |
| Session Security | Session tokens must be protected to prevent hijacking or replay attacks |
| Secure Credential Storage | Passwords should be securely stored using hashing mechanisms |
| Audit Logging | Important user actions should be recorded for monitoring and accountability |
| Input Validation | All user input should be validated to reduce abuse and malicious manipulation |
| Secure Communication | Data should be transmitted securely between client and server |


7.Security Assumptions:

i.The portal is a web-based application accessed through standard web browsers.

ii.Patients, doctors, and administrators have separate roles in the system.

iii.Sensitive data is stored in a backend database.

iv.Users must authenticate before accessing protected resources.

v.The system exchanges data between frontend and backend through controlled application requests.

vi.The portal is expected to handle confidential healthcare-related information and therefore requires stronger protection than ordinary public applications.


8.Conclusion:

The Secure Patient Record & Appointment Portal keeps track of very private information about patients, doctors, and appointments. So, system assets need to be well protected from threats like unauthorised access, data leaks, tampering, credential theft, and session misuse. This PNE report listed the system's most important assets, biggest threats, and protection needs. These are the things that should guide the system's safe design and implementation.
