"""
Tavern
Один менеджер скажет “тестирование” — миллионы разработчиков ему ответят “pytest”. Да, действительно, для многих
программистов pytest стало синонимом слова “тестирование”. При этом абсолютно не важно, что и как мы тестируем —
компоненты, интеграцию или поведение: этой либой можно заткнуть любую дырку.

Ничего ужасного в этом нет — pytest и правда позволяет это все делать. Берем эту либу, прикручиваем requests,
пишем кучу всяких кейсов и операций с ответами и запросами к API — готово, мы получили комбайн по тестированию
этого самого API.

Однако, при применении pytest для тестирования API код со временем начинает разрастаться, появляются обработчики
заголовков, проверка ответов сервера, работа с куками и многие другие вещи. Те, кому приходилось поддерживать систему
тестирования большого приложения на бэкенде, понимают, о чем идет речь.

Поэтому для тестирования API появился отдельный инструмент — tavern.

Tavern позволяет описывать тесты API в декларативной форме в формате YAML. И в эти декларативные сценарии уже заложено
все, что вам нужно — вызовы сервера, обработка разных кодов ответа, заголовков, проверка данных в ответах.Растет
гибкость, читаемость тестов и реюзабельность сценариев тестирования — а что нам еще нужно?
"""
