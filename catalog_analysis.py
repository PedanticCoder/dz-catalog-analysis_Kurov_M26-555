import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1
def average_rating(movies):
    ratings = [movie["rating"] for movie in movies if "rating" in movie]

    if not ratings:
        return 0.0

    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies if "year" in movie]

    if not ages:
        return 0, 0

    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}h {minutes}min"
    
# Этап 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"
            
# Этап 3
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    #print(movie["title"])

i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        #print(movies[i]["title"])
        break
    i += 1
#else:
#    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
    
# Этап 4
def normalize_title(title):
    words = title.split()

    if not words:
        return ""

    normalized_words = []
    for word in words:
        new_word = word[0].upper() + word[1:]
        normalized_words.append(new_word)

    return " ".join(normalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    duration_pretty_str = duration_in_hours(movie["duration_min"])
    genres_str = ", ".join(movie["genres"])
    return (
        f'"{movie["title"]}" ({movie["year"]}) - {movie["rating"]}/10, '
        f'{duration_pretty_str}, жанры: {genres_str}'
    )
    
# Этап 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]
    
# Этап 6
def count_by_genre(movies):
    genres_dict = dict()

    for movie in movies:
        for genre in movie["genres"]:
            genres_dict[genre] = genres_dict.get(genre, 0) + 1

    return genres_dict

def actor_filmography(movies):
    actors_dict = dict()

    for movie in movies:
        for actor in movie["actors"]:
            current_films = actors_dict.get(actor, [])
            current_films.append(movie["title"])
            actors_dict[actor] = current_films

    return actors_dict

def get_above_average_movies(movies):
    avg_res = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg_res
    }
    
# Этап 7
def all_genres(movies):
    genres_set = set()
    for movie in movies:
        genres_set = genres_set | movie["genres"]
    return genres_set


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b

# Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

#for movie in iter_high_rated(movies):
    #print(format_report_line(movie))

#print("\n" + "=" * 50 + "\n")

total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

#print(f"Суммарная длительность фильмов с рейтингом > 7: {total_duration} минут")


def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")

    avg_rating = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет\n")

    print("Топ-3 фильма:")
    for movie in iter_high_rated(movies, min_rating=8.6):
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    genres_counts = count_by_genre(movies)
    sorted_genres = sorted(genres_counts.items(), key=lambda x: x[1], reverse=True)
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()

    unique_genres = all_genres(movies)
    genres_str = ", ".join(sorted(unique_genres))
    print(f"Все жанры каталога: {genres_str}")


build_report(movies)
