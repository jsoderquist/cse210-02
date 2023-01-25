from constants import *
from simulation.objects.things import Things
from simulation.scripting.fresnel_calculation import FresnelCalculation
from simulation.objects.silicon import Silicon
#from simulation.scripting.script import Script

class Simulator:
    """Software that controls the XRD simulation
    
    The responsibility of a Simulator is to control the sequence of the simulation.

    Attributes:
        
    """

    def __init__(self):
        """Constructs a new Simulator
        
        Args:
            
        """

        self._things = Things()
        
        
    def start_simulation(self):
        """Starts the game using the given things. Runs the main simulation loop.

        Args:
            things (Things): The a list of objects in Things.
        """
        FRESNEL_CALCULATION = FresnelCalculation()
        self._things.add_object(MATERIAL_GROUP, Silicon())

        FRESNEL_CALCULATION.execute(self._things)

