class Drone:
    def __init__(self, id, altitude=0):
        self.id = id
        self.altitude = altitude

    def takeoff(self):
        self.altitude = 100
        print(f"Поднялись на высоту: {self.altitude}")


def main():
    my_drone = Drone('ID001')
    my_drone.takeoff()

if __name__ == "__main__":
    main()
    