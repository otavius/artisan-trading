class Instrument:

    def __init__(self,name, ins_type, displayName, pipLocation, tradeUnitsPrecision, marginRate):
        self.name = name
        self.ins_type = ins_type
        self.displayName = displayName
        self.pipLocation = pow(10, pipLocation)
        self.tradeUnitsPercision = tradeUnitsPrecision
        self.marginRate = float(marginRate)

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def fromApiObject(cls, ob):
        return Instrument(
            ob["name"],
            ob["type"],
            ob["displayName"],
            ob["pipLocation"],
            ob["tradeUnitsPrecision"],
            ob["marginRate"],
        )

