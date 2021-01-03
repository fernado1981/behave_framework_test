#!/bin/bash

# Delete any previous report files
rm -f reports/allure-results/*.json

behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features