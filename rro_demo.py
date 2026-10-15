"""RRO demonstration. Printed messages stand in for robot actions."""
from time import sleep

POLL_INTERVAL_S = 0.5  # s between status updates


def extend_arm():
    print("Arm: not configured")


def close_gripper():
    print("Gripper: not configured")


def main():
    extend_arm()
    close_gripper()
    for update in range(1, 4):
        print(f"Status update {update}")
        sleep(POLL_INTERVAL_S)


if __name__ == "__main__":
    main()
