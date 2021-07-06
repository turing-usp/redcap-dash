import awswrangler as wr


path = "s3://turing-redcap-dashboard/dataset/"

df = wr.s3.read_parquet(path, dataset=True)
