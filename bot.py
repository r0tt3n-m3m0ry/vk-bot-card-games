# -*- coding: utf-8 -*-
try:
	import vk_api
	from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
	from vk_api.keyboard import VkKeyboard, VkKeyboardColor
except:
	print('Установите необходимые модули через \'pip install -r requirements.txt\' перед запуском скрипта')

def vk_send_message_to_user(vk, user_id, message, attachments = None, keyboard = None):
	vk.messages.send(user_id = int(user_id), random_id = vk_api.utils.get_random_id(), message=message, attachment = attachments, keyboard = keyboard)

def vk_send_message_to_chat(vk, chat_id, message, attachments = None, keyboard = None):
	vk.messages.send(chat_id = int(chat_id), random_id = vk_api.utils.get_random_id(), message=message, attachment = attachments, keyboard = keyboard)

MAX_PLAYERS = 4

vk_group_token = 'ddb3f9f5097558d2c261e01fecfce6599fe954aad0e109c23e1df40f7fe8006331066b36409857a0dc7ef'
vk_group_id = '166545677'

vk_session = vk_api.VkApi(token=vk_group_token)
longpoll = VkBotLongPoll(vk_session, vk_group_id)
vk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Учавствую', color=VkKeyboardColor.POSITIVE)

game_lobby = []

vk_chat_id = ''

try:
	while true:
		for event in longpoll.listen():
			if event.type == VkBotEventType.MESSAGE_NEW:
				if event.from_chat:
					if event.obj.text.lower() == 'старт игра' and str(event.obj.from_id) == '612651547':
						vk_send_message_to_chat(vk, event.chat_id, 'Олежа скомандовал начать игру. Я начинаю, а он идет нахуй')
						vk_chat_id = event.chat_id
						raise IndexError('wdwdwd')
except:
	pass			

print('брейкнуто')

try:
	while true:
		if len(game_lobby) != 4:
			for event in longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					if event.from_chat:
						if event.obj.text == 'я_в_говне':
							vk_send_message_to_chat(vk, event.chat_id, f'Ты в говне! Ой, в игре! Сейчас участников: {len(game_lobby)}, их список: {game_lobby}')
		else:
			raise IndexError
except:
	pass

vk_send_message_to_chat(vk, vk_chat_id, f'Участники: {game_lobby}. Готовьтесь получить карты в личку и сосите мой хуй. Да начнется порево анальное!')