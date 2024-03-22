# Databricks notebook source
# Mount ADLS Gen2 using SAS token
container_name = "raw"
storage_account_name = "ucsc01"
sas_token = "sp=r&st=2024-03-17T18:18:31Z&se=2024-03-18T02:18:31Z&spr=https&sv=2022-11-02&sr=c&sig=OYbCIJHWncI1GNaHiby%2BzzINSBvtYGLuVbEpvyBfLxM%3D"

mount_command = f"""dbutils.fs.mount(
  source="abfss://{container_name}@{storage_account_name}.dfs.core.windows.net",
  mount_point="/mnt/salary.csv",
  extra_configs={{"fs.azure.sas.raw.ucsc01.dfs.core.windows.net": "{sas_token}"}}
)"""
exec(mount_command)
