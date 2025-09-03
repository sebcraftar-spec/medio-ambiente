import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Datos ambientales: tiempo de descomposición y idea de reutilización
objetos = {
    "botella de plastico": {
        "descomposicion": "450 años",
        "reutilizacion": "Córtala para hacer una maceta o un embudo casero."
    },
    "lata de aluminio": {
        "descomposicion": "200 años",
        "reutilizacion": "Haz un portalápices o una pequeña vela decorativa."
    },
    "bolsa plastica": {
        "descomposicion": "100 a 1000 años",
        "reutilizacion": "Trénzala como cuerda o relleno para cojines."
    },
    "cepillo de dientes": {
        "descomposicion": "500 años",
        "reutilizacion": "Úsalo para limpiar esquinas o para arte con pintura."
    },
    "colilla de cigarro": {
        "descomposicion": "10 años",
        "reutilizacion": "No se recomienda reutilización. Desechar correctamente."
    }
}

@bot.event
async def on_ready():
    print(f"✅ Hemos iniciado sesión como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    contenido = message.content.lower()

    if contenido.startswith("!descomposicion"):
        partes = contenido.split(" ", 1)
        if len(partes) == 2:
            objeto = partes[1].strip()
            if objeto in objetos:
                info = objetos[objeto]
                await message.channel.send(
                    f"🧪 **{objeto.capitalize()}** tarda en descomponerse aproximadamente **{info['descomposicion']}**.\n"
                    f"♻️ Idea para reutilizar: {info['reutilizacion']}"
                )
            else:
                await message.channel.send("❌ No tengo información sobre ese objeto. Prueba con: botella de plastico, lata de aluminio, etc.")
        else:
            await message.channel.send("ℹ️ Usa el comando así: `!descomposicion botella de plastico`")

    elif contenido == "!manualidad":
        mensaje = "**🎨 Ideas de manualidades ecológicas:**\n"
        for obj, info in objetos.items():
            mensaje += f"🔹 {obj.capitalize()}: {info['reutilizacion']}\n"
        await message.channel.send(mensaje)

    elif contenido == "!imagen":
        try:
            with open('medio.jpg', 'rb') as f:  # Usa una imagen llamada medio.jpg
                picture = discord.File(f)
                await message.channel.send(content="🌍 Aquí tienes una imagen ecológica:", file=picture)
        except FileNotFoundError:
            await message.channel.send("No creo que pueda representar esto con una imagen")

    await bot.process_commands(message)
