import time
import random

print("Это программа, которая замеряет скорость печати.")
print("Вам будет показана случайная фраза, которую вам предстоит напечатать самостоятельно. Готовы?")
input("Нажмите Enter, если готовы:")

phrase1 = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
phrase2 = "Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."
phrase3 = "Съешь ещё этих мягких французских булок да выпей же чаю."

start_time = time.time()

a = random.randint(1,3)
if a == 1:
    s = phrase1
    print(phrase1)
elif a == 2:
    s = phrase2
    print(phrase2)
else:
    s = phrase3
    print(phrase3)

user_input = input("Напечатайте фразу выше: ")
end_time = time.time()

# Расчет времени и скорости
elapsed_time = end_time - start_time
symbols_per_minute = len(phrase1) / elapsed_time * 60

if user_input == s:
    print(f"Ваша скорость печати: {symbols_per_minute} символов в минуту.")
    print(f"Время, затраченное на печать: {elapsed_time} секунд.")
else:
    print('Вы не правильно ввели фразу')