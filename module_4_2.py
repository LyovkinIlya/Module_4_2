def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function()
'''
Невозможно вызвать inner_function вне функции test_function.
Возникает ошибка NameError.
'''
test_function()