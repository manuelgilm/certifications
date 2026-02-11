# Operational Excellence in Machine Learning

**Standardize MLOps** processes for consistent and reliable ML.

* Implement **DevOps processes** (CI/CD) by automating building, testing, and deploying code.

* **Modularize code** for clearly defined steps, testing and simplify refactoring.

* Encapsulate individual pipelines and workflows into an **orchestrator**.

* Incorporate **versioning** for tracking models and datasets.

* Set Up **monitoring** , **alerting** , and **logging**

Operational excellence in machine learning is all about driving efficiency, reliability, and scalability through standardized MLOps practices with Databricks. This means:

* setting up consistent workflows
* Automating CI/CD pipelines with tools like GitHub Actions or Jenkins
* Modularizing code so workflows are reusable and easier to test.
* Versioning with MLflow and Delta Lake ensures traceability
* Monitoring and loging, and real-time alerts

## What is MLOps?

* A combination of **DevOps**, **DataOps** and **ModelOps**.
* A set of **processes** and **automation** for managing: **models**, **data**, and **code** assets. 

### Results of MLOps Implementation:

* **Efficiency**: Higher quality models in less time.
* **Scalability**: Thousands of models can be overseen, controlled, managed, and monitored.
* **Risk reduction**: Through repeatable workflows, automated monitoring and transparency.

### DataOps

(Ensure data quality) 

* Optimize data **processing**
* Centralize data **discovery**, **management** , and **governance**
* Establish traceable data **lineage** and **monitoring**
* Enhance collaboration across teams.
* Monitor data

### DevOps
(treat Machine Learning as Code)

* Automate CI/CD
* Enable continuous code testing.
* Versiong control
* Establish Production-grade **workflows**
	* Orchestration & Automation.
* Monitor system performance.

### ModelOps

(Move beyond mdoels as **objects**)

* Treating **model code** as **software**
* Treating models as data.
* Manage the model lifecycle.
* Monitor model performance.


# Streamlining Development to Deployment

## Environment Separation

(How many databricks workspaces do we have?)

### Direct Separation (Recommended)

* **Completely separate** Databricks workspaces for each environment.
* **simpler environments**
	* Easier the risk of cross-environment interactions.
	* More straightforward to **track** changes and issues.
* **Reduces the risk** of cross-environment interactions.
* **Scales** well to multiple projects
	* Might require more administrative effort to manage multiple environments.
	* Might lead to **higher costs** due to the need for separate resources for each workspace.

### Indirect Separation

* One databricks workspace with enforced separation using **naming conventions** and access control.
* Simpler overall infrastructure.
	* Less permissions required
	* Can be more **cost-effective** needing fewer resources.
* Easier cross-environment **Collaboration** and sharing.
* Does not scale well to multiple projects.
	* **Complex** individual environment.
	* Requires management to maintain the separation and prevent accidental cross-environment interactions.
	* Can be more challenging to manage **Security** and **compliance** requirements.

## Deployment Patterns

### Moving from Deploy Model to Deploy Code. 

When deploying models the process is as follows:

1. Models are trained in dev and promoted to staging
2. Models are tested in Staging
3. Models are promoted to prod.

**Trade-offs**

* Simplicity  (+)
* DS familiarity (+)
* Computational cost (+)
* Automation (-)
* Scalability (-)
* Reproducibility (-)

### Deeper dive into benefits of "Deploy Code"

**Automation**: (+) Supports automated retraining in secure and controlled environments.

**Data Access Control**: (+) Restricts data access efficiently, where only the production environment requires read permissions to sensitive training data.

**Reproducible models**: (+) Every step of the model generation process can be replicated consistently across environments, allowing teams to recreate models consistently.

**Support for large projects**:(+) SCales well for larger projects by promoting modularized, organized, reusable code and structured testing workflows. 

**Testing**: (+) First unit and integration testing in the development environment followed by unit and integration testing in staging, which closely mimics production.

**Data science familiarity** (-) Requires thed ata science team to write production-ready, modular code. Ensuring smooth hand-offs to engineering teams.

**Eng setup & maintainance**: (-) Requires robust (CI/CD) infrastructure, supporting consistent unit and integration testing for all models.


## ML Operations Guiding Principles.

* Automated and Orchestrated **Continuous Integration and Continuous Deployment**
	* Set up CI/CD pipelines to automate the machine learning lifecycle
	* Reducing manual steps and ensuring consistency.
	* Break down ML workflows into manageable modules.
* Automate Comprehensive **Testing**
	* Implement a testing strategy including: unit, integration, and end-to-end tests.
	* Incorporate canary tests and blue/green deployment with CI/CD pipelines.
* Monitoring and Alerts
	* Monitor model performance and operations with visuals, custom metrics, and insights. 
	* Set up automated alerts to detect issues early.
* Build ML **Assets as Code**
	* Standardize and automate ML asset creation using Infrastructure as Code and predefined templates.

