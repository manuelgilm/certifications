# Automate Comprehensive testing.

## Testing Pyramid

* Unit Tests
	* Test only only specific function, on small amount of data.
	* Fast, able to run locally
* Integration tests
	* Test business logic on limited amount of data 
	* Usually run in a separate environment, as part of CI implementation.
* Acceptance/End-to-End tests.
	* Run on data, close to production. (volume/velocity)
	* Run in environment, close to production.

## Unit Tests / Small tests

These tests help to improve the quality and consistency of your notebook's code.

* Checks a single component of an application.
* Focuses on testing functionality of individual units only.
* Does not uncover issues arising when different modules interact.

Best practices include writing tests for critical and edge cases, using clear test cases, and integrating them into CI/CD for automated checks.

## What should you test in ML?

### Data Validation

* Data Validation:  Data is in the correct form and free from errors. 

* Modelling functions: Test functions written to build and operate your models

* Data Transformations: Ensure transformations are carried out properly

* Model Integration: Model Integrates and functions well with the system.

## Integration Tests 

Ensure that different components of your system work together correctly. 

* Identifies issues, ensures end-to-end functionality, and verifies requirements.

* Tests combined modules together and ensures they are interacting and working as expected.

* Often performed in Staging environment which should match the production environment as closely as possible. 

**Suggestions for Time and Cost Reductions**

* use small subsets of data or run fewer training iterations.
* Instead of a full-scale load testing in integration tests, just test small batch jobs or requests to a temporary endpoint. 

## End-to-End tests (E2E)

Validates the entire system workflow from start to finish, mimicking real-world scenarios. 

* Covers the complete process, from data ingestion to final output, including all intermediate steps.
* Crucial to ensure operational separation between development (dev), staging, and production (prod) environments.

-> Run on data, close to production
-> Run in environment, close to production.

## Optimize tests in the CI/CD process
we cannot afford to run all the tests for every change at any stage of the pipelines, we need to be more selective.

* Zero-defect in production, is not a goal these expectations would not lead to a good ROI
* Funnel for catching defects:
	* Catch them as soon as possible
		* The later defects are detected, the more expensive their handling.
	* Implement tests for catching defects that cannot be caught earlier.
* Ensure the ability to detect and roll back issues in production.
	* e.g using additional approaches such as canary deployments, experiments, probing, etc.

# Model Rollout Strategies with Databricks

Ensuring Smooth Deployment of New Model Versions
	* A/B Testing: Comparing the performance of the new model against the current one with real-time data.
	* Canary Releases: Gradually rolling out the new model to a small percentage of users before full deployment.
	* Monitoring Post-Deployment: Tracking KPIs and user feedback to identify any issues.
	* Rollback Mechanisms: having a plan to revert to the previous model version if significant problems arise.

## Model Rollout Strategies

### Shadow

New deployment shows existing system but not used for decision making.

### Rolling

Updates nodes in a target environment incrementally in batches with the new version.

### Blue-Green 

Utilize two identical environments, a "blue" and a "green" environment with different versions of an application or service. 

### Canary

Releases an application or service incrementally to a subset of users.

### A/B Testing

Different versions of the same service run simultaneously in the same environment for a period of time. A/B testing is essentially an experiment where two or more variants of a deployment are shown to users at random, and statistical analysis is used to determine which variation performs better for a given conversion goal.

 	
