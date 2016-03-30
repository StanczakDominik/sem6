import numpy as np
from time import sleep
string = """/emc/det/setMat foo
/emc/scorers/dump/trajectories 0
/emc/initial_energy {} MeV

/random/setSeeds {} {}

/run/beamOn 100000"""

for e in [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]:
    filename = "{}.cfg".format(e)
    x, y = np.random.randint(low=0,high=2**16-1,size=2)
    print("start")
    #write multiline string to file
    print(string.format(e,x,y))
    print("finish")
    sleep(1)

# for file.cfg in dir
# run async geant4sim.exe file.cfg
