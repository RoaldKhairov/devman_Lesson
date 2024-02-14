import smtplib
from dotenv import load_dotenv

text = '''\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

# Переменные в тексте
link = 'dvmn.org'
friend_name = 'Пупа'
my_name = 'Лупа'
text_latter = text.replace('%website%', link).replace('%friend_name%', friend_name).replace('%my_name%', my_name)

# Логин и пароль
password = load_dotenv("PASSWORD")
login = load_dotenv("LOGIN")

# Сообщение
service = "smtp.yandex.ru:465"
SUBJECT = "Invite"
TO = "roald.hairov@gmail.com"
FROM = login
 
message = "\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text_latter
)).encode("UTF-8")

# Отправка письма 
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(FROM, TO, message)
server.quit()