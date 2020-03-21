from flask import Flask, request, render_template, redirect, url_for
from game import Game
app = Flask(__name__)
game = Game()
game.preparation()


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        chosen_card = request.form["request_change"]
        game.request_move(int(chosen_card))
    return render_template("index.html", player_one_cards = game.players[0].deck.return_in_list(), main_deck_cards = game.main_deck.return_in_list(),
                           player_two_cards = game.players[1].deck.return_in_list(), end_of_game = game.end_of_game, player_one_move = game.players[0].player_move,
                           player_two_move = game.players[1].player_move)

@app.route("/reset")
def reset():
    game.reset()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()

