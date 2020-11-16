from breezypythongui import EasyFrame

class BouncyGUI(EasyFrame):
    """Application window for the bouncy program"""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Bouncy GUI")

        #Label and field for the height
        self.addLabel(text = "Initial height",
                      row = 0, column = 0)
        self.heightField = self.addFloatField(value = 0.0,
                                              row = 0,
                                              column = 1)

        #Label and field for bounciness index
        self.addLabel(text = "Index", row = 1, column = 0)
        self.indexField = self.addFloatField(value = 0.0,
                                             row = 1,
                                             column = 1)

        #Label and field for number of bounces
        self.addLabel(text = "Number of Bounces", row = 2, column = 0)
        self.bounceField = self.addIntegerField(value = 0,
                                                row = 2,
                                                column = 1)

        #The command button
        self.addButton(text = "Compute", row = 3, column = 0,
                       columnspan = 2,
                       command = self.computeDistance)

        #Label and field for the distance
        self.addLabel(text = "Total Distance", row = 4, column = 0)
        self.distanceField = self.addFloatField(value = 0.0,
                                                row = 4,
                                                column = 1,
                                                precision = 2)

    #The event handler method for the button
    def computeDistance(self):
        """Obtains the data from the input fields and uses them
        to compute the distane of bounce, which is sent to the
        output field."""
        initialHeight = self.heightField.getNumber()
        bounceIndex = self.indexField.getNumber()
        bounceNum = self.bounceField.getNumber()

        height = initialHeight
        distance = 0
        while bounceNum > 0:
            distance = distance + height
            height = height * bounceIndex
            distance = distance + height
            bounceNum -= 1
        self.distanceField.setNumber(distance)

def main():
    BouncyGUI().mainloop()

if __name__ == "__main__":
    main()
        
