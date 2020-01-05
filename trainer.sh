#!/bin/bash

python neg_file_writer.py
python pos_file_writer.py

for file in "pos"/*
do
    COUNTER=$(expr $COUNTER + 1)
    opencv_createsamples -img $file -bg neg.txt -info info/$COUNTER/info.lst -pngoutput -maxxangle 0.1 -maxyangle 0.1 -maxzangle 0.1
done

for dir in "info"/*
do
    opencv_createsamples -info $dir/info.lst -num 1950 -w 20 -h 20 -vec $dir/positives.vec
done

if [ ! -d "vectors" ]; then
  mkdir "vectors"
fi

for dir in "info"/*
do
    COUNTER=$(expr $COUNTER + 1)
    mv $dir/positives.vec vectors/$COUNTER.vec
done

python mergevec.py -v vectors -o positives.vec

opencv_traincascade -data data -vec positives.vec -bg neg.txt -numPos 10000 -numNeg 502 -numStages 20 -w 20 -h 20 -maxFalseAlarmRate 0.2
opencv_traincascade -data data -vec positives.vec -bg neg.txt -numPos 10000 -numNeg 502 -numStages 20 -w 20 -h 20 -maxFalseAlarmRate 0.2

mv data/cascade.xml detectortje.xml