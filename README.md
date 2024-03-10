# claude3-video

claude3 を使って動画を作成します

## 必要条件

- Python 3.7 以上
- Manim ライブラリ
- FFmpeg

## セットアップ

1. このリポジトリをクローンします。

```bash
git clone https://github.com/Sunwood-ai-labs/claude3-video.git
cd claude3-video
```

2. 必要な依存関係をインストールします。

### Ubuntu / Mint / Debian

```bash
apt update
apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

### その他の OS

お使いの OS に応じて、Cairo、Pango、および FFmpeg をインストールしてください。

3. Manim ライブラリをインストールします。

```bash
pip install manim
```

4. Manim のバージョンを確認します。

```bash
pip show manim
```

## 使用方法

アニメーションをレンダリングするには、以下のコマンドを実行します。

```bash
manim -pqh A_Neurons_Perspective.py NeuronPOV
```

- `-p` フラグは、レンダリング後にアニメーションを再生します。
- `-qh` フラグは、高品質でレンダリングします。
- `A_Neurons_Perspective.py` は、Python スクリプトのファイル名です。
- `NeuronPOV` は、レンダリングするシーンの名前です。

レンダリングが完了すると、`media/videos/main/1080p60/NeuronPOV.mp4` にアニメーションが保存されます。
