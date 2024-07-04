import pdb
from main import Drone


def test_takeoff():
    pdb.set_trace()
    test_drone = Drone('TestDrone')
    test_drone.takeoff()
    assert test_drone.altitude == 100, "Успешно взлетели на 100 м"


if __name__ == "__main__":
    test_takeoff()  # запуск теста взлета

