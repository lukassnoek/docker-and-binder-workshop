# Script takes one argument, which should be
# the data.csv file
data=$1

# Calculate the sum of the data, as a proxy
# for a real analysis
sum=$(numsum $data)

# Print out the results!
echo "Result of analysis (sum): $sum"