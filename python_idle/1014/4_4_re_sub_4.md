# Python 維基百科精準清洗結果

關於與「Python」標題相近或相同的條目，請見「Python (消歧義)」。

Python

編程範型	多範式：程序式、結構化、模組化、反射式、物件導向、函數式

設計者	吉多·范羅蘇姆

實作者	Python軟體基金會

面市時間	1991年，​35年前​（1991）[1]

目前版本
3.15.0（2026年10月9日；穩定版本）[2]

類型系統	鴨子型別[3]、動態、強型別[4]、漸進（英語：gradual typing）（自從3.5）[5]

作業系統	跨平臺[6]

授權條款	Python軟體基金會授權條款

副檔名	.py、.pyi、.pyc、.pyd、.pyo（3.5之前）[7]、.pyw、.pyz（自從3.5）[8]

網站	www.python.org

主要實作產品

CPython、PyPy、Stackless Python、MicroPython、CircuitPython（英語：CircuitPython）、IronPython、Jython

衍生副語言

Cython、RPython

受影響於

ABC[9]、ALGOL 68[10]、APL[11]、C[12]、C++[13]、CLU[14]、Dylan[15]、Haskell[16]、Icon[17]、Java[18]、Lisp[19]、Modula-3[13]、Perl[20]、Standard ML[11]

影響語言

Boo[21]、Cobra（英語：Cobra (programming language)）[22]、CoffeeScript[23]、D、F#、GDScript[24]、Genie、Go[25]、Groovy[26]、JavaScript[27][28]、Julia[29]、Kotlin[30]、Mojo[31]、Nim[32]、Ruby[33]、Starlark（英語：Starlark）[34]、Swift[35]、V（英語：V (programming language)）[36]

維基教科書中有關zh:Python的文字

Python（英語發音：/ˈpaɪθən/；英語發音：/ˈpaɪθɑːn/），是一種廣泛使用的直譯式、進階和通用的程式語言。Python支援多種程式設計範式，包括結構化、程序式、反射式、物件導向和函數式程式設計。它擁有動態型別系統和垃圾回收功能，能夠自動管理主記憶體使用，並且其本身擁有一個巨大而廣泛的標準庫。它的語言結構以及物件導向的方法，旨在幫助程式設計師為小型的和大型的專案編寫邏輯清晰的程式碼。

吉多·范羅蘇姆於1980年代後期開始研發Python，作為ABC語言的後繼者[17]，它也可以被視為採用了叫做M-表達式（英語：M-expression）的中綴表示法的一種LISP方言[37]。吉多·范羅蘇姆於1991年首次釋出 Python 0.9.0[38]。Python 2.0於2000 年釋出並引入了新功能。Python 3.0於2008年釋出，它是該語言的主要修訂版，並非完全向下相容。Python 2於2020年隨2.7.18版停止支援[39]。

Python的設計哲學，強調程式碼的可讀性和簡潔的語法，尤其是使用空格縮排來劃分程式碼塊。相比於C語言或Java，Python讓開發者能夠用更少的代碼表達想法。

Python直譯器本身幾乎可以在所有的作業系統中執行，它的官方直譯器CPython是用C語言編寫的。Python是一個由社群驅動的自由軟體，目前由Python軟體基金會管理。Python是最受歡迎的程式語言之一[40][41]。

歷史
[編輯]
主條目：Python的歷史

Python創始人吉多·范羅蘇姆在2024年PyCon的相片

Python的創始人吉多·范羅蘇姆，在1982年至1995年間，參與了荷蘭數學和電腦科學研究學會多個專案的工作[42]。1989年的聖誕節期間，他決心開發一個新的指令碼解釋程式，作為ABC語言的後繼者，並且用它替代Unix shell和C語言來進行系統管理[17]，擔負與Amoeba作業系統（英語：Amoeba (operating system)）[43]之間的互動操作並進行例外處理[9]。他是BBC電視劇《Monty Python的飛行馬戲團》的愛好者，所以選取了Python作為這個程式語言的名字[44]。

在1991年2月，范羅蘇姆在Usenet新聞群組alt.sources上釋出了標記為版本0.9.0的最初程式碼[1]，這時就已經存在了帶繼承的類、例外處理、函式和核心類型list、dict、str等。在這個最初發行中就有了從Modula-3引進的模組系統[45]，和例外處理機制[9]。

在1994年1月，Python 1.0釋出[46]，其主要新特徵是由Amrit Prem提供的函數式程式設計工具lambda、map、filter和reduce[47]。受Modula-3啟發，版本1.1介入了參數預設值，版本1.3介入了關鍵字參數。版本1.4介入了對複數的內建支援[48]。

在2000年10月，Python 2.0發布，它從函數式程式設計語言Haskell中引進了列表推導式[49]。版本2.1支援了靜態巢狀範疇[50]。版本2.2將用C語言寫成的類型，和用Python語言寫成的類，統一成純粹而一致的對象模型[51]；還介入了迭代器[52]，受CLU和Icon啟發的生成器[53]，和描述器協定[54]。版本2.3介入了從Dylan引進的方法決定次序[15]。版本2.4介入了集合（英語：Set (abstract data type)）類型，和函式修飾器[55]。版本2.5在官方實作中介入了抽象語法樹[56]。

在2008年12月，Python 3.0發布，它對語言做了較大修訂而不能完全後向相容[57]，故而版本2.7的產品壽命結束推延到了2020年元旦。版本3.4介入了非同步I/O模組[58]。版本3.5介入了類型提示[59]，和採用async/await語法的協程[60]。吉多·范羅蘇姆擔任終身仁慈獨裁者（BDFL）直到2018年7月12日[61][62]，他參與了2019年第一屆領導專案發展的五人掌控委員會[63][64]。

在2020年10月，版本3.9介入了內建的針對容器類的泛化別名（types.GenericAlias）類型[65]，並在官方實作中介入了新的語法解析器[66]。版本3.10介入了從Haskell和OCaml等借鑑來的結構式模式匹配[67]，和內建的聯合類型（types.UnionType）[68]。版本3.11對官方實作進行了最佳化提速[69]。版本3.12介入了類型參數語法[70]，並廢棄或移除了一些過時的模組和功能。

在2024年10月，版本3.13介入了從PyPy引進的新互動式直譯器，支援了實驗性的即時編譯器和自由執行緒[71]。版本3.14改進了自由執行緒模態，並在官方實作中增加了使用尾呼叫的新類型直譯器[72]。版本3.15介入了對模組的顯式惰性匯入[73]。

目前每個版本首次發行後，享有2年的完全支援，隨後是3年的安全支援。當前只有Python 3的穩定版本3.14與3.15正在被完全支援，但仍提供對版本3.11、3.12和3.13的安全性修正[74]。

自從2003年，Python始終排行於TIOBE程式社群索引（英語：TIOBE Programming Community Index）前十最流行程式語言，在2021年10月它首次達到了第一名最流行語言（居於C和Java之前），並被選為2007年、2010年、2018年、2020年、2021年和2024年的年度程式語言[41]。

在2025年12月，活躍的Python核心開發者，選舉Pablo Galindo Salgado、Savannah Ostrowski、Barry Warsaw、Donghee Na和Thomas Wouters，為2026年度掌控委員會的五位成員來領導這個專案[75]。

特徵與設計哲學
[編輯]

Python是多範式程式語言。它完全支援結構化程式和物件導向程式設計，還有很多特徵支援函數式程式設計和元程式設計比如元對象協定（元類和魔術方法[76]）。通過擴充還可以支援很多範式，包括面向方面程式[77]、契約式設計[78]和邏輯程式[79]。

Python使用動態型別，在主記憶體管理上採用的垃圾回收器基於了參照計數[80]，並且結合了檢測環參照的分代垃圾回收最佳化[81]。它的特徵還有動態名字解析（後期繫結（英語：late binding）），即在程式執行期間繫結方法和變數的名字。

Python對遵循LISP傳統的函數式程式設計提供了有限的支援[82]，它提供了 map、filter和reduce函式[83]；列表推導式、字典推導式、集合（英語：Set (abstract data type)）推導式和生成器表達式。標準庫中的模組functools和itertools，實作了從Haskell和Standard ML借鑑來的函數式工具[84]。

Python的設計理念是「優雅」、「明確」、「簡單」，它的一些重要準則被合稱為「Python之禪」。在Python解釋器內運行import this可以獲得完整的列表，下面舉出其中首要：

優美優於醜陋。明瞭優於隱晦。

簡單優於複雜。複雜優於凌亂。

扁平優於巢狀。稀疏優於稠密。

可讀性很重要。

Python開發者的方法論是「用一種方法，最好是只有一種方法來做一件事」，顯著不同於以Perl語言為代表的「不止一種方法去做一件事」風格。Python開發者在設計語言時，如果面臨多種選擇，一般會選擇明確沒有或者很少有歧義的語法。

范羅蘇姆將Python本身設計為可擴充的[85]，並不把所有的特性和功能都整合到語言核心，而是提供了豐富的API和工具，以便程式設計師能夠輕鬆地使用Python、C語言、Cython來編寫擴充模組。Python還可以通過外界函式介面（英語：Foreign function interface）如標準庫中的ctypes等，來提供C語言相容資料類型，並訪問動態連結庫或共享庫中的函式[86]，從而對用其他語言編寫的程式進行整合和封裝。

在Python的官方直譯器實作CPython中，一般避開不成熟的或者對非重要部位的加快運行速度的優化。在某些對運行速度要求很高的情況，可以使用具備即時編譯技術的直譯器[87]。

語法和語意
[編輯]
主條目：Python語法及語義

Python為了讓程式碼具備高度的可閱讀性，在設計時盡量使用了其它語言常用的符號和英文單字。

行結構
[編輯]

Python程式在詞法分析上被分成若干邏輯行。簡單語句包含在一個單一的邏輯行之內，Python支援使用分號作為分隔符，將多個簡單語句合併入一個邏輯行之中[88]。

注釋開始於並非字串文字（英語：string literal）一部份的一個井號#，並結束於物理行結尾；注釋標示邏輯行的結束，除非已受制於隱式行接續規則；注釋在語法上被忽略[89]。

Python支援使用反斜槓作為行接續符，將多個物理行合成為一個邏輯行[90]。在圓括號、方括號或花括號之中的表達式，可以分裂跨越多於一個物理行而不使用反斜槓，這被稱為「隱式行接續」[90]。

縮排
[編輯]

Python語法中的複合語句，包含了一些其他語句，它們以某種方式影響或控制這些其他語句的執行。Python的複合語句包含一個或多個子句（clause），子句構成自一個頭部（header）和一個套件（suite）。特定複合語句的子句頭部都在同樣的縮排層級上，每個子句頭部開始於一個唯一標識關鍵字，並結束於一個冒號。套件即語法意義上的塊，是這個子句所控制的一組語句。

套件有兩種形式：可以是與頭部在同一行上的一個或多個由分號分隔的簡單語句，它們跟隨在這個頭部的冒號之後；或者是遵循越位規則的在連續諸行上的一個或多個縮排的語句，只有這種套件形式可以包含巢狀的複合語句[91]。[a]

根據PEP 8的規定[92]，使用4個空格來表示每級縮排。[b]
縮排層級的變遷，被用來生成語法解析器才能見到的INDENT和DEDENT記號[94]，增加縮排就生成INDENT記號，減少縮排就生成DEDENT記號。二者的作用相當於C語言家族的花括號，或Pascal語言家族的關鍵字begin和end。

關鍵字
[編輯]

Python有如下35個關鍵字；它們不能用作識別碼[95]：

and

as

assert

async

await

break

class

continue

def

del

elif

else

except

False

finally

for

from

global

if

import

in

is

lambda

None

nonlocal

not

or

pass

raise

return

True

try

while

with

yield

內建常數True、False和None於Python版本3.0中成為關鍵字，關鍵字nonlocal介入於版本3.0[96]，關鍵字async和await介入於版本3.5[97]，並在版本3.7中成為正式關鍵字[98]。

在Python中，將只在特定上下文中保留的識別碼，稱為「軟關鍵字」[99]：

match、case和萬用字元_，介入於版本3.10，它們在與模式匹配語句有關的上下文中，可以在語法上充當關鍵字；但是這種區分只在語法解析器層次進行，並非在詞法分析記號化層次。

type，介入於版本3.12，它用於type語句。

lazy，介入於版本3.15，它用於import語句。

識別碼
[編輯]

識別碼就是名字，在ASCII範圍內（U+0001..U+007F），可用於識別碼的字元為：大寫字母A至Z和小寫字母a至z，底線_以及數字0至9，但首字不可以用數字。如下命名約定[100]，是為「保留識別碼類」[101]：

_spam（單底線開頭）：弱「內部使用」標識。對於from M import *，將不匯入所有以底線開頭的對象。

spam_（單底線結尾）：為了避免與python關鍵字的命名衝突。

__spam（雙底線開頭）：在命名一個類特性的時候，採用名字修飾，比如在類SpamEggs內，__spam將變成_SpamEggs__spam[102]。

__spam__（雙底線開頭結尾）：指那些包含在使用者控制的命名空間中的「魔術」方法或特性，比如__delattr__、__dir__、__doc__、__getattribute__[103]、__init__、__new__、__repr__、__setattr__、__sizeof__等。建議永遠不要將這樣的命名方式應用於自己的變數或函式。

語句
[編輯]

Python的語句包括簡單語句：

賦值語句，採用的中綴記號是等號=。賦值語句被用來將名字繫結（含重新繫結）到值，以及用來修改可變對象的特性或專案。賦值語句支援鏈式賦值。

支援「序列解包」[104]：在等號左側可以是一個表達式列表，其中每個表達式都可求值成能被賦值的東西；在等號右側相應的是一個「可迭代」對象，它在被迭代時產生的值的數量，同於左手側可寫表達式的數量；賦值語句對這個對象進行迭代，將產生的每個值分別賦值給左側對應的可賦值者。在等號右側直接包裝出序列解包所要求的元組，就形成了並列賦值。[c]

支援增廣賦值語句[105]，將一個二元運算和一個賦值語句合併成一個單一語句，例如x += 1。

自從版本3.6，介入了標註賦值語句[106]。

表達式（英語：Expression (computer science)）語句，用來互動式的計算並寫出一個值，或者用來呼叫一個過程（即返回無含義結果的函式），在Python中過程返回值None。

global語句，是在整個當前程式碼塊中成立的聲明，它意味著隨後列出的識別碼被直譯為總體變數。

nonlocal語句，導致隨後列出的識別碼，提及在除了全域範疇之外的最近包圍範疇中的先前繫結變數。

del語句，遞迴的進行刪除。

type語句，聲明作為類型別名類型（typing.TypeAliasType）的實例的一個類型別名。

pass語句，充當無操作指令，表示此行為空，不執行任何操作。

assert語句，用於程式調適階段時測試執行條件是否滿足。

continue語句，越過這次迭代並繼續進行下個專案。

break語句，從迴圈中跳出。

raise語句，丟擲一個例外。

return語句，用來從函式返回值。當函式執行到return語句時，它會停止執行並將指定的值返回給呼叫者。

yield語句，用來從一個生成器中返回一個值[107]，yield語句在語意上等價於加圓括號的yield表達式[108]，在函式主體中使用yield表達式將導致它成為生成器函式。[d]

通過生成器的send()方法傳入的資訊，就是其中yield表達式的返回值。[e]

自從版本3.3，介入了yield from語句，它在語意上等價於加圓括號的yield from表達式，含有此表達式的生成器函式將特定任務委託給另一個子生成器函式，將傳入資訊遞送給它並直接回傳它產生的值[110]。

自從版本3.6，在協程函式主體中使用yield表達式將導致它成為非同步生成器函式[111]。

import語句，匯入一個模組或包，它組合了兩種操作，尋找指名的模組，接著將找到的結果繫結到在局部範疇中的名字。匯入語句有三種形式（下述語句樣本採用了EBNF，這裡的方括號表示其中內容為可選的）：

import 模块名字 [as 别名]，找到一個模組，裝載它，如果有需要的話初始化它；在這個匯入語句出現的範疇的局部命名空間中，定義一個名字或一些名字[112]。

from 模块名字 import 定义1 [as 别名1], 定义2 [as 别名2], …，找到、裝載、必需時初始化一個模組；接著在局部命名空間中，增加到找到指名特性的參照[112]。

from 模块名字 import *，在匯入語句出現的範疇的局部命名空間中，繫結模組中定義的所有公開的名字[113]。

複合語句：

if語句，當條件成立時執行語句套件。它經常包含elif、else子句。

while語句，當條件為真時，重複執行語句套件。

for語句，遍歷列表、字串、字典、集合等迭代器，依次處理迭代器中的每個元素。

match語句，用於模式匹配。

class語句，是定義類的可執行語句。[f]

def語句，是定義函式和方法的可執行語句。[g]

async def語句，用於協程函式定義。await表達式、async for語句和async with語句，只能用在協程函式的主體中。[h]

try（英語：Exception handling syntax）語句，它經常包含except、else、finally子句，處理在程式執行中出現的例外情況。版本3.11介入了except*子句[114]。Python支援並廣泛使用EAFP（請求原諒比獲得授權更容易）風格的例外處理，作為檢測錯誤狀況和程式中其他「例外」事件的方式。例如：在訪問一個檔案或資源之時，事先不進行測試就嘗試使用它，事後再擷取可能的訪問失敗所引發的例外。[i]

with語句，把一塊程式碼包裹在一個上下文管理器之內。它允許了RAII（對象初始化時取得資源）方式的行為，可替代常見的try/finally慣用法（英語：Programming idiom）。Python使用with語句處理資源[115]，例如：在執行一塊程式碼時，事先取得一個鎖，並且事後釋放這個鎖；或事先打開一個檔案，並且事後關閉這個檔案。[j]

塊與模組
[編輯]

在Python的執行模型中，程式構造自塊（也稱為程式碼塊）。塊是作為一個單元執行的Python程式文字，模組、函式主體和類別定義都是塊。互動式鍵入的每個命令、指令碼檔案和指令碼命令都是塊。傳遞給內建函式eval()和exec()執行的字串是塊。塊在執行框架（frame）中執行。框架包含一些用於偵錯的管理資訊，並確定在這個塊執行完成後，執行在何處以及如何繼續。

模組是包含Python定義和語句的一個檔案，這個檔案名字是模組名字附加上字尾.py；在一個模組中，模組的名字（作為字串）可獲得為總體變數__name__的值[113]。包（package）是可以包含子模組或遞迴性的子包的模組。包在技術上是具有__path__特性的Python模組。可以將包視為檔案系統上的目錄，而將模組視為這種目錄中的檔案，但是包和模組不必然源自檔案系統[116]。

名字即識別碼，是通用的參照持有者，它不關聯於一個固定的資料類型，但是，一個名字在給定時間，總是被繫結到有一個類型的某個對象上，這就是動態型別的特徵。名字的儲存位置不「包含」所指示的值，一個共同的值可以賦值給多個名字，一個名字在任何時候，都可以重新繫結到各種不同類型的對象上，包括字串、過程、具有資料和方法的複雜對象等。

如果一個名字繫結在一個塊中，它是這個塊的局部變數，除非被聲明為nonlocal或global。如果一個名字繫結在模組層次，它是總體變數。模組對應的塊的變數，既是局部的也是全域的。如果一個變數使用在一個塊中，卻不定義在這裡，它是自由變數[117]。[k]

在Python中，賦值所進行的操作，是將一個名字繫結為到一個分立的動態分配的對象的一個參照。[l]
範疇定義一個名字在一個塊中的可見性。如果一個局部變數被定義在一個塊中，它的範疇包括這個塊。如果這個定義出現在一個函式塊中，範疇擴充到在所界定範疇內包含的任何塊，除非所包含的塊為這個名字介入了不同的繫結。對一個塊可見的所有這種範疇的集合，叫做這個這個塊的「環境」[117]。[m]

當一個名字在一個塊之中使用，它採用最近包圍範疇來解析。如果一個名字繫結在一個塊中，並且在其中於繫結之前就被使用，會導致一個錯誤。[n]當一個函式或類的定義被巢狀到其他函式的定義之內，它的非局部範疇就是這個包圍函式的局部範疇。nonlocal語句導致其列出的識別碼，提及在非局部範疇內先前繫結的名字（即非局部變數（英語：Non-local variable））[117]。[o]

命名空間是儲存變數的地方，它被實作為字典。有局部命名空間、全域空間即包含這個塊對應的模組的命名空間，和內建命名空間即模組builtins的命名空間；對象的方法是定義在類主體內的函式，它有著巢狀的命名空間。命名空間通過防止命名衝突而支援了模組性，還通過明晰了哪個模組實作了哪個函式而增進可讀性和可維護性。

如果global語句出現在一個塊之中，在這個語句中指定的所有名字，提及在頂層命名空間中這些名字的繫結。名字在頂層命名空間解析，首先尋找全域命名空間，未果尋找內建命名空間。global語句與在同一個塊中的名字繫結運算有同樣的範疇。如果一個自由變數的最近包圍範疇包含針對它的global語句，這個自由變數被當作全域的[117]。[p]

表達式
[編輯]

Python的表達式（英語：Expression (computer science)）主要包括如下：

在Python中，表達式的最基本元素被稱為原子，最簡單的原子是文字（英語：Literal (computer programming)）或識別碼。函式呼叫和特性參照，被歸類為表示語言中最緊密運算繫結的初等項（primary）。由逗號,分隔的一系列表達式，叫做表達式列表。

在Python中，加圓括號（parenthesized）形式被歸類為原子，它是包圍在圓括號中的可選的表達式列表。加圓括號的表達式列表產生的東西，就是這個表達式列表所產生的：如果這個列表包含至少一個逗號，例如(a,b,c)，則它產生一個元組；否則它產生的就是這個單一表達式，例如(a)產生a[120]。要表示僅有單個元素的元組，需要給這個元素字尾一個逗號，例如(a,)。空的圓括號產生空元組對象。元組不是圓括號形成的，而是使用逗號形成的，在沒有歧義的情況下，元組的圓括號是可選的。

Python提供了稱為展示（display）的特殊語法來構造列表、字典或集合（英語：Set (abstract data type)），展示被歸類為原子，並且有兩種方式：要麼其所包容的元素是顯式的列舉出來的，要麼它們是通過叫做「推導式」的特定迴圈和過濾指令運算出來的。列表展示，是包圍在方括號中的可以為空的一系列表達式，例如[a,b,c]。字典展示，是包圍在花括號中的可能為空的一系列的用冒號:分隔的鍵-值對。集合（英語：Set (abstract data type)）展示，是包圍在花括號中的一系列表達式[121]。[q]

Python支援列表推導式和更一般性的生成器表達式[122]，Python 3.0增補了字典推導式和集合推導式。[r]自從版本3.5，介入了在表達式列表中的「可迭代解包」*，和在字典展示中的「字典解包」**[123]。[s]

Python對容器類實例，比如序列類型的列表、元組或字串，支援被歸類為初等項的下標和分片（英語：array slicing）。下標的形式為a[索引]，這裡的索引是基於零的，負數是相對於結尾的。分片的形式為a[开始:停止]或a[开始:停止:步长]，這裡的範圍起自開始索引，直至但不包括停止索引；分片的第三個步長參數，允許元素被跳過和用負數指示反向；分片索引可以省略。分片的每個元素都是淺層複製（英語：Object copying）的。[t]

在Python中，算術運算的加法+、減法-、乘法*，與C語言和java相同的。除法和模除%的行為有所不同，在Python中有兩種除法：除法/和下取整除法//。Python增加了指數算符**。自從版本3.5，介入了矩陣乘法算符@[124]，它已經用於了NumPy庫[125]。中綴算符+、-，還可以分別表示取原數和取相反數的一元算符。

在Python中，有如下只適用於整數的位元運算：逐位與&、逐位或|、逐位非~、逐位互斥或^、右移>>、左移<<。

在Python中，有針對對象的值的如下比較運算：大於>、小於<、大於等於 >=、小於等於<=、等於==、不等於!=。Python有針對對象的同一性測試算符：is和is not，還有針對容器類實例的成員關係測試算符：in和not in。Python允許由比較運算連結起來的布林表達式[126]，比如a < b < c，它測試a < b and b < c；C語言將它解析為(a < b) < c[127]。

Python使用and、or、not表示邏輯運算的與、或、非，不採用C語言和Java中所用的符號&&、||、!。

Python的條件表達式表示為x if c else y。意思是當c為真時，表達式的值為x，否則表達式的值為y。

Python的lambda表達式是匿名函式，其函式體只能是一個表達式。[u]

自從版本3.8，介入了記號為:=的賦值表達式[129][130]。它將一個表達式賦值給一個識別碼，同時還返回這個表達式的值。[v]

Python中運算子具有優先級，下表中的運算子按照從最高（最先繫結）到最低（最後繫結）的次序列出。在相同儲存格中運算子具有相同的優先級，它們從左至右結合，除了指數表達式和條件表達式從右至左結合之外[132]：

運算子
描述

(表达式 …)，[表达式 …]，{键: 值 …}，{表达式 …}
繫結或加圓括號表達式，列表展示，字典展示，集合展示

x[索引]，x[索引:索引]，x(参数 …)，x.特性
下標，分片，呼叫，特性參照

await x
await表達式

**
指數

+x，-x，~x
取原數，相反數，逐位非

*，@，/，//，%
乘法，矩陣乘法，除法，下取整除法，餘數

+，-
加法和減法

<<，>>
移位

&
逐位與

^
逐位互斥或

|
逐位或

in，not in，is，is not，<，<=，>，>=，!=，==
包含成員關係測試，同一測試，各種比較

not x
布林非

and
布林與

or
布林或

… if … else …
條件表達式

lambda …: …
lambda表達式

:=
賦值表達式

Python為序列提供了串接算符+和倍增算符*[133]。自從版本3.9，介入了字典合併算符|和字典更新算符|=[134]。

Python為集合（英語：Set (abstract data type)）提供了集合論運算：併集|、交集&、相對補集-、對稱差^，和子集測試<=、真子集測試<、超集測試>=、真超集測試>。

在Python中，語句不能成為表達式的一部份，表達式比如列表推導式和字典推導式以及lambda表達式，都不能包含語句。這能夠避免C語言程式中的一個常見錯誤，即在條件判斷時把等於算符==誤寫為賦值算符=，這不是預期程式碼卻在語法上有效而能通過C語言編譯器檢查，在Python中這會導致一個語法錯誤。

數值運算
[編輯]

Python的二元算術運算，先將兩運算元轉為共同類型，加法、減法、乘法、下取整除法、模除和指數運算的結果也採用此類型，舉下取整除法//例子：5//2 == 2而5.0//2 == 2.0。自從Python 3.0，除法/總是產生浮點數結果，例如5/2 == 2.5。

下取整除法//的修約是朝向負無窮的，這意味著等式(a + n)//n == a//n + 1在n != 0條件下永遠成立；很多其它程式語言比如C99，其整數除法採用截尾取整規則，不能保證這個等式永遠成立。Python提供了round()內建函式，用於把一個浮點數修約成最近的整數[135]，自從Python 3.0，為了打破平局它採用了IEEE 754的約半成偶規則，例如round(1.5) == 2 == round(2.5)。

Python的模除%運算結果餘數的定義，需要確使等式a == (a//n)*n + a%n在n != 0條件下永遠成立[136]；由於//採用下取整規則，%所得餘數的符號同於除數，例如-5%2 == 1而5%-2 == -1。數學中的歐幾里得除法，其餘數總是非負數。很多其它語言的整數除法採用截尾取整規則，其模除所得餘數的符號同於被除數。

Python對所有整數運算，使用任意精度算術。在decimal模組中的Decimal類[137]，提供十進制浮點數（英語：Decimal floating point），具有使用者可按需要而更改的預設28個十進制有效數位精度，並有多種修約方式[138]。在fractions模組中的Fraction類，提供任意精度的有理數[139]。第三方庫gmpy2[140]，提供了到任意精度計算庫GMP/MPIR（英語：MPIR (mathematics software)）、MPFR（英語：GNU MPFR）和MPC的介面。

除了求絕對值函式abs()列入內建函式之外，大多數數學函式，處於math和cmath模組內。前者用於實數運算，而後者用於複數運算。Python有著廣泛的數學庫，特別是第三方庫NumPy進一步擴充了原生能力。

字串操作
[編輯]

Python的文字序列類型，包括字串str和位元組序列bytes與bytearray。文字序列的文字有多種寫法：

短字串文字（英語：string literal），由單引號'或雙引號"界定。不同於Unix shell、Perl和受Perl影響的語言，單引號和雙引號功能相同。這二種字串都使用反斜槓\作為跳脫字元。

長字串文字，是開始並結束於三個單引號'''或三個雙引號"""的序列。它們可以跨越多行，其功能就像shell、Perl和Ruby中的here文件。

位元組文字（英語：Literal (computer programming)）總是字首上一個b或B，它產生bytes類型的實例。它們只可以包含ASCII字元，其數值大於等於128的位元組必須通過跳脫來表達。

字串文字或位元組文字都可選的能字首上一個r或R，這叫做原始字串（英語：String literal#Raw strings）。跳脫序列不被直譯，因此在文字反斜槓常見的地方很有用，比如正規表示式和Windows風格的路徑。

Python允許多個毗鄰的字串文字或位元組文字（它們以空白分界並可以使用不同的引述約定），在編譯時間於語法層面上串接起來。要在執行時間串接字串，必須使用序列串接算符+[141]。

自從Python 3.0，字串類str提供了格式化（英語：Content format）方法format()[142]，例如"spam={0} eggs={1:04d}".format("blah", 2)，它求值為'spam=blah eggs=0002'。格式化方法被推薦用來替代早先的字串對象內建格式化算符%，它在功能上類同於C語言中的printf格式化字串[143]，例如"spam=%s eggs=%04d" % ("blah", 2)。

自從版本3.6，介入了字串插值（英語：String interpolation）[144]，即「格式化字串文字」或稱為「f字串」，它向字串文字字首上f或F[145]，例如x="blah"; y=2; f'spam={x} eggs={y:04d}'。

類型
[編輯]
Python 3的標準類型層級[146]

Python使用鴨子型別，並擁有有類型的對象，和無類型的變數名字。在編譯期不檢查類型約束，而寧願在一個對象上的操作出現可能的失敗，表現出這個給定對象不具有適合的類型。儘管是動態型別系統，Python卻是強型別的，禁止沒有明確定義的操作，比如將一個數和一個字串相加，而不是默默的去嘗試轉換使其有意義。

Python有著範圍廣泛的基本資料類型。同時具備常規的整數和浮點算術，它透明的支援任意精度算術、複數和十進制浮點數（英語：Decimal floating point）。Python支援種類繁多的字串操作。在Python中，字串是不可變的，所以在其他程式語言中可能就地改變字串的字串操作，比如字元替換，在Python中返回新的字串。

Python有一個非常有用特徵，就是搜集（或稱容器）類型的概念。一般的說，搜集是以一種易於參照或索引的方式，包含其他對象的對象。Python的搜集類型包括了序列、對映和集合，Python提供了廣泛的搜集操縱能力，比如內建包含檢查和通用迭代器協定。

列表（動態陣列）、元組和字串是序列類型。所有序列類型都有位置索引，並且除了字串，都可以包含任意類型的對象，在同一個序列中可以包括多種類型的對象。字串和元組是不可變的，使得它們成為字典的鍵的完美候選者。列表是可變的，元素可以被插入、刪除、修改、添加或就地排序。

字典是無次序的對映類型，它將一組不可變的鍵，對映到相應的元素上。在字典中的鍵，必須是不可變的Python類型，比如整數或字串，因為在底層它們是通過雜湊函式實作的。集合（英語：Set (abstract data type)）是無次序的類型，它包含唯一性的不可變對象作為元素。有二種類型的集合：可變的set和不可變的frozenset。

Python允許程式者使用類，定義自己的類型[51]。類的新實例，是通過呼叫這個類的構造器而建立的，而類型和類都是元類type的實例，元類type更是其自身的實例，這允許了元程式設計和反射。Python支援對類型和類的廣泛內省，它們可以被讀取和比較。[w]

Python支援漸進類型（英語：gradual typing）[5]，自從版本3.5[147]，在語法上逐漸允許建立靜態型別系統[148]。預設官方實作CPython不檢查靜態型別，可選的靜態型別檢查器mypy，支援編譯期型別檢查[149]。

Python 3內建類型舉要

類型

可變性

描述

語法例子

bool

不可變

布林值，有表示值False和True的兩個對象。作為整數類型的子類型，除了在轉換成字串時轉換為"False"和"True"之外，它們在幾乎所有上下文中表現得如同0和1。

True

False

int

不可變

整數，其大小在理論上無限制，實際上受限於主記憶體[150]。

42

float

不可變

雙精度浮點數，確切精度依賴於機器。一般實作為IEEE 754標準binary64浮點數，它有53個二進制有效數位精度[151]。

1.414

complex

不可變

複數，即分別表示實部與虛部的兩個雙精度浮點數的有序對。

3+2.7j

range

不可變

數的序列，通常用在for迴圈中指定迴圈次數[152]。

range(1, 10)

range(10, -5, -2)

str

不可變

字串，即Unicode程式碼點序列[153]。其程式碼點都在區間[\u0000, \uffff]或[\U00010000, \U0010ffff]之內。

'Wiki' "pedia"

"""Spanning
multiple lines"""

bytes

不可變

位元組序列，其專案是8位元位元組，可以用區間[0x00, 0xff]的整數表示。

b'Wiki' b"pedia"

bytes([0x68, 0x65, 0x78])

bytearray

可變

bytearray(b'Wiki' b"pedia")

bytearray([0x68, 0x65, 0x78])

list

可變

列表，可以包含任意的Python對象。

[4.0, 'string', True]

[]

tuple

不可變

元組，可以包含任意的Python對象。

(4.0, 'string', True)

()

dict

可變

字典是鍵-值對的搜集。鍵在其生存期間是不可變的（稱其為可雜湊的），列表、字典或其它可變對象和包含它們的對象不可以用作鍵。

{'key1': 1.0, 3: False}

{}

set

可變

無序的集合（英語：Set (abstract data type)），包含唯一性的不可變的對象，它們不能用任何下標來索引。

{4.0, 'string', True}

set()

frozenset

不可變

frozenset([4.0, 'string', True])

types.EllipsisType

不可變

這個類型的值是有一個單一對象，它表示為文字（英語：Literal (computer programming)）...或內建名字Ellipsis，它的真值為真。它用於NumPy多維陣列索引[154]。

...

Ellipsis

types.NoneType

不可變

這個類型的值是一個單一對象None（相當於其他語言的Null）[155]，它被用來指示值的缺席，它的真值為假。

None

types.NotImplementedType

不可變

這個類型的值是一個單一對象NotImplemented，數值方法和豐富比較方法如果沒有實作在所提供運算元上的這個運算則應當返回這個值，它不應該在布林值上下文中求值。

NotImplemented

除了各種資料類型，Python直譯器還內建了很多其他類型，包括可呼叫類型：使用者定義函式、實例方法、生成器函式、協程函式、非同步生成器函式、內建函式、內建方法、類、類別方法；模組，客製化類，類別實例，I/O對象（也叫做檔案對象），和暴露給使用者的一些內部類型：程式碼對象、框架對象、溯回對象、切片對象、靜態方法對象、類別方法對象。

函式
[編輯]

Python中的使用者定義函式是其內建的函式類型的實例，函式的遞迴呼叫被限制了最大深度[x]。
Python不支援函式多載即不能建立具有相同名字而有不同實作的多個函式，但自從版本3.4，其標準庫可支援單一分派泛化函式[156]。Python中的函式支援閉包[157]和其他頭等函式特徵[y]。Python官方實作不提供尾呼叫最佳化或頭等續體，吉多·范羅蘇姆曾聲稱他不會對其加以支援[158]，有第三方函數式程式設計庫支援彈跳床（英語：Trampoline (computing)）[159]。

Python的修飾器（decorator）可用來修改任何可呼叫對象，其用法是將已定義的對象比如函式、方法或類別定義傳遞給修飾器，再將它所返回的修改後的對象繫結到原來對象的名字。Python使用@作為關鍵字形成修飾詞，它是用來應用修飾器的語法糖。[z]
通過在毗連的行上放置多個修飾詞，多個修飾器可以連結起來應用。[aa]
修飾器可用於元程式設計例如：設定先決條件和後置條件，還可以用來實作記憶化和可作為主程式設計範式的多分派[160]。

在Python中，函式呼叫的實際參數與函式定義的形式參數之間的結合，所傳遞的是「對象參照」，函式在被呼叫之時，所給予的實際參數被介入到一個局部符號表中，實際參數使用傳值呼叫來傳遞，而這個值總是對象參照，並非這個對象的值[161]。如果形式參數繫結到一個可變對象，則通過形式參數對此對象內容的修改，在函式外也是可見的。如果形式參數繫結到一個不可變對象，則通過形式參數不能修改此對象內容，但可以把形式參數重新繫結到其它對象上，這並不影響函式外的對象的值。[ab]

Python在函式定義時，可以在形式參數序列中，以形式参数=值的樣式指定形式參數預設值。在函式呼叫時可以省略有預設值的形式參數，這時這個預設值就被代入到它的位置中。在這個函式定義被執行之時，從左至右的求值作為形式參數的預設值的這些表達式。這意味著這種表達式在這個函式被定義之後只被求值一次，而每次函式呼叫之時都使用相同的「預先計算」的值。[ac]

Python在函式呼叫中，可以給予位置實際參數和關鍵字實際參數。實際參數可以如同C語言那樣，按照位置與函式定義的形式參數匹配；也可以採用關鍵字實際參數，即形式参数=值樣式的實際參數。Python在函式定義中，可以使用不對應實際參數的特殊形式參數/和*，將形式參數序列分為三部份：唯位置形式參數、可位置可關鍵字形式參數和唯關鍵字形式參數。如果一個形式參數有預設值，則在其後直到*之前的所有形式參數也都必須有預設值。[ad]

在函式定義中的位置形式參數序列和關鍵字形式參數序列，可以分別在其末尾有*args或**kwargs這樣的加了字首*或**的形式參數，它們擷取在函式呼叫時提供的，超出形式參數序列規定而無所對應的多個實際參數；在形式參數args前加*號，則args是元組類型，它擷取可變數目的位置實際參數；在形式參數kwargs前加**號，則kwargs是字典類型，它擷取可變數目的關鍵字實際參數。[ae]

在函式呼叫的實際參數序列中，關鍵字實際參數必須出現在位置實際參數之後。如果要傳遞給一個函式的一些位置實際參數，已經在一個序列類型如列表或元組的對象中，則可以在函式呼叫中給它字首*來進行可迭代解包；如果要傳遞的一些關鍵字實際參數已經在字典對象中，則可以給它加**號來進行字典解包。

在函式定義頭部之後可以插入「文件字串」，用作函式的使用幫助，它可以使用內建函式help()列印出來。自從Python 3.0，函式定義可以對形式參數與返回值增加類型標註[162]。自從版本3.5，開始支援類型提示[147]。

對象
[編輯]

在Python中所有東西都是對象，包括數、函式、類和模組，其標準庫支援對對象的弱參照[163]。Python允許多型性，採用了鴨子型別方式[3]，就是說針對變數的方法呼叫和特性（attribute）訪問，不事先限制這個的變數的類型，它可被繫結到任何對象。Python的類繼承支援多重繼承，這可以用來實作混入。Python支援元類[164]，還支援抽象基礎類別[165]，自從版本3.6，提供了客製化化類建立的簡單機制[166]。

對象的方法，是附屬於這個對象的類的函式。對於正常的方法和函式，語法实例.方法(实际参数)，是类.方法(实例, 实际参数)的語法糖。Python不提供其他一些物件導向程式設計語言比如C++和Java中的隱式的this（英語：this (computer programming)）關鍵字[167]，Python的對象方法沿襲自Modula-3，使用顯式的第一個形式參數來訪問實例特性，習慣上將其命名為self（英語：this (computer programming)）。[af]

Python不提供隱式的super關鍵字而是提供了super()內建函式，在一個類的方法中呼叫此函式返回一個代理（proxy）對象，它為了在類層級內這個類所有基礎類別中尋找實作了特定方法的基礎類別，確定了優先次序即方法決定次序（MRO），次序居前的基礎類別優先於位居其後的它的父輩類或平輩類[168]。當一個子類的方法覆蓋了其超類方法的時候，可通過呼叫super().方法，將這個方法呼叫委託給與子類的self.方法同名的超類別方法。[ag]

Python使用名字修飾，有限的支援私有變數[102]。自從版本3.6，Python介入了變數標註語法[169]。Python支援一些名字以__開始和結束的特殊方法，它們用於實作實作多種特殊功能[76]，某些特殊方法可以實作運算子多載，比如定義了__add__()，將會允許在這個類別的實例上使用+算符。

在Python中，最常用的特殊方法是實例初始化方法__init__()，它在實例建立之後返回給呼叫者之前被呼叫，給它的實際參數就是傳遞給對象構造器表達式的那些實際參數。自從版本3.7，Python標準庫提供了@dataclass修飾詞，用來向使用者定義類自動增加特殊方法比如__init__()和__repr__()[170]。

在Python中，不強制採用訪問子與變異子方法，來訪問對象的資料成員。對象的特殊特性__dict__，是儲存其所有（可寫）特性的字典[171]。在一個類中的類別變數__slots__，可以被賦值為變數名字序列，它為所聲明的這些變數在類別實例對象中保留空間，並阻止其自動建立__dict__[172]。[ah]

在Python中，定義了一個或多個特殊方法__get__()、__set__()、__delete__()的類，可以用作描述器（descriptor）[173]。Python使用@classmethod和@staticmethod修飾詞，來分別建立類別方法和靜態方法[55]。在方法呼叫之時，類別方法接收這個類的作為其隱式的第一個實際參數，而靜態方法不接收隱式的第一個實際參數。[ai]

在類的定義中，如果一個成員若是另一個描述器類別的實例，則它被稱為這個類的屬性（property），使用與特性（attribute）訪問相同的語法，訪問這個類別的實例對象中的屬性。[aj]
Python使用@property修飾詞或property內建函式，將一個類中特殊定義的訪問某個特性的那些方法，包裝成的這個類的一個屬性[174]。[ak]

標準庫
[編輯]

Python擁有一個強大的標準庫[175]。Python標準庫包括了如下功能：

內建函式

內建常數

內建類型

內建例外

執行緒安全保證

Python執行時服務

客製化Python直譯器

匯入模組

Python語言服務

文字處理（英語：Text processing）服務

二進制資料（英語：Binary data）服務

資料類型

數值和數學模組

函數式程式設計模組

檔案和目錄訪問

資料持久化

資料壓縮和存檔

檔案格式

加密服務

通用作業系統服務

MS Windows專有服務

Unix專有服務

命令列介面庫

並行執行

網路和行程間通訊

網際網路資料處理

結構式（英語：Structured document）標記處理工具

網際網路協定及其支援

多媒體服務

國際化

Tk圖形化使用者介面

開發工具

偵錯和分析

軟體打包和釋出（英語：Software distribution）

程式碼實例
[編輯]

一個在標準輸出裝置上輸出Hello World的簡單程式通常被作為開始學習程式語言時的第一個程式。可將如下程式碼錄入純文字檔案並命名（如program01.py），然後執行這個命令python3 program01.py以執行該程式：

print("Hello, world!")

Python也可以單步直譯執行。執行Python直譯器進入互動式命令列的環境後，你可以在提示符號>>>旁輸入print("Hello, world!")，按Enter鍵輸出結果：

>>> print('Hello, world!')
Hello, world!

計算非負整數的階乘的程式碼：

n = int(input('輸入一個數，就會印出其階乘: '))
if n < 0:
raise ValueError('錯誤，請輸入一個非負整數')
fact = 1
for i in range(2, n + 1):
fact *= i
print(fact)

注意：在Python 3.0及以上版本中，print是個函式，需要在要列印的參數前後加上圓括號；在Python 2.x版本中，print是一個關鍵字而可以不加圓括號。

實作
[編輯]

Python是一門跨平台的手稿語言，Python規定了一個Python語法規則，根據該規則可編寫Python直譯器[176]。Python屬於動態語言，其官方實作CPython將Python程式編譯成中間形式的位元組碼[177]，並接著在它的虛擬機器上執行[178]，執行速度緩慢於C/C++所編譯出的機器碼和在HotSpot JVM上執行的java位元組碼[179]。

活躍開發的實作

CPython：官方的Python直譯器，需要區別於其他直譯器的時候才以CPython稱呼。CPython預設採用全域直譯器鎖（GIL），以確保在任何時刻只有一個執行緒執行Python位元組碼；一些擴充模組被設計為在進行計算密集任務時釋放GIL，還有在進行I/O時總是釋放GIL[180]。

MicroPython：為微控制器而最佳化的Python 3變體，它實作了完整的Python 3.4語法，和補充自版本3.5的async/await關鍵字，以及後來版本的一些選定特徵；它提供了實作Python標準庫模組功能子集的內建模組，和特定於微控制器的一些模組。CircuitPython（英語：CircuitPython）是Adafruit（英語：Adafruit Industries）開發的MicroPython分叉。

Codon：高效能且無執行時開銷的Python編譯器[181]，它將Python程式碼編譯成本機機器碼，並且支援本機多執行緒和GPU並列運算，還包括了特徵齊全的完全編譯的內建NumPy實作。它由MIT CSAIL的研究人員開發[182]，其語意在資料類型等方面上與CPython有所不同[183]。

PyPy：採用了跟蹤JIT（英語：Tracing just-in-time compilation）的Python實作，支援應用層無棧特徵[184]，它是用RPython編寫的，當前支援Python版本3.11和2.7。

Numba：使用LLVM JIT的Python最佳化編譯器，它將包括很多NumPy函式的聚焦數值計算的Python子集，轉譯成快速的機器碼，它為在CPU和GPU上並列化Python程式碼提供了大量選項。

Pyodide：基於WebAssembly/Emscripten的用於瀏覽器和Node.js的Python釋出[185]，源出自Mozilla，支援任何在PyPI上wheel形式的純Python包，並且已經移植了很多具有C、C++和Rust擴充的包，它具有健壯的JavaScript與Python雙向外界函式介面（英語：Foreign function interface），還可通過wgpy利用上WebGPU/WebGL加速[186]。

RustPython：用Rust編寫的Python直譯器[187]，它可以嵌入到Rust應用程式中從而將Python用作手稿語言，還可以被編譯成WebAssembly從而在瀏覽器中執行Python程式碼。

Brython：用JavaScript編寫的在瀏覽器中執行的Python實作[188]，支援用Python書寫的模組但排除瀏覽器上下文所不容許的特徵，具有函式庫用以互動於DOM元素與事件和現存JavaScript庫。

GraalPy：針對JVM的基於GraalVM（英語：GraalVM）的Python高效能實作[189]。

第三方工具pyenv可以在多個Python版本間輕易切換[190]。

轉譯成其他語言的編譯器

Cython：將增加了靜態型別聲明的Python超集編譯成C或C++的編譯器。Cython補充支援呼叫C語言函式並且在變數和類特性上聲明C語言類型，還支援以OpenMP為後端的本機多執行緒並列[191]。

mypyc：作為mypy發行的可選依賴[149]，它是將Python模組編譯成C擴充的編譯器[192]，它使用標準的Python類型提示生成快速程式碼，並使用mypy進行型別檢查和類型推論。

Nuitka（英語：Nuitka）：用Python編寫的到C11或替補為C++03的編譯器[193]，它將Python模組轉譯成使用CPython的libpython共享庫和自己的靜態C檔案的C層級程式，接著將其編譯成本機機器碼。

Shed Skin（英語：Shed Skin）：將純粹但隱含為靜態型別的Python有限子集程式碼轉譯成最佳化的C++程式碼的編譯器[194]，它依賴於貝姆垃圾收集器，可以生成獨立程式或者能匯入其他Python程式的擴充模組。

Pythran：將聚焦於科學計算的Python子集編譯成C++17的提前編譯器（英語：Ahead-of-time compilation）[195]，它依賴於Boost和xsimd庫，將標註了介面描述的Python模組編譯為本機共享庫模組，能利用上多核和SIMD指令單元。

py2many：將Python轉譯成多種語言如C++17、Rust、Go和Julia等的轉譯器[196]。

其他實作舉例：Jython，它是用Java實作的Python 2.7。IronPython，它是基於DLR之上的Python 2.7和Python 3.4實作。Grumpy，它是Python 2.7到Go的轉譯器和執行時系統[197]。Stackless Python，它是實作微執行緒（英語：microthread）的CPython 3.8分叉。Pyston，它是具有JIT等效能最佳化的CPython 3.8.12的分叉[198]。Transcrypt，用Python編寫的Python 3.9到JavaScript編譯器[199]。Pyjion，將Python程式碼編譯成本機CIL的CPython 3.10的JIT擴充[200]。CinderX，它是Meta孵化器釋出的增進Python執行時效能的擴充[201]。MyHDL（英語：MyHDL），將Python編譯成Verilog或VHDL[202]。

開發環境
[編輯]

通用文字編輯器
[編輯]

很多並非整合式開發環境軟體的文字編輯器，也對Python有不同程度的支援，並且加上專門為Python設計的編輯器外掛程式也會有很高的可用性。

VS Code

Atom

Eclipse

emacs

SlickEdit

TextMate

Vim

Sublime Text

EditPlus

UltraEdit

PSPad

Notepad++

專用開發環境
[編輯]

適用於Python的整合式開發環境（IDE）軟體，除了標準二進制釋出包所附的IDLE之外，還有許多其他選擇。其中有些軟體設計有語法著色、語法檢查、執行偵錯、自動補全、智慧型感知等便利功能。由於Python的跨平台出身，這些軟體往往也具備各種作業系統的版本或一定的移植性。

IDLE：Python「標準」IDE，一般隨Python而安裝，支援較少的編輯功能，偵錯功能也比較弱。

Eric：基於PyQt的自由的IDE，支援自動補全、智慧型感知、自動語法檢查、工程管理、svn/mercurial整合、自動單元測試等功能，具有可延伸的外掛程式系統，通過可選外掛程式支援Git整合。偵錯功能與Visual Studio和Eclipse類似。

Spyder：開源的跨平台科學計算IDE。

PyCharm：由JetBrains公司出品，具備一般IDE的功能，比如偵錯、語法突顯、Project管理、程式碼跳轉、智慧型提示、自動完成、單元測試、版本控制等等，另外，它還提供了一些功能用於Django開發，還支援IronPython。它是商業軟體，但也具有社群版和教育版。

第三方擴充包
[編輯]
主條目：Python軟體列表（英語：List of Python software）

Python社群提供了大量的功能覆蓋眾多領域的第三方模組，其使用方式與標準庫類似。第三方模組可以使用Python/Cython或者C語言編寫。軟體工具比如SWIG，通過定義介面檔案或規定檔案的方式，可以將C/C++編寫的程式庫包裝為Python模組。Python直譯器本身也可以被整合到其它需要手稿語言的程式內。

Python包索引是公開的軟體套件線上倉庫。pip是官網推薦的以安全方式安裝Python應用及其依賴軟體套件的工具[203]。要安裝在整個作業系統範圍內共享的Python包，現在需要通過作業系統的軟體套件管理系統。為了將特定於應用的依賴包隔離於共享的Python安裝，需要建立虛擬環境，這可以使用標準庫的venv[204]，或第三方工具比如virtualenv[205]和pipenv[206]。uv是用Rust編寫的極快的Python軟體套件和專案管理器[207]。

網路應用
[編輯]

Python標準庫對於各種網路協定的支援很完善，因此適用於編寫伺服器軟體、網路爬蟲等Web開發。Python定義了Web伺服器閘道器介面（WSGI）和非同步伺服器閘道器介面（英語：Asynchronous Server Gateway Interface）（ASGI），來協調HTTP伺服器與基於Python的Web程式之間的溝通。

用Python編寫的一些Web框架，有助於輕鬆地開發和管理複雜的Web程式。重要的第三方網路程式（英語：Computer network programming）庫和Web框架有：

Zope：著名的開源Web應用伺服器。

Beautiful Soup：用作HTML/XML解析器的一個簡單易用Python包。

Twisted：事件驅動的網路程式框架，它支援很多常見的網路協定並包括了很多不同用途的模組，它支援所有主要的系統事件迴圈和各種GUI事件迴圈。

Django：MTV架構[208]的Web框架，它注重組件的重用性和「可插拔性」、快速開發和DRY法則。

Tornado：使用單執行緒事件迴圈的非同步非阻塞式web伺服器，也是輕量級的Web框架。

Flask：微Web框架，不要求特定的工具或庫。

Requests：適合於常人使用的HTTP庫，封裝了許多繁瑣的HTTP功能，極大地簡化了HTTP請求所需要的程式碼量。

aiohttp：基於asyncio的HTTP客戶端和伺服器二者[209]。

uvloop：對內建asyncio事件迴圈的快速的、直截了當的替代者[210]，它用Cython實作並在底層使用了libuv。

FastAPI：基於ASGI（英語：Asynchronous Server Gateway Interface）的用於建造服務API的Web框架，它自動生成OpenAPI文件並可以支援WebSocket。

圖形化使用者介面
[編輯]

Python本身包含了Tkinter庫，它是Python的業界標準GUI並被整合進入了IDLE。Tkinter基於了Tcl命令工具，能夠支援簡單的GUI開發。但是為了讓所開發的軟體執行速度更快，並與使用者的桌面環境更契合，人們一般會選擇採用第三方GUI庫或框架。主要的第三方GUI庫有：

PyQt：Qt的Python繫結庫，由Riverbank Computing公司自從1998年發行，採用GPL授權條款或商業授權條款。

PySide：Qt的Python繫結庫，由Qt公司自從2009年發行，採用LGPL授權條款。

PyGObject：替代了PyGTK，它是為Python程式訪問基於GObject的庫而提供的包裝庫[211]，GObject是GTK、GIO（英語：GIO (software)）和GStreamer等庫使用的對象系統。

Kivy：用於開發多點觸控應用軟體的開源Python庫，採用了自然使用者介面（NUI）。

WxPython：GUI程式框架wxWidgets的Python包裝庫。

Dear PyGui：快速而強力的具有極小依賴性的GUI工具箱[212]。

pywebview：輕量級跨平台的對WebView構件的包裝器[213]，允許在其本地GUI窗口中顯示HTML內容。

資料科學
[編輯]

重要的資料科學用第三方軟體庫有：

NumPy：Python的基礎性的科學計算軟體庫，它提供了強力的多維陣列對象，廣播式陣列運算[214]，整合C/C++和Fortran程式碼的工具，較為有用的線性代數、傅立葉變換和亂數功能。

SciPy：用於數學、科學和工程的Python軟體庫，它以NumPy的多維陣列作為基本資料結構，所包含的模組針對了：統計、最佳化、數值積分、常微分方程求解、插值、線性代數、傅立葉變換、訊號處理、圖像處理等。

CuPy（英語：CuPy）：NumPy/SciPy相容的GPU加速的陣列庫[215]，它可在NVIDIA CUDA或AMD ROCm平台上充當其直截了當的替代者，來執行現存的NumPy/SciPy程式碼。

NumKong：採用SIMD加速的距離、點積、矩陣、地理空間與幾何運算的核心庫的Python繫結[216]，它跨越指令集架構並支援多種數值類型。

Autograd：針對原生Python和NumPy程式碼的自動微分庫[217]，它可以處理較大子集的Python特徵，包括迴圈、條件、遞迴和閉包，甚至可以求取高階導數。

matplotlib：基於NumPy的綜合性繪圖（英語：Plot (graphics)）庫，用於建立靜態的、動畫的和互動式的資料視覺化。地圖繪製庫Cartopy提供了介面使得可以使用matplotlib來建立地圖[218]。

pandas：用於資料分析和資料操縱的軟體庫，它在NumPy基礎上，提供了加標籤資料結構「資料訊框」[219]，和統計函式等。它的預設繪圖後端是matplotlib，還可以擴充上第三方繪圖（英語：Plot (graphics)）後端[220]。

Modin：直截了當替代pandas並將其工作流程縮放至Ray、Dask（英語：Dask (software)）或通過Unidist縮放至MPI[221]。

資料視覺化
[編輯]

主要的資料視覺化軟體庫及儀錶板框架有[222]：

VisPy：高效能互動式2D/3D資料視覺化庫[223]，它通過OpenGL庫利用GPU的計算能力來顯示非常大的資料集。

Datoviz：通過Vulkan庫利用GPU的用於資料視覺化的高效能渲染庫[224]。

seaborn：基於matplotlib的資料視覺化庫[225]，它提供了繪製統計圖形的高層介面。

Vega-Altair：基於Vega-Lite JSON規定設計的聲明式統計視覺化庫[226]。

Bokeh：針對現代Web瀏覽器的互動式資料視覺化庫[227]，它在大型或串流（英語：Streaming data）的資料集上提供高效的互動性。

plotly：互動式開源的基於瀏覽器的圖形繪製庫[228]，它是基於plotly.js實作的聲明式圖表庫。

Dash：資料應用和儀錶板框架，它可將現代使用者介面元素如下拉選單、滑動條（英語：Slider (computing)）和圖形，直接連結至分析型Python程式碼[229]，它由Plotly（英語：Plotly）公司出品，基於了React、Flask和plotly.js[230]。

Panel：資料探索（英語：Data exploration）和Web應用框架，它能無縫的整合於PyData生態系統，提供互動式資料表格和視覺化等功能[231]，它可用在Pyodide之中[232]。Panel是HoloViz生態系統的成員[233]，這個工具組還包括了：hvPlot、HoloViews、GeoViews、Datashader、Lumen、Param和Colorcet。

Streamlit：迅速將Python指令碼轉變為Web應用的框架[234]，所生成的應用可共享於Streamlit社群雲平台。

Voilà：將Jupyter Notebook轉變為獨立的Web應用的框架[235]。

機器學習
[編輯]

基礎性的機器學習軟體庫及框架有：

scikit-learn：機器學習軟體庫，它提供的功能包括：監督學習中的分類和回歸，無監督學習中的聚類和降維，還有模型選擇和資料預處理（英語：Data Preprocessing）。它基於了NumPy、SciPy、資料訊框庫相容層Narwhals[236]、輕量級管道庫Joblib[237]和執行緒池控制庫threadpoolctl[238]，其繪圖功能依賴於matplotlib，還可用到sklearn-onnx[239]、scikit-image（英語：scikit-image）、seaborn和plotly。

PyMC：基於從Theano分叉出的PyTensor的概率程式庫，它用於建立貝葉斯統計模型，並使用馬爾可夫鏈蒙特卡洛（MCMC）方法進行模型擬合。

TensorFlow：Google開發的「端到端」開源機器學習平台，它提供了Python API[240]，其中實作了Keras API[241]。Keras現在是在TensorFlow 2上建立的深度學習高層API。

PyTorch：Meta在Torch（英語：Torch (machine_learning)）基礎上開發的開源的Python軟體套件，提供了具有強大的GPU加速的張量計算，和建立在基於tape的自動微分系統上的深度神經網路。

JAX：Google開發的開源機器學習框架，其核心是可任意組合的對數值純函式的變換[242]，它可以自動微分原生Python和NumPy函式，並使用加速線性代數庫XLA（英語：Accelerated Linear Algebra）來在GPU和TPU上編譯和執行NumPy程式[243]。

其它種類
[編輯]

Pegen：Python的PEG文法解析器的生成器[244]。

llvmlite：輕量級的LLVM的Python繫結，用於編寫即時編譯器[245]。

xDSL：圍繞靜態單賦值（SSA）中間表示（IR）構建的Python原生的編輯器框架[246]，它的設計受到了MLIR編譯器框架（英語：MLIR (software)）的影響。

wgpu-py：WebGPU本地實作的Python包裝器[247]。Pygfx，是基於wgpu-py的強力且多用途的渲染引擎[248]。fastplotlib，是建立在Pygfx之上的快速繪圖庫[249]。tinygrad，是可以利用wgpu-py作為加速器的深度學習框架[250]。

PyCUDA/PyOpenCL：PyCUDA提供對CUDA API的Python風格訪問[251]，PyOpenCL提供對OpenCL API的Python風格訪問[252]。

Kompute：基於Vulkan的通用計算框架[253]，它是高速的、支援行動裝置、非同步的並且針對進階GPU資料處理用例做了最佳化。

Dask（英語：Dask (software)）：伸縮範圍從筆記型電腦至電腦叢集的平行計算庫[254]，它提供的使用者介面鏡像了PyData生態系統中pandas、scikit-learn和NumPy的API。

Ray：對人工智慧及Python應用的執行規模進行伸縮的統一框架[255]，由Anyscale公司開發。它構成自一個核心的分散式執行時系統，和加速機器學習工作負載的AI軟體庫。

SQLAlchemy：Python的SQL工具包和採用資料對映器模式的對象關係對映器（ORM）。

Graphene：GraphQL框架[256]，支援各種資料來源如SQLAlchemy、Mongo、Django和客製化Python對象等。GQL是GraphQL客戶端Python庫[257]。

Pillow（英語：Python Imaging Library）：基於Python的圖像處理軟體庫[258]，它支援廣泛的圖形檔案格式，分叉於已終止的PIL。

pstutil：檢索執行行程和系統利用資訊的跨平台庫[259]。

Fabric：經由SSH遠端執行shell命令的高層庫[260]，它產生有用的Python對象作為回饋。

fsspec：即Python的檔案系統規定[261]，它是針對Python的資料儲存IO層。

pygame：pygame和它的分叉pygame-ce[262]，是開發電動遊戲的Python軟體庫，基於了SDL軟體庫[263]。

pyglet：Python編寫的物件導向的遊戲和多媒體庫，利用了FFmpeg軟體庫並需要OpenGL 3.3+。

SymPy：支援數學符號運算的軟體庫，用於提供電腦代數系統。

SimPy：基於由Python生成器函式定義的行程的離散事件類比框架[264]。

有些C、C++或Rust軟體庫也提供Python繫結，例如：Nvidia CUDA提供cuda-python[265]，Intel OpenCV提供opencv-python[266]，Polars（英語：Polars (software)）提供Python API[267]。

應用
[編輯]

在很多作業系統裡，Python是標準的系統元件，它被列入了ISO/IEC 23360-1-4:2021 Linux標準規範（LSB）之語言規定[268]。大多數Linux發行版和macOS都整合了Python，可以在終端模擬器或虛擬控制台（英語：Virtual console）下直接執行Python。第三方工具pipx可以將Python應用安裝於隔離的環境中並在其中執行它[269]。

雖然Python可被粗略地分類為手稿語言，Python的支持者較喜歡稱它為一種高階動態語言，常像「膠水」一樣被用來連接軟體組件，已經顯著的區別於Unix shell、Windows PowerShell這樣的語言。基於Python的xonsh，是跨平台的、青睞Unix的shell語言和命令列介面[270]。

應用程式
[編輯]

下面舉例使用Python編寫的一些應用程式：

IPython：以多種程式語言進行互動式計算的命令shell和Jupyter的核心，最初為Python開發，它提供了內省、富媒體、shell語法、tab補全（英語：Command-line completion）和歷史。

Conda：跨平台的、語言無關的二進制包管理器，它被Python的Anaconda發行版採用。

Trac：用於軟體開發專案的改進wiki和缺陷追蹤系統。

Ansible：開源的IT自動化引擎，自動進行供應、組態管理、應用部署、編排和很多其它IT流程。

OpenStack：自由、開源的雲端運算平台，主要作為基礎設施即服務（IaaS）部署在公用雲和私有雲中，提供虛擬伺服器和其他資源給使用者使用。

Orange（英語：Orange (software)）：基於scikit-learn和pandas的開源機器學習和資料視覺化軟體，利用了PyQt6和PyQt6-WebEngine，通過廣大多樣的工具箱來搭建資料分析工作流程[271]，由盧布林雅那大學開發。

SageMath：涵蓋許多數學功能的應用軟體，基於NumPy、SciPy、matplotlib、SymPy、Maxima、GAP、FLINT、R等開源軟體套件進行實作。

MayaVi（英語：MayaVi）：基於VTK的應用程式和庫，用於互動式科學資料視覺化和採用Python的3D繪圖[272]。

Pitivi：用Python開發的基於GStreamer的影片編輯軟體。

一些Linux發行版，使用Python語言編寫安裝器，比如Ubuntu的Ubiquity和Fedora的Anaconda；或使用它編寫軟體包管理系統，比如Gentoo的Portage。Blender、Inkscape、QGIS和LibreOffice等軟體將Python作為嵌入式手稿語言。

人工智慧
[編輯]

經由Python開發了眾多的機器學習模型[273]和開發人工智慧應用的軟體庫：

Kornia：基於PyTorch的可微分電腦視覺軟體庫[274]。

spaCy（英語：spaCy）：用Python和Cython開發的工業級實力的自然語言處理軟體庫[275]，它具有自己的輕量級深度學習庫Thinc[276]。

ComfyUI（英語：ComfyUI）：開源的基於節點（英語：Node graph architecture#Use in computer graphics）的程式，它允許使用者從一系列的文字提示生成圖像。ComfyUI使用自由的擴散模型比如Stable Diffusion作為其圖像功能的基礎模型，還合併了其它工具比如ControlNet和LCM低秩適應，這裡每個工具都表示為程式中的一個節點。

Transformers：為下載和訓練前沿的預訓練模型提供API和工具[277]，由Hugging Face開發，支援在PyTorch、TensorFlow和JAX之間的框架互操作性。

Gradio：它是一個Python庫，允許快速建立和分享用於機器學習模型、API或任何任意Python函式的Web應用程式。使用Gradio，可以構建互動式使用者介面，與各種機器學習框架相容。還可以使用Gradio以互動方式偵錯模型、從使用者取得回饋，並通過自動生成的可共享連結輕鬆部署模型。[278][279]

LangChain：它是一個應用框架，旨在簡化使用大型語言模型的應用程式。作為一個語言模型整合框架，LangChain的用例包括文件分析和總結摘要, 程式碼分析和聊天機器人。[280] LangChain提供了一個標準介面，用於將不同的語言模型（LLM）連接在一起，以及與其他工具和資料來源的整合。

影響的語言
[編輯]

Python的設計和哲學已經影響了很多其他程式語言，例如：

ECMAScript/JavaScript：從Python借鑑了迭代器和生成器。

Genie：基於Vala編譯器的具有近似Python語法的語言。

Go：其設計原則受到了Python的可讀性與易用性的啟發[25]，享有相同風格的陣列分片語法。

Groovy：受到Python等動態型別語言的影響[26]。

Julia：在表達進階數值計算的方式和支援通用程式上借鑑了Python等語言[29]。

Kotlin：融合了Python和Java特徵，極小化了樣板程式碼（英語：Boilerplate code）而增加了開發效率[30]。

Nim：使用縮排和類似的語法[32]。

Ruby：主要從Python等語言中借鑑了特徵[33]。

Swift：有受Python啟發的語法[35]。

此外還有：Boo[21]、Cobra（英語：Cobra (programming language)）[22]、CoffeeScript[23]、GDScript[24]、Starlark（英語：Starlark）[34]和V（英語：V (programming language)）[36]等等。

在Python基礎上開發的程式語言有：

Taichi Lang：採用同Python幾乎一樣語法的指令式並列程式語言[281]，源出自MIT CSAIL實驗室，它嵌入在Python之中並使用即時編譯器框架如LLVM，將計算密集的Python程式碼轉變成本機GPU或CPU指令，它支援多數主流GPU API比如CUDA和Vulkan。

Coconut：在Python語法之上增加了用於函數式程式設計的新特徵的Python變體[282]。

Snek：受Python啟發的微小的可嵌入式語言，其目標處理器僅有數以kB計的快閃記憶體和靜態主記憶體[283]。

Pycopy：極簡主義（英語：Minimalism (computing)）、輕量級且可延伸的MicroPython相容語言實作[284]，它在精神上承襲了Python AST元迴圈直譯器[285]。

Mojo：基於MLIR編譯器框架（英語：MLIR (software)）並設計為Python超集的語言[31]。

Hy：嵌入到Python中的Lisp方言，它將Lisp程式碼變換成Python抽象語法樹對象，從而以Lisp形式操控全部Python庫。

範例與注釋
[編輯]

^ 縮排範例：

def is_even(a: int) -> bool:
"""确定数a是否是偶数."""
if a % 2 == 0:
print('偶数!')
return True
print('奇数!')
return False

# 参数比后续部份多一层缩进
def long_function_name(
var_one, var_two, var_three,
var_four):
# 可选的圆括号内后续行多一层缩进
if (this_is_first_thing
and that_is_second_thing):
do_something()
# 可选的圆括号内后续行不额外缩进
elif (this_is_third_thing and
that_is_fourth_thing):
do_something_different()
# 参数相对行首缩进一层
spam = long_function_name(
arg_one, arg_two,
arg_three, arg_four)
# 参数按开括号界定垂直对齐
eggs = long_function_name(arg_one, arg_two,
arg_three, arg_four)
# 可选的闭括号位置
my_list = [
1, 2, 3,
4, 5, 6,
]
# 可选的闭括号位置
my_set = {
1, 2, 3,
4, 5, 6,
}

^
tab字元（從左至右）被替代為1至8個空格，使得直到tab之前的諸字元加上這些替代空格的字元總數，是8的倍數（這意圖同於Unix所用規則）。前導於第一個非空白字元的空格的總數，確定了這一行的縮排層級。縮排所用諸字元，不能使用反斜槓來拆分成多個物理行；直到第一個反斜槓之前的空白確定縮排層級。如果原始碼檔案混合了tab和空格，並且在這種方式下縮排的意義依賴於一個tab相當於多少個空格，則這種縮排因不一致性而被報錯並拒絕[93]。

^
序列解包範例：

>>> a = [1, 2, 3]
>>> i, j, k = a
>>> print(i, j, k)
1 2 3

採用了並列賦值的斐波那契數列函式範例：

def fib(n): # 写出从第0项到第n项的Fibonacci系列
a, b, i = 0, 1, 0
while i <= n:
print(a, end=' ')
a, b, i = b, a+b, i+1
print()

^ 產生素數的惰性生成器的範例：

from itertools import count

def generate_primes(stop_at=0):
if stop_at != 1:
primes = [2]
yield 2
for n in count(3, 2):
if 0 < stop_at < n:
return # 引发StopIteration例外
composite = False
for p in primes:
if not n % p:
composite = True
break
elif p ** 2 > n:
break
if not composite:
primes.append(n)
yield n

上述函式的隱式迭代用例：

for i in generate_primes(): # 迭代于100以内所有素数上
if i > 100:
break
print(i)

在生成器表達式中使用上述函式，定義了一個惰性的、巨大而並非無限的搜集的範例：

from itertools import islice

primes_under_million = (i for i in generate_primes() if i < 1000000)
two_thousandth_prime = islice(primes_under_million, 1999, 2000)
print(next(two_thousandth_prime))

^ 下面的範例用生成器類比協程[109]：

def produce(n):
try:
for item in range(n):
print(f'producing item {item} ->')
yield item
except GeneratorExit:
return

def consume():
item = None
try:
while True:
item = yield item
print(f'consuming item {item} <-')
except GeneratorExit:
return

def main():
r = []
t1 = produce(10)
t2 = consume()
try:
next(t2)
while True:
p = next(t1)
r += [t2.send(p)]
except StopIteration:
t2.close()
print(f'result items: {r}')

main()

^ class語句的類衍化列給出基礎類列表，沒有衍化列的類，預設繼承基礎類object。類的套件接著在新的執行框架（frame）中執行，它使用新建的局部命名空間和原來的全域命名空間。當這個類套件完成執行之時，丟棄它的執行框架並儲存它的局部命名空間。一個類對象接著被建立，其基礎類採用衍化列，其特性字典採用儲存的局部命名空間。類名字接著在原來的局部命名空間中，被繫結到這個類對象。

^ def語句的執行，在當前局部命名空間中，將函式名字繫結到一個函式對象（對函式的可執行程式碼的包裝器）。這個函式對象包含到當前全域命名空間的參照，作為呼叫這個函式時使用的全域命名空間。

^ 原生的協程範例：

import asyncio
import random

async def produce(queue, n):
for item in range(n):
# 生产一个项目，使用sleep模拟I/O操作
print(f'producing item {item} ->')
await asyncio.sleep(random.random())
# 将项目放入队列
await queue.put(item)
# 指示生产完毕
await queue.put(None)

async def consume(queue):
while True:
# 等待来自生产者的项目
item = await queue.get()
if item is None:
break
# 消费这个项目，使用sleep模拟I/O操作
print(f'consuming item {item} <-')
await asyncio.sleep(random.random())

async def main():
queue = asyncio.Queue()
task1 = asyncio.create_task(produce(queue, 10))
task2 = asyncio.create_task(consume(queue))
await task1
await task2

asyncio.run(main())

^ 遵循EAFP（請求原諒比獲得授權更容易）風格的例外處理範例：

f = None
try:
f = open("aFileName", mode="w")
f.write(could_make_error()) # 不存在could_make_error()则产生错误
except IOError as error:
print(error)
print("不能打开文件")
except: # 捕获所有例外
print("未预期的错误")
else: # 在没有出现例外时执行
print("文件写入完全成功")
finally: # 清除行动，总是执行
if f:
f.close()

^ 使用with將檔案作為資源來管理的範例：

from contextlib import contextmanager
@contextmanager
def opened(filename, mode="r"):
try:
f = open(filename, mode)
except IOError as error:
print(error)
yield None
else:
try:
yield f
finally:
f.close()

with opened("aFileName", mode="w") as f:
try:
f.write(could_make_error()) # 不存在could_make_error()则产生错误
except AttributeError:
print("不能打开文件")
except: # 捕获所有例外
print("未预期的错误")
else: # 在没有出现例外时执行
print("文件写入完全成功")

^
內建vars()函式，返回一個模組、類、實例或任何具有字典特性__dict__的對象的字典特性。內建globals()函式，返回實作當前模組的命名空間的一個字典。內建locals()函式，更新並返回表示當前局部符號表的一個字典。在函式塊中而非類塊中呼叫locals()之時，它返回自由變數。在模組層級上，locals()和globals()返回同一個字典。內建dir()函式，在無參數時，返回在當前局部範疇內的名字列表；在有一個參數時，嘗試返回這個對象的有效特性的列表。[118]

^
除了在塊中出現的每個賦值語句或匯入語句之外，下列構造也繫結名字：給函式的形式參數、類別定義、函式定義、賦值表達式、在for語句頭部中和各種as關鍵字之後的識別碼目標（target），as關鍵字出現在import語句、with語句、except子句、except*子句和結構式模式匹配的as模式之中。

^
完整的Python程式，在一個極小初始化的環境中執行：所有內建和標準模組均可獲得，但除了sys（各種系統服務）、builtins（內建函式、例外和None）和__main__之外都未被初始化。__main__用來為完整程式的執行提供局部和全域名字。當直譯器被呼叫在互動模態下的時候，它一次一個的讀取並執行語句；初始環境同於完整程式，每個語句都在__main__的命名空間中執行。

頂層程式碼是啟動執行的首個使用者指定Python模組。__main__是頂層程式碼執行所在的環境。從命令列使用-m參數，作為頂層指令碼執行的模組（作為模組__main__）是塊。此時__name__變數被設定為"__main__"，籍此可在這個模組中增加直接執行時候執行的程式碼[113][119]。

^ 局部變數範例：

>>> def spam():
... print(a)
...
>>> a = 10
>>> spam()
10
>>> def spam():
... a = 100
... print(a)
...
>>> spam()
100
>>> a
10
>>> def spam():
... a *= 10
... print(a)
...
>>> spam()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 2, in spam
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

^ 非局部變數範例：

>>> def spam():
... def eggs():
... nonlocal a
... a *= 10
... print(a)
... a = 10
... eggs()
...
>>> spam()
100
>>> def spam():
... def eggs():
... nonlocal a
... a *= 10
... print(a)
... global a
... eggs()
...
File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'a' found

^ 總體變數範例：

>>> def spam():
... global a
... a *= 10
... print(a)
...
>>> a = 10
>>> spam()
100
>>> a
100
>>> def spam():
... def eggs():
... print(a)
... global a
... eggs()
...
>>> a = 10
>>> spam()
10
>>> def spam():
... def eggs():
... a *= 10
... print(a)
... global a
... eggs()
...
>>> spam()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 6, in spam
File "<stdin>", line 3, in eggs
UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

^
通過表達式列表建立元組範例：

a_tuple = 1, 2, 3, 'four'

通過列表展示建立列表範例：

a_list = [1, 2, 3, 'a dog']

通過字典展示建立字典範例：

a_dictionary = {'key 1': 'value 1', 2: 3, 4: []}

通過集合展示建立集合範例：

some_set = {0, (), False}

^
列表推導式範例：

>>> [x + 3 for x in range(4)]
[3, 4, 5, 6]

使用列表推導式可以優雅的將快速排序演算法表達為：

def qsort(L):
if L == []:
return []
pivot = L[0]
return (qsort([x for x in L[1:] if x < pivot])
+ [pivot]
+ qsort([x for x in L[1:] if x >= pivot]))

生成器表達式範例：

>>> sum(x * x for x in range(10))
285
>>> dict((n, n*n) for n in range(5))
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>> set(n*n for n in range(5))
{0, 1, 4, 9, 16}

字典推導式範例：

>>> {x: x + 3 for x in range(4)}
{0: 3, 1: 4, 2: 5, 3: 6}

集合推導式範例：

>>> {x + 3 for x in range(4)}
{3, 4, 5, 6}

^ 可迭代解包和字典解包範例：

>>> a = [1, 2, 3]; b = [4, 5]
>>> c = [*a, b]
>>> c
[1, 2, 3, [4, 5]]
>>> d = {*a, *b}
>>> d
{1, 2, 3, 4, 5}
>>> e = (*a, *b)
>>> e
(1, 2, 3, 4, 5)
>>> f = {'as':1, 'bs':2 }; g = {'cs':3, 'ds':4}
>>> h = {**f, **g}
>>> h
{'as': 1, 'bs': 2, 'cs': 3, 'ds': 4}

^ 列表分片範例：

>>> nums = [0, 1, 2, 3, 4, 5, 6]
>>> nums[2:5] #从下标2的元素剪切直到下标5之前的元素
[2, 3, 4]
>>> nums[1:] #从下标1的元素剪切直到末位元素
[1, 2, 3, 4, 5, 6]
>>> nums[:-3] #从首位元素剪切直到倒数第3个元素之前的元素
[0, 1, 2, 3]
>>> nums[:] #复制所有元素
[0, 1, 2, 3, 4, 5, 6]
>>> nums[::-1] #反转所有元素
[6, 5, 4, 3, 2, 1, 0]
>>> nums[1:5:2] #从下标1的元素剪切直到下标5之前的元素且步长为2
[1, 3]

^ lambda表達式範例：

>>> from functools import reduce
>>> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
15
>>> fac = lambda n: (1 if n<2 else n*fac(n-1))
>>> fac(5)
120
>>> [*map(fac, [1, 2, 3, 4, 5])]
[1, 2, 6, 24, 120]

不動點組合子和邱奇編碼可參見專門介紹[128]。

^ 賦值表達式在用作子表達式，即位於分片表達式、條件表達式、lambda表達式、關鍵字參數中的表達式和推導式中的if表達式之中，以及在assert和with語句之中的時候，必須圍繞著圓括號。在它們可以使用的所有其他地方，包括在if和while語句之中，都不要求圓括號[131]。

^
兩個類及元類等的實例關係（藍色連接）與繼承關係（綠色連接）示意圖：

 

r = object
c = type
class M(c): pass

class A(metaclass=M): pass

class B(A): pass

b = B()

>>> type(b)
<class '__main__.B'>
>>> print(type(B), B.__bases__)
<class '__main__.M'> (<class '__main__.A'>,)
>>> print(type(A), A.__bases__)
<class '__main__.M'> (<class 'object'>,)
>>> print(type(M), M.__bases__)
<class 'type'> (<class 'type'>,)
>>> print(type(c), c.__bases__)
<class 'type'> (<class 'object'>,)
>>> print(type(r), r.__bases__)
<class 'type'> ()

^ 可以通過sys.getrecursionlimit()，獲知當前的遞迴最大深度限制，還可以通過sys.setrecursionlimit()來設定這個限制。例如遞迴定義的階乘函式：

def fac(n):
return 1 if n <= 1 else fac(n-1) * n

目前fac(994)可以遞迴執行至預設的最大深度限制1000，CPython直譯器自身占用了初始的那幾層。

^ 詞法閉包的例子：

def f(x):
def g(y):
return x + y
return g # 返回一个闭包。

h = lambda x: lambda y: x + y

# 将指定闭包赋值给变量。
a = f(1)
b = h(1)
c = f(2)
# 使用存储在变量中的闭包。
assert a(5) == 6
assert b(5) == 6
assert c(5) == 7
# 使用闭包而不事先把它们绑定到变量。
assert f(1)(5) == 6 # f(1)是个闭包。
assert h(1)(5) == 6 # h(1)是个闭包。
assert f(2)(5) == 7 # f(2)是个闭包。

^ 定義修飾器的範例：

def viking_chorus(func):
def wrapper(*args, **kwargs):
for i in range(3):
func(*args, **kwargs)
return wrapper

呼叫修飾器的範例：

@viking_chorus
def menu_item(*args):
print(", ".join(args)+", and spam")

它等價於：

def menu_item(*args):
print(", ".join(args)+", and spam")

menu_item = viking_chorus(menu_item)

viking_chorus修飾後的menu（英語：Spam (Monty Python sketch)）_item將原來定義執行3次：

>>> menu_item("egg","bacon")
egg, bacon, and spam
egg, bacon, and spam
egg, bacon, and spam

^ 修飾器工廠範例，這裡的favourite_colour接受一個實際參數，並返回一個修飾器：

def favourite_colour(colour):
def decorator(func):
def wrapper(*args, **kwargs):
print(f"My favourite colour is {colour}.")
func(*args, **kwargs)
return wrapper
return decorator

def invincible(func):
def wrapper(*args, **kwargs):
print("I'm invincible!")
func(*args, **kwargs)
return wrapper

使用毗連的修飾詞連結修飾器範例：

@invincible
@favourite_colour("blue")
def black_knight():
print("None shall pass.")

它等價於：

black_knight = invincible(favourite_colour("blue")(black_knight))

black_knight（英語：Black Knight (Monty Python)）()結果為：

>>> black_knight()
I'm invincible!
My favourite colour is blue.
None shall pass.

^ 函式的形實參數二者結合範例。例如：

>>> def spam(a):
... a.append('LovelySpam')
...
>>> def eggs(b):
... b=100 #实际上是重新绑定了另一个整型对象100
...
>>> a=[]
>>> b=10
>>> spam(a)
>>> eggs(b)
>>> print(a)
['LovelySpam']
>>> print(b)
10

^ 當形式參數的預設值是可變對象比如列表或字典的時候，如果這個函式修改了這個對象，則這個形式參數的預設值就在實效上被修改了。比如：

>>> def f(a, L=[]):
... L.append(a)
... return L
...
>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
>>> print(f(0, []))
[0]
>>> print(f(3))
[1, 2, 3]

這通常不是所預期的效果。一種解決辦法是使用None作為預設值，並在函式主體中顯式的測試它：

def f(a, L=None):
if L is None:
L = []
L.append(a)
return L

^ 函式的形式參數預設值的定義範例：

>>> from inspect import getfullargspec
>>> def func(p1, /, p2, p3="x", *, p4): pass
...
>>> getfullargspec(func)
FullArgSpec(args=['p1', 'p2', 'p3'], varargs=None, varkw=None, defaults=('x',), kwonlyargs=['p4'], kwonlydefaults=None, annotations={})

^ 函式的可變參數的定義範例：

>>> from inspect import getfullargspec
>>> def func(p1, /, p2, *args, p3, **kwargs): pass
...
>>> getfullargspec(func)
FullArgSpec(args=['p1', 'p2'], varargs='args', varkw='kwargs', defaults=None, kwonlyargs=['p3'], kwonlydefaults=None, annotations={})

^ 對象的方法範例：

>>> class Fish(object):
... hungry = True
... def eat(self, food=None):
... if food is not None:
... self.hungry = False
...
... def status(self):
... print("Hungray!" if self.hungry else "Not hungray!")
...
>>> e = Fish()
>>> Fish.hungry = False
>>> e.hungry
False
>>> Fish.hungry = True
>>> e.hungry
True
>>> e.__dict__
{}
>>> status(e)
Hungray!
>>> Fish.status = status
>>> type(Fish.status)
<class 'function'>
>>> type(e.status)
<class 'method'>
>>> e.status()
Hungray!
>>> e.eat("earthworm")
>>> e.__dict__
{'hungry': False}
>>> e.status()
Not hungray!
>>> Fish.hungry
True

^ 類別方法__init_subclass__和在子類中用內建函式super()呼叫超類別的實例方法和類別方法的例子：

>>> class Thought(object):
... __cls_descr = "Thought类型"
... @classmethod
... def descript(cls):
... return cls.__cls_descr
... def __init_subclass__(cls, /, **kwargs):
... super().__init_subclass__(**kwargs)
... cls.__cls_descr = "Thought类型的子类型"
... def __init__(self, *args, **kwargs):
... self.idea = "我感觉自己斜停在了平行宇宙里。"
... print(f"我是{type(self).descript()}的新对象！")
... def message(self, *args):
... print("\n".join([self.idea] + [*args]))
...
... class Advice(Thought):
... @classmethod
... def descript(cls):
... return super().descript() + "Advice类型"
... def message(self):
... super().message("警告：日历中的日期比实际显示的更近！")
...
>>> t = Thought()
我是Thought类型的新对象！
>>> t.message()
我感觉自己斜停在了平行宇宙里。
>>> a = Advice()
我是Thought类型的子类型Advice类型的新对象！
>>> a.message()
我感觉自己斜停在了平行宇宙里。
警告：日历中的日期比实际显示的更近！
>>> super(Advice, a).message()
我感觉自己斜停在了平行宇宙里。
>>> Advice.super = super(Advice)
>>> a.super.message()
我感觉自己斜停在了平行宇宙里。
>>> [*super.__dict__]
['__new__', '__repr__', '__getattribute__', '__get__', '__init__', '__thisclass__', '__self__', '__self_class__', '__doc__']
>>> super(Advice).__thisclass__
<class '__main__.Advice'>
>>> assert super(Advice).__self__ is None
>>> assert super(Advice).__self_class__ is None
>>> super(Advice, a).__self__
<__main__.Advice object at 0x754299f19940>
>>> super(Advice, a).__self_class__
<class '__main__.Advice'>
>>> super(Thought, Advice).__thisclass__
<class '__main__.Thought'>
>>> super(Thought, Advice).__self__
<class '__main__.Advice'>
>>> super(Thought, Advice).__self_class__
<class '__main__.Advice'>

^ 特殊方法__init__和類別變數__slots__（槽）範例：

>>> class Bird(object):
... __slots__ = ['hungry']
... def __init__(self, *args, **kwargs):
... self.hungry = True
... def eat(self, food=None):
... if food is not None:
... self.hungry = False
... def status(self):
... print("Hungray!" if self.hungry else "Not hungray!")
...
>>> Bird.hungry
<member 'hungry' of 'Bird' objects>
>>> type(Bird.hungry)
<class 'member_descriptor'>
>>> f = Bird()
>>> f.status()
Hungray!
>>> f.eat("mealworm")
>>> f.status()
Not hungray!

^ 類別方法、靜態方法__new__（它是特殊情況而不需要加以修飾）、特殊方法__call__、__len__、__getitem__、__setitem__和弱參照集合（英語：Set (abstract data type)）範例：

>>> from weakref import WeakSet
... class D():
... __template = {}
... __obj_set = WeakSet()
... def __new__(cls, *args, **kwargs):
... obj = super().__new__(cls)
... cls.__obj_set.add(obj)
... return obj
... @classmethod
... def load(cls, dict):
... cls.__template |= dict
... @classmethod
... def create(cls, *args, **kwargs):
... return cls(cls.__template, *args, **kwargs)
... @classmethod
... def count(cls):
... return len(cls.__obj_set)
... @classmethod
... def contains(cls, obj):
... return obj in cls.__obj_set
... def __init__(self, dict={}, /, *args, **kwargs):
... self.__dict__ |= dict
... self.__dict__ |= kwargs
... def __call__(self, *args, **kwargs):
... self.__dict__ |= kwargs
... return self.__dict__.copy()
... def __len__(self):
... return len(self.__dict__)
... def __getitem__(self, key):
... return self.__dict__[key]
... def __setitem__(self, key, value):
... self.__dict__[key] = value
...
>>> a = {'ak': 1, 'bk': 2, 'ck': 3}
>>> d = D(a, dk=4)
>>> d()
{'ak': 1, 'bk': 2, 'ck': 3, 'dk': 4}
>>> D.load(a)
>>> e = D.create(ck=4)
>>> e()
{'ak': 1, 'bk': 2, 'ck': 4}
>>> f = D(ak=1, bk=2)
>>> f(ck=3)
{'ak': 1, 'bk': 2, 'ck': 3}
>>> f['ak']
1
>>> f['ak'] = 5
>>> f()
{'ak': 5, 'bk': 2, 'ck': 3}
>>> len(f)
3
>>> D.count()
3
>>> del f
>>> D.count()
2
>>> d.__weakref__
<weakref at 0x72652697ede0; to 'D' at 0x72652713b230>
>>> D.contains(d)
True
>>> D.contains(1)
False

^ 在類中採用資料描述器的範例：

>>> from weakref import WeakKeyDictionary
>>> class RevealAccess():
... """ 在存取时披露提示消息的数据描述器
... """
... def __init__(self, default=None):
... self.default = default
... self.dict = WeakKeyDictionary()
... def __get__(self, obj, objtype=None):
... print('Retrieving')
... return (self.dict[obj] if obj in self.dict
... else self.default)
... def __set__(self, obj, val):
... print('Updating')
... self.dict[obj] = val
...
>>> class MyClass():
... x = RevealAccess(10)
...
>>> a = MyClass()
>>> a.x
Retrieving
10
>>> a.x = 20
Updating
>>> a.x
Retrieving
20
>>> b = MyClass()
>>> b.x
Retrieving
10

^ 在類中呼叫property()的例子：

>>> class C():
... def __init__(self, *args, **kwargs):
... self.__x = None
... def getx(self):
... return self.__x
... def setx(self, value):
... self.__x = value
... def delx(self):
... del self.__x
... x = property(getx, setx, delx, "I'm the 'x' property.")
... del getx, setx, delx
...
>>> c = C()
>>> vars(c)
{'_C__x': None}
>>> {*C.__dict__}
{'__init__', '__static_attributes__', 'x', '__weakref__', '__module__', '__doc__', '__firstlineno__', '__dict__'}

上述程式碼可以採用修飾詞進一步的書寫為：

>>> class C():
... def __init__(self, *args, **kwargs):
... self.__x = None
... @property
... def x(self):
... """I'm the 'x' property."""
... return self.__x
... @x.setter
... def x(self, value):
... self.__x = value
... @x.deleter
... def x(self):
... del self.__x
...
>>> c = C()
>>> vars(c)
{'_C__x': None}
>>> {*C.__dict__}
{'__init__', '__static_attributes__', 'x', '__weakref__', '__module__', '__doc__', '__firstlineno__', '__dict__'}

參照
[編輯]

^ 1.0 1.1 GitHub repository of Python 0.9.1 source. [2023-02-25]. （原始內容存檔於2023-03-05）. 

HISTORY. Python source distribution. Python Foundation. [2017-11-23]. （原始內容存檔於2017-12-01）. 

^ Python 3.15.0 (final) is here!. 2026年10月9日 （英語）.  引文格式1維護：未辨識語文類型 (link)

^ 3.0 3.1 Glossary — duck-typing. [2023-06-28]. （原始內容存檔於2020-06-25）. 

^
Why is Python a dynamic language and also a strongly typed language - Python Wiki. wiki.python.org. [2021-01-27]. （原始內容存檔於2021-03-14）. 

^ 5.0 5.1 PEP 483 – The Theory of Type Hints. [2023-03-16]. （原始內容存檔於2023-03-26）. 

^ PEP 11 – CPython platform support. [2025-07-17]. （原始內容存檔於2026-07-22）. 

^ File extension .pyo was removed in Python 3.5. See PEP 0488 （頁面存檔備份，存於網際網路檔案館）

^ Holth, Moore. PEP 0441 -- Improving Python ZIP Application Support. 2014-03-30 [2015-11-12]. （原始內容存檔於2018-12-26）. 

^ 9.0 9.1 9.2 Why was Python created in the first place?. Python FAQ. [2007-03-22]. （原始內容存檔於2008-02-23）. 

^ Andrew Kuchling, Guido van Rossum. LJ Interviews Guido van Rossum. 1998-11-01 [2023-03-21]. （原始內容存檔於2023-03-30）. String slicing came from Algol-68 and Icon. 

^ 11.0 11.1
The Python Standard Library － Functional Programming Modules － itertools — Functions creating iterators for efficient looping. [2020-04-22]. （原始內容存檔於2020-06-14）. 

^
van Rossum, Guido. An Introduction to Python for UNIX/C Programmers. Proceedings of the NLUUG Najaarsconferentie (Dutch UNIX Users Group). 1993 [2021-03-14]. （原始內容存檔於2013-06-17）. even though the design of C is far from ideal, its influence on Python is considerable. 

^ 13.0 13.1
The Python Tutorial － 9. Classes. [2012-02-20]. （原始內容存檔於2012-10-23）. Compared with other programming languages, Python’s class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. 

^ Fredrik Lundh. Python-list mailing list － passing by refference. [2023-03-06]. （原始內容存檔於2023-03-06）. replace "CLU" with "Python", "record" with "instance", and "procedure" with "function or method", and you get a pretty accurate description of Python's object model. 

^ 15.0 15.1
Simionato, Michele. The Python 2.3 Method Resolution Order. Python Software Foundation. [2021-03-14]. （原始內容存檔於2020-08-20）. The C3 method itself has nothing to do with Python, since it was invented by people working on Dylan and it is described in a paper intended for lispers. 

^
Kuchling, A. M. Functional Programming HOWTO. Python v2.7.2 documentation. Python Software Foundation. [2012-02-09]. （原始內容存檔於2012-10-24）. 

^ 17.0 17.1 17.2 Guido van Rossum. Python Reference Manual － Version 1.2 (PDF). CWI Report CS-R9525. May 1995 [2023-03-04]. （原始內容存檔 (PDF)於2023-03-05）. Python is a simple, yet powerful, interpreted programming language that bridges the gap between C and shell programming, and is thus ideally suited for "throw-away（英語：Software_prototyping#Throwaway_prototyping） programming" and rapid prototyping. Its syntax is put together from constructs borrowed from a variety of other languages; most prominent are influences from ABC, C, Modula-3 and Icon.

The Python interpreter is easily extended with new functions and data types implemented in C. Python is also suitable as an extension language for highly customizable C applications such as editors or window managers. 

^
Smith, Kevin D.; Jewett, Jim J.; Montanaro, Skip; Baxter, Anthony. PEP 318 – Decorators for Functions and Methods. Python Enhancement Proposals. Python Software Foundation. 2004-09-02 [2012-02-24]. （原始內容存檔於2020-06-03）. 

^
More Control Flow Tools. Python 3 documentation. Python Software Foundation. [2015-07-24]. （原始內容存檔於2016-06-04）. 

^ re — Regular expression operations. docs.python.org. [2022-09-06]. （原始內容存檔於2018-07-18）. This module provides regular expression matching operations similar to those found in Perl. 

^ 21.0 21.1 Gotchas for Python Users. boo.codehaus.org. Codehaus Foundation. [2008-11-24]. （原始內容存檔於2008-12-11）. 

^ 22.0 22.1 Esterbrook, Charles. Acknowledgements. cobra-language.com. Cobra Language. [2010-04-07]. （原始內容存檔於2008-02-08）. 

^ 23.0 23.1 CoffeeScript for Python Programmers. [2025-07-03]. （原始內容存檔於2025-07-03）. CoffeeScript is a programming language whose syntax is clearly designed to match much of Python (with additional inspirations from Perl, ECMAScript, Ruby, etc.). 

^ 24.0 24.1 FAQ: What is GDScript and why should I use it?. [2020-09-13]. （原始內容存檔於2020-05-19）. 

^ 25.0 25.1 Frequently Asked Questions (FAQ) - The Go Programming Language. The Go Programming Language. [2016-02-26]. （原始內容存檔於2020-05-03）. 

^ 26.0 26.1 Strachan, James. Groovy – the birth of a new dynamic language for the Java platform. 2003-08-29 [2007-06-11]. （原始內容存檔於2007-04-05）. 

^ Perl and Python influences in JavaScript. www.2ality.com. 2013-02-24 [2015-05-15]. （原始內容存檔於2018-12-26）. 

^ Rauschmayer, Axel. Chapter 3: The Nature of JavaScript; Influences. O'Reilly, Speaking JavaScript. [2015-05-15]. （原始內容存檔於2018-12-26）. 

^ 29.0 29.1 Home · The Julia Language. docs.julialang.org. [2018-08-15]. （原始內容存檔於2021-01-11） （英語）. 

^ 30.0 30.1 Jalan, Nishant Aanjaney. Programming in Kotlin. CodeX. 2022-11-10 [2024-04-29]. （原始內容存檔於2024-11-30） （英語）. 

^ 31.0 31.1 Krill, Paul. Mojo language marries Python and MLIR for AI development. InfoWorld. 2023-05-04 [2023-05-05]. （原始內容存檔於2023-05-05） （英語）. 

^ 32.0 32.1 Yegulalp, Serdar. Nim language draws from best of Python, Rust, Go, and Lisp. InfoWorld. 2017-01-16 [2020-09-13]. （原始內容存檔於2018-10-13）. Nim's syntax is strongly reminiscent of Python's, as it uses indented code blocks and some of the same syntax (such as the way if/elif/then/else blocks are constructed). 

^ 33.0 33.1 Bini, Ola. Practical JRuby on Rails Web 2.0 Projects: Bringing Ruby on Rails to Java. Berkeley: APress. 2007: 3. ISBN 978-1-59059-881-8. It draws primarily on features from Perl, Smalltalk, Python, Lisp, Dylan, and CLU. 

^ 34.0 34.1 Starlark Language. [2019-05-25]. （原始內容存檔於2020-06-15）. 

^ 35.0 35.1
Lattner, Chris. Chris Lattner's Homepage. Chris Lattner. 2014-06-03 [2014-06-03]. （原始內容存檔於2018-12-25）. Of course, it also greatly benefited from the experiences hard-won by many other languages in the field, drawing ideas from Objective-C, Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list. 

^ 36.0 36.1 V documentation (Introduction). GitHub. [2024-12-24]. （原始內容存檔於2026-07-15） （英語）. 

^ 彼德·諾米格. Python for Lisp Programmers. [2020-04-21]. （原始內容存檔於2020-06-14）. Python can be seen as a dialect of Lisp with "traditional" syntax (what Lisp people call "infix" or "m-lisp" syntax). 

^ Rossum, Guido Van. The History of Python: A Brief Timeline of Python. The History of Python. 2009-01-20 [2021-03-05]. （原始內容存檔於2020-06-05）. 

^ Peterson, Benjamin. Python Insider: Python 2.7.18, the last release of Python 2. Python Insider. 2020-04-20 [2020-04-27]. （原始內容存檔於2020-04-26）. 

^ Stack Overflow Developer Survey 2025. [2026-02-23]. （原始內容存檔於2025-12-16）. After more than a decade of steady growth, Python's adoption has accelerated significantly. 

the State of Developer Ecosystem Report 2025. [2026-02-23]. （原始內容存檔於2026-06-12）. 

PYPL PopularitY of Programming Language index. pypl.github.io. [2021-03-26]. （原始內容存檔於2017-03-14） （英語）. 

^ 41.0 41.1 TIOBE Index. TIOBE - The Software Quality Company. [2021-10-06]. （原始內容存檔於2020-06-14）. 

^ Guido van Rossum - Resume. [2022-10-12]. （原始內容存檔於2022-12-21）. 

^ amoeba operating system. [2023-02-25]. （原始內容存檔於2023-03-05）. 

^ Whetting Your Appetite. The Python Tutorial. Python Software Foundation. [2012-02-20]. （原始內容存檔於2012-10-26）. 

^ The Making of Python. Artima Developer. [2007-03-22]. （原始內容存檔於2016-09-01）. 

^ Older source releases (1.0.1 - 1.6). [2023-03-05]. （原始內容存檔於2023-03-05）. 

^ HISTORY. [2020-09-12]. （原始內容存檔於2017-12-01）. Lambda expressions are particularly useful in combination with map(), filter() and reduce(), described below. Thanks to Amrit Prem for submitting this code (as well as map(), filter(), reduce() and xrange())! 

^ LJ #37: Python 1.4 Update. [2007-04-29]. （原始內容存檔於2007-05-01）. 

^ Kuchling, A. M.; Zadka, Moshe. What's New in Python 2.0. Python Software Foundation. 2000-10-16 [2012-02-11]. （原始內容存檔於2012-10-23）. 

^ Hylton, Jeremy. PEP 227 － Statically Nested Scopes. 2000-11-01 [2007-03-22]. （原始內容存檔於2007-03-29）. 

^ 51.0 51.1 Guido van Rossum. Unifying types and classes in Python 2.2. [2020-09-26]. （原始內容存檔於2019-09-28）. 

^ What’s New in Python 2.2 － PEP 234: Iterators. [2020-10-21]. （原始內容存檔於2021-02-07）. 

^ What’s New in Python 2.2 － PEP 255: Simple Generators. [2020-10-21]. （原始內容存檔於2021-02-07）. 

^ What’s New in Python 2.2 － Descriptors. [2020-10-21]. （原始內容存檔於2021-02-07）. 

^ 55.0 55.1 What’s New in Python 2.4 － PEP 318: Decorators for Functions and Methods. [2020-10-21]. （原始內容存檔於2021-02-07）. 

^ PEP 339 – Design of the CPython Compiler. 2005 [2023-03-06]. （原始內容存檔於2023-03-06）. 

^ Guido van Rossum. What’s New In Python 3.0. [2023-02-18]. （原始內容存檔於2012-11-02）. 

^ What’s New In Python 3.4 － asyncio. [2023-02-22]. （原始內容存檔於2023-06-13）. 

^ What’s New In Python 3.5 － PEP 484 - Type Hints. [2023-02-25]. （原始內容存檔於2016-06-18）. 

^ PEP 492 － Coroutines with async and await syntax. [2019-11-21]. （原始內容存檔於2019-01-05）. 

^ Benevolent dictator for life. Linux Format. 2005-02-01. （原始內容存檔於2006-10-01）. 

^ Transfer of power. （原始內容存檔於2018-07-12）. 

^ PEP 8100. python. Python Software Foundation. [2019-05-04]. （原始內容存檔於2020-06-04）. 

^ Steering Council nomination: Guido van Rossum (2020 term). [2020-10-11]. （原始內容存檔於2019-12-29）. 

^ The Python Standard Library － Built-in Types － Generic Alias Type. [2023-03-17]. （原始內容存檔於2020-06-14）. 

^ What’s New In Python 3.9 － New Parser. [2023-02-22]. （原始內容存檔於2020-10-07）. 

^ What’s New In Python 3.10 － PEP 634: Structural Pattern Matching. [2023-02-22]. （原始內容存檔於2023-06-11）. 

^ The Python Standard Library － Built-in Types － Union Type. [2023-03-17]. （原始內容存檔於2020-06-14）. 

^ What’s New In Python 3.11 － Faster CPython. [2023-03-24]. （原始內容存檔於2023-06-13）. 

^ What’s New In Python 3.12 — PEP 695: Type Parameter Syntax. [2023-10-20]. （原始內容存檔於2023-11-13）. 

^ What’s New In Python 3.13. [2024-09-17]. （原始內容存檔於2024-09-29）. 

^ What’s new in Python 3.14. [2025-07-08]. （原始內容存檔於2026-07-21）. 

^ What’s new in Python 3.15. [2026-07-07]. （原始內容存檔於2026-07-22）. 

^ Python Developer's Guide — Status of Python Version. devguide.python.org. [2022-08-26]. （原始內容存檔於2022-08-26）. 

^ PEP 8107 – 2026 Term Steering Council election. Python Software Foundation. [2025-12-14]. （原始內容存檔於2026-07-08）. 

^ 76.0 76.1 The Python Language Reference － 3. Data model － Special method names. [2020-09-25]. （原始內容存檔於2012-10-26）. 

^ aspectlib. [2025-07-01]. （原始內容存檔於2025-09-02）. aspectlib is an aspect-oriented programming, monkey-patch and decorators library. It is useful when changing behavior in existing code is desired. It includes tools for debugging and testing: simple mock/record and a complete capture/replay framework. 

^ PEP 316 -- Programming by Contract for Python. [2021-01-17]. （原始內容存檔於2021-01-22）. 

Deal. [2021-06-20]. （原始內容存檔於2021-07-16）. python library for design by contract (DbC) and checking values, exceptions, and side-effects. 

icontract. [2021-01-17]. （原始內容存檔於2021-01-21）. icontract provides design-by-contract to Python3 with informative violation messages and inheritance. 

^ Datalog logic programming in python. [2026-07-10]. （原始內容存檔於2026-07-20）. 

^ Extending Python with C or C++ — Reference Counting in Python. Docs.python.org. [2020-06-05]. （原始內容存檔於2012-10-18） （英語）. 

^ CPython’s internals — Garbage collector design. [2025-11-08]. （原始內容存檔於2026-06-22）. 

^ Functional Programming HOWTO. [2020-09-26]. （原始內容存檔於2012-10-24）. 

^ van Rossum, Guido. The fate of reduce() in Python 3000. Artima Developer. [2007-03-22]. （原始內容存檔於2007-04-07）. 

^ Functional Programming Modules. Docs.python.org. [2020-09-26]. （原始內容存檔於2020-09-20）. 

^ Guido van Rossum. Extending and Embedding the Python Interpreter － Version 1.2 (PDF). CWI Report CS-R9527. May 1995 [2023-03-05]. （原始內容存檔 (PDF)於2023-03-05）. Python is an interpreted object oriented programming language. This document describes how to write modules in C or C++ to extend the Python interpreter with new modules. Those modules can define new functions but also new object types and their methods. The document also describes how to embed the Python interpreter in another application, for use as an extension language. Finally, it shows how to compile and link extension modules so that they can be loaded dynamically (at run time) into the interpreter, if the underlying operating system supports this feature. 

^ The Python Standard Library － Generic Operating System Services － ctypes — A foreign function library for Python. [2022-01-14]. （原始內容存檔於2022-04-27）. 

^ PEP 523 – Adding a frame evaluation API to CPython. [2022-08-29]. （原始內容存檔於2022-08-29）. 

^ The Python Language Reference － 7. Simple statements. [2020-10-30]. （原始內容存檔於2023-06-06）. 

The Python Language Reference － 10. Full Grammar specification. [2023-02-17]. （原始內容存檔於2023-06-06）.

simple_stmts:

    | simple_stmt !';' NEWLINE # Not needed, there for speedup

    | ';'.simple_stmt+ [';'] NEWLINE 

^ The Python Language Reference － 2. Lexical analysis － Comments. [2023-03-11]. （原始內容存檔於2018-01-09）. 

^ 90.0 90.1 The Python Language Reference － 2. Lexical analysis － Explicit line joining. [2023-02-17]. （原始內容存檔於2018-01-09）. 

^ The Python Language Reference － 8. Compound statements. [2023-02-18]. （原始內容存檔於2019-11-27）. 

^ PEP 8 – Style Guide for Python Code － Indentation. [2020-09-26]. （原始內容存檔於2018-07-13）. 

^ The Python Language Reference － 2. Lexical analysis － Indentation. [2023-02-18]. （原始內容存檔於2018-01-09）. 

^ The Python Language Reference － 10. Full Grammar specification. [2023-02-17]. （原始內容存檔於2023-06-06）.

statements: statement+

statement: compound_stmt | simple_stmts

……

block:

    | NEWLINE INDENT statements DEDENT

    | simple_stmts 

^ The Python Language Reference － 2. Lexical analysis － Keywords. [2020-09-26]. （原始內容存檔於2018-01-09）. 

^ What’s New In Python 3.0 － Overview Of Syntax Changes. [2023-02-18]. （原始內容存檔於2012-11-02）. 

^ What’s What’s New In Python 3.5 － New Keywords. [2016-06-01]. （原始內容存檔於2016-06-18）. 

^ What’s New In Python 3.7. [2019-11-21]. （原始內容存檔於2019-11-28）. 

^ The Python Language Reference － 2. Lexical analysis － Soft Keywords. [2023-03-03]. （原始內容存檔於2018-01-09）. 

^ PEP 8 – Style Guide for Python Code － Naming Conventions. [2017-10-06]. （原始內容存檔於2018-07-13）. 

^ The Python Language Reference － 2. Lexical analysis － Reserved classes of identifiers. [2023-03-03]. （原始內容存檔於2018-01-09）. 

^ 102.0 102.1 9.6. Private Variables. [2020-09-27]. （原始內容存檔於2012-10-23）. 

^ What’s New in Python 2.2 — Attribute Access. [2025-07-24]. （原始內容存檔於2021-02-07）. 

^ The Python Tutorial － 5. Data Structures － Tuples and Sequences. [2018-10-17]. （原始內容存檔於2020-06-10）. 

^ The Python Language Reference － 7. Simple statements － Augmented assignment statements. [2023-03-08]. （原始內容存檔於2023-06-06）. 

^ The Python Language Reference — Simple statements — Annotated assignment statements. [2026-07-07]. （原始內容存檔於2026-07-22）. 

^ The Python Language Reference － 7. Simple statements － The yield statement. [2023-03-15]. （原始內容存檔於2023-06-06）. 

^ The Python Language Reference － 6. Expressions － Yield expressions. [2023-03-15]. （原始內容存檔於2022-09-07）. 

^ PEP 342 － Coroutines via Enhanced Generators. [2019-11-21]. （原始內容存檔於2020-05-29）. 

^ PEP 380 － Syntax for Delegating to a Subgenerator. [2019-11-21]. （原始內容存檔於2020-06-04）. 

^ PEP 525 – Asynchronous Generators. [2023-03-16]. （原始內容存檔於2023-05-21）. 

^ 112.0 112.1 The Python Language Reference － 7. Simple statements － The import Statement. [2020-10-30]. （原始內容存檔於2021-02-07）. 

^ 113.0 113.1 113.2 The Python Tutorial － 6. Modules. [2020-10-30]. （原始內容存檔於2021-02-06）. 

^ What’s New In Python 3.11 － PEP 654: Exception Groups and except*. [2023-10-20]. （原始內容存檔於2023-06-13）. 

^ PEP 343 – The “with” Statement. [2020-09-26]. （原始內容存檔於2014-12-14）. 

^ The Python Language Reference － 5. The import system － Packages. [2023-03-07]. （原始內容存檔於2022-08-27）. 

^ 117.0 117.1 117.2 117.3 The Python Language Reference － 4. Execution model － Naming and binding. [2023-03-06]. （原始內容存檔於2022-09-08）. 

^ The Python Standard Library － Built-in Functions. [2020-09-25]. （原始內容存檔於2012-10-25）. 

^ The Python Standard Library － Python Runtime Services － __main__ — Top-level code environment. [2020-10-30]. （原始內容存檔於2021-02-07）. 

^ The Python Language Reference － 6. Expressions － Parenthesized forms. [2023-03-13]. （原始內容存檔於2022-09-07）. 

^ The Python Language Reference － 6. Expressions － Displays for lists, sets and dictionaries. [2023-03-13]. （原始內容存檔於2022-09-07）. 

^ Hettinger, Raymond. PEP 289 – Generator Expressions. Python Enhancement Proposals. Python Software Foundation. 2002-01-30 [2012-02-19]. （原始內容存檔於2020-06-14）. 

^ What’s New In Python 3.5 － PEP 448 － Additional Unpacking Generalizations. [2023-03-08]. （原始內容存檔於2016-06-18）. 

^ What’s New In Python 3.5 － PEP 465 － A dedicated infix operator for matrix multiplication. [2023-03-08]. （原始內容存檔於2016-06-18）. 

^ NumPy Reference － Routines － Linear algebra (numpy.linalg) － numpy.matmul. [2022-01-18]. （原始內容存檔於2022-04-10）. 

^ The Python Language Reference － 6. Expressions － Comparison. [2023-03-21]. （原始內容存檔於2022-09-07）. 

^ Brian Kernighan, Dennis Ritchie. The C Programming Language, Second Edition (PDF). Prentice Hall. 1988 [2023-03-23]. （原始內容存檔 (PDF)於2023-03-25）. The relational operators group left-to-right, but this fact is not useful; a<b<c is parsed as (a<b)<c, and evaluates to either 0 or 1. 

^ Equational derivations of the Y combinator and Church encodings in Python. [2020-10-21]. （原始內容存檔於2020-11-12）. 

^ Paul Krill, Guido Van Rossum. Guido van Rossum resigns: What’s next for Python. 2018-07-27 [2023-03-19]. （原始內容存檔於2023-03-19）. 

^ What’s New in Python 3.8 － Assignment expressions. [2023-03-08]. （原始內容存檔於2021-06-01）. 

^ The Python Language Reference － 6. Expressions － Assignment expressions. [2023-03-08]. （原始內容存檔於2022-09-07）. 

^ The Python Language Reference － 6. Expressions － Operator precedence. [2023-03-12]. （原始內容存檔於2022-09-07）. 

^ The Python Standard Library － Built-in Types － Common Sequence Operations. [2023-03-17]. （原始內容存檔於2020-06-14）. 

^ What’s New in Python 3.9 － Dictionary Merge & Update Operators. [2021-06-12]. （原始內容存檔於2020-10-07）. 

^ The Python Standard Library － Built-in Functions － round(), [2023-03-21], （原始內容存檔於2012-10-25） 

^ Guido van Rossum. Python Reference Manual － Version 1.2 (PDF). CWI Report CS-R9525. May 1995 [2023-03-04]. （原始內容存檔 (PDF)於2023-03-05）. The modulo operator always yields a result with the same sign as its second operand (or zero); …… The integer division and modulo operators are connected by the following identity: x == (x/y)*y + (x%y). 

^ PEP 327 – Decimal Data Type. [2015-09-26]. （原始內容存檔於2020-06-04）. 

^ The Python Standard Library － Numeric and Mathematical Modules － decimal — Decimal fixed point and floating point arithmetic. [2023-03-21]. （原始內容存檔於2023-06-13）. 

^ The Python Standard Library － Numeric and Mathematical Modules － fractions — Rational numbers. [2023-03-21]. （原始內容存檔於2023-05-26）. 

^ gmpy2 is an optimized, C-coded Python extension module that supports fast multiple-precision arithmetic. [2024-10-14]. （原始內容存檔於2024-12-19）. 

^ The Python Language Reference － 2. Lexical analysis － String literal concatenation. [2023-03-12]. （原始內容存檔於2018-01-09）. 

^ The Python Standard Library － Text Processing Services － string — Common string operations － Format String Syntax. [2023-03-21]. （原始內容存檔於2023-06-06）. 

^ The Python Standard Library － Built-in Types － printf-style String Formatting. [2023-03-21]. （原始內容存檔於2020-06-14）. 

^ PEP 498 － Literal String Interpolation. python.org. [2017-03-08]. （原始內容存檔於2020-06-15）. 

^ The Python Language Reference － 2. Lexical analysis － Formatted string literals. [2023-03-13]. （原始內容存檔於2018-01-09）. 

^ The Python Language Reference － 3. Data model － The standard type hierarchy. 

^ 147.0 147.1 PEP 484 -- Type Hints. [2021-03-01]. （原始內容存檔於2021-02-09）. 

^ Static Typing with Python. [2026-07-07]. （原始內容存檔於2026-07-10）. 

^ 149.0 149.1 mypy - Optional Static Typing for Python. [2017-01-28]. （原始內容存檔於2020-06-06）. 

^ Moshe Zadka, Guido van Rossum. PEP 237 － Unifying Long Integers and Integers. 2001-03-11. （原始內容存檔於2020-05-28）. 

^ The Python Tutorial － 15. Floating Point Arithmetic: Issues and Limitations. [2023-03-23]. （原始內容存檔於2023-06-02）. almost all platforms map Python floats to IEEE-754 「double precision」. 

^ The Python Standard Library － Built-in Types － Ranges. [2019-10-03]. （原始內容存檔於2020-06-14）. 

^ Python HOWTOs — Unicode HOWTO. [2025-07-11]. （原始內容存檔於2026-07-22）. 

^ NumPy fundamentals － Indexing on ndarrays － Dimensional indexing tools. [2023-03-23]. （原始內容存檔於2023-06-01）. 

^ The Python Standard Library － Built-in Types － The Null Object. [2023-03-24]. （原始內容存檔於2023-03-24）. 

^ functools — Higher-order functions and operations on callable objects — @functools.singledispatch. [2025-10-24]. （原始內容存檔於2021-06-02）. 

^ Glossary — closure variable. [2025-07-28]. （原始內容存檔於2020-06-25）. 

^ van Rossum, Guido. Language Design Is Not Just Solving Puzzles. Artima forums. Artima. 2006-02-09 [2007-03-21]. （原始內容存檔於2020-01-17）. the complexity introduced by a solution to a design problem must be somehow proportional to the problem's importance. …… Mathematicians don't mind these -- a proof is a proof is a proof, no matter whether it contains 2 or 2000 steps, or requires an infinite-dimensional space to prove something about integers. …… Features of a programming language, whether syntactic or semantic, are all part of the language's user interface. And a user interface can handle only so much complexity or it becomes unusable. This is also the reason why Python will never have continuations, and even why I'm uninterested in optimizing tail recursion. 

van Rossum, Guido. Tail Recursion Elimination. Neopythonic.blogspot.be. 2009-04-22 [2012-12-03]. （原始內容存檔於2018-05-19）. Once tail recursion elimination exists, developers will start writing code that depends on it, and their code won't run on implementations that don't provide it …… I don't believe in recursion as the basis of all programming. This is a fundamental belief of certain computer scientists, especially those who love Scheme and like to teach programming by starting with a "cons" cell and recursion. 

^ returns documentation — Trampolines. [2024-09-28]. （原始內容存檔於2024-12-23）. 

^ The Python Standard Library － Functional Programming Modules － functools — Higher-order functions and operations on callable objects. [2023-03-18]. （原始內容存檔於2021-06-02）. 

^ The Python Tutorial － 4. More Control Flow Tools － Defining Functions. [2023-03-06]. （原始內容存檔於2023-06-10）. 

^ PEP 3107 -- Function Annotations. [2021-03-01]. （原始內容存檔於2015-01-06）. 

^ The Python Standard Library — Data Types — weakref. [2026-07-15]. （原始內容存檔於2026-07-22）. 

^ PEP 3115 – Metaclasses in Python 3000. [2023-03-21]. （原始內容存檔於2023-04-02）. 

^ PEP 3119 – Introducing Abstract Base Classes. [2025-07-25]. （原始內容存檔於2026-07-11）. 

^ The Python Language Reference － 3. Data model － Customizing class creation. [2023-03-21]. （原始內容存檔於2012-10-26）. 

PEP 487 – Simpler customisation of class creation. [2023-03-21]. （原始內容存檔於2023-03-21）. 

^ Why must 'self' be used explicitly in method definitions and calls?. Design and History FAQ. Python Software Foundation. [2012-02-19]. （原始內容存檔於2012-10-24）. 

^ The Python Standard Library － Built-in Functions － class super. [2020-09-25]. （原始內容存檔於2018-10-26）. 

^ PEP 526 – Syntax for Variable Annotations. 

^ The Python Standard Library — Python Runtime Services — dataclasses. [2026-07-15]. （原始內容存檔於2026-01-30）. 

^ The Python Language Reference — Data model — Class instances. [2025-07-10]. （原始內容存檔於2022-09-08）. 

^ The Python Language Reference — Data model — Customizing attribute access. [2025-07-15]. （原始內容存檔於2022-09-08）. 

^ Descriptor HowTo Guide. [2020-09-26]. （原始內容存檔於2020-09-18）. 

^ The Python Standard Library － Built-in Functions － class property. [2020-09-25]. （原始內容存檔於2018-10-26）. 

^ The Python Standard Library. [2023-03-09]. （原始內容存檔於2023-06-06）. 

^ Python Interpreters Benchmarks. [2022-08-30]. （原始內容存檔於2022-08-20）. 

^ Python Bytecode Instructions. Docs.python.org. [2016-02-16]. （原始內容存檔於2020-06-05）. 

Python module to generate and modify bytecode. [2023-02-22]. （原始內容存檔於2023-04-04）. 

^ Obi Ike-Nwosu. Inside The Python Virtual Machine. [2023-01-29]. （原始內容存檔於2021-01-29）.  version 2019-03-02 (PDF). [2023-01-30]. （原始內容存檔 (PDF)於2023-03-05）.  中文翻译. [2023-01-30]. （原始內容存檔於2023-03-05）. 

^ The Computer Language Benchmarks Game. [2025-07-02]. （原始內容存檔於2026-01-10）. 

^ Glossary — global interpreter lock. [2023-09-19]. （原始內容存檔於2020-06-25）. 

^ Codon － A high-performance, zero-overhead, extensible Python compiler with built-in NumPy support. [2023-03-24]. （原始內容存檔於2023-05-25）. 

^ Rachel Gordon. Python-based compiler achieves orders-of-magnitude speedups. MIT CSAIL. 2023-03-14 [2023-03-25]. （原始內容存檔於2023-03-26）. 

^ Differences with Python. [2024-09-26]. （原始內容存檔於2023-05-25）. 

^ Application-level Stackless features. [2025-07-03]. （原始內容存檔於2026-03-10）. 

^ Pyodide is a Python distribution for the browser and Node.js based on WebAssembly. [2023-12-28]. （原始內容存檔於2024-04-03）. 

^ wgpy - WebGPU/WebGL accelerated numpy-compatible array library for web browser. [2026-07-11]. （原始內容存檔於2025-10-04）. 

^ RustPython — A Python Interpreter written in Rust. [2025-11-09]. （原始內容存檔於2026-06-21）. 

^ Brython (Browser Python) is an implementation of Python 3 running in the browser. [2023-06-17]. （原始內容存檔於2023-10-28）. 

^ GraalPy – A high-performance embeddable Python 3 runtime for Java. [2025-07-03]. （原始內容存檔於2026-06-24）. 

^ Simple Python Version Management: pyenv. [2026-07-06]. （原始內容存檔於2022-09-08）. 

^ Cython Users Guide — Using Parallelism. [2023-09-19]. （原始內容存檔於2023-10-11）. 

^ Mypyc compiles Python modules to C extensions. 

^ Nuitka is a Python compiler written in Python. [2023-09-18]. （原始內容存檔於2023-11-11）. 

^ Shed Skin is a restricted-Python-to-C++ compiler. [2025-07-03]. （原始內容存檔於2026-05-04）. 

^ Pythran － Ahead of Time compiler for numeric kernels. [2022-08-29]. （原始內容存檔於2022-08-29）. 

^ py2many: Python to many CLike languages transpiler. [2025-07-07]. （原始內容存檔於2026-05-09）. 

^ Grumpy is a Python to Go source code transcompiler and runtime. [2025-07-03]. （原始內容存檔於2020-04-15）. 

^ Pyston － A faster and highly-compatible implementation of the Python programming language. [2022-08-29]. （原始內容存檔於2022-08-29）. Pyston was started at Dropbox in 2014 ……. …… In 2017 …… Pyston project was shut down. …… In 2019 the Pyston developers regrouped ……. …… In mid-2021 the Pyston developers joined Anaconda ……. 

^ Transcrypt — Python 3.9 to JavaScript compiler - Lean, fast, open!. [2023-09-18]. （原始內容存檔於2023-09-19）. 

^ Pyjion － A JIT for Python based upon CoreCLR. [2022-08-29]. （原始內容存檔於2022-08-29）. 

^ CinderX is a Python extension that improves the performance of the Python runtime.. 

^ MyHDL － From Python to Silicon!. [2023-03-05]. （原始內容存檔於2023-06-05）. 

^ Tool recommendations. python.org. [2022-04-21]. （原始內容存檔於2022-09-06） （英語）. 

^ venv — Creation of virtual environments. [2023-05-07]. （原始內容存檔於2023-06-13）. 

^ virtualenv — A tool for creating isolated virtual python environments. [2023-05-07]. （原始內容存檔於2023-06-11）. 

^ Pipenv — Python Development Workflow for Humans. [2022-08-29]. （原始內容存檔於2019-11-17）. 

^ uv — An extremely fast Python package and project manager, written in Rust. 

^ FAQ: Django appears to be a MVC framework, but you call the Controller the “view”, and the View the “template”. How come you don’t use the standard names?. [2022-09-01]. （原始內容存檔於2022-09-02）. 

^ Asynchronous HTTP Client/Server for asyncio and Python. [2021-01-14]. （原始內容存檔於2021-01-15）. 

^ uvloop is a fast, drop-in replacement of the built-in asyncio event loop. [2023-03-24]. （原始內容存檔於2023-05-25）. 

^ PyGObject is a Python package which provides bindings for GObject based libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more. [2023-03-05]. （原始內容存檔於2023-06-07）. 

^ Dear PyGui: A fast and powerful Graphical User Interface Toolkit for Python with minimal dependencies. [2023-03-18]. （原始內容存檔於2023-05-18）. 

^ pywebview is a lightweight cross-platform wrapper around a webview component that allows to display HTML content in its own native GUI window. [2023-03-18]. （原始內容存檔於2023-05-06）. 

^ NumPy Fundamentals and usage — Broadcasting. [2023-09-20]. （原始內容存檔於2022-07-03）. The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is 「broadcast」 across the larger array so that they have compatible shapes. 

^ CuPy: NumPy & SciPy for GPU. [2022-08-31]. （原始內容存檔於2022-08-31）. 

^ NumKong: Mixed Precision for All. [2026-07-15]. （原始內容存檔於2026-06-24）. 

^ Autograd － Efficiently computes derivatives of numpy code. [2022-08-28]. （原始內容存檔於2022-07-18）. 

^ Cartopy — a cartographic python library with matplotlib support. [2026-07-07]. （原始內容存檔於2026-05-13）. 

^ DataFrame. [2022-09-01]. （原始內容存檔於2022-09-01）. DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. 

^ Python tools for data visualization — High-level tools. [2023-09-19]. （原始內容存檔於2023-09-28）. 

^ Modin: Scale your Pandas workflows by changing a single line of code. [2026-07-13]. （原始內容存檔於2026-07-04）. 

^ Python tools for data visualization. [2022-09-21]. （原始內容存檔於2024-05-04）. 

^ VisPy － interactive scientific visualization in Python. [2022-08-30]. （原始內容存檔於2022-07-13）. 

^ Datoviz: high-performance GPU rendering for scientific data visualization. [2026-02-23]. （原始內容存檔於2025-09-15）. 

^ seaborn: statistical data visualization. [2024-09-24]. （原始內容存檔於2020-12-03）. 

^ Vega-Altair: Declarative Visualization in Python. [2024-09-25]. （原始內容存檔於2025-02-02）. 

^ Bokeh — Interactive Data Visualization in the browser, from Python. [2023-09-19]. （原始內容存檔於2023-10-12）. 

^ plotly.py is an interactive, open-source, and browser-based graphing library for Python. [2024-09-24]. （原始內容存檔於2025-01-24）. 

^ Dash － Analytical Web Apps for Python, R, Julia, and Jupyter. [2022-09-21]. （原始內容存檔於2022-12-05）. 

^ Plotly.js － Open-source JavaScript charting library behind Plotly and Dash. [2022-09-21]. （原始內容存檔於2022-12-21）. 

^ Panel － A high-level app and dashboarding solution for Python. [2022-09-21]. （原始內容存檔於2023-01-16）. 

^ Using Panel in Pyodide & PyScript. [2025-07-03]. （原始內容存檔於2026-02-21）. 

^ HoloViz — High-level tools to simplify visualization in Python. [2023-09-19]. （原始內容存檔於2023-10-11）. 

^ Streamlit — The fastest way to build data apps in Python. [2022-09-21]. （原始內容存檔於2023-01-17）. 

^ Voilà － Voilà turns Jupyter notebooks into standalone web applications. [2022-09-21]. （原始內容存檔於2022-12-31）. 

^ Narwhals — Lightweight and extensible compatibility layer between dataframe libraries. [2026-07-13]. （原始內容存檔於2026-07-01）. 

^ Joblib: running Python functions as pipeline jobs. [2022-09-19]. （原始內容存檔於2022-12-07）. 

^ Thread-pool Controls. [2022-09-19]. （原始內容存檔於2022-11-02）. 

^ sklearn-onnx — Convert scikit-learn models and pipelines to ONNX. [2023-09-22]. （原始內容存檔於2023-10-11）. 

^ TensorFlow API Documentation － Module: tf. [2022-08-31]. （原始內容存檔於2022-09-05）. 

^ TensorFlow API Documentation － Module: tf.keras. [2022-08-31]. （原始內容存檔於2020-01-22）. 

^ JAX － Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more. [2022-08-28]. （原始內容存檔於2021-02-05）. 

^ XLA (Accelerated Linear Algebra) is an open-source compiler for machine learning. 

^ PEG parser generator for Python. [2023-02-22]. （原始內容存檔於2023-03-05）. 

Pablo Galindo Salgado. Guide to the Parser. [2025-11-08]. （原始內容存檔於2026-02-20）. 

Bryan Ford. The Packrat Parsing and Parsing Expression Grammars Page. [2023-04-18]. （原始內容存檔於2023-06-02）. 

^ llvmlite — A lightweight LLVM python binding for writing JIT compilers. [2024-09-21]. （原始內容存檔於2025-02-06）. 

^ xDSL is a Python-native compiler framework built around SSA-based intermediate representations (IRs). [2025-07-01]. （原始內容存檔於2026-06-30）. 

^ wgpu-py — A Python implementation of WebGPU. [2026-07-11]. （原始內容存檔於2026-06-28）. 

wgpu-native — Native WebGPU implementation based on wgpu-core. [2026-07-11]. （原始內容存檔於2026-07-15）. 

^ Pygfx — Powerful and versatile visualization for Python. [2026-07-10]. （原始內容存檔於2026-06-30）. 

^ fastplotlib — Next-gen fast plotting library running on WGPU using the pygfx rendering engine. [2026-07-11]. （原始內容存檔於2025-12-26）. 

^ tinygrad is an end-to-end deep learning stack. [2026-07-11]. （原始內容存檔於2026-07-04）. 

^ PyCUDA gives you easy, Pythonic access to Nvidia’s CUDA parallel computation API. [2022-05-29]. （原始內容存檔於2022-06-28）. 

^ PyOpenCL gives you easy, Pythonic access to the OpenCL parallel computation API. [2021-07-29]. （原始內容存檔於2022-03-08）. 

^ Kompute — General purpose GPU compute framework built on Vulkan to support 1000s of cross vendor graphics cards (AMD, Qualcomm, NVIDIA & friends). 

^ Dask － Parallel computing with task scheduling. [2022-08-31]. （原始內容存檔於2022-08-31）. 

^ Ray － Effortlessly scale your most complex workloads. [2022-09-19]. （原始內容存檔於2022-12-13）. 

^ Graphene — GraphQL framework for Python. [2023-12-20]. （原始內容存檔於2024-04-28）. 

^ GQL — A GraphQL client in Python. [2023-12-25]. （原始內容存檔於2024-04-24）. 

^ Pillow — Python Imaging Library (Fork). [2025-07-04]. （原始內容存檔於2026-07-08）. 

^ psutil is a cross-platform library for retrieving information about running processes and system utilization (CPU, memory, disks, network, sensors) in Python. 

^ Fabric － Pythonic remote execution. [2013-04-08]. （原始內容存檔於2014-04-11）. 

^ python filesystem spec — data storage IO layer for python. 

^ pygame - Community Edition is a FOSS Python library for multimedia applications (like games). Built on top of the excellent SDL library. 

^ SDL3 Language Bindings. 

^ SimPy — Discrete event simulation for Python. [2023-08-17]. （原始內容存檔於2016-12-12）. 

^ CUDA Python Manual. [2022-08-30]. （原始內容存檔於2022-08-30）. 

^ opencv-python — Automated CI toolchain to produce precompiled opencv-python, opencv-python-headless, opencv-contrib-python and opencv-contrib-python-headless packages. 

^ Polars: Extremely fast Query Engine for DataFrames. 

^ LSB — Runtime Languages — Python Interpreter. [2023-06-16]. （原始內容存檔於2016-05-01）. The default installed Python version shall be 2.4.2 or greater. 

^ pipx — Install and Run Python Applications in Isolated Environmentspipenv. [2023-05-07]. （原始內容存檔於2023-06-05）. 

^ XONSH is a Python-powered shell. [2022-08-28]. （原始內容存檔於2022-09-03）. 

^ Data Mining Fruitful and Fun － Open source machine learning and data visualization. Build data analysis workflows visually, with a large, diverse toolbox.. [2023-06-14]. （原始內容存檔於2023-06-06）. 

^ Mayavi: 3D scientific data visualization and plotting in Python. [2023-09-20]. （原始內容存檔於2023-10-11）. 

^ Netron — Visualizer for neural network, deep learning and machine learning models. [2026-07-15]. （原始內容存檔於2026-07-09）. 

^ Kornia － Open Source Differentiable Computer Vision Library. [2022-09-22]. （原始內容存檔於2023-01-10）. 

^ spaCy: Industrial-strength NLP. [2023-09-22]. （原始內容存檔於2023-10-11）. 

^ Thinc: A refreshing functional take on deep learning, compatible with your favorite libraries. 

^ Transformers — State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX. [2023-10-19]. （原始內容存檔於2023-09-27）. 

^ Gradio: The New Frontier in Interactive Python Data Apps. [2023-12-22]. （原始內容存檔於2023-12-22）. 

^ Python library for easily interacting with trained machine learning models https://pypi.org/project/gradio/ （頁面存檔備份，存於網際網路檔案館）

^ Buniatyan, Davit. Code Understanding Using LangChain. Activeloop. 2023 [2023-12-22]. （原始內容存檔於2023-12-16）. 

^ Taichi — Productive, portable, and performant GPU programming in Python. [2025-01-23]. （原始內容存檔於2025-01-09）. 

^ Coconut — Simple, elegant, Pythonic functional programming. [2024-09-27]. （原始內容存檔於2025-01-20）. 

^ Snek — a tiny python-inspired language for embedded computing. [2025-07-07]. （原始內容存檔於2026-03-02）. 

^ Pycopy aims to develop and maintain a minimalist, lightweight, and extensible implementation of Python(-compatible) language. [2025-10-23]. （原始內容存檔於2026-04-22）. 

^ pyastinterp — Python AST interpreter (aka tree-walking interpreter) in Python. Aka meta-circular interpreter. [2025-10-23]. （原始內容存檔於2022-12-25）. 

延伸閱讀
[編輯]

John DeNero. Composing Programs, a free online introduction to programming and computer science. [2020-10-09]. （原始內容存檔於2021-01-28）. 

Allen B. Downey. Think Python: How to Think Like a Computer Scientist - Third Edition. Green Tea Press. 2024 [2025-12-08]. ISBN 978-1098155438. （原始內容存檔於2026-07-12）. 

Luciano Ramalho. Fluent Python (2nd ed.). O'Reilly Media. 2022 [2025-12-08]. ISBN 978-1-4920-5632-4. （原始內容存檔於2024-04-20）. 

Raphaël Monat. Static Type and Value Analysis by Abstract Interpretation of Python Programs with Native C Libraries (PDF). PhD thesis, Sorbonne Université. 2021 [2025-12-08]. （原始內容存檔 (PDF)於2025-08-08）. 

參閲
[編輯]

電腦程式設計主題

自由軟體主題

程式語言列表

Python語法及語義

Python的歷史

Python軟體列表（英語：List of Python software）

外部連接
[編輯]

Python在維基百科的姊妹計畫

維基共享資源上的多媒體資源

維基語錄上的名言

維基教科書上的教科書和手冊

維基學院上的學習資源

官方網站

Awesome Python （頁面存檔備份，存於網際網路檔案館）

Real Python Tutorials （頁面存檔備份，存於網際網路檔案館）

programingz － Learn Python Programming （頁面存檔備份，存於網際網路檔案館）

w3schools － Python Tutorial （頁面存檔備份，存於網際網路檔案館）

ItsMyCode－ Learn Python Programming （頁面存檔備份，存於網際網路檔案館）

Codecary － Learn Python Programming （頁面存檔備份，存於網際網路檔案館）

dainikchorcha － Learn Python Programming（頁面存檔備份，存於網際網路檔案館）

Tutlane - Learn Python Online （頁面存檔備份，存於網際網路檔案館）

Brmgha - Learn & Challenges Python Online （頁面存檔備份，存於網際網路檔案館）

AlmaBetter- Python Tutorial （頁面存檔備份，存於網際網路檔案館）

閱

論

編
Python

實作

CircuitPython（英語：CircuitPython）

CLPython（英語：CLPython）

CPython

Cython

Jython

IronPython

MicroPython

Numba

PyPy

Python for S60（英語：Python for S60）

Psyco

Stackless Python

Shed Skin（英語：Shed Skin）

Unladen Swallow

更多……

IDE

Boa

Eclipse

Eric Python IDE

IDLE

SPE（英語：Stani's Python Editor）

Ninja-IDE

PyCharm

PyDev（英語：PyDev）

Aptana（英語：Aptana）

更多……

專題

WSGI

ASGI（英語：Asynchronous Server Gateway Interface）

軟體列表

Python軟體基金會

PyCon

閱

論

編
程式語言

範式分類

程序式

FORTRAN

COBOL

JOVIAL

ALGOL 60

JOSS（英語：JOSS）

BASIC

PL/I

MUMPS

ALGOL 68

Pascal

C

Modula-2

Ada

Go

物件導向

Simula 67

Smalltalk

Objective-C

Eiffel

Object Pascal

Self

Visual Basic

Java

C#

Crystal（英語：Crystal (programming language)）

多範式

C++

Modula-3

Fortran 90

Python

Ada 95

JavaScript

Nim

Rust

Swift

Zig

V（英語：V (programming language)）

Mojo

函數式

LISP

Scheme

Common Lisp

Clojure

Logo

APL/J

ML

Standard ML

OCaml

Erlang

Haskell

Futhark

Gleam（英語：Gleam (programming language)）

邏輯式

Prolog

Datalog

Mercury

AnsProlog

ProbLog（英語：ProbLog）

手稿語言

動態語言

SNOBOL

Forth

Icon

AWK

Perl

CLOS

Tcl/Tk

Python

Lua

Ruby

PHP

REBOL

Factor

jq

外殼指令碼

Unix shell

sh/ash/dash

csh/tcsh

ksh

bash

zsh

PowerShell

前端指令碼

ECMAScript/JavaScript

Dart

TypeScript

PureScript

Reason

特定平台

.NET

C#

C++/CLI

F#

VB.NET

Small Basic

JVM

Java

AspectJ（英語：AspectJ）

Scala

Clojure

Groovy

Kotlin

特定領域

科學計算

Speakeasy（英語：Speakeasy (computational environment)）

IDL/GDL

Maxima

Maple

MATLAB

Octave

Scilab

Wolfram

R

SageMath

Julia

GPU計算

Cg/HLSL

GLSL/GLSL ES

CUDA/PTX（英語：Parallel Thread Execution）

OpenCL/SPIR-V（英語：Standard Portable Intermediate Representation）

WGSL（英語：WebGPU Shading Language）

資料查詢

SQL

PL/SQL

T-SQL

SQL/PSM（英語：SQL/PSM）

xBase（英語：xBase）

XPath

XQuery（英語：XQuery）

GraphQL

視覺化

Flowchart

Simulink

LabVIEW

Orange（英語：Orange (software)）

KNIME（英語：KNIME）

Scratch

Snap!

App Inventor

Power Fx

傳媒設計

SuperCollider

Pure Data

AviSynth

Processing

ChucK

其它語言

Assembly

Plankalkül

APT（英語：APT (programming language)）

GPSS（英語：GPSS）

ISWIM

dc

occam

XSLT

LLVM IR

WebAssembly

Esolang

目錄

列表

按類型排列（英語：List of programming languages by type）

歷史

比較（英語：Comparison of programming languages）

時間線

閱

論

編
Python web框架

BlueBream

Bottle

CherryPy

CubicWeb（英語：CubicWeb）

Django

FastAPI

Flask

Grok（英語：Grok (web framework)）

Nevow（英語：Nevow）

Paste（英語：Python Paste）

Pylons

Pyramid

Quixote

Spyce（英語：Spyce (software)）

TACTIC

Tornado

TurboGears

web2py

Zope 2

框架比較

閱

論

編
Python科學軟體

NumPy

SciPy

matplotlib

pandas

scikit-learn

scikit-image（英語：scikit-image）

MayaVi（英語：MayaVi）

更多

閱

論

編
可微分計算

概論

可微分程式

自動微分

張量微積分

資訊幾何

統計流形

神經形態工程（英語：Neuromorphic engineering）

模式辨識

運算學習理論（英語：Computational learning theory）

歸納偏置

概念

梯度下降

SGD（英語：Stochastic gradient descent）

聚類

回歸

過適

注意力

卷積

損失函式

反向傳播

激勵函數

softmax

sigmoid

ReLU

正則化

資料集

擴散（英語：Diffusion process）

自回歸

應用

機器學習

類神經網路

深度學習

科學計算

人工智慧

語言模型

大型語言模型

硬體

TPU

VPU

IPU（英語：Graphcore）

憶阻器

SpiNNaker（英語：SpiNNaker）

軟體庫

Theano

TensorFlow

Keras

PyTorch

Caffe

JAX

MindSpore（英語：MindSpore）

Flux.jl（英語：Flux (machine-learning framework)）

主題

電腦程式

技術

分類

類神經網路

機器學習

閱

論

編
自由及開放原始碼軟體

常見概念與條目	自由軟體及其定義、其他稱謂（英語：Alternative terms for free software） · 與封閉原始碼的比較（英語：Comparison of open source and closed source） · 開源軟體及其開發（英語：Open-source software development） · 自由軟體代管服務比較 · 自由軟體專案列表（英語：List of free software project directories）與軟體列表 · 「免費」與「自由」的差別（英語：Gratis versus libre） · 長期支援 · 自由軟體大綱（英語：Outline of free software）

作業系統（核心）	AROS Research Operating System（英語：AROS） · BSD · Darwin · FreeDOS · GNU Hurd · Haiku · Inferno · Linux · Mach · Minix · OpenSolaris · Plan 9 · ReactOS · Symbian · 開源鴻蒙

軟體列表	軟體開發（英語：Comparison of open-source programming language licensing） · 生物資訊學（英語：List of open-source bioinformatics software） · 數學（英語：List of open-source software for mathematics） · 文書處理軟體 · 音訊（英語：Comparison of free software for audio） · 商業軟體（英語：List of commercial open-source applications and services）

歷史與運動	GNU · Haiku · Linux · Mozilla (Application Suite · Firefox · Thunderbird) · 自由軟體運動 · 開源軟體運動（英語：Open-source software movement） · 大事記（英語：List of free-software events）

組織（英語：List of free and open-source software organizations）與社群	Android開源專案 · Apache軟體基金會 · Blender基金會 · Eclipse基金會 · freedesktop.org · 自由軟體基金會 (歐洲 · 印度 · 拉丁美洲) · FSMI · GNOME基金會 · GNU Project · Google Code · KDE e.V. · Linux基金會 · Mozilla基金會 · 開源地理空間基金會 · 開放原始碼促進會 · SourceForge · Symbian基金會 · VideoLAN組織 · 維基媒體基金會 · Xiph.Org基金會 · XMPP標準基金會  · X.Org基金會  · 文件基金會 · 軟體自由法律中心  · 開放原子開源基金會

授權條款

Apache

AFL

Artistic

APSL

Boost

BSD

自由軟體基金會

GNU GPL

GNU LGPL

GNU AGPL

ISC

MIT

MPL

Python

Python軟體基金會授權條款

zlib

WTFPL

反996授權條款

類型與標準

自由及開放原始碼軟體授權條款比較

貢獻者授權條款協定（英語：Contributor License Agreement）

Copyleft

Debian自由軟體指導方針

自由文化作品定義

自由授權條款（英語：Free license）

自由軟體定義

開源定義

寬鬆自由軟體授權條款

公有領域

Viral license（英語：Viral license）

挑戰	FUD · 擁抱、擴充功能再消滅 · 二進制blob · 數位版權管理 · 自由及開放原始碼顯示卡驅動程式（英語：Free and open-source graphics device driver） · 授權擴散（英語：License proliferation）  · Mozilla 軟體品牌重塑（英語：Mozilla Corporation software rebranded by the Debian project） · 專有軟體 · SCO-Linux爭議 · 安全性 · 軟體專利 · 硬體限制 · 可信計算 · 對 GPL 的有關批評

其他	Linux發行版 · 分叉 (軟體開發) · 微軟開放規範承諾（英語：Microsoft Open Specification Promise） · 共享原始碼 · 《作業系統革命》

分類 · 維基共享資源 · 主題

權威控制資料庫

國際

FAST

各地

法國

BnF data

德國

以色列

美國

捷克

其他

IdRef