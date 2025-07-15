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
- Date: **June 15, 2025**
- Version: **0.1**
- Include Oracle's standard **Confidentiality Disclaimer**: 
"This document contains confidential information and is intended only for authorized personnel. Distribution or disclosure to unauthorized parties is strictly prohibited."


# 2. SoW Version History Table
| Version # | Date       | Revised By          | Description of Change              |
|-----------|------------|---------------------|------------------------------------|
| 0.1       | 2025-06-15 | Oracle Team         | Initial version                    |


# 3. Status and NEXT STEPS
- Current project status: *In Progress*
- Next 3 actions required:
  1. **Owner: Oracle**, Description: Complete Terraform scripts for OCI environment setup.
  2. **Owner: Tecnotree**, Description: Provide detailed application architecture and existing infrastructure diagrams.
  3. **Owner: Joint**, Description: Schedule weekly progress check-ins to ensure alignment and address potential issues.


# 4. Project Participants Table


 Oracle Team
| Name            | Role                  | Email                 |
|-----------------|-----------------------|-----------------------|
| Heikki Ridanpaa | Account Cloud Engineer| heikki.ridanpaa@oracle.com |
| Maria Solvsteen | Sales Representative  | maria.solvsteen@oracle.com |
| Marc Torné      | Cloud Solution Architect| marc.torne@oracle.com    |
| Laura Taunasescu| Service Delivery Manager| laura.taunasescu@oracle.com |



 Tecnotree Team
| Name            | Role                  | Email                 |
|-----------------|-----------------------|-----------------------|
| Markus Kivilä   | Senior Enterprise Architect | markus.kivila@tecnotree.com |
| Suhail Thusu    | Director – Technology Alliances | suhail.thusu@tecnotree.com |
| Hannu Vuori     | Enterprise Architect  | hannu.vuori@tecnotree.com  |


# 5. Project Framework
This section outlines the working model, shared responsibilities, deliverables, and infrastructure requirements for the validation project between Oracle ISV Labs and **Tecnotree**. The engagement is focused on the application validation stage only and does not include production workloads.



 5.1 Objective and Scope  
The goal of this collaboration is to validate the **Digital BSS Solution** on Oracle Cloud Infrastructure (OCI), assess its compatibility, and define a target architecture. Oracle ISV Labs will provide deployment tooling, infrastructure recommendations, and technical guidance during this process.  
**Note:** No intellectual property will be transferred during the engagement.



 5.2 Collaboration Model  
Both Oracle and **Tecnotree** will actively participate throughout the engagement. Clear communication channels and shared ownership will be established to ensure progress and alignment.

- The project will formally begin upon sign-off of the Statement of Work (SoW).
- Status updates will be shared on a regular basis to ensure that timelines and dependencies are met.



 5.3 Responsibility Domains  
Responsibility for document inputs and project actions will be clearly delineated:

- **Oracle (Tan areas)**: Provides architectural guidance, Terraform automation, and technical documentation.
- **Tecnotree (Green areas)**: Supplies required architecture diagrams, technical points of contact, and necessary environment access.



 5.4 Feedback and Communication  
Continuous communication and iterative validation are key to the success of this engagement. Oracle and **Tecnotree** will maintain feedback loops via:

- Weekly progress check-ins
- Shared tracking documents (status reports, action logs)
- Direct communication (email, messaging platforms)



 5.5 Estimated Timeline  
The standard validation window is expected to last **2 to 3 weeks**, provided that the required resources and inputs are delivered on time by **Tecnotree**.



 5.6 Required Contribution from Tecnotree  
To support the validation effort, **Tecnotree** is expected to provide the following:

- **Technical Points of Contact**: Engineers or architects who can support OCI validation efforts.
- **Existing Architecture Documentation**: Including current infrastructure diagrams, integration details, and system specs.
- **Environment Access**: Credentials or role-based access to development or testing environments needed for OCI provisioning and testing.



 5.7 Expected Deliverables from Oracle ISV Labs  
Oracle ISV Labs will provide a standard set of outputs to support OCI adoption:

- **Terraform Modules**: Infrastructure-as-code templates to replicate the target environment on OCI.
- **Target Architecture**: OCI-aligned architecture diagrams and deployment topologies.
- **Technical Documentation**: Guidance on best practices, assumptions, and recommended next steps.
- **CI/CD Examples (if applicable)**: Samples or recommendations for integrating OCI into existing pipelines.


# 9. Tecnotree Company Profile
- Legal Name: Tecnotree Corporation
- Country of Operations: Finland
- Company Overview: Tecnotree is a global provider of IT solutions for the telecom industry, offering digital transformation solutions for telecom operators.
- Website link: [www.tecnotree.com](http://www.tecnotree.com)


# 10. In-Scope Application: Digital BSS Solution Validation
- Application Name: Digital BSS Solution
- General Description: A comprehensive suite of telecom business support systems.
- Key Technologies: Kubernetes, Docker, Java, Oracle Database.
- Current Hosting: On-premises data centers.


# 11. Project Overview
- **Validation Summary**: Validation of Tecnotree’s Digital BSS Solution on Oracle Cloud Infrastructure (OCI) using a Lift & Shift approach. The goal is to assess the compatibility of the existing containerized application architecture (Kubernetes, OKE) with OCI’s managed services, including database, storage, networking, and security.
- **Project Dates**:
  - Kick-off Version Date: June 1, 2025
  - Latest Update / Current Version: June 15, 2025
  - Estimated Project Duration: 2–3 weeks
- **Project Team**:
  - Oracle Team: Heikki Ridanpaa, Maria Solvsteen, Marc Torné, Laura Taunasescu
  - Tecnotree Team: Markus Kivilä, Suhail Thusu, Hannu Vuori
- Desired outcome: Successfully validate the Digital BSS Solution on OCI, ensuring compatibility, performance, and scalability.
- Scope boundaries: The validation will focus on the application’s core functionalities and will not include custom or third-party integrations.
- Joint goals: Achieve a smooth lift-and-shift migration, ensure high availability, and define a cost-effective OCI architecture.


# 12. Scope
- **In-Scope Items**: OKE deployment, Terraform automation, MySQL Database Service setup, OCI Streaming integration, security and networking configuration.
- **Out-of-Scope Items**: Production migration, custom application development, licensing and support agreements.
- Validation boundaries and limitations: The validation will be conducted in a controlled environment and will not impact production systems.


# 13. Major Project Milestones
| Milestone                         | Target Date | Completed | Comments                 |
|----------------------------------|-------------|-----------|--------------------------|
| Kickoff with Cloud Architect     | 2025-06-01  |           |                          |
| OCI Network Setup                | 2025-06-05  |           |                          |
| Terraform Code Finalization      | 2025-06-10  |           |                          |
| Application Deployment in OCI    | 2025-06-12  |           |                          |
| Final Validation & Review        | 2025-06-20  |           |                          |


# 14. Acceptance Criteria
| Capability/Metric                                | Acceptance Criteria                                                       | Status  |
|--------------------------------------------------|----------------------------------------------------------------------------|---------|
| Kubernetes Deployment                            | Digital BSS Solution Validation runs successfully on OCI OKE                 | TBD     |
| OCI Streaming                                     | Kafka integration tested using OSS workloads                              | TBD     |
| MySQL Database Service                            | DB deployed, configured, accessible                                       | TBD     |
| Monitoring                                        | Basic metrics visible in OCI Monitoring dashboard                         | TBD     |
| Security                                          | IAM + NSG + Encryption in Transit & At Rest                               | TBD     |


# 15. Current State Architecture
- **Diagram Description**: The current setup consists of on-premises data centers hosting the Digital BSS Solution on a Kubernetes cluster, with Oracle Database, and integrated with various telecom systems.
- **Tech Stack**: Docker, Kubernetes, Java, Oracle Database, Jenkins.
- **Known Issues/Pain Points**: Manual deployment processes, limited scalability, and high maintenance costs.


# 16. Target OCI Architecture
The target architecture will utilize the following OCI services:
- **Compute**: E5 shapes for VMs, with OCPUs and memory optimized for the application.
- **OKE (Oracle Kubernetes Engine)**: For container orchestration and management.
- **Block Storage**: For persistent storage needs.
- **File Storage**: For shared file systems.
- **Load Balancer**: For traffic distribution and high availability.
- **WAF**: For web application security.
- **OCI Cache**: For caching and performance optimization.
- **MySQL Database Service**: For relational database needs.
- **OCI Streaming**: For event-driven architecture and real-time data processing.
- **Container Registry**: For container image management.
- **Bastion**: For secure access to the OCI environment.
- **VPN**: For secure connectivity to the on-premises environment.
- **VCN**: For virtual networking and subnet management.
- **IAM**: For identity and access management.


# 17. Implementation Details and Configuration Settings


 1. Networking
- VCN design: A single VCN with multiple subnets for different application components.
- CIDRs: 10.0.0.0/16 for the VCN, with subnets divided accordingly.
- Internet/NAT Gateways: Used for outbound internet access.
- Local Peering Gateways (LPGs): Used for connecting to other VCNs in the same region.
- Route tables, security lists, NSGs: Configured for secure traffic flow and access control.



 2. Compute
- VM shapes and OCPUs/memory: E5 shapes with optimized OCPUs and memory for the application.
- OS and images used: Oracle Linux, with custom images for the application.
- Bastion/jump hosts: Used for secure access to the OCI environment.
- GPU instances: Not required for this application.



 3. Storage
- Block Volumes: Used for persistent storage needs.
- Object Storage: Used for storing and serving static assets.
- Boot volume size and configuration: Optimized for the application’s requirements.



 4. Container Services
- OKE deployment process: Using Terraform for automated deployment.
- Integration with OCI: Using Oracle Cloud Infrastructure APIs for integration.



 5. IAM & Security
- Compartments: Used for organizing and managing OCI resources.
- IAM policies: Created for access control and permission management.
- Use of resource tags: For categorizing and tracking OCI resources.
- Access control via NSGs or Security Lists: Configured for secure traffic flow.



 6. Deployment Automation
- Terraform/Resource Manager usage: Used for automated deployment and management of OCI resources.
- CLI or Console steps: Used for manual configuration and troubleshooting.


# 18. Security Considerations
- IAM Policy examples: Policies created for access control and permission management.
- NSG configuration: Configured for secure traffic flow and access control.
- Data encryption approach: Using OCI’s encryption services for data at rest and in transit.
- Audit logs or Logging Analytics setup: Configured for monitoring and logging.


# 19. High Availability & Disaster Recovery
High Availability (HA) and Disaster Recovery (DR) are crucial for ensuring the continuous operation of the Digital BSS Solution on OCI. The main principles for HA in OCI include distributing resources across multiple Availability Domains (ADs) or Fault Domains (FDs) and using managed services that provide built-in HA capabilities.

For the Digital BSS Solution, HA will be achieved through:
- **OKE**: Using Node Pools distributed across multiple ADs to ensure resilience against hardware or AD failures.
- **MySQL Database Service**: Utilizing standby databases and replicas for high availability.
- **OCI Streaming**: Configuring streams for high availability and durability.

Disaster Recovery will focus on:
- **Cross-region replication**: For Object Storage and other data storage services.
- **Regular backups**: Of databases and critical data.
- **DR strategy summary**: The architecture will be designed to recover from regional failures, with a recovery time objective (RTO) of 4 hours and a recovery point objective (RPO) of 1 hour.


# 20. Closing Feedback
- Placeholder for feedback from Oracle and Tecnotree.


# 21. Sign-Off Section
- Client Acceptance: Tecnotree accepts the Statement of Work as outlined.
- Oracle Confirmation: Oracle confirms the acceptance and agrees to proceed with the project.
- Final next steps: Schedule a project kickoff meeting and begin the validation process.
- Version tagging: This document will be version-controlled, with changes tracked and approved by both parties.
---

