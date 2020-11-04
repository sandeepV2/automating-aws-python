from enum import Enum,unique,auto

@unique
class Family(Enum):
    WIFE = 1
    MOM = 2
    SIS = 3
    #TEST = 1
    SON = auto()



print Family.WIFE.name, Family.WIFE.value 
