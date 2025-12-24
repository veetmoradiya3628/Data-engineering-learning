### Hadoop

**Hadoop** is an open-source distributed computing framework designed for processing and storing large-scale datasets across clusters of commodity hardware. It provides scalable, fault-tolerant storage and processing capabilities.

#### Core Components:

- **YARN** (Yet Another Resource Negotiator) - Resource management and job scheduling framework that manages cluster resources and coordinates application execution
  - **RM** (Resource Manager) - Central authority for managing cluster resources, scheduling applications, and allocating resources across the cluster
  - **NM** (Node Manager) - Agent running on each node for managing individual nodes, monitoring resource usage, and reporting to Resource Manager
  - **AM** (Application Master) - Per-application component for managing application lifecycle, negotiating resources, and coordinating task execution

- **HBase** - Column-oriented NoSQL database built on top of HDFS for real-time read/write access to large datasets with billions of rows and millions of columns

- **HDFS** (Hadoop Distributed File System) - Distributed file system for storing large datasets across multiple machines with high fault tolerance and throughput
  - **File metadata stored at Name Node:**
    - File name - Unique identifier for the file
    - Directory location - Hierarchical path in the filesystem
    - File size - Total size of the file in bytes
    - File blocks - Block ID, block sequence, block location for distributed storage

- **Hive** - Data warehouse infrastructure providing SQL-like query language (HiveQL) for data warehousing, analysis, and querying large datasets stored in HDFS

- **Pig** - High-level scripting language (Pig Latin) for data analysis and transformation, simplifying complex MapReduce tasks into sequential data operations

- **MapReduce** - Programming model for distributed data processing that divides work across multiple nodes for parallel computation
  - **Architecture Components:**
      - **Job Client** - Submits MapReduce jobs to the system and provides job configuration
      - **Job Tracker** - Master daemon that manages job execution, resource allocation, and task scheduling across the cluster
      - **Task Tracker** - Slave daemon that executes map and reduce tasks on worker nodes and reports progress to Job Tracker
  - **Processing Phases:**
      - **Map Phase** - Processes input data in parallel and generates intermediate key-value pairs
      - **Shuffle Phase** - Sorts and transfers intermediate data to reducers, grouping values by key
      - **Reduce Phase** - Aggregates and processes mapped data to produce final output results
  - **Data Flow:**
      - Input splits → Mappers → Intermediate key-value pairs → Partitioner → Shuffling → Reducers → Final output
  - **Map Function** - Transforms input records into intermediate key-value pairs
  - **Reduce Function** - Aggregates intermediate values by key to produce final results

**💡 When to Use Hadoop:**
- Batch processing of massive datasets (TB/PB scale)
- Cost-effective storage of historical data
- Complex ETL workflows
- Organizations with existing Hadoop infrastructure

---

### Apache Spark

**Apache Spark** is an open-source unified analytics engine for large-scale data processing, providing high-performance distributed computing with in-memory processing capabilities. It offers **up to 100x faster** processing than MapReduce by keeping data in memory across operations.

#### Core Components:

- **Spark Core** - Foundation engine providing basic I/O functionality, task scheduling, memory management, and fault recovery

- **Spark SQL** - Module for structured data processing using SQL queries and DataFrames, supporting various data sources (JSON, Parquet, Hive)

- **Spark Streaming** - Real-time stream processing framework for processing live data streams with micro-batch processing

- **MLlib** - Scalable machine learning library providing algorithms for classification, regression, clustering, and collaborative filtering

- **GraphX** - Graph processing framework for graph-parallel computation and analysis of graph-structured data

#### Key Concepts:

- **RDD** (Resilient Distributed Dataset) - Fundamental immutable distributed collection of objects that can be processed in parallel
  - **Transformations** - Lazy operations that create new RDDs (map, filter, flatMap, groupBy)
  - **Actions** - Operations that trigger computation and return results (collect, count, reduce, save)

- **DataFrame** - Distributed collection of data organized into named columns, similar to relational database tables

- **Dataset** - Strongly-typed distributed collection combining benefits of RDDs and DataFrames with compile-time type safety

- **DAG** (Directed Acyclic Graph) - Execution plan representing sequence of computations and dependencies between RDD operations

#### Execution Model:

- **Driver Program** - Main program that creates SparkContext and coordinates job execution
- **Cluster Manager** - External service for acquiring cluster resources (Standalone, YARN, Mesos, Kubernetes)
- **Executors** - Worker processes running on cluster nodes that execute tasks and cache data
- **Tasks** - Individual units of work sent to executors for parallel execution

#### Spark Deployment Modes:

**Spark with Hadoop:**
- ✅ **Integration Benefits** - Leverages existing Hadoop infrastructure (HDFS, YARN) for storage and resource management
- ✅ **HDFS Storage** - Uses Hadoop Distributed File System for reliable, distributed data storage
- ✅ **YARN Resource Manager** - Runs Spark applications on YARN cluster for unified resource management
- ✅ **Data Locality** - Processes data where it's stored in HDFS, minimizing network transfer
- ✅ **Shared Cluster** - Multiple frameworks (MapReduce, Spark, Hive) can coexist on same cluster
- 🎯 **Use Case** - Large enterprises with existing Hadoop investments and batch processing workloads

**Spark Standalone (Without Hadoop):**
- ✅ **Independent Deployment** - Runs without Hadoop dependencies using Spark's built-in cluster manager
- ✅ **Flexible Storage** - Can use alternative storage systems (S3, Azure Blob, local file systems, Cassandra)
- ✅ **Lightweight Setup** - Simpler architecture without Hadoop overhead and complexity
- ✅ **Resource Management** - Uses Spark's standalone cluster manager or alternatives (Mesos, Kubernetes)
- ✅ **Performance** - Potentially faster for in-memory operations without HDFS overhead
- 🎯 **Use Case** - Real-time analytics, streaming applications, organizations without Hadoop infrastructure

**⚡ Spark vs Hadoop Quick Comparison:**
| Feature | Hadoop MapReduce | Apache Spark |
|---------|------------------|--------------|
| Speed | Disk-based (slower) | In-memory (up to 100x faster) |
| Ease of Use | Complex Java code | Simple APIs (Python, Scala, Java, R) |
| Real-time | Batch only | Batch + Streaming |
| ML Support | Limited | Native MLlib |
| Interactive | No | Yes (shell available) |

---

### PySpark

**PySpark** is the Python API for Apache Spark, enabling Python developers to harness Spark's distributed computing capabilities using familiar Python syntax. It provides access to all Spark features while leveraging Python's rich ecosystem of data science libraries.

#### Key Features:

- **Python Integration** - Seamless integration with Python libraries (NumPy, Pandas, Scikit-learn) for data analysis and machine learning
- **Interactive Shell** - PySpark shell for interactive data exploration and prototyping
- **Performance** - Near-native Spark performance despite Python overhead, optimized through JVM communication
- **Ease of Use** - Pythonic API making distributed computing accessible to Python developers

#### Core APIs:

- **SparkSession** - Unified entry point for PySpark functionality, replacing older SparkContext and SQLContext
  ```python
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("app").getOrCreate()
  ```

- **PySpark RDD API** - Low-level API for distributed data processing with Python objects
  - Creation methods: `parallelize()`, `textFile()`, `wholeTextFiles()`
  - Transformations: `map()`, `filter()`, `flatMap()`, `reduceByKey()`
  - Actions: `collect()`, `count()`, `take()`, `reduce()`

- **PySpark DataFrame API** - High-level API for structured data manipulation
  - Reading data: `spark.read.csv()`, `spark.read.json()`, `spark.read.parquet()`
  - Operations: `select()`, `filter()`, `groupBy()`, `join()`, `agg()`
  - SQL queries: `spark.sql("SELECT * FROM table")`

- **PySpark SQL Functions** - Built-in functions for data transformation (col, when, lit, concat, split)

#### Common Operations:

- **Data Loading** - Read from various sources (CSV, JSON, Parquet, databases, S3)
- **Data Transformation** - Apply operations using DataFrame API or SQL queries
- **Data Aggregation** - Group and aggregate data using groupBy() and aggregation functions
- **Data Writing** - Save results to different formats and storage systems

#### MLlib in PySpark:

- **ML Pipelines** - Framework for constructing and tuning machine learning workflows
- **Feature Engineering** - Transformers for feature extraction, scaling, and vectorization
- **Algorithms** - Classification, regression, clustering, recommendation models
- **Model Evaluation** - Metrics and cross-validation for model assessment

**📌 Quick Start Example:**
```python
# Read CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Transform
filtered_df = df.filter(df.age > 25).select("name", "age")

# Aggregate
result = df.groupBy("department").agg({"salary": "avg"})

# Write
result.write.parquet("output/")
```

---

### Data Lake Architecture

**Data Lake** is a centralized repository that stores vast amounts of raw data in its native format (structured, semi-structured, and unstructured) until needed. It provides a scalable, cost-effective storage solution for big data analytics.

#### Key Characteristics:

- **Schema-on-Read** - Data stored without predefined schema; structure applied during analysis
- **Raw Data Storage** - Preserves original data format and granularity for maximum flexibility
- **Scalability** - Horizontally scalable storage accommodating petabytes of data
- **Cost-Effective** - Uses commodity hardware and object storage (HDFS, S3, Azure Data Lake)
- **Diverse Data Types** - Supports structured (databases), semi-structured (JSON, XML), and unstructured (logs, images, videos)

#### Architecture Layers:

1. **Ingestion Layer** - Tools for batch and real-time data ingestion (Kafka, Flume, NiFi, custom ETL)
2. **Storage Layer** - Distributed file systems or object storage (HDFS, S3, Azure Blob Storage)
3. **Processing Layer** - Data processing engines (Spark, MapReduce, Flink) for transformation and analysis
4. **Catalog/Metadata Layer** - Metadata management and data discovery (Hive Metastore, AWS Glue, Atlas)
5. **Consumption Layer** - Analytics and BI tools (Spark SQL, Presto, Athena, Tableau)

#### Data Zones:

- **Raw/Landing Zone** - Ingested data in original format, immutable storage
- **Curated/Refined Zone** - Cleaned, validated, and transformed data
- **Consumption/Analytics Zone** - Aggregated, business-ready datasets for reporting

#### Challenges:

- ⚠️ **Data Swamp Risk** - Without governance, can become disorganized and unusable
- ⚠️ **Performance** - Querying raw data can be slow without optimization
- ⚠️ **Data Quality** - Lack of validation during ingestion may compromise quality
- ⚠️ **Security** - Requires robust access controls and data governance

**🎯 Best Practices:**
- Implement data governance from day one
- Define clear data zones and naming conventions
- Use metadata catalogs for discoverability
- Apply partitioning for query performance
- Establish data quality checks

---

### Lakehouse Architecture

**Lakehouse** is a modern data architecture combining the best features of data lakes and data warehouses, providing ACID transactions, schema enforcement, and governance on top of low-cost data lake storage.

#### Key Features:

- **ACID Transactions** - Ensures data consistency and reliability for concurrent operations
- **Schema Enforcement & Evolution** - Supports schema validation while allowing flexibility
- **Unified Storage** - Single platform for structured and unstructured data (eliminates data silos)
- **BI & ML Support** - Optimized for both business intelligence and machine learning workloads
- **Open Formats** - Uses open table formats (Delta Lake, Apache Iceberg, Apache Hudi)
- **Time Travel** - Access historical versions of data for audit and rollback

#### Architecture Components:

1. **Storage Layer** - Cloud object storage (S3, ADLS, GCS) with cost-effective scalability
2. **Metadata Layer** - Transaction log tracking all changes for ACID guarantees
3. **Table Format Layer** - Open formats providing structure (Delta Lake, Iceberg, Hudi)
4. **Processing Layer** - Unified engine for batch and streaming (Spark, Flink)
5. **Governance Layer** - Data quality, lineage, access control, and compliance

#### Popular Lakehouse Platforms:

- **Delta Lake** - Open-source storage layer bringing reliability to data lakes (Databricks)
- **Apache Iceberg** - Table format for huge analytic datasets (Netflix, Apple)
- **Apache Hudi** - Streaming data lake platform (Uber)
- **Databricks Lakehouse** - Unified analytics platform built on Delta Lake
- **AWS Lake Formation** - Service for building and managing data lakes

#### Lakehouse vs Data Lake vs Data Warehouse:

| Feature | Data Warehouse | Data Lake | Lakehouse |
|---------|---------------|-----------|-----------|
| Data Types | Structured only | All types | All types |
| Storage Cost | High | Low | Low |
| Performance | Excellent for BI | Variable | Excellent |
| Schema | Rigid (schema-on-write) | Flexible (schema-on-read) | Flexible with enforcement |
| ACID Support | ✅ Yes | ❌ No | ✅ Yes |
| Data Quality | High | Variable | High |
| ML Support | Limited | Good | Excellent |

#### Use Cases:

- ✅ **Real-Time Analytics** - Streaming data ingestion with immediate query capabilities
- ✅ **ML & AI** - Single platform for feature engineering, training, and inference
- ✅ **Data Science** - Exploratory analysis on diverse datasets with governance
- ✅ **Business Intelligence** - Fast SQL queries on structured data with reliability
- ✅ **Unified Analytics** - End-to-end analytics from raw data to insights without data movement

**💡 When to Choose Lakehouse:**
- Need both BI and ML/AI workloads
- Require ACID guarantees on data lake
- Want to eliminate data silos
- Need governance without sacrificing flexibility
- Processing both batch and streaming data

---

## 📚 Quick Reference Guide

**Technology Selection Decision Tree:**

```
Need to process big data?
├─ Batch processing only? → Hadoop MapReduce
├─ Need speed + flexibility? → Apache Spark
├─ Python developer? → PySpark
└─ Storage architecture?
   ├─ Raw data, cheap storage → Data Lake
   ├─ Structured data, fast queries → Data Warehouse
   └─ Best of both worlds → Lakehouse
```

**Common Integration Patterns:**
- **Hadoop + Spark**: Spark on YARN with HDFS storage
- **Lakehouse + Spark**: Delta Lake with Spark processing
- **Data Lake + PySpark**: S3 storage with PySpark analytics
- **End-to-End**: Kafka → Spark Streaming → Lakehouse → BI Tools
