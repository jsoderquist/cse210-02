class Things:
    """A collection of objects."""

    def __init__(self):
        """Constructs a new set of things."""
        self._objects = {}
        
    def add_object(self, group, object):
        """Adds an object to the given group.
        
        Args:
            group: A string containing the name of the group.
            object: The instance of Object (or a subclass) to add.
        """
        if group not in self._objects.keys():
            self._objects[group] = []
        self._objects[group].append(object)

    def clear_objects(self, group):
        """Clears objects from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._objects:
            self._objects[group] = []
    
    def clear_all_objects(self):
        """Clears all objects."""
        for group in self._objects:
            self._objects[group] = []
    
    def get_objects(self, group):
        """Gets the objects in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Object instances.
        """
        results = []
        if group in self._objects.keys():
            results = self._objects[group].copy()
        return results

    def get_object(self, group, object):
        """Gets the objects in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Object instances.
        """
        result = None
        if group in self._objects.keys():
            result = self._objects[group][object]
        
        return result

    def get_objects(self, group):
        """Gets the objects in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Object instances.
        """
        results = []
        if group in self._objects.keys():
            results = self._objects[group].copy()
        return results
    
    def get_all_objects(self):
        """Gets all of the objects in the cast.
        
        Returns:
            A list of object instances.
        """
        results = []
        for group in self._objects:
            results.extend(self._objects[group])
        return results

    def get_first_object(self, group):
        """Gets the first object in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of Object.
        """
        result = None
        if group in self._objects.keys():
            result = self._objects[group][0]
        return result

    def remove_object(self, group, object):
        """Removes an object from the given group.
        
        Args:
            group: A string containing the name of the group.
            object: The instance of Object (or a subclass) to remove.
        """
        #print(self._objects[group])
        if group in self._objects:
            self._objects[group].remove(object)