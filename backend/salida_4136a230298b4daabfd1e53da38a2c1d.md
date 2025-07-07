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


**1. Document Header**  
- **ISV**: TechGlobal Solutions Inc.  
- **Application**: TGW OSS Platform  
- **Type**: Statement of Work  
- **Date**: October 15, 2023  
- **Version**: 1.3  
- **Confidentiality Disclaimer**: This document contains proprietary information intended solely for the use of TechGlobal Solutions Inc. and Oracle. Unauthorized disclosure or distribution is prohibited.  

---


 **2. Version History Table**  

| **Version** | **Date**       | **Author**          | **Description**                                                                 |  
|-------------|----------------|---------------------|---------------------------------------------------------------------------------|  
| 1.0         | Sep 1, 2023    | John Doe            | Initial draft of the validation document.                                       |  
| 1.1         | Sep 15, 2023   | Jane Smith          | Added OCI architecture diagrams and technical specifications.                   |  
| 1.2         | Oct 1, 2023    | Alex Johnson        | Incorporated client feedback on validation criteria and scope.                  |  
| 1.3         | Oct 15, 2023   | John Doe            | Finalized document with implementation plan and sign-off section.               |  

---


 **3. Project Status**  
- **Current Phase**: Validation  
- **Next 3 Critical Actions**:  
  - **Action 1**: Finalize OCI architecture diagram (Owner: Jane Smith)  
  - **Action 2**: Complete performance testing on VM with GPU (Owner: Alex Johnson)  
  - **Action 3**: Validate Oracle DB on IaaS migration script (Owner: Sarah Lee)  

---


 **4. Participant Table**  

| **Role**               | **Name**        | **Title**               | **Email**                |  
|------------------------|-----------------|-------------------------|--------------------------|  
| **Oracle Solution Architect** | Jane Smith    | Senior Architect       | jane.smith@oracle.com    |  
| **Oracle Cloud Engineer**     | Alex Johnson   | Cloud Engineer          | alex.johnson@oracle.com  |  
| **Oracle Project Manager**    | Sarah Lee      | Project Manager         | sarah.lee@oracle.com     |  
| **TGW Technical Lead**        | John Doe       | Technical Lead          | john.doe@tgw.com         |  
| **TGW DevOps Engineer**       | Emily White    | DevOps Engineer         | emily.white@tgw.com      |  
| **TGW Database Admin**        | Michael Brown  | Database Administrator  | michael.brown@tgw.com    |  

---


 **5. Project Summary**  
**Client Business Overview**:  
TechGlobal Solutions (TGW) is a leading provider of enterprise software solutions, specializing in microservices-based applications for financial institutions. TGW aims to modernize its infrastructure by migrating to Oracle Cloud Infrastructure (OCI) to improve scalability, performance, and operational efficiency.  

**Application Purpose**:  
The TGW OSS Platform consists of approximately 300 microservices, delivering core banking functionalities. The application relies on Kubernetes for container orchestration, PostgreSQL/Oracle DB for data persistence, and Apache Kafka for event streaming.  

**Key Technologies**:  
- Kubernetes (on-premises and public cloud)  
- Docker for containerization  
- Helm for deployment automation  
- PostgreSQL/Oracle DB  
- Apache Kafka  
- S3-compatible object storage  

**OCI Services Being Implemented**:  
- **Openshift**: Managed Kubernetes service for container orchestration.  
- **VM with GPU**: High-performance compute instances for AI/ML workloads.  
- **Oracle DB on IaaS**: Dedicated Oracle Database deployment for mission-critical data.  

---


 **6. Scope Definition**  
**In-Scope Components**:  
- Migration of 300 microservices to OCI Openshift.  
- Deployment of VM with GPU for AI/ML workloads.  
- Migration of Oracle DB to OCI IaaS.  
- Integration with Apache Kafka and S3-compatible object storage.  
- Performance and security validation.  

**Out-of-Scope Items**:  
- Redesign of existing microservices architecture.  
- Migration of on-premises network infrastructure.  
- Third-party software licensing.  

**Validation Boundaries**:  
Validation will focus on functional compatibility, performance benchmarks, and security compliance within the OCI environment.  

---


 **7. Milestone Timeline**  

| **Milestone**                          | **Date**       | **Status**       | **Dependencies**                                                                 |  
|----------------------------------------|----------------|------------------|----------------------------------------------------------------------------------|  
| OCI Architecture Design                | Sep 10, 2023   | Completed        | Client approval                                                                  |  
| Openshift Cluster Setup                | Sep 25, 2023   | Completed        | OCI networking configuration                                                     |  
| VM with GPU Deployment                 | Oct 5, 2023    | In Progress      | GPU driver installation                                                          |  
| Oracle DB on IaaS Migration            | Oct 15, 2023   | Not Started      | Data migration script validation                                                 |  
| Performance Testing                    | Oct 20, 2023   | Not Started      | Application deployment completion                                                |  
| Security and Compliance Validation     | Oct 25, 2023   | Not Started      | Performance testing results                                                      |  
| Final Sign-Off                         | Nov 1, 2023    | Not Started      | All validation criteria met                                                      |  

---


 **8. Validation Criteria**  
**Technical Metrics Table**:  

| **Metric**              | **Target**          | **Description**                                                                 |  
|--------------------------|---------------------|---------------------------------------------------------------------------------|  
| **Latency**             | < 100ms             | End-to-end request latency for critical microservices.                          |  
| **Throughput**          | 1000 req/sec        | Maximum requests per second handled by the application.                         |  
| **Availability**        | 99.9%               | Uptime for all services post-migration.                                         |  

**Security Requirements**:  
- Encryption of data at rest and in transit.  
- Role-based access control (RBAC) for OCI resources.  
- Regular vulnerability scanning.  

**Compliance Checks**:  
- GDPR compliance for data handling.  
- SOC 2 Type II certification.  

---


 **9. Architecture Sections**  
**Current Environment**:  
- **Diagram Description**: On-premises Kubernetes clusters with microservices deployed via Helm. PostgreSQL and Oracle DB instances hosted on-premises. Apache Kafka for event streaming.  
- **Technology Stack**: Kubernetes, Docker, PostgreSQL, Oracle DB, Apache Kafka, S3-compatible storage.  
- **Pain Points**:  
  - Limited scalability due to tightly coupled microservices.  
  - High operational overhead for infrastructure management.  
  - Lack of GPU resources for AI/ML workloads.  

**OCI Target Architecture**:  
- **Services Diagram**:  
  - Openshift for Kubernetes orchestration.  
  - VM with GPU for AI/ML workloads.  
  - Oracle DB on IaaS for database migration.  
  - Integration with OCI Object Storage and Apache Kafka.  
- **Component Mapping**:  
  - Microservices → Openshift Pods.  
  - PostgreSQL/Oracle DB → Oracle DB on IaaS.  
  - GPU workloads → VM with GPU.  
- **Migration Approach**: Lift-and-shift for microservices, followed by database migration and GPU workload deployment.  

---


 **10. Implementation Plan**  
**Openshift Configuration**:  
- **Cluster Size**: 3 master nodes, 6 worker nodes.  
- **Networking**: VPC with public and private subnets.  
- **Storage**: OCI Block Volumes for persistent storage.  

**VM with GPU Configuration**:  
- **Instance Type**: BM.GPU3.8 (8 GPUs).  
- **OS**: Oracle Linux 8.  
- **Drivers**: NVIDIA GPU drivers pre-installed.  

**Oracle DB on IaaS Configuration**:  
- **DB Version**: Oracle 19c.  
- **Storage**: NVMe SSDs for high I/O performance.  
- **Backup**: Automated backups to OCI Object Storage.  

**Security Settings**:  
- **Encryption**: AES-256 for data at rest, TLS 1.2 for data in transit.  
- **Firewall**: OCI Security Lists to restrict inbound/outbound traffic.  
- **Monitoring**: OCI Monitoring and Logging for real-time insights.  

---


 **11. Sign-off Section**  
**Client Acceptance Criteria**:  
- Application functionality validated in OCI environment.  
- Performance metrics meet or exceed targets.  
- Security and compliance requirements fulfilled.  

**Oracle Validation Approval**:  
- Oracle team confirms all validation criteria met.  

**Next Steps Post-Validation**:  
- Finalize
---

