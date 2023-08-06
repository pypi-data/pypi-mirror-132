# recentquake
　過去３０日の地震のリアルタイムのデータからどのような特徴があるのかを示したグラフを表示する。国名とマグニチュードを指定することができる。知りたい国で知りたいマグニチュードを引数に入力すれば、指定した条件のデータ数と、その条件にあった4つのグラフが表示され、1つのhtmlファイルがブラウザで表示される。
データ：usgs(https://earthquake.usgs.gov/earthquakes/feed/v1.0/) 世界中のリアルタイムのデータベース

グラフ１：指定したマグニチュードと国での、マグニチュードの箱ひげ図<br>
グラフ２：指定したマグニチュードと国での、マグニチュードのヒストグラム<br>
グラフ３：指定したマグニチュードと国での、マグニチュードと深さの散布図<br>
グラフ４：指定したマグニチュードと国での、1日ごとの地震の回数の棒グラフ<br>
htmlファイル：指定したマグニチュードと国での、地震が起きたところの緯度経度をプロットした地図

<h1>recentquakeのインストール方法</h1>
recentquakeは公開されており、次のPyPIパッケージコマンドでインストールできます。<br>
$pip install recentquake

<h1>recentquakeを実行する方法</h1>
recentquakeには3つのパラメータ(国、マグニチュードの最小値、マグニチュードの最大値)を設定する必要がある。<br>
国名は一度実行した時にcountry_listとして得られるが、例として下に示しておく。<br>
$recentquake 'Japan' 4 7

```
#出力例
$recentquake 'Japan' 4 7
country_list
['Nevada', 'CA', 'Hawaii', 'Alaska', 'Pakistan', 'Timor Leste', 'south of the Kermadec Islands', 'California', 'Peru', 'Fiji region', 'France', 'South Sandwich Islands region', 'Papua New Guinea', 'Idaho', 'Puerto Rico region', 'New Zealand', 'Puerto Rico', 'Fiji', 'Laos', 'Southern Alaska', 'Myanmar', 'Greece', 'Yemen', 'Chile', 'Maine', 'Afghanistan', 'Indonesia', 'Mexico', 'Washington', 'Oklahoma', 'Colorado', 'California-Nevada border region', 'Turkey', 'Pacific-Antarctic Ridge', 'Nicaragua', 'Mongolia', 'Banda Sea', 'India region', 'Italy', 'Utah', 'Montana', 'Tennessee', 'Bolivia', 'U.S. Virgin Islands', 'B.C., MX', 'Texas', 'Wyoming', 'Kentucky', 'Japan', 'Canada', 'New Mexico', 'Morocco', 'Vanuatu', 'Antigua and Barbuda', 'Oregon', 'Argentina', 'Central Alaska', 'south of the Fiji Islands', 'Dominican Republic', 'China', 'Molucca Sea', 'Russia', 'Iceland', 'Alabama', 'Japan region', 'Missouri', 'India', 'Mona Passage', 'Western Montana', 'Iran', 'Haiti', 'Tristan da Cunha region', 'Guatemala', 'central Mid-Atlantic Ridge', 'Alaska, Alaska', 'South Atlantic Ocean', 'Philippines', 'off the coast of Oregon', 'Svalbard and Jan Mayen', 'Tonga', 'Ecuador', 'South Carolina', 'Virgin Islands region', 'Central California', 'Colombia', 'western Montana', 'Aleutian Islands, Alaska', 'northern Alaska', 'Illinois', 'Solomon Islands', 'Kuril Islands', 'Arkansas', 'Arizona', 'Guam', 'El Salvador', 'Prince Edward Islands region', 'Taiwan', 'Costa Rica', 'Kansas', 'Chagos Archipelago region', 'Greenland Sea', 'Tajikistan', 'Nepal', 'Kermadec Islands region', 'Honduras', 'Celebes Sea', 'Somalia', 'western Xizang', 'south of Panama', 'Mid-Indian Ridge', 'southeastern Missouri', 'western Texas', 'Federated States of Micronesia', 'Malawi', 'South Africa', 'western Indian-Antarctic Ridge', 'Carlsberg Ridge', 'northwest of the Kuril Islands', 'Philippine Islands region', 'Flores Sea', 'north of Severnaya Zemlya', 'South Korea', 'Northern Mariana Islands', 'Bonaire, Saint Eustatius and Saba ', 'southeast of Easter Island', 'Vietnam', 'New Caledonia', 'southern East Pacific Rise', 'Sea of Okhotsk', 'south of Africa', 'Ohio', 'west of Macquarie Island', 'Mauritius - Reunion region', 'Balleny Islands region', 'Anguilla', 'Washington-Oregon border region', 'Poland', 'Australia', 'Panama', 'central East Pacific Rise', 'Alaska Peninsula', 'South Indian Ocean', 'Venezuela', 'Gulf of Alaska', 'Azores-Cape St. Vincent Ridge', 'West Virginia', 'Louisiana', 'West Chile Rise', 'Afghanistan-Tajikistan-Pakistan region', 'Southwest Indian Ridge', 'near the coast of Nicaragua', 'North Carolina', 'Near the coast of western Turkey', 'southeast of the Loyalty Islands', 'Easter Island region', 'Norway', 'southern Mid-Atlantic Ridge', 'Chile-Argentina border region', 'southern Iran', 'North Atlantic Ocean', 'Azerbaijan', 'New Hampshire', 'OR', 'Wallis and Futuna', 'Idaho-Montana border region', 'southeast Indian Ridge', 'Myanmar-India border region', 'north of Svalbard', 'central Peru', 'Reykjanes Ridge', 'northern Mid-Atlantic Ridge', 'Vanuatu region', 'Santa Cruz Islands']
データ数：68
```
<img src="japan4-7.png" width="400">
<img src="japan4-7map.png" width="400">














