## Part_1_number_13
<p>Решение:</p>

<p>Это консольное приложение, у которого один запускаемый файл - это task.py</p>

<p>Внутри файла определён класс <b>GeneratePassword</b>, внутри которого инициализуется <i>алфавит</i>, в который включены буквы, цифры и специальные символы, а также <i>длина пароля</i>, принимающая значение по умолчанию None.</p>

<p>Также внутри класса определены функции generate и start:</p>

<p><b>generate()</b> - проверяет, что <i>длина пароля</i> - это целое число, далее проверяет длину пароля (значение должно принадлежать отрезку от 8 до 32), после создает пароль, используя <i>алфавит</i>, и выводит в консоли <i>длину пароля</i>, который задал пользователь и сам пароль</p>

<p><b>start()</b> - выводит приглашающее предложение, проверяет введено ли было в <i>длину пароля</i> значение "exit", если да, то приложение заканичивает работу, иначе запускается функция <b>generate()</b></p>
