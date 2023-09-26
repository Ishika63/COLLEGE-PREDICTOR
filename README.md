# COLLEGE-PREDICTOR


College Predictor is a web application built with Flask that helps predict colleges based on various input criteria, including rank, branch, seat pool and category. This project aims to assist students in making informed decisions about their college choices.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Screenshorts](#screenshorts)

## Getting Started

These instructions will guide you through setting up and running the College Predictor locally for testing and development purposes.

### Prerequisites

Before you begin, make sure you have the following software installed on your system:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/COLLEGE-PREDICTOR.git

2. Navigate to the project directory:

   ```bash
   cd COLLEGE-PREDICTOR
   
3. Install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt

### Running the Application

4. Start the Flask development server:

   ```bash
   python app.py
   
5. Access the web application in your web browser:

   ```bash
   http://127.0.0.1:5000/new
   
6. Fill in the form with your input criteria and submit to get college predictions.


## Project Structure

The structure of the project is organized as follows:

1. **`app.py`**: This file contains the main Flask application. It's where the web application logic is implemented, including routing and handling user requests.

2. **`templates/`**: This directory contains HTML templates used to render web pages. You can customize these templates to change the look and feel of the application.

3. **`ROUND1/`, `ROUND2/`, `ROUND3/`, `ROUND4/`**: This directory is where you store CSV files that contain data for colleges and their details. The application reads these CSV files to provide predictions based on user input.


## Screenshorts

![1](https://github.com/Ishika63/COLLEGE-PREDICTOR/assets/80192358/4047f448-3e79-49e6-82a0-eb69937b60c1)

![2](https://github.com/Ishika63/COLLEGE-PREDICTOR/assets/80192358/b2172245-be1b-4f4f-ae95-1d1a1487bb73)

![3](https://github.com/Ishika63/COLLEGE-PREDICTOR/assets/80192358/49bb2621-825d-4b19-a1ec-f95d5299a16c)

![4](https://github.com/Ishika63/COLLEGE-PREDICTOR/assets/80192358/2654478d-b696-4884-9d5e-6d34c92c2196)

![5](https://github.com/Ishika63/COLLEGE-PREDICTOR/assets/80192358/aebf9be6-69a0-4861-bb56-b45f97b924f9)






