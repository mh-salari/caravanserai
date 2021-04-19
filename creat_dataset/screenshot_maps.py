import pyautogui
from tqdm import tqdm
import time
import os
import csv

# os.environ["DISPLAY"] = ":1"
# os.environ["XAUTHORITY"] = "/run/user/1000/gdm/Xauthority"
# os.system("export DISPLAY=:1")
# os.system('export XAUTHORITY=:"/run/user/1000/gdm/Xauthority"')


def google_map(location):
    # Search
    pyautogui.click(200, 1190)
    time.sleep(0.25)
    pyautogui.write(f"{location}\n")
    time.sleep(5)

    # Zoom into location
    pyautogui.click(1885, 2050, clicks=5, interval=0.25)
    pyautogui.click(1885, 2080, clicks=3, interval=0.25)
    time.sleep(2.5)

    # Turn of the Labels
    pyautogui.click(45, 1200)
    time.sleep(0.25)
    pyautogui.click(105, 1325)
    time.sleep(0.25)

    # close search window
    pyautogui.click(445, 1195, clicks=2, interval=0.25)

    # Move the location to center
    pyautogui.click(1205, 1650)
    pyautogui.mouseDown()
    pyautogui.dragTo(960, 1645, 1, button="left")
    pyautogui.mouseUp()
    time.sleep(0.25)

    pyautogui.scroll(10)
    # time.sleep(15)


def bing_map(location):
    # Search
    pyautogui.click(250, 150)
    time.sleep(0.25)
    pyautogui.write(f"{location}\n")
    time.sleep(5)

    # Zoom into location
    pyautogui.click(1860, 325, clicks=5, interval=0.25)
    pyautogui.click(1860, 345, clicks=1, interval=0.25)
    time.sleep(2.5)
    # Close search
    pyautogui.click(535, 250)
    time.sleep(0.25)
    # Mote the location to the center of page
    pyautogui.click(1256, 680)
    pyautogui.mouseDown()
    pyautogui.dragTo(985, 700, 1, button="left")
    pyautogui.mouseUp()


def screenshot(location, name, output_path):

    bing_map(location)
    google_map(location)
    time.sleep(7.5)

    pyautogui.screenshot(os.path.join(output_path, f"{name}.png"))

    for _ in range(5):
        pyautogui.click(955, 600)
        time.sleep(0.25)
        pyautogui.drag(-150, 100, 0.25)
        time.sleep(0.25)

    for _ in range(5):
        pyautogui.click(1205, 1650)
        pyautogui.drag(100, -150, 0.25)

    time.sleep(5)
    pyautogui.screenshot(os.path.join(output_path, f"{name}_g1.png"))

    for _ in range(5):
        pyautogui.click(955, 600)
        time.sleep(0.25)
        pyautogui.drag(250, 250, 0.25)
        time.sleep(0.25)

    for _ in range(5):
        pyautogui.click(1205, 1650)
        pyautogui.drag(250, 250, 0.25)
    time.sleep(5)
    pyautogui.screenshot(os.path.join(output_path, f"{name}_g2.png"))


def load_carvansaras(path):
    carvansaras = list()
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        FIRST_LINE = True
        for row in csv_reader:
            if FIRST_LINE:
                FIRST_LINE = False
                continue
            carvansaras.append([row[0], row[1], row[2]])

    return carvansaras


if __name__ == "__main__":

    dataset_base_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "dataset"
    )
    carvansaras_location_path = os.path.join(
        dataset_base_path, "carvansara_and_other_places.csv"
    )
    output_path = os.path.join(dataset_base_path, "raw_images")
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    carvansaras = load_carvansaras(carvansaras_location_path)

    print("Sleeping for 5s")
    time.sleep(5)

    for number, _, location in tqdm(carvansaras[:]):
        screenshot(location, number, output_path)