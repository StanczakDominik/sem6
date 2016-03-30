#!/bin/bash
echo '/emc/det/setMat foo'
echo '/emc/scorers/dump/trajectories 0'
echo ''
echo "/emc/initial_energy $1 MeV"
echo ''
echo ''
echo "/random/setSeeds $RANDOM $RANDOM"
echo ''
echo '/run/beamOn 100000'
