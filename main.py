class StudentsInMLOps:
    #making a change to commit
    def __init__(self):
        # Initialize the total strength of students to 0
        self.total_strength = 0

    def enrollStudents(self, count):
        """Enroll a specified number of students into the class."""
        self.total_strength += count

    def dropStudents(self, count):
        """Drop a specified number of students from the class."""
        # Ensure total strength doesn't go negative
        self.total_strength = max(0, self.total_strength - count)

    def getTotalStrength(self):
        """Return the current total strength of the class."""
        return self.total_strength

    def getClassName(self):
        """Return the name of the class."""
        return "StudentsInMLOps"
