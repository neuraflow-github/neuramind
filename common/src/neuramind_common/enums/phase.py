from enum import Enum


class Phase(str, Enum):
    LIVESTAGE = "LIVESTAGE"
    PLAYGROUND = "PLAYGROUND"
    TESTBENCH = "TESTBENCH"
