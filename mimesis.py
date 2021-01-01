"""
Mimesis

Когда программисты пишут базовые тесты для своего кода, в приложении появляются пользователи с именем qwerty,
фамилией asdf  и живущие в городе zxcv. Оно и понятно — надо писать код, а не сидеть и придумывать имена тестовым
юзерам. Но у действительно крутых спецов даже тесты выглядят аккуратно и с вниманием к деталям.  А самые крутые из
крутых используют генераторы реалистичных тестовых данных.

Mimesis генерирует реалистичные тестовые данные для имен, фамилий, емейлов и прочих полей, над генерацией значений для
которых обычно нет времени думать.
"""

from mimesis import Person
person = Person('en')

person.full_name()
# 'Brande Sears'

person.email(domains=['mimesis.name'])
# 'roccelline1878@mimesis.name'

person.email(domains=['mimesis.name'], unique=True)
# 'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

person.telephone(mask='1-4##-8##-5##3')
# '1-436-896-5213
