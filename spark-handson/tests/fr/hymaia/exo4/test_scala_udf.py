import unittest
from tests.fr.hymaia.spark_session_test import spark
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pyspark.sql.functions as F
from src.fr.hymaia.exo4.scala_udf import addCategoryName


