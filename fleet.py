from robot import Robot

class Fleet:
    def __init__(self):
        self.fleet_of_robots = []


    def create_fleet(self):
        robot1 = robots.Robot('Buzz', 250, 100)
        robot2 = robots.Robot('Max', 175, 70)
        robot3 = robots.Robot('Omega', 150, 60)
        self.robot_team.append(robot1, robot2, robot3)
        print(self.robot_team)

