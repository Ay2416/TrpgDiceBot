# TrpgDiceBot

#Japanese
## 概要
Discord上でBCDiceシステムを利用し、TRPG用のダイスロールやシークレットダイス機能を提供するDiscord Botです。
## 使用技術
- 言語: Python 3.x
- ライブラリ/フレームワーク: discord.py, python-dotenv, requests
- 外部API: BCDice-API
- その他: なし
## 使い方
### 前提条件
- Python 3.x がインストールされていること
- Discord Botのトークンを取得済みであること
### インストール方法
以下の手順に従って、ご自身の環境にプロジェクトをセットアップしてください。

1. リポジトリをクローンします。
```bash
git clone https://github.com/Ay2416/TrpgDiceBot.git
```

2. プロジェクトのディレクトリに移動します。
```bash
cd TrpgDiceBot
```

3. 必要なパッケージをインストールします。
```bash
pip install -r requirements.txt
```
### 基本的な使い方
```bash
python main.py
```
## 主な機能

- **`/trpg dice [secret] [args]`**
  ダイスを振るコマンドです。
  - `secret` (必須): `on`（実行者のみに結果を表示するシークレットダイス）、`off`（全体に結果を表示）のいずれかを指定します。
  - `args` (必須): `1d100` など、ダイスの種類や計算式などの引数を指定します。

## 設定
プロジェクトルートディレクトリに `.env` ファイルを作成し、以下の環境変数を設定してください。
- `token` : Discord Botのトークン

## APIリファレンス / ドキュメント
- BCDice
  - [https://bcdice.org/](https://bcdice.org/)
  - [https://github.com/bcdice/BCDice](https://github.com/bcdice/BCDice)

## ライセンス
- Author
  - Faceless さん
  - たいたい竹流 さん
- License
  - BSD 3-Clause License
  - [https://github.com/Ay2416/TrpgDiceBot/blob/main/LICENSE](https://github.com/Ay2416/TrpgDiceBot/blob/main/LICENSE)

# English
## Overview
A Discord Bot that provides TRPG dice rolling and secret dice features on Discord using the BCDice system.
## Technologies Used
- Language: Python 3.x
- Libraries/Frameworks: discord.py, python-dotenv, requests
- External API: BCDice-API
- Other: None
## Usage
### Prerequisites
- Python 3.x must be installed.
- A Discord Bot token must be obtained.
### Installation
Follow these steps to set up the project in your local environment.

1. Clone the repository.
```bash
git clone https://github.com/Ay2416/TrpgDiceBot.git
```

2. Move to the project directory.
```bash
cd TrpgDiceBot
```

3. Install the required packages.
```bash
pip install -r requirements.txt
```
### Basic Usage
```bash
python main.py
```
## Main Features

- **`/trpg dice [secret] [args]`**
  A command to roll the dice.
  - `secret` (Required): Specify either `on` (secret dice, result is visible only to the executor) or `off` (result is visible to everyone).
  - `args` (Required): Specify the dice type or calculation formula as an argument, such as `1d100`.

## Configuration
Create a `.env` file in the project root directory and set the following environment variable.
- `token` : Your Discord Bot token.

## API Reference / Documentation
- BCDice
  - [https://bcdice.org/](https://bcdice.org/)
  - [https://github.com/bcdice/BCDice](https://github.com/bcdice/BCDice)

## License
- Author
  - Faceless
  - たいたい竹流 (Taitai Takeru)
- License
  - BSD 3-Clause License
  - [https://github.com/Ay2416/TrpgDiceBot/blob/main/LICENSE](https://github.com/Ay2416/TrpgDiceBot/blob/main/LICENSE)
