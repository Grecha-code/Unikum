import requests
import json
import geonamescache

api_key = "8e9d5190a22f15f8ff466edc3a9a54cc"
headers = {'User-Agent': 'Mozilla/5.0'}

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()
city_names = [city['name'] for city in cities.values()]


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return None
        return response.json()
    except:
        return None


def format_weather(data, city):
    return (f"Погода в городе: {city}\n"
            f"Состояние атмосферы: {data['weather'][0]['description']}\n"
            f"Температура: {data['main']['temp']}°C\n"
            f"Макс. температура: {data['main']['temp_max']}°C\n"
            f"Мин. температура: {data['main']['temp_min']}°C\n"
            f"Скорость ветра: {data['wind']['speed']} м/с")


def found_city(temp, desc, min_wind, max_wind, limit=20):
    matched = []

    for city in city_names[:limit]:  # ограничение запросов!
        data = get_weather(city)
        if not data:
            continue

        current_temp = data['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        temp_match = (temp - 5) <= current_temp <= (temp + 5)
        desc_match = desc.lower() in description.lower()
        wind_match = min_wind <= wind_speed <= max_wind

        if temp_match and desc_match and wind_match:
            matched.append({
                "city": city,
                "temp": current_temp,
                "description": description,
                "wind": wind_speed
            })

    return matched


if __name__ == "__main__":

    choice = int(input(
        "Что вы хотите сделать?\n"
        "1) Ничего\n"
        "2) Найти город по условиям\n"
        "3) Узнать погоду\n"
    ))

    if choice == 1:
        print("Ладно…")
        exit()

    elif choice == 2:
        temp = int(input("Температура: "))
        desc = input("Описание погоды: ")
        min_wind = int(input("Мин. ветер: "))
        max_wind = int(input("Макс. ветер: "))

        result = found_city(temp, desc, min_wind, max_wind)
        print(json.dumps(result, ensure_ascii=False, indent=4))
        with open("file.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

    elif choice == 3:
        city = input("Введите город (латиницей): ")

        data = get_weather(city)

        if not data:
            print("Город не найден!")
        else:
            print("\n" + "=" * 30)
            print(format_weather(data, city))
            print("=" * 30)

            with open("file.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    else:
        print("Введите нормальное число!")