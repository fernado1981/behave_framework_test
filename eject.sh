#!/bin/bash

# Delete any previous report files
rm -f reports/allure-results/*.json

# Run Every tuto
#for folder in features/orange_hrm/*; do
  behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features
  #behave $folder -f json.pretty -o reports/allure-results/$folder.json || true;
#done

# Convert every report to cucumber format for further jenkins report
#for f in reports/allure/results/* ; do
 # python convert2cucumber.py $f
#done
