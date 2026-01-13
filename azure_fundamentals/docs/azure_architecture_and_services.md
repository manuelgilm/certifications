# Describe the Core Architectural components of Azure

## Use availability zones in your apps

You can use availability zones to run mission-critical applications and build high-availability into your application architecture by co-locating your compute, storage, networking, and data resources within an availability zone and replicating in other availability zones. Keep in mind that there could be a cost to duplicating your services and transferring data between availability zones.

Availability zones are primarily for VMs, managed disks, load balancers, and SQL databases. Azure services that support availability zones fall into three categories:

    Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
    Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
    Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.

## Region Pairs

* Most Azure regions are paired with another region within the same geography (such as US, Europe, or Asia) at least 300 miles away. 

* It allows for the replication of resources across a geography that helps reduce the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect an entire region.

## Sovereign Regions

In addition to regular regions, Azure also has sovereign regions. Sovereign regions are instances of Azure that are isolated from the main instance of Azure. You may need to use a sovereign region for compliance or legal purposes.

**Azure sovereign regions include**:

* US DoD Central, US Gov Virginia, US Gov Iowa and more: These regions are physical and logical network-isolated instances of Azure for U.S. government agencies and partners. These datacenters are operated by screened U.S. personnel and include additional compliance certifications.

* China East, China North, and more: These regions are available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly maintain the datacenters.

## Azure resources and resource groups

* A resource is the basic building block of Azure. 
* Anything you create, provision, deploy, etc. is a resource.
    * Virtual Machines
    * Virtual Networks
    * Databases
    * Cognitive Services
    * etc

* **Resource groups** are simply groupings of resources.
* When you create a resource, you’re required to place it into a resource group. 
* While a resource group can contain many resources, a single resource can only be in one resource group at a time.
* Some resources may be moved between resource groups.
* when you move a resource to a new group, it will no longer be associated with the former group.
* resource groups **can't** be nested, meaning you can’t put resource group B inside of resource group A.
* Resource groups provide a convenient way to group resources together.
* When you apply an action to a **resource group**, that action will apply to all the resources within the resource group.
* If you delete a **resource group**, all the resources will be deleted. 
* If you grant or deny access to a **resource group**, you’ve granted or denied access to all the resources within the **resource group**.

**There are two types of subscription boundaries that you can use:**

* Billing boundary: This subscription type determines how an Azure account is billed for using Azure. You can create multiple subscriptions for different types of billing requirements. Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.

* Access control boundary: Azure applies access-management policies at the subscription level, and you can create separate subscriptions to reflect different organizational structures. An example is that within a business, you have different departments to which you apply distinct Azure subscription policies. This billing model allows you to manage and control access to the resources that users provision with specific subscriptions

## Create Additional Azure Subscriptions.

Similar to using resource groups to separate resources by function or access, you might want to create additional subscriptions for resource or billing management purposes.

* **Environments**: You can choose to create subscriptions to set up separate environments for development and testing, security, or to isolate data for compliance reasons. This design is particularly useful because resource access control occurs at the subscription level.

* **Organizational Structures**: You can create subscriptions to reflect different organizational structures. For example, you could limit one team to lower-cost resources, while allowing the IT department a full range. This design allows you to manage and control access to the resources that users provision within each subscription.

* **Billing**: You can create additional subscriptions for billing purposes. Because costs are first aggregated at the subscription level, you might want to create subscriptions to manage and track costs based on your needs. For instance, you might want to create one subscription for your production workloads and another subscription for your development and testing workloads.

## Azure management groups

* Azure management groups provide a level of scope above subscriptions. 
* You organize subscriptions into containers called management groups and apply governance conditions to the management groups. 
* All subscriptions within a management group automatically inherit the conditions applied to the management group.
* Management groups can be nested.

**Examples of how you could use management groups might be:**

* Create a hierarchy that applies a policy: You could limit VM locations to the US West Region in a group called Production. This policy will inherit onto all the subscriptions that are descendants of that management group and will apply to all VMs under those subscriptions. This security policy can't be altered by the resource or subscription owner, which allows for improved governance.

* Provide user access to multiple subscriptions: By moving multiple subscriptions under a management group, you can create one Azure role-based access control (Azure RBAC) assignment on the management group. Assigning Azure RBAC at the management group level means that all sub-management groups, subscriptions, resource groups, and resources underneath that management group would also inherit those permissions. One assignment on the management group can enable users to have access to everything they need instead of scripting Azure RBAC over different subscriptions.

**Important facts about management groups:**

* 10,000 management groups can be supported in a single directory.
* A management group tree can support up to six levels of depth. This limit doesn't include the root level or the subscription level.
* Each management group and subscription can support only one parent.

# Azure compute and networking services

## Azure Virtual Machines

* VMs provide infrastructure as a service (IaaS) in the form of a virtualized server and can be used in many ways.

* VMs are an ideal choice when you need:
    * Total control over the operating system (OS).
    * The ability to run custom software.
    * To use custom hosting configurations.

* As an IaaS offering, you still need to configure, update, and maintain the software that runs on the VM.
* You can even create or use an already created image to rapidly provision VMs.
* An image is a template used to create a VM and may already include an OS and other software, like development tools or web hosting environments.

## Virtual machine scale sets

* Virtual machine scale sets let you create and manage a group of identical, load-balanced VMs.

* If you simply created multiple VMs with the same purpose, you’d need to ensure they were all configured identically and then set up network routing parameters to ensure efficiency. You’d also have to monitor the utilization to determine if you need to increase or decrease the number of VMs.

* with virtual machine scale sets, Azure automates most of that work

* Scale sets allow you to centrally manage, configure, and update a large number of VMs in minutes. 

* The number of VM instances can automatically increase or decrease in response to demand, or you can set it to scale based on a defined schedule.

* Virtual machine scale sets also automatically deploy a load balancer to make sure that your resources are being used efficiently.

* With virtual machine scale sets, you can build large-scale services for areas such as compute, big data, and container workloads.

## Virtual machine availability sets

* Availability sets are designed to ensure that VMs stagger updates and have varied power and network connectivity, preventing you from losing all your VMs with a single network or power failure.

* Availability sets accomplish these objectives by grouping VMs in two ways: 
    * **Update domain**: The update domain groups VMs that can be rebooted at the same time. This setup allows you to apply updates while knowing that only one update domain grouping is offline at a time. All of the machines in one update domain update. An update group going through the update process is given a 30-minute time to recover before maintenance on the next update domain starts.

    * **Fault domain**: The fault domain groups your VMs by common power source and network switch. By default, an availability set splits your VMs across up to three fault domains. This helps protect against a physical power or networking failure by having VMs in different fault domains (thus being connected to different power and networking resources).

## Azure Container Instances (ACI)

* ACI offer the fastest and simplest way to run a container in Azure; without having to manage any virtual machines or adopt any additional services.

* **ACI** are a platform as a service (PaaS) offering. Azure Container Instances allow you to upload your containers and then the service runs the containers for you.


## Azure Container APPs (ACA)

* ACA are similar in many ways to a container instance.
* They allow you to get up and running right away, they remove the container management piece, and they're a PaaS offering. 
* Container Apps have extra benefits such as the ability to incorporate load balancing and scaling. 

## Azure Functions
* Azure Functions is an event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers.

## Application hosting options

### Azure App Service

* App Service enables you to build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers automatic scaling and high availability. App Service supports Windows and Linux. It enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.

* Azure App Service is a robust hosting option that you can use to host your apps in Azure. Azure App Service lets you focus on building and maintaining your app, and Azure focuses on keeping the environment up and running.

**Types of App Services**

With app service, you can host most common app services styles like:

* web apps
* API apps
* WebJobs
* Mobile apps

App Service handles most of the infrastructure decisions you deal with in hosting web-accessible apps:

* Deployment and management are integrated into the platform.
* Endpoints can be secured.
* Sites can be scaled quickly to handle high traffic loads.
* The built-in load balancing and traffic manager provide high availability.

## Azure Virtual Networking

Azure virtual networks provide the following key networking capabilities:


* Isolation and segmentation
* Internet communications
* Communicate between Azure resources
* Communicate with on-premises resources
* Route network traffic
* Filter network traffic
* Connect virtual networks

Azure virtual networking supports both **public and private endpoints** to enable communication between external or internal resources with other internal resources.


* **Public endpoints** have a public IP address and can be accessed from anywhere in the world.
* **Private endpoints** exist within a virtual network and have a private IP address from within the address space of that virtual network.

## Isolation and segmentation

Azure virtual network allows you to create multiple isolated virtual networks. When you set up a virtual network, you define a private IP address space by using either public or private IP address ranges. The IP range only exists within the virtual network and isn't internet routable. You can divide that IP address space into subnets and allocate part of the defined address space to each named subnet.

For name resolution, you can use the name resolution service built into Azure. You also can configure the virtual network to use either an internal or an external DNS server.

## Internet Communications.

You can enable incoming connections from the internet by assigning a public IP address to an Azure resource, or putting the resource behind a public load balancer.

## Communicate between Azure resources.

You want to enable Azure resources to communicate securely with each other. You can do that in one of two ways:


* Virtual networks can connect not only VMs but other Azure resources, such as the App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual machine scale sets.
* Service endpoints can connect to other Azure resource types, such as Azure SQL databases and storage accounts. This approach enables you to link multiple Azure resources to virtual networks to improve security and provide optimal routing between resources.

## Communicate with on-premises resources

https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/8-virtual-network