from datetime import datetime
import pandas as pd
import requests

def get_album(search_term):
    # Buscando artista pela rota 'search' da API
    search = requests.get(f"http://theaudiodb.com/api/v1/json/2/search.php?s={search_term}")
    artist = search.json()['artists']

    if not artist:
        return {'message': 'artist not found'}, 404

    artist_id = artist[0]['idArtist']
    artist_name = artist[0]['strArtist']

    # Pegando os albums do artista pela rota 'album' da API
    albums = pd.json_normalize(requests.get(f"http://theaudiodb.com/api/v1/json/2/album.php?i={artist_id}").json()['album'])
    albums.sort_values('intYearReleased', ascending=False, inplace=True)
    last = albums.iloc[[0]]
    album_id = last.idAlbum.item()
    album_name = last.strAlbum.item()
    album_year = last.intYearReleased.item()

    # Pegando as faixas do album pela rota 'track' da API
    tracks = pd.json_normalize(requests.get(f"http://theaudiodb.com/api/v1/json/2/track.php?m={album_id}").json()['track'])
    track_names = tracks.strTrack.to_dict()

    response = {
        "artist": artist_name,
        "lastest-album": album_name,
        "album-year": album_year,
        "tracks": track_names
    }

    return response