from constants import *
from simulation.objects.material import Material

class Silicon(Material):
    """The element Silicon."""

    def __init__(self, debug = False):
        """Constructs a new material of silicon.
        
        Args:
            debug: If it is being debugged. 
        """
        self._n = SILICON_N