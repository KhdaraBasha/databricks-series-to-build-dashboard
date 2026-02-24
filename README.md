# Databricks Series: Data Extraction and Dashboard

## Project Overview
This project demonstrates a data extraction pipeline that downloads CSV and JSON files from a remote GitHub repository, saves them locally, and prepares them for further analytics and dashboarding in Databricks.

## Folder Structure
- `github_data_extrcator.py`: Main script to run the extraction pipeline.
- `utility/extractors.py`: Utility functions for extracting and saving CSV/JSON files.
- `extracted_data/`: Folder where all extracted files are saved.
- `requiremnets.txt`: Python dependencies.

## Data Extraction Process
1. **Environment Setup**: The script loads environment variables (such as the base URL) from a `.config` file using `python-dotenv`.
2. **File Lists**: Lists of CSV and JSON files to extract are defined in the main script.
3. **Extraction Functions**: Utility functions handle downloading and saving of each file type.
4. **Output**: Extracted files are saved in the `extracted_data/` directory for further use.

## Example Data Columns
### Emissions_Data_2023.csv
- `state_id`, `state_abbr`, `county_state_name`, `county_id`, `county_name`, `latitude`, `longitude`, ...
	- Contains emissions, population, utility, and climate data by county.

### customerscsv.csv
- `customer_id`, `first_name`, `last_name`, `country`, `signup_date`
	- Customer master data.

### orderscsv.csv
- `order_id`, `customer_id`, `product_id`, `order_date`, `quantity`, `total_amount`
	- Order transactions.

### productscsv.csv
- `product_id`, `product_name`, `category`, `price`
	- Product catalog.

## Next Steps
After extraction, you can push the data to Databricks and use it to build interactive dashboards and analytics.

---
**Author:** [Your Name]
**Last Updated:** February 24, 2026