01-02-2022 - scripts to calculate root zone storage capacity globally

1) grid_to_catchments_final -> match gridded data products with catchment shapes and extract timeseries for catchments
2) postprocess_grid_to_catchments -> postprocess the catchment timeseries to get mean values, yearly values, and combined csv tables of different data products
3) google_earth_engine_treecoverdata -> in the code editor of earth engine extract mean tree cover (MODIS satellite) for all catchments
4) process_treecover_data -> process treecover data to usable tables
5) catchment_waterbalance -> evaluate catchment water balances using the timeseries
6) catchment_characteristics -> calculate catchment characteristics based on timeseries and store in tables
7) sr_calculation -> calculate root zone storage capacity based on catchment timeseries

8) linear regression model -> script in progress, not uploaded yet
