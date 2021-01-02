#!/bin/bash

# Delete any previous report files
rm -f reports/allure/results/*.json

# Run Every feature
for folder in features/orange_hrm/orange*; do
	behave $folder -f json.pretty -o reports/allure/results/$folder.json || true;
done

cp -R reports/allure/results/features/orange_hrm/orange*.json reports/allure

# Convert every report to cucumber format for further jenkins report
for f in reports/allure/results/features/orange_hrm/* ; do
	python convert2cucumber.py $f
done
