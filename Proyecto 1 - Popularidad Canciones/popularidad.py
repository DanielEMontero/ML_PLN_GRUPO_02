# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 17:24:46 2025

@author: Juanca Mejía
"""

import pandas as pd
import joblib
import sys
import os

modelo = joblib.load(os.path.dirname(__file__) + '/modelo_regresion.pkl')
encoder_genre = joblib.load(os.path.dirname(__file__) + '/encoder_genre.pkl')
encoder_artist = joblib.load(os.path.dirname(__file__) + '/encoder_artist.pkl')
scaler = joblib.load(os.path.dirname(__file__) + '/scaler.pkl')

columnas_modelo = [
    'artists', 'duration_ms', 'explicit', 'danceability', 'energy', 'key',
    'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo', 'time_signature', 'track_genre']

def predict_popularity(data_dict):
    df = pd.DataFrame([data_dict])

    df['track_genre'] = encoder_genre.transform(df[['track_genre']])
    df['artists'] = encoder_artist.transform(df[['artists']])

    df = df[columnas_modelo]

    df_scaled = pd.DataFrame(scaler.transform(df), columns=columnas_modelo)

    pred = modelo.predict(df_scaled)[0]
    return pred

if __name__ == "__main__":
    if len(sys.argv) != 17:
        print("\nUso: python predict_song.py <artists> <duration_ms> <explicit> <danceability> <energy> <key> "
              "<loudness> <mode> <speechiness> <acousticness> <instrumentalness> <liveness> <valence> "
              "<tempo> <time_signature> <track_genre>")
        sys.exit(1)

    song_data = {
        'artists': sys.argv[1],
        'duration_ms': float(sys.argv[2]),
        'explicit': float(sys.argv[3]),
        'danceability': float(sys.argv[4]),
        'energy': float(sys.argv[5]),
        'key': float(sys.argv[6]),
        'loudness': float(sys.argv[7]),
        'mode': float(sys.argv[8]),
        'speechiness': float(sys.argv[9]),
        'acousticness': float(sys.argv[10]),
        'instrumentalness': float(sys.argv[11]),
        'liveness': float(sys.argv[12]),
        'valence': float(sys.argv[13]),
        'tempo': float(sys.argv[14]),
        'time_signature': float(sys.argv[15]),
        'track_genre': sys.argv[16]}

    pred = predict_popularity(song_data)
    print("Popularidad canción:", round(pred, 2))