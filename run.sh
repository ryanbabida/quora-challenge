#!/usr/bin/env bash

echo "Problem 2: Now computing overlap scores for training.csv..."
python ComputeScore.py training.csv

echo
echo

thresholds=(0.1 0.2 0.3 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.8 1.0)

MAX=0
MAX_OUTPUT=0

echo "Problem 3: Now computing accuracy with stop words..."

for i in ${thresholds[@]}
do
	OUTPUT=$(python ComputeAccuracy.py training.csv $i)
	if (( $(echo "$OUTPUT > $MAX_OUTPUT" |bc -l) ))
	then
		MAX=$i
		MAX_OUTPUT=$OUTPUT
	fi
	echo "Training accuracy with threshold of $i: $OUTPUT"
done

echo "Best accuracy $MAX_OUTPUT with threshold of $MAX"

echo "Now calculating with validation set..."
OUTPUT=$(python ComputeAccuracy.py validation.csv $MAX)

echo "Validation accuracy with threshold of $MAX: $OUTPUT"
echo "done"

echo
echo

echo "Problem 4: Now computing accuracy with removing stop words..."


MAX=0
MAX_OUTPUT=0

for i in ${thresholds[@]}
do
	OUTPUT=$(python AccuracyRemoveStops.py training.csv $i)
	if (( $(echo "$OUTPUT > $MAX_OUTPUT" |bc -l) ))
	then
		MAX=$i
		MAX_OUTPUT=$OUTPUT
	fi
	echo "Training accuracy with threshold of $i: $OUTPUT"
done

echo "Best accuracy $MAX_OUTPUT with threshold of $MAX"

echo "Now calculating with validation set..."
OUTPUT=$(python AccuracyRemoveStops.py validation.csv $MAX)

echo "Validation accuracy with threshold of $MAX: $OUTPUT"
echo "done"