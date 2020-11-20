import random				

deck = ('The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World', 'The Fool')

position = ('Upright', 'Reversed')


count = 0
while count != 3:
	sampled_list = random.sample(deck, 1)
	sampled_position = random.sample(position, 1)
	print(sampled_list + sampled_position)
	count = count + 1