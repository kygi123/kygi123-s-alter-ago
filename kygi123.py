import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("botstart")
    await client.change_presence(status=discord.Status.online)


    @client.event
    async def on_message(message):
        if message.author.bot:
            return None


        if message.content.startswith("?"):
            string_pool ="!?????왜?????ㅋ???"
            num = random.choice(string_pool)
            await message.channel.send(num)



        if message.content == ("태준"):
            await message.channel.send("ㅖ")

        if message.content == ("김태준"):
            await message.channel.send("ㅖ")

        if message.content == ("돼준"):
            await message.channel.send("왜")

        if message.content == ("돼지"):
            await message.channel.send("?")

        if message.content == ("어디감"):
            await message.channel.send("밖에?")

        if message.content == ("언제옴"):
            await message.channel.send("곧?")

        if message.content == ("그러게"):
            await message.channel.send("말이야")

        if message.content == ("나의라임오렌지나무"):
           await message.channel.send("Meu Pé de Laranja Lima")

        if message.content.startswith("와"):
            await message.channel.send("샌즈!")

        if message.content == ("머하누"):
            await message.channel.send("ㅉㅉ")

        if message.content.startswith("오잉"):
            await message.channel.send("잉오")

        if message.content == ("이스터에그"):
            await message.channel.send("그걸 여기서 왜찾누")

        if message.content == ("클라이언트 코드"):
            await message.channel.send("Njc0Mjc3MjMwODU1MzIzNjQ5.Xj5PTg.3bxfGsWDt7BpBXcdD8ZXZ5duzIk")

        if message.content == ("탈모"):
            await message.channel.send("?")

        if message.content == ("태준아"):
            await message.channel.send("ㅖ")

        if message.content == ("태준 탈모"):
            await message.channel.send("뒤져")

        if message.content == ("태준 돼지"):
            await message.channel.send("머래 아님")

        if message.content == ("돼지 태준"):
            await message.channel.send("아님")

        if message.content == ("머누"):
            await message.channel.send("머임")

        if message.content.startswith("샌즈"):
            e = discord.Embed(title='Wa!', description="sans!", color=0xAFEEEE)
            e.set_footer(text="so strong")
            e.set_image(url="https://media.giphy.com/media/UCkZPALajEs8M/giphy.gif")
            await message.channel.send(" ", embed=e)

        if message.content.startswith("닉"):
            await message.channel.send("kygi123")

        if message.content == ("주사위"):
            dice = "123456"
            dice = random.choice(dice)
            await message.channel.send(dice)

        if message.content.startswith("도배"):
            await message.channel.send("하지마")

        if message.content == ("애옹"):
            await message.channel.send("애옹")

        if message.content == ("마"):
            await message.channel.send("자신 있나")

        if message.content ==("자기소개"):
            await message.channel.send("My Manufacture Name is kygi123's Alter ago, 21 Millenium old and Created by kygi123")














client.run("Njc0Mjc3MjMwODU1MzIzNjQ5.XkEd1g.KWkAvEuoTs-eD8FaUlweEvGLqv0")
