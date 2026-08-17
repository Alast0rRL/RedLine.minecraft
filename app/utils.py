# app/utils.py
from mcstatus import JavaServer

# Замени на IP своего сервера. 
# Если сервера пока нет, используй 'mc.hypixel.net' для тестов, чтобы видеть цифры.
MC_SERVER_IP = "redline.necr0manth.dev" 

async def get_minecraft_status():
    try:
        # Асинхронный запрос статуса
        server = await JavaServer.async_lookup(MC_SERVER_IP)
        status = await server.async_status()
        
        return {
            "online": True,
            "players": status.players.online,
            "max_players": status.players.max,
            "latency": round(status.latency)
        }
    except Exception as e:
        # Если сервер выключен или ошибка
        return {
            "online": False,
            "players": 0,
            "max_players": 0,
            "error": str(e)
        }