# Databricks notebook source
# MAGIC %md # Forecasting Data

# COMMAND ----------

# MAGIC %md ## Simple Forecasting Methods
# MAGIC 
# MAGIC - https://www.otexts.org/fpp/2/3
# MAGIC 
# MAGIC ### Average Method
# MAGIC ### Naïve method
# MAGIC ### Seasonal naïve method
# MAGIC ### Drift method
# MAGIC ### Examples

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Cyclic and Seasonal Time Series
# MAGIC - http://robjhyndman.com/hyndsight/cyclicts/
# MAGIC 
# MAGIC ### Seasonal Pattern
# MAGIC A seasonal pattern exists when a series is influenced by seasonal factors (e.g., the quarter of the year, the month, or day of the week). Seasonality is always of a fixed and known period. Hence, seasonal time series are sometimes called periodic time series.
# MAGIC 
# MAGIC ### Cyclic Pattern
# MAGIC A cyclic pattern exists when data exhibit rises and falls that are not of fixed period. The duration of these fluctuations is usually of at least 2 years. Think of business cycles which usually last several years, but where the length of the current cycle is unknown beforehand.

# COMMAND ----------

# MAGIC %md ## Resources
# MAGIC 
# MAGIC ### Online Forecasting Textbook (Hyndman)
# MAGIC - https://www.otexts.org/fpp/1/1
# MAGIC 
# MAGIC ### Prophet 
# MAGIC - http://blog.revolutionanalytics.com/2017/02/facebook-prophet.html
# MAGIC - https://facebookincubator.github.io/prophet/docs/quick_start.html#python-api
# MAGIC 
# MAGIC ### Charting a time-series in D3
# MAGIC - https://github.com/mcaule/d3-timeseries
# MAGIC - https://bl.ocks.org/mbostock/1157787
# MAGIC  
