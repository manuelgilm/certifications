# Describe Cloud Computing

## Introduction to Cloud Computing 

### Shared Responsability Model

* **Traditional approach**: The IT department is responsible for maintaining all the infrastructure and software needed to keep the datacenter up and running. They’re also likely to be responsible for keeping all systems patched and on the correct version.

* With the **Shared responsability model**, responsibilities get shared between the cloud provider and the consumer. Physical security, power, cooling, and network connectivity are the responsibility of the cloud provider. 

* With the **Shared responsability model**, consumer is responsible for the data and information stored in the cloud. (**You wouldn’t want the cloud provider to be able to read your information**.) The consumer is also responsible for access security, meaning you only give access to those who need it.

* for some things, the responsibility depends on the situation.
    * Using a cloud SQL database, the cloud provider would be responsible for maintaining the actual database. However, you’re still responsible for the data that gets ingested into the database. 
    
* With an on-premises datacenter, you’re responsible for everything. With cloud computing, those responsibilities shift. 

* With an on-premises datacenter, you’re responsible for everything. With cloud computing, those responsibilities shift. The **shared responsibility model** is heavily tied into the cloud service types:
    * Infrastructure as a service (IaaS): places the most responsibility on the consumer, with the cloud provider being responsible for the basics of physical security, power, and connectivity.

    * Platform as a Service (PaaS): A middle ground between IaaS and SaaS, rests somewhere in the middle and evenly distributes responsibility between the cloud provider and the consumer.

    * Software as a Service (SaaS): Places most of the responsibility with the cloud provider

**Takeaways**
* With a cloud provider, you will always be responsible for:
    * The information and data stored in the cloud.
    * Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
    * The accounts and identities of the people, services, and devices within your organization.

* The cloud provider is always responsible for:
    * The physical Data Center
    * The physical network.
    * The physical hosts

* Your service model will determine responsibility for things like:

    * Operating Systems.
    * Network controls.
    * Applications.
    * Idenitty and infrastructure.

## Cloud Models

Cloud models define the deployment type of cloud resources.

### Private Cloud

* A private cloud is, in some ways, the natural evolution from a corporate datacenter.
* Private cloud provides much greater control for the company and its IT department. 
* it also comes with greater cost and fewer of the benefits of a public cloud deployment.
* A private cloud may be hosted from your on site datacenter. It may also be hosted in a dedicated datacenter offsite.

### Public Cloud

* A public cloud is built, controlled, and maintained by a third-party cloud provider.
* Anyone that wants to purchase cloud services can access and use resources. 
* The general public availability is a key difference between public and private clouds.

### Hybrid Cloud

* Is a computing environment that uses both public and private clouds in an inter-connected environment. 
* It can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources.
* It can be used to provide an extra layer of security. 

### Multi-Cloud

* In a multi-cloud scenario, you use multiple public cloud providers. 
* You may use different features from different cloud providers. 
* You started your cloud journey with one provider and are in the process of migrating to a different provider.

### Azure Arc

* Azure Arc is a set of technologies that helps manage your cloud environment.
* Azure Arc can help manage your cloud environment (providing support for most cloud types)

### Azure VMware Solution

* Azure VMware Solution lets you run your VMware workloads in Azure with seamless integration and scalability.

## Consumption-Based Model

* When comparing IT infrastructure models, there are two types of expenses to consider. 
**Capital expenditure (CapEx)** and **operational expenditure (OpEx)**.

* **CapEx** is typically a one-time, up-front expenditure to purchase or secure tangible resources. Examples:

    * A new building.
    * Repaving the parking lot.
    * Building a Data Center.
    * Buying a company vehicle

* **OpEx** is spending money on services or products over time. 
    * Renting a convention center.
    * Leasing a company vehicle.
    * Signing Up for cloud services.

* Cloud computing falls under OpEx because cloud computing operates on a consumption-based model.

* This consumption-based model has many benefits, including:

    * No upfront costs. 
    * No need to purchase and manage costly infrastructure that users might not use to its fullest potential.
    * The ability to pay for more resources when they're needed.
    * The ability to stop paying for resources that are no longer needed.

# Describe the Benefits of using cloud computing

## High Availability

* High availability focuses on ensuring maximum availability, regardless of disruptions or events that may occur.

* You’ll need to account for service availability guarantees. 
* Azure is a highly available cloud environment with uptime guarantees depending on the service. These guarantees are part of the **service-level agreements** (SLAs).

## Scalability

* Scalability refers to the ability to adjust resources to meet demand.
* You aren't overpaying for services

### Vertical Scaling

* Vertical scaling is focused on increasing or decreasing the capabilities of resources.

### Horizontal Scaling

* Horizontal scaling is adding or subtracting the number of resources.

## Reliability 

* Reliability is the ability of a system to recover from failures and continue to function. 

* The cloud, by virtue of its decentralized design, naturally supports a reliable and resilient infrastructure. 

* The cloud enables you to have resources deployed in regions around the world.

*  With this global scale, even if one region has a catastrophic event other regions are still up and running. 

* In some cases, your cloud environment itself will automatically shift to a different region for you, with no action needed on your part. 

## Predictability

* Predictability in the cloud lets you move forward with confidence.
* It can be focused on Performance or cost.
* Both performance and cost predictability are heavily influenced by the Microsoft Azure Well-Architected Framework. 

### Performance

* Performance predictability focuses on predicting the resources needed to deliver a positive experience for your customers.

* Autoscaling, load balancing, and high availability are just some of the cloud concepts that support performance predictability.

### Cost 

* Cost predictability is focused on predicting or forecasting the cost of the cloud spend.
* By operating in the cloud and using cloud analytics and information, you can predict future costs and adjust your resources as needed. 
* You can even use tools like the **Total Cost of Ownership** (TCO) or **Pricing Calculator** to get an estimate of potential cloud spend.

## Benefits of security and governance in the cloud.

* Cloud features support governance and compliance.
* Things like set templates help ensure that all your deployed resources meet corporate standards and government regulatory requirements. 
* You can update all your deployed resources to new standards as standards change. 
* Cloud-based auditing helps flag any resource that’s out of compliance with your corporate standards and provides mitigation strategies. 
*  If you want maximum control of security, infrastructure as a service provides you with physical resources but lets you manage the operating systems and installed software.
* If you want patches and maintenance taken care of automatically, **platform as a service** or **software as a service** deployments may be the best cloud strategies for you.

## Management of the cloud.

* Automatically scale resource deployment based on need.
* Deploy resources based on a preconfigured template, removing the need for manual configuration.
* Monitor the health of resources and automatically replace failing resources.
* Receive automatic alerts based on configured metrics, so you’re aware of performance in real time.

## Management in the cloud.

* Through a web portal.
* Using a command line interface.
* Using APIs.
* Using PowerShell.

# Describe Cloud Service Types

## Infrastructure as a Service

* IaaS is the most flexible category of cloud services, as it provides you the maximum amount of control for your cloud resources. 
* In an IaaS model, the cloud provider is responsible for maintaining the hardware, network connectivity (to the internet), and physical security.
* You’re responsible for everything else:
    * Operating system installation
    * Configuration.
    * Maintenance
    * Network Configuration
    * Database and storage configuration.
* With IaaS, you’re essentially renting the hardware in a cloud datacenter, but what you do with that hardware is up to you.

**Some common scenarios where IaaS might make sense include:**

* Lift-and-shift migration: You’re setting up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to running on the IaaS infrastructure.
* Testing and development:
    * You have established configurations for development and test environments that you need to rapidly replicate.
    * You can start up or shut down the different environments rapidly with an IaaS structure, while maintaining complete control.

## Platform as a Service

* **PaaS** is a middle ground between renting space in a datacenter (infrastructure as a service) and paying for a complete and deployed solution (software as a service).
* In a **PaaS** environment, the cloud provider maintains the physical infrastructure, physical security, and connection to the internet.
* They also maintain the operating systems, middleware, development tools, and business intelligence services that make up a cloud solution. 
* In a **PaaS** scenario, you don't have to worry about the licensing or patching for operating systems and databases.
* **PaaS** is well suited to provide a complete development environment without the headache of maintaining all the development infrastructure.

**Some common scenarios where PaaS might make sense include**

* Development framework:
    * **PaaS** provides a framework that developers can build upon to develop or customize cloud-based applications.
    * **PaaS** lets developers create applications using built-in software components. 
    * Cloud features such as scalability, high-availability, and multi-tenant capability are included, reducing the amount of coding that developers must do.

* Analytics or business intelligence:
    *  Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions.

## Software As A Service

**SaaS** is the most complete cloud service model from a product perspective. With SaaS, you’re essentially renting or using a fully developed application. Email, financial software, messaging applications, and connectivity software are all common examples of a SaaS implementation.

While the SaaS model may be the least flexible, it’s also the easiest to get up and running. It requires the least amount of technical knowledge or expertise to fully employ.

Some common scenarios for **SaaS** are: 

* Email and messaging.
* Business productivity applications.
* Finance and expense tracking.