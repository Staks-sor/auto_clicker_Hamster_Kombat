import pyautogui
import keyboard


class AreaSelector:
    def __init__(self):
        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None

    def select_area(self):
        print("Выберите область на экране.")
        print("Нажмите F5, чтобы начать выделение.")
        print("Нажмите F6, чтобы закончить выделение.")

        # Ожидание нажатия клавиши F5 для начала выделения
        keyboard.wait("F5")

        # Начало выделения: получение координат начальной точки
        self.start_x, self.start_y = pyautogui.position()
        self.end_x, self.end_y = self.start_x, self.start_y

        # Ожидание нажатия клавиши F6 для завершения выделения
        keyboard.wait("F6")

        # Завершение выделения: получение координат конечной точки
        self.end_x, self.end_y = pyautogui.position()

        # Вычисление координат и размеров прямоугольной области
        left = min(self.start_x, self.end_x)
        top = min(self.start_y, self.end_y)
        width = abs(self.end_x - self.start_x)
        height = abs(self.end_y - self.start_y)

        return left, top, width, height


if __name__ == '__main__':
    selector = AreaSelector()
    selected_area = selector.select_area()
    print("Координаты выделенной области:", selected_area)
