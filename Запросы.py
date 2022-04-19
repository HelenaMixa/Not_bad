# создать объект
>>> tom = Person.objects.create(name="Tom", surname="Ivanov",coach="Pavlihenko")
>>>Ivan=Person.objects.create(name="Ivan", surname="Ivanov",birth_date="2000-10-12",coach="Omelhenko")

>> Mark = Person.objects.create(name="Mark", surname="Petrov",coach="Pavlihenko")
>>> Anna = Person.objects.create(name="Anna", surname="Mixa",coach="Omelhenko")

>>> prestige = Club.objects.create(name_club="Prestige", coach="Omelhenko",town="Zaporizhzhia")
>>> ukrdance = Club(name_club="Ukrdance", coach="Pavlihenko",town="Odessa")
>>> ukrdance.save

# получаем все имеющиеся объекты
>>> Person.objects.all()
<QuerySet [<Person: Tom>, <Person: Mark>, <Person: Anna>]>

#получение первого объекта персона
>>> person = Person.objects.first()
>>> person.name
'Tom'

#получение списка всех танцоров, у которых тренер Pavlihenko
>>> Person.objects.filter(coach='Pavlihenko')
<QuerySet [<Person: Tom>, <Person: Mark>]>

# вывод списка полей
list(Person.objects.values('name','coach'))
[{'name': 'Tom', 'coach': 'Pavlihenko'}, {'name': 'Mark', 'coach': 'Pavlihenko'}, {'name': 'Anna', 'coach': 'Omelhenko'}]

# количество танцоров, у которых тренер Pavlihenko
>>> Person.objects.filter(coach='Pavlihenko').count()
2

# обновление данных
>>> Club.objects.filter(id=2).update(name_club="Marich")
1
>>> list(Club.objects.values())
[{'id': 1, 'name_club': 'Prestige', 'coach': 'Omelhenko', 'town': 'Zaporizhzhia'}, {'id': 2, 'name_club': 'Marich', 'coach': 'Pavlihenko', 'town': 'Odessa'}]


# запрос по двум связанным таблицам
>>> Petr = Person(name="Petr", surname="petrov",coach="Omelhenko")
>>> Petr.save()

>>> Member1 = Member.objects.create(Pay=150, People=Petr)
>>> member = Member.objects.first()
>>> member.People.name
'Petr'

