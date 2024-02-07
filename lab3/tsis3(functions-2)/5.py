
movies = [
{
"name": "true beauty", 
"imdb": 8.0,
"category": "Romance"
},
{
"name": "boxing",
"imdb": 8.3,
"category": "Action"
},
{
"name": "hello world",
"imdb": 3.0,
"category": "Adventure"
},
{
"name": "2521",
"imdb": 7.0,
"category": "Drama"
},
{
"name": "Tomorrow",
"imdb": 9.2,
"category": "Romance"
},
{
"name": "Snowdrop",
"imdb": 6.4,
"category": "Romance"
},
{
"name": "Alice in borderland",
"imdb": 10.0,
"category": "Romance"
},
{
"name": "At a distance spring is green",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "The heavenly idol",
"imdb": 3.2,
"category": "War"
},
{
"name": "Top Management",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Mouse",
"imdb": 9.2,
"category": "Comedy"
},
{
"name": "alie serdca koree",
"imdb": 9.2,
"category": "History"
},
{
"name": "F4",
"imdb": 10.0,
"category": "Suspense"
},
{
"name": "Duties after school",
"imdb": 7.2,
"category": "Fantasy"
},
{
"name": "We all died",
"imdb": 10.0,
"category": "Thriller"
}]

def category_rate_list(dic, category):
    s = 0
    cnt = 0
    for x in dic:
        if (x["category"] == category):
            s += float(x["imdb"])
            cnt += 1
    print (s / cnt)

categ = input()
category_rate_list(movies, categ)