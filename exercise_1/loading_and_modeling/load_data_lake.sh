#!/bin/bash

# save my current working directory
MY_CWD=$(pwd)

# creating staging directories
mkdir ~/staging
mkdir ~/staging/exercise_1

# downloading zip file from data.medicare.gov
MY_URL="https://data.medicare.gov/views/bg9k-emty/files/4a66c672-a92a-4ced-82a2-033c28581a90?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"
wget "$MY_URL" -O medicare_data.zip

# unzipping the medicare data file
unzip medicare_data.zip

# removing first lines of files and renaming

OLD_FILE="Hospital General Information.csv"
NEW_FILE="hospitals.csv"
tail -n +2 "$OLD_FILE" >$NEW_FILE

OLD_FILE="Timely and Effective Care - Hospital.csv"
NEW_FILE="effective_care.csv"
tail -n +2 "$OLD_FILE" >$NEW_FILE

OLD_FILE="Complications and Deaths - Hospital.csv"
NEW_FILE="readmissions.csv"
tail -n +2 "$OLD_FILE" >$NEW_FILE

OLD_FILE="Measure Dates.csv"
NEW_FILE="measures.csv"
tail -n +2 "$OLD_FILE" >$NEW_FILE

OLD_FILE="hvbp_hcahps_11_10_2016.csv"
NEW_FILE="survey_responses.csv"
tail -n +2 "$OLD_FILE" >$NEW_FILE

# create our main hospital compare hdfs directory
hdfs dfs -mkdir /user/w205/hospital_compare

# create a hdfs directory for each file and copy each file to hdfs

hdfs dfs -mkdir /user/w205/hospital_compare/hospitals
hdfs dfs -put hospitals.csv /user/w205/hospital_compare/hospitals

hdfs dfs -mkdir /user/w205/hospital_compare/effective_care
hdfs dfs -put effective_care.csv /user/w205/hospital_compare/effective_care

hdfs dfs -mkdir /user/w205/hospital_compare/readmissions
hdfs dfs -put readmissions.csv /user/w205/hospital_compare/readmissions

hdfs dfs -mkdir /user/w205/hospital_compare/measures
hdfs dfs -put measures.csv /user/w205/hospital_compare/measures

hdfs dfs -mkdir /user/w205/hospital_compare/survey_responses
hdfs dfs -put survey_responses.csv /user/w205/hospital_compare/survey_responses

# change directory back to the original
cd $MY_CWD

# clean exit
exit
