from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image

# Открываем диалоговое окно для выбора изображения
Tk().withdraw()
filename = askopenfilename()

# Открываем изображение
image = Image.open(filename)

# Обрезаем изображение с заданными значениями
left = 100
top = 100
right = 300
bottom = 300
cropped_image = image.crop((left, top, right, bottom))

# Сохраняем обрезанную версию в той же папке
cropped_image.save(filename)

# Завершение программы
print("Изображение успешно обрезано и сохранено.")