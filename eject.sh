#!/bin/bash

rm -f reports/allure-results/*.json

behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features