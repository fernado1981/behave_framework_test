#!/bin/bash
#esto es una prueba
behave -f allure_behave.formatter:AllureFormatter -o reports/allure/results ./features
allure serve reports/allure/results
