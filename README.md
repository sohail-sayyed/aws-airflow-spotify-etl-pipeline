# Spotify Data Pipeline with Airflow, S3, AWS Glue, and Athena

## 🎵 Efficient Spotify Data Management with AWS and Airflow
This project demonstrates a powerful data pipeline that handles Spotify API data extraction, processing, and storage. Using Apache Airflow, the pipeline uploads data to Amazon S3, with schema discovery by AWS Glue and querying enabled through Amazon Athena.

This solution is ideal for developers seeking to build scalable ETL pipelines, manage data workflows, and perform SQL-based analytics on cloud infrastructure.

## 📂 Table of Contents:
1. Key Features
2. Tech Stack
3. Architecture Overview
4. Setup Instructions
5. How It Works
6. Directory Structure
7. Potential Improvements
8. License
9. Contact

## 🌟 Key Features:
- **Spotify API Integration:** Automate the retrieval of data about songs, artists, and playlists.
- **Apache Airflow Orchestration:** Manage complex task dependencies in the ETL pipeline.
- **Amazon S3 Storage:** Store and retrieve raw and processed data with ease.
- **AWS Glue Schema Discovery:** Automatically detect and catalog data structure in S3 buckets.
- **Amazon Athena Querying:** Perform scalable, serverless queries using SQL.
- **Dockerized Deployment:** Simplified setup and portability with Docker Compose.

## 🛠️ Tech stack:
- **Programming Language:** Python 3.x
- **Data Orchestration:** Apache Airflow
- **Containerization:** Docker
- **Cloud Storage:** Amazon S3
- **Data Catalog:** AWS Glue
- **Query Engine:** Amazon Athena
- **Cloud Hosting:** AWS EC2

## 🏗️ Architecture Overview:

### Workflow Diagram

![Airflow-AWS-SPotify-ETL-Pipeline](https://drive.google.com/uc?export=view&id=1XGE3MN0p2HQ6x_imBi6W29v6R6T0fTbV)

### Key Workflow Steps:
- **Extract Data:** Fetch tracks, playlists, and metadata using the Spotify API.
- **Process Data:** Transform and validate data through Airflow DAGs.
- **Upload to S3:** Store both raw and processed data in dedicated Amazon S3 buckets.
- **Run AWS Glue Crawler:** Automate schema discovery to populate the AWS Glue Data Catalog.
- **Query with Athena:** Use Athena for insights and analysis with SQL queries.

## 🚀 Setup Instructions:

### Prerequisites:
- Active AWS Account
- Installed: Docker, Docker Compose, and Python 3.x
- Spotify Developer Account with valid API credentials
- Configure Environment Variables: Add Spotify API credentials and AWS access keys.

### 📘 How It Works:

**Key Pipeline Tasks**
1. **Data Extraction:**
     - Use the Spotify Web API to fetch data.
     - Store raw JSON files in the S3 raw bucket.
2.  **Data Processing:**
      - Transform JSON into parquet format for efficiency.
      - Save to the S3 processed bucket.
3. **AWS Glue Crawling:**
     - Automatically discover schema for both raw and processed datasets.
4. **Query Execution:**
     - Run SQL queries on Athena for reporting and analytics.

### 🚀 Potential Improvements:

- Add streaming support for real-time Spotify updates using AWS Kinesis.
- Enhance data visualization with dashboards using AWS QuickSight.
- Integrate automated infrastructure management with Terraform or AWS CDK.
- Extend functionality to other music platforms like Apple Music API.

### 📲 Contact:

- Author: Sohail Sayyed
- Email:  ["**Gmail**"](jabmsohail@gmail.com)
- LinkedIn: ["**LinkedIn**"](https://www.linkedin.com/in/sohailsayyed09/)
- GitHub: ["**Github**"](https://github.com/Sohail-09)
