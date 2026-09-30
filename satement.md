# Project: Weather App - Real-Time Weather CLI

## Problem Statement

Checking basic weather updates often requires navigating ad-heavy websites or bloated mobile applications. Users and developers who spend significant time working in a command-line environment lack a simple, fast, and lightweight tool to check immediate weather conditions for any city without leaving the terminal.

## Scope of the Project

This project is a lightweight, procedural Python application designed to retrieve and display live weather data. The application prompts the user for a city name, communicates with the OpenWeatherMap REST API using the `requests` library, parses the returned JSON payload, and formats key weather parameters—such as temperature, weather conditions, humidity, and wind speed—into a clean console display. It includes basic HTTP status verification to handle invalid city names or connection failures gracefully.

## Target Users

* Terminal enthusiasts looking for a quick, text-based weather utility.
* Students and beginner developers seeking a clear example of Python REST API consumption and JSON parsing.
* Anyone needing immediate, distraction-free weather reports.

## High-Level Features

**Interactive Console Input:** Prompts the user to enter any city name dynamically upon execution.

**Live API Ingestion:** Fetches real-time weather metrics in metric units (°C, m/s) via OpenWeatherMap's REST endpoint.

**Data Extraction & Formatting:** Parses raw JSON responses and presents essential attributes—temperature, condition description, humidity percentage, and wind speed—in a structured format.

**Response Status Handling:** Validates HTTP status codes (verifying `200 OK`) and delivers a helpful error message if the input city is not found or if the API call fails.