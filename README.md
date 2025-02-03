Big Box Inventory Retrieval

🚀 Overview

This project creates a local server that holds inventory data and their associated physical location codes. Employees can access the server through their web browser and quickly input UPC codes to locate the associated items. I have added the python prototype, which includes all the features, without creating a local server to host the application.

✨ Features

  Inventory Data Storage: Loads and stores UPC codes and their corresponding location codes from a CSV file.

  Web-Based Search: Employees can enter a UPC suffix in their browser to locate items.

  Static File Hosting: Serves a frontend (index.html) from the public folder.

  Real-Time Data Retrieval: Queries the stored data and returns matching locations in JSON format via /search.

  CSV Parsing: Reads UPC-location mappings from a CSV file at startup.

🛠 Installation

Prerequisites

Install Node.js (Ensure you have Node.js installed on your system).

Required Dependencies

This project requires the following Node.js packages:

  - express (for creating the web server)

  - csv-parser (for parsing CSV files)

  - body-parser (for handling request bodies)

Steps to Install and Run

1. Clone the repository

git clone https://github.com/Karan-SB399/big-box-inventory.git
cd big-box-inventory

2. Install dependencies

npm install 

3. Ensure you have the required CSV file (SampleData.csv) inside the project directory.

4. Start the server

npm start

Access the application in your browser at http://localhost:3000.

📌 Usage

Web Interface:

  Open a web browser and navigate to http://localhost:3000

  Enter a UPC suffix in the search field to locate associated items.

  Matching storage locations will be highlighted on the shelf layout.


⚙️ Configuration

The project reads inventory data from SampleData.csv at startup.

Ensure the CSV file is correctly formatted with UPCs and location codes. I have added a sample file for reference.

The public folder contains static files, including styles.css and scripts.js.
