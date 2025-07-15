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


1. Document Header
- **ISV**: Tecnotree
- **Application**: Digital BSS Solution Validation
- **Type**: Statement of Work
- **Date**: October 10, 2023
- **Version**: 0.1

**Confidentiality Disclaimer**  
This document is confidential and proprietary to Oracle and is provided solely for the purpose of evaluating Oracle Cloud Infrastructure services. It may not be reproduced, distributed, or disclosed to any third party without the prior written consent of Oracle. The information contained herein is subject to change without notice and is not warranted to be error-free. Oracle assumes no responsibility or liability for any errors or inaccuracies that may appear in this document.


 2. SoW Version History Table

| Version # | Date          | Revised By       | Description of Change                  |
|-----------|---------------|------------------|----------------------------------------|
| 0.1       | October 10, 2023 | Oracle Cloud Architect | Initial version                        |


 3. Status and NEXT STEPS
- **Current project status**: Planning

**Next 3 actions required**:

| Owner          | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Oracle Team    | Schedule kickoff meeting with Tecnotree to align on scope and contributions. |
| Tecnotree Team | Provide current architecture diagrams and access to dev/test environment.    |
| Joint (Oracle & Tecnotree) | Review and finalize target OCI architecture design.                         |


 4. Project Participants Table

**Oracle Team** (Tan color-coded in original format):

| Name              | Role                     | Email                     |
|-------------------|--------------------------|---------------------------|
| Heikki Ridanpaa   | Account Cloud Engineer   | heikki.ridanpaa@oracle.com|
| Maria Solvsteen   | Sales Representative     | maria.solvsteen@oracle.com|
| Marc Torné        | Cloud Solution Architect | marc.torne@oracle.com     |
| Laura Taunasescu  | Service Delivery Manager | laura.taunasescu@oracle.com|

**Client (Tecnotree) Team** (Green color-coded in original format):

| Name             | Role                        | Email                     |
|------------------|-----------------------------|---------------------------|
| Markus Kivilä    | Senior Enterprise Architect | markus.kivila@tecnotree.com|
| Suhail Thusu     | Director – Technology Alliances | suhail.thusu@tecnotree.com|
| Hannu Vuori      | Enterprise Architect        | hannu.vuori@tecnotree.com |


 5. Project Framework
This Statement of Work outlines a collaborative validation project between Oracle and Tecnotree for the Digital BSS Solution on OCI. Oracle will lead the architecture design, deployment, and validation using OCI best practices, while Tecnotree provides application-specific expertise, artifacts, and testing support.  

- **Responsibility Areas**: Oracle handles OCI infrastructure setup, Terraform automation, and technical guidance. Tecnotree is responsible for application configuration, functional testing, and validation of business logic.  
- **Feedback Loops**: Weekly status meetings for progress reviews, issue resolution, and adjustments. Daily collaboration via shared tools (e.g., email, Slack, or Oracle Cloud Console access).  
- **Expected Validation Duration**: 2-3 weeks, starting from kickoff, assuming timely contributions from both parties.


 6. Required Contribution From Client
Tecnotree must provide the following to ensure successful validation:  
- **Technical Resources**: Dedicated personnel (e.g., architects and developers) for collaboration, including access to SMEs for application troubleshooting.  
- **Diagrams or Architectural Artifacts**: Current state architecture diagrams, container manifests (e.g., Helm charts), database schemas, and network topology.  
- **Access to Dev/Test Environment**: Credentials or VPN access to on-prem or existing cloud setups for replication; sample data sets for testing; and application binaries or Docker images for deployment.


 7. Expected Deliverables From Oracle ISV Labs
Oracle will deliver:  
- **Terraform Modules**: Reusable code for provisioning OCI resources, including OKE clusters, networking, and storage.  
- **Target Architecture in OCI**: Detailed diagrams and descriptions of the validated setup.  
- **Technical Documentation**: Step-by-step deployment guides, configuration settings, and best practices for scaling and security.  
- **CI/CD Integration Examples**: Sample pipelines using OCI Container Registry and Terraform for automated deployments, if relevant to the validation scope.


 8. Cloud Environment Used
The PoC will run in a **Temporary Test Tenancy** provided by Oracle, configured in the Frankfurt region (eu-frankfurt-1) for low-latency testing. This tenancy will be pay-as-you-go, with resources provisioned via Terraform. If Tecnotree is already onboarded, validation can shift to their tenancy upon mutual agreement.


 9. Tecnotree Company Profile
- **Legal Name**: Tecnotree Corporation  
- **Country of Operations**: Finland (headquartered), with global operations in telecom sectors across Europe, Americas, and Asia.  
- **Company Overview**: Tecnotree is a leading provider of digital Business Support Systems (BSS) for telecommunications, offering solutions for customer management, billing, and service orchestration. With over 40 years of experience, they enable telecom operators to digitize operations and enhance customer experiences.  
- **Website Link**: [www.tecnotree.com](https://www.tecnotree.com)


 10. In-Scope Application: Digital BSS Solution Validation
- **Application Name**: Digital BSS Solution  
- **General Description**: A containerized telecom BSS platform for managing subscriber services, billing, and orchestration, leveraging Kubernetes for deployment.  
- **Key Technologies**: Docker, Helm, Java-based microservices, relational and NoSQL databases.  
- **Current Hosting**: Hybrid (on-prem Kubernetes with some public cloud components).


 11. Project Overview
**Validation Summary**: Validation of Tecnotree’s Digital BSS Solution on Oracle Cloud Infrastructure (OCI) using a Lift & Shift approach. The goal is to assess the compatibility of the existing containerized application architecture (Kubernetes, OKE) with OCI’s managed services, including database, storage, networking, and security. The validation will include functional testing, automated deployment using Terraform, and the definition of a target OCI architecture based on best practices.  

**Project Dates**:  
- Kick-off Version Date: May 28, 2025  
- Latest Update / Current Version: June 4, 2025  
- Estimated Project Duration: 2–3 weeks  

**Project Team**:  
**Oracle Team**:  
- Heikki Ridanpaa – Account Cloud Engineer  
- Maria Solvsteen – Sales Representative  
- Marc Torné – Cloud Solution Architect  
- Laura Taunasescu – Service Delivery Manager  

**Tecnotree Team**:  
- Markus Kivilä – Senior Enterprise Architect  
- Suhail Thusu – Director – Technology Alliances  
- Hannu Vuori – Enterprise Architect  

- **Desired Outcome**: To be provided by Tecnotree and then agreed together with Oracle. If the SoW is filled in separately, Tecnotree can add the desired outcome and then sync with Oracle. Any change in the objectives and scope of the work will require mutual agreement between Tecnotree and Oracle.  

Initial understanding of the scope - needs to be validated with Tecnotree:  
Replicating the customer’s environment in a pay-as-you-go tenancy in Frankfurt to enable functional testing of Tecnotree's containerized Kubernetes setup. The focus is on a lift-and-shift approach without managed services, using a 6-node OKE cluster and supporting components like databases (MySQL, MongoDB, Cassandra) and UI servers, with specific latency and connectivity needs.  

Desired outcome of Tecnotree:  
Successfully validate their application stack in a replicated, containerized environment on OCI that mirrors the customer’s setup. This includes ensuring functional compatibility, performance within latency requirements, and readiness for future automation or cloud-native enhancements—ultimately enabling a smooth lift-and-shift migration path for customer environments.  

Desired Outcome, as jointly agreed with Oracle:  
Demonstrate that OCI can reliably host Tecnotree’s containerized workloads in a way that matches customer requirements, including performance, scalability, and connectivity (e.g., to external systems via VPN).  

- **Scope Boundaries**: Limited to dev/test validation; no production data or live traffic.  
- **Joint Goals**: Achieve a validated reference architecture for OCI deployment, identify optimization opportunities, and document migration best practices.


 12. Scope
**In-Scope Items**:  
- Deployment of OKE clusters for containerized workloads.  
- Configuration of MySQL Database Service, MongoDB, and Cassandra for data persistence.  
- Setup of OCI Streaming for messaging, Block Storage and File Storage for volumes.  
- Networking with VCN, Load Balancer, WAF, Bastion, and VPN.  
- Integration with OCI Cache, Container Registry, Compute instances, and IAM for security.  
- Functional testing of core BSS features in a replicated environment.  

**Out-of-Scope Items**:  
- Full production migration or data transfer.  
- Custom licensing setup for third-party components.  
- SLA guarantees or 24/7 support during validation.  
- Advanced customizations beyond lift-and-shift (e.g., serverless refactoring).  

**Validation Boundaries and Limitations**: Testing limited to non-production workloads; assumes Tecnotree provides compatible images; any external dependencies (e.g., on-prem connectivity) simulated via VPN.


 13. Major Project Milestones

| Milestone                         | Target Date | Completed | Comments                 |
|-----------------------------------|-------------|-----------|--------------------------|
| Kickoff with Cloud Architect      | 2025-05-28  |           | Align on scope and contributions |
| OCI Network Setup                 | 2025-06-01  |           | VCN, VPN, Bastion configuration |
| Terraform Code Finalization       | 2025-06-04  |           | Automation scripts ready |
| Application Deployment in OCI     | 2025-06-10  |           | OKE and services deployed |
| Final Validation & Review         | 2025-06-18  |           | Testing and documentation complete |


 14. Acceptance Criteria

| Capability/Metric                  | Acceptance Criteria                                                       | Status  |
|------------------------------------|---------------------------------------------------------------------------|---------|
| Kubernetes Deployment             | Digital BSS Solution runs successfully on OCI OKE with 6-node cluster     | TBD     |
| OCI Streaming                     | Integration tested with workloads, ensuring message delivery < 50ms latency | TBD     |
| MySQL Database Service            | DB deployed, configured, accessible with sample BSS data loaded           | TBD     |
| Monitoring                        | Basic metrics visible in OCI Monitoring dashboard for Compute and OKE     | TBD     |
| Security                          | IAM policies enforced; NSG rules applied; Encryption in Transit & At Rest | TBD     |


 15. Current State Architecture
**Diagram Description**: The current setup includes on-prem Kubernetes clusters hosting microservices, with Kafka for streaming, relational databases (e.g., MySQL) for subscriber data, NoSQL (MongoDB, Cassandra) for logs and sessions, and manual load balancing. Connectivity to external systems via VPN.  

**Tech Stack**: Docker containers, Helm charts for orchestration, Java/Spring Boot microservices, MySQL/PostgreSQL, MongoDB, Cassandra, Kafka.  

**Known Issues/Pain Points**: Manual deployments leading to downtime; scaling challenges during peak loads; lack of automated backups; high latency in hybrid connectivity.


 16. Target OCI Architecture
The target architecture lifts and shifts Tecnotree's Digital BSS Solution to OCI, leveraging **OKE** for container orchestration, **Compute** for VMs, **Block Storage** and **File Storage** for persistent data, **Load Balancer** and **WAF** for traffic management and security, **OCI Cache** for performance, **MySQL Database Service**, **MongoDB**, and **Cassandra** for databases, **OCI Streaming** for messaging, **Container Registry** for images, **Bastion** and **VPN** for secure access, **VCN** for networking, and **IAM** for access control.  

**Service Mapping** Table:

| Current Component     | OCI Service Mapping                  |
|-----------------------|--------------------------------------|
| Kubernetes Cluster    | OKE (Oracle Kubernetes Engine)       |
| VMs/Servers           | Compute (E5 shapes)                  |
| Persistent Volumes    | Block Storage, File Storage          |
| Load Balancing        | Load Balancer, WAF                   |
| Caching               | OCI Cache                            |
| Relational DB         | MySQL Database Service               |
| NoSQL DBs             | MongoDB, Cassandra (self-managed on Compute) |
| Messaging             | OCI Streaming                        |
| Image Registry        | Container Registry                   |
| Secure Access         | Bastion, VPN                         |
| Networking            | VCN                                  |
| Security/Access       | IAM                                  |

**Component Interaction**: OKE pods interact with MySQL Database Service via VCN; OCI Streaming feeds data to Cassandra/MongoDB; Load Balancer routes traffic through WAF to OKE; Compute instances use Block/File Storage; Bastion/VPN enables secure admin access; all governed by IAM policies.  

**Diagram Placeholder**: Text description - A central VCN with public/private subnets; OKE in private subnet across 3 ADs; Load Balancer/WAF in public subnet; Databases (MySQL, MongoDB, Cassandra) in dedicated subnets; OCI Streaming and Cache integrated via service gateways; Bastion for access; VPN for hybrid connectivity.


 17. Implementation Details and Configuration Settings


# 1. Networking
- **VCN Design, CIDRs, Subnets**: VCN with CIDR 10.0.0.0/16; public subnet (10.0.0.0/24) for Load Balancer; private subnets (10.0.1.0/24 for OKE, 10.0.2.0/24 for databases); regional subnets across 3 ADs for HA.  
- **Internet/NAT Gateways, Service Gateways**: Internet Gateway for public access; NAT Gateway for private outbound; Service Gateway for OCI services (e.g., Container Registry).  
- **Local Peering Gateways (LPGs)**: LPG for inter-VCN peering if multi-tenancy needed.  
- **Route Tables, Security Lists, NSGs**: Default route to NAT/Internet; NSGs restricting traffic (e.g., allow 443 to WAF, 3306 to MySQL); Security Lists for subnet-level rules.


# 2. Compute
- **VM Shapes and OCPUs/Memory**: VM.Standard.E5.Flex with 4 OCPUs and 64 GB memory per instance; scaled to 6 nodes for OKE workers.  
- **OS and Images Used**: Oracle Linux 8 for base images; custom images for application-specific needs.  
- **Bastion/Jump Hosts**: Bastion service with session-based access; Compute instance as jump host in public subnet.  
- **GPU Instances (if any)**: Not applicable; standard E5 shapes used.


# 3. Storage
- **Block Volumes, Object Storage**: Block Volumes (500 GB, balanced performance) attached to Compute for databases; Object Storage for backups (Standard tier).  
- **Boot Volume Size and Configuration**: 100 GB boot volumes for Compute VMs, encrypted with OCI Vault keys.  
- **File Storage**: NFS-based File Storage (1 TB) for shared application files, mounted to OKE pods via PVs.


# 4. Container Services
- **OKE Deployment Process**: Cluster creation via OCI Console/Terraform; 6 worker nodes in E5 shapes; Helm for app deployment.  
- **Integration with OCI**: Terraform for provisioning; Container Registry for pushing/pulling Docker images; OCI Cache for session data.


# 5. IAM & Security
- **Compartments**: Dedicated compartments for networking, compute, storage, and databases.  
- **IAM Policies**: Policies allowing OKE to access Container Registry (e.g., allow group OKE-Admins to manage repos).  
- **Use of Resource Tags**: Tags for cost tracking (e.g., Project: BSS-Validation, Environment: Test).  
- **Access Control via NSGs or Security Lists**: NSGs for fine-grained control (e.g., allow ingress from Load Balancer to OKE on port 8080).


# 6. Deployment Automation
- **Terraform/Resource Manager Usage**: Terraform modules for full stack (VCN, OKE, databases); deployed via OCI Resource Manager stacks.  
- **CLI or Console Steps**: OCI CLI for initial setup (e.g., oci network vcn create); Console for monitoring.  
- **Image Upload**: Docker images pushed to Container Registry via OCI CLI.


 18. Security Considerations
- **IAM Policy Examples**: `allow group BSS-Admins to manage compute-instances in compartment BSS where target.compartment.id = 'ocid1.compartment.oc1..example'`.  
- **NSG Configuration**: Stateful rules; e.g., ingress from 0.0.0.0/0 to Load Balancer on 443, egress to MySQL on 3306.  
- **Data Encryption Approach**: OCI-managed keys for Block Storage (AES-256); encryption at rest for MySQL Database Service; transit encryption via TLS 1.3.  
- **Audit Logs or Logging Analytics Setup**: Enable OCI Logging for all services; integrate with Logging Analytics for centralized querying and alerts.


 19. High Availability & Disaster Recovery
High Availability (HA) in OCI is achieved by distributing resources across multiple Availability Domains (ADs) and Fault Domains (FDs) to mitigate single points of failure. Disaster Recovery (DR) focuses on data replication, backups, and failover mechanisms to ensure business continuity with defined RPO/RTO (e.g., RPO < 1 hour, RTO < 4 hours).

- **OKE**: Node Pools distributed across 3 ADs and FDs for resilience; auto-scaling enabled; Kubernetes replicas for pods.  
- **Database Services (e.g., MySQL Database Service, MongoDB, Cassandra)**: MySQL uses OCI-managed HA with automatic failover to standby in another AD; MongoDB/Cassandra self-managed with replicas across ADs; multi-AD deployment for fault tolerance (OCI manages underlying infrastructure for MySQL).  
- **Block Storage and File Storage**: Cross-AD replication via Volume Groups; automatic backups to Object Storage with retention policy.  
- **Load Balancer and WAF**: Deployed across multiple ADs with active-active backends; health checks for failover.  
- **OCI Streaming and OCI Cache**: Replicated partitions across ADs; cache clusters with redundancy.  
- **Networking & DNS**: VCN with redundant gateways; VPN with multiple tunnels for hybrid HA.  
- **Backup & Restore**: Automated backups for Compute (boot volumes), databases, and storage; RPO 1 hour via snapshots, RTO 2 hours via restore.  
- **DR Strategy Summary**: Active-passive DR across regions (e.g., Frankfurt to Amsterdam); cross-region replication for Object Storage and databases; quarterly testing; failover scripted via Terraform for recovery in <4 hours.


 20. Closing Feedback
- **Oracle Feedback**: [Placeholder for Oracle's comments post-validation].  
- **Tecnotree Feedback**: [Placeholder for Tecnotree's comments on outcomes and suggestions].


 21. Sign-Off Section
**Client Acceptance**: I hereby accept the terms and scope outlined in this SoW.  
Name: ___________________________ Signature: ___________________________ Date: ________________  

**Oracle Confirmation**: Oracle confirms the deliverables and framework.  
Name: ___________________________ Signature: ___________________________ Date: ________________  

**Final Next Steps**: Upon sign-off, initiate kickoff meeting and resource provisioning.  

**Version Tagging**: This version (0.1) is tagged as "Initial Draft" for review.
---

