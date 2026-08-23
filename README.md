# サイエンス・ディープダイブ

物理・化学・数学の「なぜ？」を、小学生の直感から大学レベルの数理まで掘り下げる科学読み物メディア。
Astro + GitHub Pagesで構築、維持費0円。

- 公開URL: https://yama-su.github.io/science-deepdive-web/
- リポジトリ: https://github.com/Yama-su/science-deepdive-web

## プロジェクト構成

```text
/
├── content-backlog.md          # 記事ネタ帳（小学生/大学生 x 物理/化学/数学）
├── scripts/                    # シミュレーション画像生成用Pythonスクリプト
├── public/assets/simulations/  # 生成したPNG/GIF置き場
├── src/
│   ├── content/blog/*.md       # 記事本文（Frontmatter付きMarkdown）
│   ├── content.config.ts       # 記事のFrontmatterスキーマ（zod）
│   ├── layouts/ArticleLayout.astro  # 記事レイアウト + 広告枠
│   ├── components/AdSlot.astro      # 広告スロットコンポーネント
│   ├── styles/science-deepdive.css  # デザインシステムCSS
│   └── pages/
│       ├── index.astro         # トップページ（記事一覧）
│       └── blog/[...slug].astro  # 記事詳細ページ
└── .github/workflows/deploy.yml  # push時に自動ビルド＆GitHub Pagesへデプロイ
```

## コマンド

| コマンド | 内容 |
| :--- | :--- |
| `npm install` | 依存関係のインストール |
| `npm run dev` | ローカル開発サーバー起動 (http://localhost:4321) |
| `npm run build` | 本番ビルド (`./dist/`) |
| `npm run preview` | ビルド結果のローカルプレビュー |
| `python scripts/generate_divide_by_zero_sim.py` | サンプルのシミュレーション画像/GIF生成例 |

## 新しい記事の追加手順

1. `content-backlog.md` から題材を選ぶ（または新しい疑問を追加する）
2. 必要ならPythonで数値シミュレーションを行い、`public/assets/simulations/` にPNG/GIFを保存
3. `src/content/blog/<slug>.md` を作成し、既存記事(`why-cannot-divide-by-zero.md`)のFrontmatter構成をコピーして編集
   - 画像パスは `/assets/...` のように**先頭スラッシュの絶対パス**で書く（ビルド時に自動でbaseパスが付与される）
4. `npm run build` でエラーが出ないか確認 → `git add` → `git commit` → `git push`
5. pushすると GitHub Actions が自動でビルド・デプロイする（数分でサイトに反映）

## アフィリエイト広告の導入手順

広告タグの挿入場所はすでに `src/components/AdSlot.astro` としてテンプレート化済み（記事上部・記事下部）。
アカウント登録・審査はご自身で行う必要がある。

### 1. どの広告サービスを使うか

| サービス | 特徴 | 審査 |
| :--- | :--- | :--- |
| Google AdSense | クリック課金、汎用的なバナー広告 | あり（サイトの記事数・品質が一定必要） |
| A8.net | 国内最大級のASP、書籍・教材等のアフィリエイト案件多数 | サイトごとに軽い審査 |
| もしもアフィリエイト | Amazon/楽天商品リンクを扱いやすい | 軽い審査 |
| Amazonアソシエイト | 関連書籍の紹介に最適 | 実績（初回売上）が必要な場合あり |

科学記事なら「関連書籍・教材」との相性が良いため、A8.net / もしもアフィリエイト + Amazonアソシエイトの組み合わせがおすすめ。

### 2. 登録の流れ（共通）

1. 各サービスのサイトで自分のGoogleアカウント等を使って新規登録（★このアカウント作成はご自身で行ってください）
2. サイトURL (`https://yama-su.github.io/science-deepdive-web/`) を登録し、審査を申請
   - 審査には記事が最低5〜10本程度ある方が通りやすい。`content-backlog.md` から数本追加しておくと良い
3. 審査通過後、広告タグ（`<ins>`や`<iframe>`、`<script>`など）が発行される

### 3. サイトへの設置方法

発行されたタグを `src/components/AdSlot.astro` の該当箇所（コメントで場所を明示済み）に貼り付けるだけで、
すべての記事の同じ位置（記事上部・記事下部）に自動で反映される。

```astro
<!-- src/components/AdSlot.astro のslot部分、または直接コンポーネント内に -->
<div class={`ad-slot ${position}-ad`}>
  <div class="ad-label">{labels[position]}</div>
  <!-- ここに発行されたタグをそのまま貼り付ける -->
</div>
```

Amazon/楽天の商品リンクなど記事ごとに変える広告は、`ArticleLayout.astro`内の
「おすすめの関連書籍・専門書」コールアウト、または各記事のMarkdown本文に直接埋め込む。

### 4. 審査に関する注意

- Google AdSenseは「サイト運営者情報（プライバシーポリシー・お問い合わせ）」ページの有無を見られることが多いため、
  必要であれば `src/pages/privacy.astro` 等を追加しておくと審査が通りやすい
- 広告タグの設置・エディット自体はコードの変更なのでいつでも私（Claude）に依頼できるが、
  各サービスへの登録・利用規約への同意・審査申請はご本人の操作が必要
