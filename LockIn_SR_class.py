# import pyvisa
import re

class Lockin:
    def __init__(self, gpibport):
        # rm = pyvisa.ResourceManager()
        self.lockin = 7 # rm.open_resource(f'GPIB0::{gpibport}::INSTR')
        # # get SR name and model (830 / 844). It is important for aux_out !!!!
        # self.name = self.lockin.query("*IDN?")
        # match = re.search(r"SR(\d{3})", self.name)
        # self.model = int(match.group(1))
        self.model = 830
        return f'LockIn is connected. Model {self.model}'

    def getXY(self):
        # get X Y signals from SR844
        # out_signal = self.lockin.query("SNAP? 1,2")
        out_signal = 120
        # signal = out_signal.split(",")
        # sigX = float(signal[0])
        # sigY = float(signal[1])
        return out_signal

    def set_aux(self, voltage):
        if self.model == 844:  # check the model number
            # set aux_out_1 voltage to SR844
            # self.write("AUXO 1, " + str(voltage))  # !!!! SR844 command. SR830 has another string
            return voltage + 800
        elif self.model == 830:  # check the model number
            # self.write("AUXV 1, " + str(voltage))  # SR830
            return voltage + 100
