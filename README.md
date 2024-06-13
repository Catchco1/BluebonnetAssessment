# BluebonnetAssessment
Technical assessment for Bluebonnet Internship

I chose Task 1: Scripting/Data Wrangling. 

All of the initial data is stored in the `data` directory. 

The output files of the script are already present in the `output` directory, but the script will recreate them if needed.

The script accomplishes the two goals of first combining the general and primary election data into a single data set for each election, and then determining if there are any duplicate voters in either data set. If there are duplicate voters, it prints out which data set contains duplicates and then prints the duplicated rows. If there are not duplicates, it prints out the required string "No Duplicates Found in [Dataset Name]!”

Please reach out if you have any questions!

# Running the code

1. Pull code from this repo.

2. Install appropriate Python dependencies using pip: `pip install -r requirements.txt`

3. Run the script: `python wrangling.py`