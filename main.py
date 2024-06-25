import os
import random
import time
import pyautogui
import keyboard
import schedule
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


class NoxController:
    def __init__(self, program_path):
        self.program_path = program_path
        self.coordinates = []
        self.paused = False
        self.run_count = 0

    async def start_program(self):
        try:
            os.startfile(self.program_path)
            logging.info('Nox started')
            await asyncio.sleep(30)
        except Exception as e:
            logging.error(f'Error starting program: {e}')

    def add_coordinate(self, x, y, width, height):
        self.coordinates.append((x, y, width, height))

    async def click_on_coordinates(self):
        for x, y, width, height in self.coordinates:
            try:
                center_x = x + width // 2
                center_y = y + height // 2
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                await asyncio.sleep(4)
            except Exception as e:
                logging.error(f'Error clicking on coordinates: {e}')

    async def run(self):
        try:
            await self.start_program()
            await self.click_on_coordinates()
            while True:
                if keyboard.is_pressed('ctrl+d'):
                    logging.info('Program paused')
                    self.paused = True
                    while self.paused:
                        if keyboard.is_pressed('ctrl+a'):
                            logging.info('Program resumed')
                            self.paused = False
                x, y, width, height = self.coordinates[-1]
                center_x = x + width // 2
                center_y = y + height // 2
                pyautogui.moveTo(center_x, center_y)
                pyautogui.click()
                await asyncio.sleep(0.01)
                if time.time() - self.start_time > 200:  # Run for 5 minutes
                    os.system("taskkill /im Nox.exe")  # Kill the Nox process
                    break
        except Exception as e:
            logging.error(f'Error running program: {e}')

    async def run_in_background(self):
        try:
            await self.run()
        except Exception as e:
            logging.error(f'Error running in background: {e}')


nox_controller = NoxController("C:/Users/staks/Desktop/Nox")
nox_controller.add_coordinate(1571, 367, 35, 41)
nox_controller.add_coordinate(1770, 147, 15, 21)
nox_controller.add_coordinate(155, 545, 41, 50)
nox_controller.add_coordinate(54, 1054, 80, 3)
nox_controller.add_coordinate(767, 911, 342, 7)
nox_controller.add_coordinate(832, 817, 178, 9)


async def countdown(countdown_time):
    try:
        while countdown_time > 0:
            minutes, seconds = divmod(countdown_time, 60)
            logging.info(f'Time until next run: {int(minutes)} minutes, {int(seconds)} seconds')
            await asyncio.sleep(1)
            countdown_time -= 1
    except Exception as e:
        logging.error(f'Error in countdown: {e}')


async def run_nox_controller():
    try:
        nox_controller.start_time = time.time()
        await nox_controller.run_in_background()
        nox_controller.run_count += 1
        logging.info(f'Nox controller has been run {nox_controller.run_count} times.')
    except Exception as e:
        logging.error(f'Error running Nox controller: {e}')


async def schedule_countdown():
    try:
        while True:
            countdown_time = random.randint(1800, 5400)
            await countdown(countdown_time)
            await run_nox_controller()
    except Exception as e:
        logging.error(f'Error in schedule countdown: {e}')


if __name__ == '__main__':
    # First run
    nox_controller.start_time = time.time()
    asyncio.run(nox_controller.run_in_background())
    nox_controller.run_count += 1
    logging.info(f'Nox controller has been run {nox_controller.run_count} times.')

    # Schedule the countdown
    asyncio.run(schedule_countdown())
