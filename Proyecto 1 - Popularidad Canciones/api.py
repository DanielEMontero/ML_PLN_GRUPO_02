# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 17:57:25 2025

@author: Juanca Mejía
"""
!pip install flask


from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from popularidad import predict_popularity

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Popularidad de la canción API',
    description='Popularidad de la canción API'
)

ns = api.namespace('predict', description='Popularity Prediction')

parser = api.parser()
parser.add_argument('danceability', type=float, required=True, help='Danceability', location='args')
parser.add_argument('energy', type=float, required=True, help='Energy', location='args')
parser.add_argument('valence', type=float, required=True, help='Valence', location='args')
parser.add_argument('duration_ms', type=int, required=True, help='Duration (ms)', location='args')
parser.add_argument('track_genre', type=str, required=True, help='Track Genre', location='args')
parser.add_argument('artists', type=str, required=True, help='Artist Name', location='args')
parser.add_argument('explicit', type=int, required=True, help='Explicit (0 or 1)', location='args')
parser.add_argument('key', type=int, required=True, help='Musical Key', location='args')
parser.add_argument('loudness', type=float, required=True, help='Loudness', location='args')
parser.add_argument('mode', type=int, required=True, help='Mode (0 or 1)', location='args')
parser.add_argument('speechiness', type=float, required=True, help='Speechiness', location='args')
parser.add_argument('acousticness', type=float, required=True, help='Acousticness', location='args')
parser.add_argument('instrumentalness', type=float, required=True, help='Instrumentalness', location='args')
parser.add_argument('liveness', type=float, required=True, help='Liveness', location='args')
parser.add_argument('tempo', type=float, required=True, help='Tempo', location='args')
parser.add_argument('time_signature', type=int, required=True, help='Time Signature', location='args')

resource_fields = api.model('Response', {
    'result': fields.Float,
})

@ns.route('/')
class PopularityApi(Resource):
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        data = {
            'danceability': args['danceability'],
            'energy': args['energy'],
            'valence': args['valence'],
            'duration_ms': args['duration_ms'],
            'track_genre': args['track_genre'],
            'artists': args['artists'],
            'explicit': args['explicit'],
            'key': args['key'],
            'loudness': args['loudness'],
            'mode': args['mode'],
            'speechiness': args['speechiness'],
            'acousticness': args['acousticness'],
            'instrumentalness': args['instrumentalness'],
            'liveness': args['liveness'],
            'tempo': args['tempo'],
            'time_signature': args['time_signature']
        }
        result = predict_popularity(data)
        return {'result': result}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
