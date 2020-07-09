from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GameConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = 'game_%s' % self.game_name

        # Join room group
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        directions = content['directions']
        # Send directions to game
        await self.channel_layer.group_send(
            self.game_group_name,
            {
                'type': 'game.directions',
                'directions': directions
            }
        )

    async def game_directions(self, message):
        await self.send_json({
            'directions': message['directions']
        })
