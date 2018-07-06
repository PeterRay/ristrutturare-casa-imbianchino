# minimal unit element for 
class room:
   def __init__(self, id, name):
       self.id = id                     # room id
       self.name = name               # room name    
   
       #room phisical size    
       self._height = 0.0
       self._width = 0.0
       self._lenght = 0.0 
       self._surface_calc = 0.0         #square meters to be processed by employee 
        
       #costs 
       self._m2InkCostEu = 0.0          # materials costs (ink cost per sqare meter)
       self._fixedCostsEu = 0.0         # costs for covers or sticks or other consumig materials
       self._totMaterialCosts = 0.0     # sum of materials costs

       self._m2timeCostHours = 0.0      # costs in terms of time to make one square meter
       self._humanPricePerHourEu = 0.0  # employee net cost per hour 
       self._totHumanCosts = 0.0        # human costs to complete the room 

       self._total=0.0                  # sum

   
   # square meters to be painted for this room
   def surface(self, width, lenght, height):
       self._height = height
       self._width = width
       self._lenght = lenght
       self._surface_calc = (2.0 * ((self._height * self._width) + ( self._height * self._lenght))) + (self._width*self._lenght)
       pass
 
   # m2inkCostEu : price to be spent for each square meter of ink
   # fixedCostsEu : fixed costs that will be simply added to materials
   def materialCosts(self, m2inkCostEu, fixedCostsEu ):
       self._m2InkCostEu = m2inkCostEu
       self._fixedCostsEu = fixedCostsEu   
       self._totMaterialCosts = (self._m2InkCostEu*self._surface_calc) + self._fixedCostsEu
       pass

   # m2timeCostHours : costs in terms of time to make one square meter
   # humanPricePerHourEu : costs in terms of euro for the employee
   def humanCosts(self, m2timeCostHours, humanPricePerHourEu ):
       self._m2timeCostHours = m2timeCostHours
       self._humanPricePerHourEu = humanPricePerHourEu
       self._totHumanCosts = (self._m2timeCostHours*self._surface_calc) * self._humanPricePerHourEu
       pass

   def total(self):
       self._total=self._totMaterialCosts+self._totHumanCosts  
       pass

   def calcAll(self, width, lenght, height, m2inkCostEu, fixedCostsEu, m2timeCostHours, humanPricePerHourEu ):
       self.surface(width, lenght, height)         
       self.materialCosts(m2inkCostEu, fixedCostsEu)        
       self.humanCosts( m2timeCostHours, humanPricePerHourEu)
       self.total()  

   def total(self):
       self._total=self._totMaterialCosts + self._totHumanCosts
       return self._total

   def report(self):
       self.total()

       print("room[" + str(self.id) + "]<" + self.name + "> --------------------------------------------------------------------------BEGIN")

       print("room[" + str(self.id) + "]<" + self.name + ">  Width(m):" + str(self._width) + "  Lenght(m):" + str(self._lenght) + "  Height(m):"+str(self._height)+ "  -->  SURFACE(m2): " + str(self._surface_calc))

       print("room[" + str(self.id) + "]<" + self.name + ">  InkCost(m2):" + str(self._m2InkCostEu) + " FixedCost(eu):" + str(self._fixedCostsEu) + " TOT. MAT. COSTS(eu) --->" + str(self._totMaterialCosts) )

       print("room[" + str(self.id) + "]<" + self.name + ">  timeCostPerMeterInHours(hours):" + str(self._m2timeCostHours) + "   HumanPricePerHour(eu):" + str(self._humanPricePerHourEu) + " TOT. HUMAN. COSTS(eu) --->" + str(self._totHumanCosts))
       print("room[" + str(self.id) + "]<" + self.name + ">  TOTAL COSTS(eu) " + str(self._total) )
       print("room[" + str(self.id) + "]<" + self.name + ">  --------------------------------------------------------------------------END")

       pass



