from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower

# Initialize Spark session
spark = SparkSession.builder.appName("TwitterRacismAnalysis").getOrCreate()

# Define keywords
keywords = ["cina", "Cina", "CINA", "jawir", "Jawir", "JAWIR", "sunda", "Sunda", "SUNDA", "bule", "Bule", "BULE", "jawa", "Jawa", "nigga", "Nigga", "NIGGA", "nigger", "Nigger", "NIGGER", "negro", "Negro", "NEGRO", "kontol", "Kontol", "KONTOL"]

# List to store results
results = []

# Process each year
for year in range(2020, 2025):
    # Load data
    df = spark.read.csv(f"hdfs://localhost:9000/user/dataset/{year}.csv", header=True, inferSchema=True)
    
    # Check if the dataframe contains the column 'full_text'
    if 'full_text' not in df.columns:
        print(f"Column 'full_text' not found in year {year} dataset")
        continue
    
    # Filter tweets containing any of the keywords
    df_filtered = df.filter(
        lower(col("full_text")).contains(keywords[0]) |
        lower(col("full_text")).contains(keywords[1]) |
        lower(col("full_text")).contains(keywords[2]) |
        lower(col("full_text")).contains(keywords[3]) |
        lower(col("full_text")).contains(keywords[4]) |
        lower(col("full_text")).contains(keywords[5]) |
        lower(col("full_text")).contains(keywords[6]) |
        lower(col("full_text")).contains(keywords[7]) |
        lower(col("full_text")).contains(keywords[8]) |
        lower(col("full_text")).contains(keywords[9]) |
        lower(col("full_text")).contains(keywords[10]) |
        lower(col("full_text")).contains(keywords[11]) |
        lower(col("full_text")).contains(keywords[12]) |
        lower(col("full_text")).contains(keywords[13]) |
        lower(col("full_text")).contains(keywords[14]) |
        lower(col("full_text")).contains(keywords[15]) |
        lower(col("full_text")).contains(keywords[16]) |
        lower(col("full_text")).contains(keywords[17]) |
        lower(col("full_text")).contains(keywords[18]) |
        lower(col("full_text")).contains(keywords[19]) |
        lower(col("full_text")).contains(keywords[20]) |
        lower(col("full_text")).contains(keywords[21]) |
        lower(col("full_text")).contains(keywords[22]) |
        lower(col("full_text")).contains(keywords[23]) |
        lower(col("full_text")).contains(keywords[24]) |
        lower(col("full_text")).contains(keywords[25])
    )
    
    # Count the number of filtered tweets
    count = df_filtered.count()
    results.append((year, count))

# Create a DataFrame from results
results_df = spark.createDataFrame(results, ["Year", "Number of Racist Tweets"])

# Save results to HDFS
results_df.write.csv("hdfs://localhost:9000/user/data_output/racist_tweets_count_prebuild-2.csv", header=True)

# Print results
results_df.show()

# Stop Spark session
spark.stop()
