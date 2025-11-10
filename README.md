# Data Engineering Roadmap

This README serves as a self-paced learning tracker to document my journey and transition into a **Data Engineer** role. It breaks down the comprehensive roadmap into manageable modules with associated resources and self-assessment steps.

---

## 🛠️ Tech Stack & Key Tools Focus

* **Languages:** Python (Pandas, NumPy), SQL (PostgreSQL/MySQL), PySpark
* **Databases:** PostgreSQL, Snowflake / Google BigQuery (Cloud DW)
* **Orchestration:** Apache Airflow
* **Big Data:** Apache Spark
* **Cloud:** AWS / GCP (Focusing on storage, compute, and managed data services)
* **Tools:** Git, Docker, dbt (data build tool)

---

## Phase 1: Foundational Core (Weeks 1-12)

| Module | Core Concepts | Resources / Courses | Mastery Check (Project/Skill) |
| :--- | :--- | :--- | :--- |
| **1. Programming** | Python (OOP, Functions), Pandas, NumPy, Virtual Environments | Codecademy/DataCamp Python Tracks, *Python Crash Course* book, Official Docs. | Write a **Python script** to consume a JSON file, clean it using **Pandas**, and generate aggregated statistics. |
| **2. Relational Databases** | Complex SQL (Joins, CTEs, Window Functions), Normalization (3NF), Indexing, Basic CRUD. | LeetCode/HackerRank SQL practice, **PostgreSQL** official docs, *SQL in 10 Minutes*. | Design and implement a simple **Star Schema** database using **PostgreSQL** and populate it with seed data. |
| **3. Command Line & Git** | Shell scripting basics, Linux commands, **Git** workflow (`commit`, `branch`, `merge`), Remote repositories. | Linux Survival, *Pro Git* book, GitHub documentation. | Maintain a personal portfolio repository on **GitHub** with proper branching, commits, and a well-written `README.md`. |

---

## Phase 2: Pipeline Development & Modeling (Weeks 13-24)

| Module | Core Concepts | Resources / Courses | Mastery Check (Project/Skill) |
| :--- | :--- | :--- | :--- |
| **4. Data Modeling** | **Kimball Dimensional Modeling** (Facts, Dimensions), **SCD Types**, Star Schema design principles. | *The Data Warehouse Toolkit* (Kimball), online tutorials on dimensional modeling. | **Model a transactional dataset** (e.g., sales data) into a Fact and multiple Dimension tables, explaining the SCD approach used. |
| **5. ETL/ELT & Orchestration** | ETL vs. ELT, Data Quality Checks, **Apache Airflow** (DAGs, Operators, XComs, Scheduling). | Airflow Official Documentation, dedicated online Airflow courses. | Build an **Airflow DAG** to extract data from a source (local/API), load it to a staging area, and trigger a transformation task. |
| **6. Data Transformation (dbt)** | Modular SQL, Jinja Templating, `ref()` function, Data Testing (schema and singular tests), Documentation. | **dbt Fundamentals course** (free), dbt Docs, building ephemeral vs. table models. | Refactor a complex 100-line SQL query into a chain of **modular dbt models** with appropriate tests and automated documentation. |

---

## Phase 3: Big Data and Cloud Ecosystem (Weeks 25+)

| Module | Core Concepts | Resources / Courses | Mastery Check (Project/Skill) |
| :--- | :--- | :--- | :--- |
| **7. Cloud Fundamentals** | **Cloud Provider (AWS/GCP/Azure):** S3/GCS (Storage), EC2/VMs (Compute), Managed Data Warehouses. | Cloud provider free-tier, free-tier courses (e.g., AWS Cloud Practitioner). | Deploy and configure a **Virtual Machine** and a **Cloud Storage Bucket** and secure access credentials. |
| **8. Big Data Processing** | **Apache Spark (PySpark):** DataFrames API, lazy evaluation, transformations, optimization techniques. | *Learning Spark* book, Databricks Community Edition tutorials. | Write a **PySpark script** to read a large Parquet file from cloud storage, perform complex joins/aggregations, and write the output back. |
| **9. Containerization** | **Docker:** Dockerfile, Docker Compose, Images and Containers. | Docker official guide, relevant online courses. | **Containerize** your local PostgreSQL/Airflow setup using **Docker Compose** for consistent deployment. |

---

## 🚀 Portfolio Projects - Demonstrate Mastery

The goal is to complete a minimum of **three** end-to-end projects, hosted on GitHub, that showcase the full spectrum of Data Engineering skills.

### Project 1: Foundational ETL Pipeline (Local/Simple)
* **Focus:** Python, Pandas, PostgreSQL, SQL Modeling.
* **Description:** Scrape data from a simple source (e.g., a public CSV), clean it with Pandas, and load it into a properly designed PostgreSQL database.

### Project 2: Cloud ELT Pipeline with Orchestration
* **Focus:** Cloud Storage, Airflow, dbt, Cloud Data Warehouse (Snowflake/BigQuery).
* **Description:** Build a pipeline orchestrated by **Airflow** that loads raw files from S3/GCS, and uses **dbt** to transform the data directly within the Cloud DW into a final dimensional model.

### Project 3: Big Data Streaming/Batch Processing
* **Focus:** PySpark, Kafka/Kinesis (Optional for Streaming), Partitioning, Performance.
* **Description:** Implement a solution using **PySpark** to process a large (simulated or real) dataset, focusing on optimizing the Spark job for performance before landing the processed results in the Data Warehouse.

---

**Current Status:** **[e.g., Currently working on Phase 2, Module 5: Airflow Orchestration]**
