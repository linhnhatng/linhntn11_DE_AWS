import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AccelerometerLanding
AccelerometerLanding_node1682593595085 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1682593595085",
)

# Script generated for node CustomerTrusted
CustomerTrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_trusted",
    transformation_ctx="CustomerTrusted_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = Join.apply(
    frame1=CustomerTrusted_node1,
    frame2=AccelerometerLanding_node1682593595085,
    keys1=["email"],
    keys2=["user"],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Drop Fields
DropFields_node1682593773591 = DropFields.apply(
    frame=ApplyMapping_node2,
    paths=["user", "timestamp", "x", "y", "z"],
    transformation_ctx="DropFields_node1682593773591",
)

# Script generated for node CustomerCurated
CustomerCurated_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1682593773591,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://stedi-lh/customer/curated/", "partitionKeys": []},
    transformation_ctx="CustomerCurated_node3",
)

job.commit()
