import matplotlib.pyplot as plt
from financeObj import *
from Factory import *
import sys


ticker = sys.argv[-1]
obj = financeObj(ticker)

# bj.pickTicker()


factory = Factory(obj)
#factory.CallsOIMap()
#factory.CallsVolume3D()
#factory.CallsVolumeMap()

#factory.PutsVolume3D()
#factory.PutsVolumeMap()

print("Ticker is " + ticker)
def repeat():
    print("PICK ONE: optionChain, OIimage, CallsVolumeMap, CallsOIMap, PutsVolumeMap, PutsOIMap, CallsVolume3D, CallsOI3D, PutsVolume3D, PutsOI3D, exit")
    choice = input().lower()
    if choice == "pickstrike":
        obj.pickStrike()
        factory.update()
        repeat()
    elif choice == "optionchain":
        print(obj.getOptionChain())
        repeat()
    elif choice == "oiimage":
        factory.OIChart()
        repeat()
    elif choice == "callsvolumemap":
        factory.CallsVolumeMap()
        repeat()
    elif choice == "callsoimap":
        factory.CallsOIMap()
        repeat()
    elif choice == "putsvolumemap":
        factory.PutsVolumeMap()
        repeat()
    elif choice == "putsoimap":
        factory.PutsOIMap()
        repeat()
    elif choice == "callsvolume3d":
        factory.CallsVolume3D()
        repeat()
    elif choice == "callsoi3d":
        factory.CallsOI3D()
        repeat()
    elif choice == "putsvolume3d":
        factory.PutsVolume3D()
        repeat()
    elif choice == "putsoi3d":
        factory.PutsOI3D()
        repeat()
    elif choice == "exit":
        sys.exit()
    else:
        print("unexpected choice")
        repeat()


repeat()
