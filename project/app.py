from flask import Flask, request, make_response
from flask_cors import CORS
from project.models.tictatoe import TicTacToe
from project.models.tablero import Tablero

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    @app.route('/auto', methods=['POST'])
    def get_best_move():
        request_json = request.get_json()
        if 'mapa' not in request_json:
            return make_response({
                'error':'No hay tablero'
            },400)
    
        mapa = request_json['mapa']
        game = TicTacToe()
        if game.obtener_espacios_libres(mapa=mapa) == []:
            return make_response({
                'error':'No hay espacios'
            },400)
        
        move = game.obtener_ficha_auto(mapa=mapa)

        return make_response({
                'msg':move
            },200)
    
    @app.route('/result', methods=['POST'])
    def is_victory():
        request_json = request.get_json()
        if 'mapa' not in request_json:
            return make_response({
                'error':'not enough data'
            },400)

        mapa = request_json['mapa']

        tablero = Tablero(mapa=mapa)
        victory = tablero.hay_victoria(True)
        defeat = tablero.hay_victoria(False)
        tie = tablero.hay_empate()
        print('hay victoria: ', victory)

        return make_response({
            'victory':victory,
            'tie':tie,
            'defeat':defeat
        },200)
        
    return app