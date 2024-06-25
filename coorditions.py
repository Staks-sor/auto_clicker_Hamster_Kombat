import pyautogui
import keyboard


def select_area():
    print("Выберите область на экране.")
    print("Нажмите F5, чтобы начать выделение.")
    print("Нажмите F6, чтобы закончить выделение.")

    start_x, start_y = None, None
    end_x, end_y = None, None

    # Ожидание нажатия клавиши F5 для начала выделения
    keyboard.wait("F5")

    # Начало выделения: получение координат начальной точки
    start_x, start_y = pyautogui.position()
    end_x, end_y = start_x, start_y

    # Ожидание нажатия клавиши F6 для завершения выделения
    keyboard.wait("F6")

    # Завершение выделения: получение координат конечной точки
    end_x, end_y = pyautogui.position()

    # Вычисление координат и размеров прямоугольной области
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    width = abs(end_x - start_x)
    height = abs(end_y - start_y)

    return left, top, width, height


if __name__ == '__main__':
    selected_area = select_area()
    print("Координаты выделенной области:", selected_area)
