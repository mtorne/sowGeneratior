# Oracle Cloud Infrastructure - Application Validation

**ISV:** None  
**Application:** None  
**Statement of Work**  
**Date:** None  
**Version:** None

---

## Disclaimer

 This document, in any form, software or printed matter, contains proprietary information that is the exclusive property of Oracle. Your access to and use of this confidential material is subject to the terms and conditions of the Non-Disclosure Agreement between RedThorn and Oracle Corp. This document and information contained herein may not be disclosed, copied, reproduced, or distributed to anyone outside Oracle without prior written consent of Oracle. This document is not part of your license or services agreement nor can it be incorporated into any contractual agreement with Oracle or its subsidiaries or affiliates.
This document is for informational purposes only and is intended solely to assist you in evaluating the Oracle IaaS and/or Paas Public Cloud Services in a non-production context. It is not a commitment to deliver any material, code, or functionality, and should not be relied upon in making purchasing decisions. The development, release, and timing of any features or functionality described for Oracle products and services  remains at the sole discretion of Oracle.
The outcome of Oracle ISV Labs is to enable Redthorn OCI as outlined in this SOW, including any open source-based terraforms and tools/procedures, and it would be available to RedThorn to use freely with no restrictions or time limits and regardless of any NDA obligations.


---

## Contents
1. [Version History](#version-history)
2. [Current Status and Next Steps](#current-status-and-next-steps)
3. [Project Participants](#project-participants)
4. [Project Summary](#project-summary)
5. [Current Architecture](#current-architecture)
6. [Target Architecture](#target-architecture)
7. [Implementation Details](#implementation-details)
8. [Closing Remarks](#closing-remarks)

---


## Introduction


# 1. Document Header
- ISV: **Tecnotree**
- Application: **Digital BSS Solution Validation**
- Type: **Statement of Work**
- Date: **2025-06-04**
- Version: **0.1**
- Include Oracle's standard **Confidentiality Disclaimer**: This document contains confidential information and is protected by copyright. It is intended only for the use of the parties involved and should not be disclosed to any third party without prior written consent.

---


# 2. SoW Version History Table
| Version # | Date       | Revised By          | Description of Change                             |
|-----------|------------|---------------------|---------------------------------------------------|
| 0.1       | 2025-06-04 | Initial Creator     | Initial version of the Statement of Work document |

---


# 3. Status and NEXT STEPS
- Current project status: *In Progress*
- Next 3 actions required:
  1. **Owner**: Oracle Team, **Description**: Completion of OCI network setup.
  2. **Owner**: Tecnotree Team, **Description**: Provision of technical resources and access to the development environment.
  3. **Owner**: Joint, **Description**: Review of the target architecture and feedback incorporation.

---


# 4. Project Participants Table


 Oracle Team
| Name              | Role                   | Email                  |
|-------------------|------------------------|------------------------|
| Heikki Ridanpaa   | Account Cloud Engineer | heikki.ridanpaa@oracle.com |
| Maria Solvsteen   | Sales Representative   | maria.solvsteen@oracle.com  |
| Marc Torné        | Cloud Solution Architect | marc.torne@oracle.com      |
| Laura Taunasescu  | Service Delivery Manager | laura.taunasescu@oracle.com |



 Client (Tecnotree) Team
| Name              | Role                   | Email                  |
|-------------------|------------------------|------------------------|
| Markus Kivilä     | Senior Enterprise Architect | markus.kivila@tecnotree.com |
| Suhail Thusu      | Director – Technology Alliances | suhail.thusu@tecnotree.com  |
| Hannu Vuori       | Enterprise Architect   | hannu.vuori@tecnotree.com    |

---


# 5. Project Framework
The collaboration between Oracle and Tecnotree will involve regular meetings and feedback loops to ensure the successful validation of the Digital BSS Solution on Oracle Cloud Infrastructure (OCI). The expected validation duration is approximately 2-3 weeks. Key areas of responsibility include:
- Oracle: Provision of OCI services, technical guidance, and best practices.
- Tecnotree: Provision of application details, technical resources, and feedback on the validation process.

---


# 6. Required Contribution From Client
Tecnotree must provide:
- Technical resources for the application.
- Diagrams or architectural artifacts of the current setup.
- Access to the development/test environment for validation purposes.

---


# 7. Expected Deliverables From Oracle ISV Labs
Oracle expects to deliver:
- Terraform modules for the target architecture.
- A detailed target architecture document outlining the use of OCI services.
- Technical documentation on the setup and configuration of the environment.
- Examples of CI/CD integration using OCI services.

---


# 8. Cloud Environment Used
The Proof of Concept (PoC) will run in a temporary test tenancy provided by Oracle.

---


# 9. Tecnotree Company Profile
- Legal Name: Tecnotree Corporation
- Country of Operations: Finland
- Company Overview: Tecnotree is a global provider of IT solutions for the telecom industry, offering a range of products and services that enable telecom operators to manage their businesses more efficiently.
- Website link: [www.tecnotree.com](http://www.tecnotree.com)

---


# 10. In-Scope Application: Digital BSS Solution Validation
- Application Name: Digital BSS Solution
- General Description: A business support system solution for telecom operators.
- Key Technologies: Containerized application using Kubernetes, MySQL Database Service, MongoDB, and Cassandra for data storage.
- Current Hosting: On-premises, with plans to migrate to a public cloud for scalability and cost efficiency.

---


# 11. Project Overview
**Validation Summary**: The goal of this project is to validate Tecnotree’s Digital BSS Solution on Oracle Cloud Infrastructure (OCI) using a lift-and-shift approach. The validation will assess the compatibility of the existing containerized application architecture with OCI’s managed services, including database, storage, networking, and security.
- **Project Dates**:
  - Kick-off Version Date: May 28, 2025
  - Latest Update / Current Version: June 4, 2025
  - Estimated Project Duration: 2–3 weeks
- **Desired Outcome**: Successfully validate the Digital BSS Solution in a replicated, containerized environment on OCI, ensuring functional compatibility, performance within latency requirements, and readiness for future automation or cloud-native enhancements.
- **Scope Boundaries**: The validation will focus on the lift-and-shift of the Digital BSS Solution to OCI, using managed services where applicable.
- **Joint Goals**: Oracle and Tecnotree aim to demonstrate that OCI can reliably host Tecnotree’s containerized workloads, meeting customer requirements for performance, scalability, and connectivity.

---


# 12. Scope
- **In-Scope Items**:
  - PostgreSQL setup for database needs.
  - Streaming configuration using OCI Streaming.
  - OKE deployment for container orchestration.
- **Out-of-Scope Items**:
  - Production migration.
  - Licensing setup.
  - SLA support.
- Validation boundaries and limitations will be defined based on the application’s requirements and OCI service capabilities.

---


# 13. Major Project Milestones
| Milestone                         | Target Date | Completed | Comments                 |
|----------------------------------|-------------|-----------|--------------------------|
| Kickoff with Cloud Architect     | 2025-05-28  |           |                          |
| OCI Network Setup                | 2025-06-01  |           |                          |
| Terraform Code Finalization      | 2025-06-08  |           |                          |
| Application Deployment in OCI    | 2025-06-12  |           |                          |
| Final Validation & Review        | 2025-06-18  |           |                          |

---


# 14. Acceptance Criteria
| Capability/Metric                                | Acceptance Criteria                                                       | Status  |
|--------------------------------------------------|----------------------------------------------------------------------------|---------|
| Kubernetes Deployment                            | Digital BSS Solution Validation runs successfully on OCI OKE                 | TBD     |
| OCI Streaming                                     | Kafka integration tested using OSS workloads                              | TBD     |
| PostgreSQL                                        | DB deployed, configured, accessible                                       | TBD     |
| Monitoring                                        | Basic metrics visible in OCI Monitoring dashboard                         | TBD     |
| Security                                          | IAM + NSG + Encryption in Transit & At Rest                               | TBD     |

---


# 15. Current State Architecture
- **Diagram Description**: The current setup involves a Kubernetes cluster, PostgreSQL database, and streaming services.
- **Tech Stack**: Docker, Helm, PostgreSQL, Java.
- **Known Issues/Pain Points**: Manual deployments, scaling issues.

---


# 16. Target OCI Architecture
The target architecture will utilize the following OCI services:
- **Compute**: For VMs and container instances.
- **OKE (Oracle Kubernetes Engine)**: For container orchestration.
- **Block Storage**: For persistent storage needs.
- **File Storage**: For shared file systems.
- **Load Balancer**: For traffic distribution.
- **WAF**: For web application security.
- **OCI Cache**: For caching frequently accessed data.
- **MySQL Database Service**: For relational database needs.
- **MongoDB**: For NoSQL database requirements.
- **Cassandra**: For distributed database needs.
- **OCI Streaming**: For streaming data processing.
- **Container Registry**: For container image management.
- **Bastion**: For secure access to instances.
- **VPN**: For secure network connections.
- **VCN**: For virtual networking.
- **IAM**: For identity and access management.


 Service Mapping
| Current Service | OCI Service      |
|-----------------|------------------|
| Kubernetes      | OKE              |
| PostgreSQL      | MySQL Database Service |
| Streaming       | OCI Streaming    |


 Component Interaction
The components will interact through APIs and service endpoints.


 Diagram Placeholder
A detailed architecture diagram will be provided, showing the interaction between services.

---


# 17. Implementation Details and Configuration Settings


 1. Networking
- VCN design: A single VCN with multiple subnets for different tiers.
- CIDRs: 10.0.0.0/16 for the VCN.
- Subnets: Three subnets for web, application, and database tiers.
- Internet/NAT Gateways: One internet gateway for outgoing traffic.
- Service Gateways: Used for accessing OCI services.
- Local Peering Gateways (LPGs): Not used in this scenario.
- Route tables, security lists, NSGs: Configured for secure access and routing.



 2. Compute
- VM shapes and OCPUs/memory: E5 shapes with 2 OCPUs and 16 GB memory.
- OS and images used: Oracle Linux 8.
- Bastion/jump hosts: Used for secure access to instances.
- GPU instances: Not used in this scenario.



 3. Storage
- Block Volumes: Used for persistent storage.
- Object Storage: Used for storing and serving files.
- Boot volume size and configuration: 50 GB boot volume.



 4. Container Services
- OpenShift OCP deployment process: Using the assisted installer.
- Integration with OCI: Via resource manager and object storage.



 5. IAM & Security
- Compartments: Used for organizing resources.
- IAM policies: Configured for access control.
- Use of resource tags: For tracking and organizing resources.
- Access control via NSGs or Security Lists: Configured for secure access.



 6. Deployment Automation
- Terraform/Resource Manager usage: Terraform used for infrastructure as code.
- CLI or Console steps: Used for manual tasks and verification.

---


# 18. Security Considerations
- IAM Policy examples: Policies for access control and resource management.
- NSG configuration: Configured for secure access and routing.
- Data encryption approach: Encryption in transit and at rest.
- Audit logs or Logging Analytics setup: Used for monitoring and auditing.

---


# 19. High Availability & Disaster Recovery
The main principles for High Availability (HA) in OCI involve distributing resources across multiple Availability Domains (ADs) to ensure resilience against hardware or AD failures. Additionally, using managed services that inherently provide HA, such as Autonomous Database, simplifies the achievement of high availability.

For the Digital BSS Solution, HA will be achieved through:
- **OKE**: Node pools distributed across multiple ADs.
- **Database Services**: Using MySQL Database Service with standby databases for HA.
- **OCI Streaming**: Configured for high availability and durability.
- **Object Storage**: Used for storing and serving files, with cross-region replication for DR.
- **Networking & DNS**: Traffic Management policies in OCI DNS for active-active or active-passive failover scenarios.
- **Backup & Restore**: Regular backups of critical data, with a recovery time objective (RTO) of 4 hours and a recovery point objective (RPO) of 1 hour.
- **DR Strategy Summary**: The architecture is designed to fail over to a different region in case of a regional failure, with a recovery time expectation of 4 hours.

---


# 20. Closing Feedback
Placeholder for feedback from Oracle and Tecnotree.

---


# 21. Sign-Off Section
- Client Acceptance: _______________________
- Oracle Confirmation: _______________________
- Final next steps: Review and finalize the target architecture.
- Version tagging: This document is version 0.1, dated June 4, 2025.
---

