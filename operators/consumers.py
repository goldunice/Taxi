from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from .serializers import *
import json
from asgiref.sync import sync_to_async


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("order_group", self.channel_name)
        await self.send_initial_order_list()

    async def send_initial_order_list(self):
        order_list = await self.get_order_list()
        await self.send(text_data=json.dumps(order_list))

    @sync_to_async
    def get_order_list(self):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return serializer.data

    async def add_new_order(self, event):
        await self.send_initial_order_list()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("order_group", self.channel_name)
