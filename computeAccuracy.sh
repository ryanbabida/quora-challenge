
thresholds=(0.1 0.2 0.3 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.8 1.0)

MAX=0
MAX_OUTPUT=0

for i in ${thresholds[@]}
do
	OUTPUT=$(python compute_accuracy.py training.csv $i)
	if (( $(echo "$OUTPUT > $MAX_OUTPUT" |bc -l) ))
	then
		MAX=$i
		MAX_OUTPUT=$OUTPUT
	fi
	echo "Training accuracy with threshold of $i: $OUTPUT"
done

echo "Best accuracy $MAX_OUTPUT with threshold of $MAX"

echo "Now calculating with validation set..."
OUTPUT=$(python compute_accuracy.py validation.csv $MAX)

echo "Validation cccuracy with threshold of $MAX: $OUTPUT"
echo "done"
