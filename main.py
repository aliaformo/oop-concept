# Define the class to check obstructions
class CheckingObstruction:
    def __init__(self, speed):
        self.speed = speed
        self.obstructions = {}

    def add_obstruction(self, start_location, end_location, distance, actual_time):
        expected_time = distance / self.speed
        self.obstructions[(start_location, end_location)] = (expected_time, actual_time)

    def obstruction_checker(self, start_location, end_location):
        if (start_location, end_location) in self.obstructions:
            expected_time, actual_time = self.obstructions[(start_location, end_location)]
            time_difference = actual_time - expected_time
            return time_difference > 60
        return False


# Example usage
speed_of_machine = 30  # Speed in miles per hour
obstruction_checker = CheckingObstruction(speed_of_machine)

# Adding obstructions (simulated data)
start_location = [53.5872, -2.4138]
end_location = [53.474, -2.2388]
distance = 15  # Example distance in miles
actual_time = 78  # Simulated actual time in minutes
obstruction_checker.add_obstruction(start_location, end_location, distance, actual_time)

# Checking obstructions
obstruction_true = obstruction_checker.obstruction_checker(start_location, end_location)

if obstruction_true:
    print("There is an impenetrable obstruction between the Start Location and the End Location.")
else:
    print("There are no obstructions between the Start Location and the End Location.")