class Action:
    """A thing that is done.
    
    The responsibility of action is to do something that is important in the simulation. Thus, it has one
    method, execute(), which should be overridden by derived classes.
    """

    def execute(self, things):
        """Executes something that is important in the simulation. This method should be overriden by 
        derived classes.

        Args:
            things: An instance of Things containing the actors in the simulation.
            #script: An instance of Script containing the actions in the simulation.
            #callback: An instance of ActionCallback so we can change the scene.
        """
        raise NotImplementedError("execute not implemented in base class")