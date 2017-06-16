import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','midterm.settings')

import django
import datetime as dt
import uuid
django.setup()
from library.models import User, Genre, Media, MediaInstance

def populate():
	users = [
		{"username": "jsmith",
		"email": "jsmith@email.com",
		"pwd": "password",
		"fname": "John",
		"lname": "Smith"},
		{"username": "jdoe",
		"email": "jdoe@email.com",
		"pwd": "password",
		"fname": "Jane",
		"lname": "Doe"}
	]

	genres = [
		"Fiction",
		"Non-Fiction",
		"Thriller",
		"Mystery",
		"Adventure",
		"Romance",
		"Science Fiction"
	]

	instances = [
		{"id": uuid.uuid4(),
		"media": 0,
		"due_date": (dt.date.today() + dt.timedelta(days=1)),
		"history": [0, 1],
		"borrower": 1,
		"status": "o"}
	]

	medias = [
		{"type": "Book",
		"title": "Hatchet",
		"isbn": "1234567891234",
		"topic": 0,
		"subtopics": [2, 3, 4],
		"instances": [instances[0]]}
	]

	genre_objs = []
	user_objs = []

	for user in users:
		u = add_user(user)
		user_objs.append(u)

	for genre in genres:
		g = add_genre(genre)
		genre_objs.append(g)

	for media in medias:
		m = add_media(media, genre_objs)
		for i in media['instances']:
			add_instance(m, i, user_objs)


	# Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()

def add_user(data):
	u = User.objects.filter(username = data['username'])
	if u.exists():
		pass
	else:
		u = User.objects.create_user(data['username'], data['email'], data['pwd'])
		u.first_name = data['fname']
		u.last_name = data['lname']
		u.save()
	return u

def add_genre(name):
	g = Genre.objects.get_or_create(name=name)[0]
	g.save()
	return g

def add_media(data, genres):
	m = Media.objects.filter(title= data["title"])
	if m.exists():
		pass
	else:
		m = Media.objects.get_or_create(title = data['title'])[0]
		m.mediaType = data['type']
		m.isbn = data['isbn']
		m.topic = genres[data['topic']]

		for s in data['subtopics']:
			m.subtopics.add(genres[s])
		m.save()
	return m

def add_instance(m, data, users):
	i = MediaInstance.objects.filter(id= data["id"])
	if i.exists():
		pass
	else:
		i = MediaInstance.objects.get_or_create(id= data["id"])[0]
		i.media = m
		i.due_date = data["due_date"]
		i.borrower = users[data["borrower"]]
		i.status = data["status"]

		for u in data['history']:
			i.rental_history.add(users[u])
		i.save()
	return i



if __name__ == '__main__':
	print("Starting Library population script...")
	populate()