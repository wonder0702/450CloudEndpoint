import datetime


class Controller:
    def __init__(self, l=None, uid=None):
        if l is None:
            l = [[1, 3, 1], [3, 3, 2], [2, 4, 3]]
        if uid is None:
            dt = datetime.datetime.now()
            uid = int(datetime.datetime.timestamp(dt)) % 200
            uid = str(uid)
        # Three elements: importance(1 lowest), energy Consumption, load id
        self.loadMatrix = l
        self.uid = uid

    def showStatus(self):
        s = f"----------Controller {self.uid}----------\n"
        for loads in self.loadMatrix:
            s = s + f"Load No.{loads[2]} Importance: {loads[0]} Energy Consumption: {loads[1]}\n"
        print(s)
        return s

    def edit(self, l):
        self.l = l

    def schedule(self, energyInput):
        energyInput = int(energyInput)
        self.loadMatrix.sort(key=lambda x: -x[0])
        resultList = []
        print(self.loadMatrix)
        for loads in self.loadMatrix:
            tempList = []
            tempList.append(loads[2])
            energyConsumption = 0
            if energyInput > 0:
                if energyInput > loads[1]:
                    energyConsumption = loads[1]
                    energyInput = energyInput - loads[1]
                else:
                    energyConsumption = energyInput
                    energyInput = 0
            tempList.append(energyConsumption)
            resultList.append(tempList)
        print("Schedule Result:")
        for res in resultList:
            print(f"Controller No.{res[0]}: Give {res[1]} unit Energy")
        return resultList


class Monitor:
    def __init__(self):
        self.controllerList = []

    def addcontroller(self, c):
        self.controllerList.append(c)
        print("Successfully add ")

    def showStatus(self):
        res = ""
        for loads in self.controllerList:
            res = res + loads.showStatus()
        return res


# c = Controller(uid="123")
# p = Controller(uid="234")
# m = Monitor()
# m.addcontroller(c)
# m.addcontroller(p)
# # energy = input("Input the total energy:\n")
# m.showStatus()
