#!/bin/bash
mkdir bash
for i in 1 2 5 10 20 50 100 200 500 1000 2000 5000; do
  ./make_cfg.sh $i > bash/$i.cfg
done

for i in 1 2 5 10 20 50 100 200 500 1000 2000 5000; do
  ./geant4sim.exe bash/$i.cfg &
  echo $i
done
echo "waiting"
wait
echo "done waiting"
rm -r bash
