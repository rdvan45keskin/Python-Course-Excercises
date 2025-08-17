# themoviedb.org => film ve dizi arşivi
# themoviedbnin sunduğu apiyi uygulamanızda kullanın
# anahtar kelimeye göre arama
# en popüler film listesi
# vizyondaki film listeleri

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "e8a9d5f82d78ca210c8076d648685c12"
    
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def nowPlaying(self):
        responseP = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return responseP.json()

    def search(self,title):
        responseS = requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&query={title}&page=1")
        return responseS.json()

momvieApi = theMovieDb()
while True:
    secim = input("1- Popular Movies\n2- Now playing\n3- Search a Movie\n4- Exit\nChoose: ")

    if secim == "4":
        break
    else:
        if secim == "1":
            movies = momvieApi.getPopulars()
            for movie in movies["results"]:
                print(f"{movie['title']} - Rating: {movie['vote_average']}")
        elif secim == "2":
            latestMovies = momvieApi.nowPlaying()
            for movie in latestMovies["results"]:
                print(f"{movie['title']} - Rating: {movie['vote_average']}")
        elif secim == "3":
            keyword = input("Film name: ")
            search = momvieApi.search(keyword)
            if search['results']:
                for movie in search["results"]:
                    print(f"{movie['title']} - Release Date: {movie['release_date']} - Rating: {movie['vote_average']}")
            else:
                print("Film bulunamadı.")
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")