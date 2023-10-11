# Discord bot import
import discord
import requests

# My program import
# none

# 変数宣言
# BCDice-APIのURL
dice_api = 'https://bcdice.onlinesession.app/v2/game_system/Cthulhu/roll?command='

class dice:
    async def trpg_dice(self, interaction, secret, args):

        if secret == 'off':
            try:
                # BCDice-APIから結果を取得
                result = requests.post(dice_api + args).json()

                print(result)

                # メッセージ表示
                embed=discord.Embed(title=args, description=result["text"])
                await interaction.response.send_message(embed=embed)

            except Exception as e:
                embed=discord.Embed(title="エラーが発生しました。", description="入力した値を確認してください。")
                await interaction.response.send_message(embed=embed)
        else:
            try:
                # BCDice-APIから結果を取得
                result = requests.post(dice_api + args).json()

                print(result)

                # メッセージ表示
                embed=discord.Embed(title=args, description=result["text"])
                await interaction.response.send_message(embed=embed, ephemeral=True)

            except Exception as e:
                embed=discord.Embed(title="エラーが発生しました。", description="入力した値を確認してください。")
                await interaction.response.send_message(embed=embed, ephemeral=True)