import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# TEST 1 - Bookmark - s3
# datasource_bk = glueContext.create_dynamic_frame.from_catalog(
#         database="default",
#         table_name='students',
#         transformation_ctx = "datasource_bk"
#     )

#datasource_bk.show()


# TEST 2 - Bookmark - JDBC (PK O)
# RDS TABLE DDL
# create table bktable (
#   rollno  INT PRIMARY KEY,
#   name varchar(10), 
#   age int, 
#   height varchar(10), 
#   weight varchar(10), 
#   address varchar(50));
  
# datasource_bk_jdbc = glueContext.create_dynamic_frame.from_catalog(
#     database="default",
#     table_name="test_bktable",
#     transformation_ctx="datasource_bk_jdbc"
#     )

# datasource_bk_jdbc.show()


# TEST 3 - Bookmark - JDBC (PK X)
# create table bktable_nopk (
#   rollno  INT,
#   name varchar(10), 
#   age int, 
#   height varchar(10), 
#   weight varchar(10), 
#   address varchar(50));
  
datasource_bk_jdbc2 = glueContext.create_dynamic_frame.from_catalog(
    database="default",
    table_name="test_bktable_nopk",
    transformation_ctx="datasource_bk_jdbc2",
    additional_options = {"jobBookmarkKeys":["rollno"],"jobBookmarkKeysSortOrder":"asc"}
    )
    
datasource_bk_jdbc2.show()


job.commit()