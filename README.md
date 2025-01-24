# python-omikuji

このプロジェクトは、作者がpythonで「おみくじ」を作成するまでの記録です。

ポートフォリオとして提出されることを想定しています。

## 「おみくじ」実行方法

```bash
python src/main.py
```

## pushまでの流れ

### 実装修正するためにブランチを作成

最新のdevelopブランチから、新しくfeatureブランチを作成

### flake8, pytest を実施

```bash
# flake8実施
flake8
```

```bash
# pytest実施
python -m pytest tests
```

エラーがないことを確認

### push

必要なファイルをコミットしプッシュする

## Windows環境でgitbash使用時の.venv activate方法

```bash
source ./.venv/Scripts/activate
```

## 備考

なし
