const express = require("express");
const fs = require("fs");
const csv = require("csv-parser");
const path = require("path");

const app = express();
const PORT = 3000;

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, "public")));

// Data storage
let upcMapping = {};

// Function to load the CSV data
function importUpcData(filePath) {
  const cellCodes = [];
  for (let shelf = 0; shelf < 3; shelf++) {
    for (let row = 0; row < 5; row++) {
      for (let col = 0; col < 3; col++) {
        cellCodes.push(`${shelf}${row}${col}`);
      }
    }
  }

  const mapping = {};
  let currentCell = null;

  return new Promise((resolve, reject) => {
    fs.createReadStream(filePath)
      .pipe(csv())
      .on("data", (row) => {
        const value = Object.values(row)[0]?.trim(); // First column value
        if (cellCodes.includes(value)) {
          currentCell = value;
          mapping[currentCell] = [];
        } else if (currentCell) {
          mapping[currentCell].push(value);
        }
      })
      .on("end", () => {
        upcMapping = mapping;
        resolve(mapping);
      })
      .on("error", (err) => reject(err));
  });
}

// Load CSV at startup
importUpcData(path.join(__dirname, "SampleData.csv"))
  .then(() => console.log("CSV loaded successfully:", upcMapping))
  .catch((err) => console.error("Error loading CSV:", err));

// Endpoint to fetch data
app.get("/search", (req, res) => {
  const upcSuffix = req.query.upc || ""; // Get the `upc` parameter
  if (!upcSuffix) {
    return res.status(400).send("UPC suffix is required.");
  }

  const foundCells = [];
  for (const [cell, upcs] of Object.entries(upcMapping)) {
    if (upcs.some((upc) => upc.endsWith(upcSuffix))) {
      foundCells.push(cell);
    }
  }

  // Return results as JSON
  res.json({
    query: upcSuffix,
    cells: foundCells,
  });
});

// Serve the HTML page
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

// Start the server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});