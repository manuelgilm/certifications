# Streamlining MLOps

## Continuous terminology

* Continuous integration (CI) Extends the testing and validating code by adding testing and validation of code, data and models.

* Continuous Training (CT) automatically (re)trains ML models on data for (re)deployment.

* Continuous Deployment (CD) concerned with delievery of a ML training pipeline that automatically deploys another ML model and needed stores.

* Continuous Monitoring (CM) Concerned with **continuous monitoring** of **production data** and **model performance metrics**

### Continuous Integration

* Automatically trigger pipelines after code commits.
* Run tests and validation on code, data and models.
* track all changes via version control.

### Continuous Training (CT)

* Retrain models automatically when new code or data is available or performance indicates.

* Log all experiments and model metrics for reproducibility.

* Automate hyperparameter tuning.

* Evaluate and validate models.

## Continuous Integration (Possible Pipelines)

* Code testing and integration pipeline:
	* Ensures code changes are merged and tested without breaking the workflow.
* Data pipeline validation pipeline:
	* verifies the integrity of data pipelines and their integration with existing workflows.
* Feature engineering validation pipeline.
	* Validates the quality and consistency of features produced by updated feature engineering scripts
* Automated Security and Compliance.
	* Ensures that security and compliance checks are in place for code and data handling.

## Continuos Training (Possible Pipelines)

* Data ingestion and Feature Engineering
	* Automate data collection, cleaning, feature creation, and validation.
* Model tuning Pipeline(optional)
	* Optimize performance by tuning hyperparameters automatically.
	* May have been previous established.
* Model training pipeline
	* Automate model training with the latest data, logging results and artifacts.
* Model evaluation pipeline:
	* test and compare models against production versions to ensure improvements. 
* Model Registry and Promotion Pipeline:
	* Manage and promote through different lifecycle stages.

## Continuous Deployment.

* Validate models in staging before production.
* Deploy code or models automatically across environments.
* Use manual approval (Continuous Delivery) or autoamte deployments (continuous deployment)

## Continuous Monitoring (CM)

* Track model peformance and drift in production.
* Automate retraining or notifications based on performance metrics.


