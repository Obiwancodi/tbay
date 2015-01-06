from tbay import User
from tbay import Item
from tbay import Bid
from tbay import session


luke = User()
luke.username = "Luke"
luke.password = "I have a father"

x_wing = Item(name="X Wing", person= luke)

leia = User()
leia.username = "Leia"
leia.password = "I love Han"

leiab1 = Bid(price_point = 50 , thing = [x_wing])
leiab2 = Bid(price_point = 65, thing = [x_wing])

han = User()
han.username = "Han"
han.password = "I know"

hanb1 = Bid(price_point = 51, thing = [x_wing])
hanb2 = Bid(price_point = 66, thing = [x_wing])
x_wing.bids = [50,51,65,66]
session.add_all([luke ,leia, han, x_wing, leiab1, leiab2, hanb1, hanb2])
session.commit()

print max(x_wing.bids)