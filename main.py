import painting

m2inkCostEu=1.0         #price of the ink for square meter
fixedCostsEu=0.0        #fixed costs for a room (time lost to prepare and materials)

m2timeCostHours=0.2             #time to paint a square meter
humanPricePerHourEu=15.0        #employee costs per hour

R1 = painting.room(1,"DINING")
R1.calcAll(6.0, 5.0, 2.80, m2inkCostEu, fixedCostsEu, m2timeCostHours, humanPricePerHourEu )
R1.report()

R2 = painting.room(2,"BATH")
R2.calcAll(2.0, 5.0, 2.80, m2inkCostEu, fixedCostsEu, m2timeCostHours, humanPricePerHourEu )
R2.report()

tot=R1.total() + R2.total()

print ("TOTAL COSTS: " + str(tot) + " EU")

del R1
del R2
