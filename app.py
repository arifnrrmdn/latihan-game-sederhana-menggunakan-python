"Latihan"

player1 = {
    "name":"zilong",
    "power":100
}

player2 = {
    "name":"balmond",
    "power":250
}

def train(player):
    player['power'] += 100

def attack(attacker, defender):
    if(attacker['power'] > defender['power']):
        print("serangan berhasil! selamat kamu menang", player1['name'])
    else:
        print("serangan gagal! kamu lemah kamu kalah dari", player2['name'])


train(player1)
train(player1)
train(player1)
train(player2)

attack(player1, player2)
