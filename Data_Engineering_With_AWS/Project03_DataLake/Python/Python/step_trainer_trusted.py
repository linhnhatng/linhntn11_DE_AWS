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

# Script generated for node Customer Curated
CustomerCurated_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-lh/customer/curated/"], "recurse": True},
    transformation_ctx="CustomerCurated_node1",
)

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1682598821285 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lh/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1682598821285",
)

# Script generated for node Renamed keys for ApplyMapping
RenamedkeysforApplyMapping_node1682601267346 = ApplyMapping.apply(
    frame=StepTrainerLanding_node1682598821285,
    mappings=[
        ("sensorReadingTime", "bigint", "`(right) sensorReadingTime`", "bigint"),
        ("serialNumber", "string", "`(right) serialNumber`", "string"),
        ("distanceFromObject", "int", "`(right) distanceFromObject`", "int"),
    ],
    transformation_ctx="RenamedkeysforApplyMapping_node1682601267346",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = Join.apply(
    frame1=CustomerCurated_node1,
    frame2=RenamedkeysforApplyMapping_node1682601267346,
    keys1=["serialNumber"],
    keys2=["`(right) serialNumber`"],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Drop Fields
DropFields_node1682598840607 = DropFields.apply(
    frame=ApplyMapping_node2,
    paths=[
        "email",
        "lastUpdateDate",
        "phone",
        "shareWithPublicAsOfDate",
        "shareWithResearchAsOfDate",
        "shareWithFriendsAsOfDate",
        "birthDay",
        "timeStamp",
        "registrationDate",
    ],
    transformation_ctx="DropFields_node1682598840607",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1682598840607,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lh/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node3",
)

job.commit()
