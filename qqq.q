// Define the table
trades: ([] date: .z.d + til 3; sym: `AAPL`GOOG`MSFT; price: 100.5 102.3 98.6; volume: 1000 2000 1500)

// The directory path where you want to save the table
outputPath: `:c:/kdb/data/

// Use .Q.dpft to partition and save the table
.Q.dpft[outputPath; trades.date; `date; `trades]
