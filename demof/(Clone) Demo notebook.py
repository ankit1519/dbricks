# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %run ./setup

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls("/databricks-datasets")
display(files)

# COMMAND ----------


