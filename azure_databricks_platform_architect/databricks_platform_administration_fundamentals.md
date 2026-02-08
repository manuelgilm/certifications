# Data intelligence Platform Overview

The Datbricks platform runs in two different accounts. 

* The first account comprises the Control Plane (Which hosts the Web App, Unity Catalog, and management services) and the Serverless Compute Plane
 (which is the compute layer of the serverless product). These are deployed in the Databricks account.

* The second account comprises the Compute Plane, which is the compute layer for non-serverless product lines (such as Databricks Workspaces and Databricks SQL) and the cloud
storage, which are in the customer account.

# Services running in the **Databricks Subscription**

The **account console** is where you administrate the databricks account for:

* Workspace creation
* User Management
* Metastore Management.

The control plane consists of several services:

* Web APP
* Workflow management: Manages job workflows and **Delta Live Tables** (DLT) to orchestrate tasks in multiple layers. 
* Compute Management: refers to the Cluster Manager, which configures and sets up Spark clusters.
* Jobs: Handle task scheduling
* Unity Catalog
* Intelligence Platform: Uses machine learning models to optimize and manage both the Control and Compute plane services within Databricks. 

# Databricks Security Model

 
