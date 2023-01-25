from constants import *


class Material():
    """An element or alloy."""

    def __init__(self, debug = False):
        """Constructs a new material.
        
        Args:
            debug: If it is being debugged. 
        """
        raise NotImplementedError("__init__ not implemented in base class")
    
    def get_index_of_refraction(self):
        """Gets material's index of refraction
        
        Returns:
            n
        """
        return self._n

    def get_index_of_refraction_real_part(self):
        """Gets real part of material's index of refraction
        
        Returns:
            n
        """
        return self._n.real
    
    def get_index_of_refraction_imaginary_part(self):
        """Gets imaginary part of material's index of refraction
        
        Returns:
            n
        """
        return self._n.imag