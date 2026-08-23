---
id: "science-deepdive-005"
title: "雷はなぜ光ってから音が遅れて聞こえるのか：光速と音速の大きな差"
slug: "why-thunder-delay"
category: "physics"
tags: ["物理学", "音速", "光速", "シミュレーション"]
target_audience: ["小学生", "中高生", "大学生・一般"]
reading_time_minutes: 9
page_count_a4: 4
published_at: "2026-08-23"
author:
  name: "サイエンス・ディープダイブ編集部"
  avatar: "/assets/authors/editorial.png"
seo:
  meta_title: "雷はなぜ光ってから音が遅れるの？光速と音速の違いを解説"
  meta_description: "稲光が見えてから、ゴロゴロという音が遅れて聞こえるのはなぜか。光速と音速の圧倒的な差から、雷までの距離を計算する方法まで解説。"
  og_image: "/assets/simulations/thunder_delay.png"
lead_excerpt: "ピカッと光った後、少し遅れてゴロゴロと音が聞こえる雷。光と音は同時に発生しているはずなのに、なぜ届くタイミングがずれるのでしょうか。"
table_of_contents: true
math: true
syntax_highlight: true
has_affiliate_links: false
---

## 1. 素朴な疑問

雷が発生すると、ピカッという光の後に、少し遅れてゴロゴロという音が聞こえます。光と音は同じ雷の放電から同時に発生しているはずなのに、なぜ届く時間がずれるのでしょうか。

## 2. よくある発想

<div class="callout callout-intuition">
  <div class="callout-title">よくある3大直感</div>
  <ul>
    <li><strong>直感1：</strong>「音の方が後から発生する」説</li>
    <li><strong>直感2：</strong>「光は目、音は耳と、感じ方の違いによる遅れ」説</li>
    <li><strong>直感3：</strong>「雲の中で音が反響して遅れる」説</li>
  </ul>
</div>

実際には光と音はほぼ同時に発生しています。ずれの正体は、両者が私たちに届くまでの「速さ」の違いです。

## 3. わかりやすい模範的答え

<div class="callout callout-kids">
  <div class="callout-title">子どもへの伝え方（要点）</div>
  <p>
    光はものすごく速く進むので、遠くの雷でもほぼ一瞬で目に届きます。
    でも音は光よりずっとゆっくり進むので、遠くまで届くのに時間がかかります。
    だから同時に発生した光と音でも、光が先に届いて、音は少し遅れて届くのです。
  </p>
</div>

## 4. わかりやすく厳密な答え

光の速さ（光速）は真空中で約 $3.0 \times 10^8$ m/s（秒速30万km）です。一方、空気中の音の速さ（音速）は気温にもよりますが、約 $343$ m/s（秒速343m）程度に過ぎません。

<div class="math-proof-box">
  <div class="proof-header">光速と音速の比</div>
  <div class="proof-body">
    $$\frac{v_{\text{light}}}{v_{\text{sound}}} = \frac{3.0 \times 10^8}{343} \approx 875{,}000$$
    光は音のおよそ87万倍の速さで進む。そのため、雷までの距離が数kmであっても、
    光はほぼ瞬間的に届くのに対し、音は数秒かけて届く。
  </div>
</div>

この性質を利用すると、光ってから音が聞こえるまでの秒数を数えるだけで、雷までのおおよその距離を計算できます。音速は約343m/sなので、1秒あたり約343m、つまり約3秒で1kmと覚えておくと便利です。

$$\text{距離(km)} \approx \text{遅延時間(秒)} \times 0.343$$

## 5. 数値シミュレーション

雷までの距離と、光ってから音が聞こえるまでの遅延時間の関係をグラフにしました。

![雷までの距離と音の遅延時間の関係を示すグラフ](/assets/simulations/thunder_delay.png)
*図1: 距離が3kmなら、光ってから音が聞こえるまで約8.7秒かかる*

```python
SPEED_OF_SOUND = 343.0  # m/s

distance_km = 3.0
delay_seconds = (distance_km * 1000) / SPEED_OF_SOUND
# delay_seconds ≈ 8.75秒
```

## 6. まとめ

<div class="callout callout-summary">
  <div class="callout-title">この疑問が教えてくれる世界の見方</div>
  <p>
    雷の光と音のずれは、単なる不思議な現象ではなく、光速と音速という物理量の差を体感できる身近な実験です。
    次に雷が鳴ったら、光ってから音が聞こえるまでの秒数を数えて、雷までの距離を計算してみましょう。
  </p>
</div>
