# 遊戲腳本位於此檔案。

# 聲明該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define z = Character("張生")
define white = Character("旁白")
define y = Character("鶯鶯")
define zf = Character("鄭婦")
define r = Character("紅娘")
define aaa = Character("？？？", color="#FF0000")
define li = Character("梁倡瑋", color="#FF0000")
define n1 = Character("評審1")
define n2 = Character("余濤大師")
define dan = Character("但丁")
define chan = Character("成振宇")
define gob = Character("歌殺")
define dra = Character("美式山海經推銷員")

# 遊戲從這裡開始。
transform slightly_higher:
    ypos 0.75  # 比預設的 1.0 再高一點（0 是畫面頂部，1 是底部）

label start:

    # 顯示背景。 預設情況下，它使用佔位符，但您可以
    # 將檔案（名為 "bg room.png" 或 "bg room.jpg"）新增至
    # images 目錄來顯示它。

    scene bg

    # 這顯示了一個角色精靈。 使用了佔位符，但您可以
    # 透過將名為 "eileen happy.png" 的檔案
    # 新增至 images 目錄來取代它。

    # 這些顯示對話行。

    white "唐貞元中，有張生者，性溫茂，美風容，內秉堅孤，非禮不可入。\n
    (而現在你就是張生，你會做什麼選擇呢?)
    "
    show char3 at left, slightly_higher
    white "這一日，你游去蒲州，蒲州向東十餘里，有一座寺廟，喚作{color=#FF0000}普救寺{/color}。"
    hide char3
    menu:
        "這時你選擇......"
        "「不遊覽了，興盡而返」":
            jump end1
        "「住進普救寺」":
            jump story1

    # 遊戲結束。

    return

label end1:
    hide char3
    white "故事還未開始就結束了，張生沒有遇見崔鶯鶯，獨自去了京城考試。"
    white "會遇到元稹，但這時他也不會有過往情事可以向元稹說嘴，元稹\n也做不出{color=#FF0000}會真詩三十韻{/color}。"
    white "也許是因為張生的內秉堅孤，他在最後臨死前喃喃著\n「餘真好色者，而適不我值。」"
    window hide
    scene gameover1
    with Pause(2.0)
    window show
    "如果某一日他能看見來自異世界的鶯鶯傳會發現自己原來這麼渣，\n恭喜獲得結局{color=#FF0000}「孤老終生-打了一輩子的光棍還在適不我值」{/color}"
    return
    
label story1:
    scene bg1
    hide bg
    show char3 at left, slightly_higher
    show char5 at right, slightly_higher
    white "這日清晨，煙雨濛濛，你向寺裡的高僧道了聲謝。"
    hide char5
    hide char3
    show clothes under the sun at truecenter
    show char3 at right, slightly_higher
    white "便去附近的河邊洗漱，你在離開寺廟前看見了外邊曬著女子的衣物\n，但那時並沒有多想。"
    hide char3
    hide clothes under the sun
    show char3 at left, slightly_higher
    show char5 at right, slightly_higher
    white "回來早膳，你食完素齋後向這裡的僧侶一問，才得知\n{color=#FF0000}「有崔氏孀婦，將歸長安，路出於蒲，亦止茲寺」{/color}。"
    hide char3
    hide char5
    hide bg1
    show bg6
    white "道了幾聲原來如此啊！便外出遊歷蒲州，向晚而歸。"
    scene bg4
    show bg5 at truecenter
    hide bg6
    white "到了晚上將睡時，你聽聞隔壁房中有兩位女性的談話聲，\n一者稍老，一者為幼。"
    menu:
        "這時你心想......"
        "「明天去認識看看，究竟是何許人也」":
            jump story2
        "「算了，還是無須有所交集」":
            jump end1
    return

label story2:
    scene bg3
    hide bg1
    hide char3
    white "明日一早，張生已洗漱完畢回去寺中，恰好見到了崔氏遺孀，\n乃是她甫用膳完畢，正要走進廂房。"
    scene bg2
    hide bg3
    show char3_1 at left, slightly_higher
    show char4 at right, slightly_higher
    white "此時張生與崔氏婦正好互相瞧見，張生向她招了招手。"
    hide char3_1
    show char3 at left, slightly_higher
    z "我想說怎麼有女孩子的衣物在外曬著呢？"
    hide char4
    show char4_1 at right, slightly_higher
    zf "公子你好，沒想到寺中還有其他人宿著，我們是要去長安的，\n暫住於此。"
    hide char4_1
    hide char3
    white "他們兩人一番交談得知\n{color=#FF0000}「崔氏婦，鄭女也；張出於鄭，緒其親，乃異派之從母」{/color}"
    window hide
    show bg4
    show bg7 at shrink_bg
    hide bg2
    with Pause(2.0)
    white "是歲，鎮守蒲州的將領渾瑊甫亡，宦官丁文雅不善用兵，\n故軍不領旨，四處趁喪而亂，奪蒲州百姓之金銀。"
    white "而當時蒲州有名的大家崔家，財產甚厚，又有諸多奴僕，\n雖暫居於普救寺，但覺惶恐不安，不知所措。"
    show bg8 
    hide bg7
    "而你，張生，與蒲將之黨認識，此時你會選擇......"
    menu:
        "而你，張生，與蒲將之黨認識，此時你會選擇......"
        "「請吏護之，遂不及於難」":
            jump story3
        "「不鳥崔家的狗屁事」":
            jump end2
    return

transform shrink_bg:
    zoom 0.8  # 將圖縮小為 80%
    xpos 0.5
    ypos 0.5
    anchor (0.5, 0.5)  # 以畫面中心為基準點顯示

label end2:
    hide char3
    hide char4
    white "崔氏被兵所擾，直至家道中落，後張生入京趕考，結識元稹，\n但崔家一事聽其母親說過，尤為遺憾。"
    window hide
    scene gameover2
    with Pause(2.0)
    window show
    show gameover2
    "在京城娶了一女，一生汲汲營營，沒有什麼功過。\n恭喜獲得結局{color=#FF0000}「中庸之輩-一輩子什麼大事都沒幹，死了連渣都不剩」{/color}"
    return

label story3:
    scene bg10
    hide bg8
    white "過了十多天後，廉使杜確奉天子之命，來主持戎節，\n重新下令軍隊，平定軍亂。"
    menu:
        "鄭婦邀請你去她家坐坐，你是否要去？"
        "推辭":
            jump isekai
        "赴宴":
            pass
    show bg4
    show bg9
    hide bg10
    show char3 at left, slightly_higher
    show char4 at right, slightly_higher
    white "鄭厚張之德甚，遂飾饌邀請張生前來，在中堂宴飲。\n\n{color=#FF0000}中堂{/color}：三進院落中，室內必有中堂，一般置兩高几、一條案、兩太師椅，\n再配個八仙桌，意指一家的四平八穩、中正平和。"
    show char4_2 at right, slightly_higher
    hide char4
    zf "我只是個未亡人，帶著幼兒們，卻不幸遇上了兵亂，自己都難以保身，\n我還有那些尚還年幼的兒女們，而正因為你讓他們都活了下來，\n這豈是平凡的恩情所能比擬的？今天我就讓他們以仁兄之禮拜見，\n冀以報您的恩情！"
    show char4 at right, slightly_higher
    hide char4_2
    show char6 at truecenter
    white "鄭婦喚來她的兒子歡郎，年約十餘歲，容甚溫美。"
    hide char6
    hide char3
    hide char4
    show bg12
    white "接著又喊她的女兒出來，說：「快點兒出來拜見妳的兄長，\n兄長對妳可是有救命之恩。」"
    show bg13
    hide bg12
    white "然而，女子久處於閨中不出，以病推辭。"
    show bg4
    show bg9
    hide bg13
    show char4_3
    zf "是張兄救妳的命，不然妳早被擄去做壓寨夫人了，哪還能像\n現在用病推辭呢？"
    window hide
    show bg11
    with Pause(2.0)
    window show
    white "過了一段時間後，一位女子方出閨，穿著一身常服，面容姣好，\n沒有用新妝粉飾。香鬟垂落於眉旁，臉上銷紅沉韻，面上未抹脂粉\n，卻若光輝動人。"
    white "張生頓時感到驚訝，急忙對她行禮，女子則坐於鄭婦旁。"
    white "由於是鄭婦強迫著她出來的，只見她斜視凝望著門戶，\n看起來內心有些怨懟，心思也不在此處。"
    menu:
        "此時你說道......"
        "「初次見面，不知姑娘芳齡？」":
            show char4_4 at right, slightly_higher
            zf "天子甲子歲之七月，到了現在貞元庚辰年，如今她已經十七\n有餘了！"
        "「我可以娶妳嗎？」":
            show char4_4 at right, slightly_higher
            zf "公子你要先納個採、問個名，我會考慮一下的。"
        "「妳就是崔鶯鶯嗎？我是來自2025年的穿越者，我是妳的大粉絲，可以跟妳要個簽名嗎？」":
            show char4_5 at right, slightly_higher
            zf "大粉絲是什麼碗糕嗎？2025年是什麼？我記得現在不是貞元庚辰年嗎？"
    show char4 at right, slightly_higher
    hide char4_3
    hide char4_4
    hide char4_5
    show char4 at left, slightly_higher
    show char2 at right, slightly_higher
    show bg4
    show bg9
    hide bg11
    zf "這是我的女兒鶯鶯。"
    white "你多次尋找話題未果，鶯鶯始終看著門窗。鄭婦看著兩人\n沒怎麼對到電波，就準備要結束宴會。"
    show char4_1 at left, slightly_higher
    show char3 at right, slightly_higher
    hide char4
    hide char2
    zf "好吧，公子我們今天宴會就先到這裡結束了，下次有約再相見。"
    hide char4_1
    hide char3
    show bg4
    show bg19
    white "你從此念念不忘，茶思飯想，每當睡前鶯鶯的神情總在你的腦海\n裡浮現，數次想去找鶯鶯。\n{color=#FF0000}（那你怎麼不去，有色心沒色膽，內秉堅孤的膽小鬼！）{/color}"
    white "身為一個好旁白，我給各位一個機會，你會怎麼選擇呢？"
    menu:
        "身為一個好旁白，我給各位一個機會，你會怎麼選擇呢？"
        "「去找紅娘」":
            jump story4
        "「直接衝去找鶯鶯」":
            jump specialend1
    return

label story4:
    show bg17
    "崔之婢女紅娘，一個可愛的小女孩。"
    menu:
        "崔之婢女紅娘，一個可愛的小女孩。"
        "「見色心起」":
            jump end3
        "「訴其心事」":
            pass
    show bg18
    white "人家一個小丫鬟，聽到你對鶯鶯如此壓迫感十足的愛意，直接羞而\n逃走了。"
    show bg20
    white "你也感到自己的確實有些唐突，隔日你向紅娘羞愧的說了抱歉，不再相求。"
    scene bg21
    show char3 at left, slightly_higher
    show char8 at right, slightly_higher
    r "公子您的心事我是不敢告知小姐的，也不敢洩漏給別人。但以公子對崔家\n的恩情，不就是一紙婚書的事嗎？"
    show bg22
    hide char3
    hide char8
    z "我自孩提時期，性情就是不苟合，在眾花叢中不尋一芳，莫曾流盼。\n當時不曾所為的事，自然是無法跨過內心裏的疙瘩，去表明自己\n的心意。"
    show bg23
    z "昨日於中堂宴中，遇見鶯鶯，我整日無法自持。走路時會忘記路邊\n的花草，以及因何而走的目的；吃飯時每每肉糜下肚，卻仍覺空腹。如果再\n不說出去的話我待會就死給妳看。"
    window hide
    show bg4
    show bg24:
        zoom 0.9
    with Pause(3.0)
    window show
    show char3 at left, slightly_higher
    show char8 at right, slightly_higher
    z "況且透過媒人娶親，需經過納采問名，則需三個月過去才有著落，\n到那時你不如去賣鹹魚的市集內找看看我吧！其中一條或許就是我，\n妳說說看我能如何是好？"
    show bg25
    r "我們家小姐性情守貞自保，即使親密如我，尊重如母，也不可以\n用是非閒話驚擾她，她會炸毛的。所以公子托我去跟小姐\n說，那更是不可能的。"
    show bg26
    r "但小姐善屬文，時常沉吟詩篇，更是怨慕詩中情愛久矣！\n如果公子可以的話，可以寫些情詩亂小姐的心境，不然的話，\n以小姐的性情再無其他方法。"
    show bg27
    white "怕大家看不懂，前面再說崔鶯鶯喜歡躲房間聽情歌，紅娘建議張生\n可以寫一首《有點甜》。"
    show bg28
    white "你聽到後眉眼見笑，趕緊寫了春詞兩首交付紅娘。是夕，紅娘拿了\n一張彩箋出來。"
    show bg29
    r "是小姐要我給你的。"
    window hide
    show poem2 at truecenter:
        zoom 1.5
    with Pause(3.0)
    white "只見紙箋一翻開，寫上＜明月三五夜＞，署名鶯鶯。"
    hide poem2
    show bg30
    white "你一見字所述，微喻其旨。是夕，當二月十四日時，在鶯鶯閨房\n東向，有杏花一株，恰好攀上它可以越牆。"
    show bg31
    white "在陰曆既望之時，月圓當空，以杏樹為梯，扶牆而逾。"
    show bg32
    white "到達西廂房後，只見門戶半開，此時紅娘躺在床上。"
    r "公子你怎麼來這？"
    z "鶯鶯信箋召我來此，替我告知一下。"
    show bg33
    white "沒過多久，紅娘出來喊著來了來了，只見你既開心又害怕，\n認為此次可謂獲濟。"
    show bg34
    white "只見崔大小姐來到，她穿著端莊素雅，面容嚴肅，開始大聲數落。"
    show bg35
    show char3 at right, slightly_higher
    show char2_1 at left, slightly_higher
    y "兄長對我們有恩德，因此母親介紹我們兄妹倆與你認識。但你為\n何叫不令之婢，致我淫逸之詞。"
    show char3_2 at right, slightly_higher
    hide char3
    y "剛開始你護我們家於危難中，是『義』，但開始乘危亂後相求，\n這不是以義相求，這是以亂易亂。{color=#FF0000}用你曾經的恩情配上壞心思去趁機\n挾取需索，你與兵亂根本相差無幾！{/color}"
    y "想要睡我，然後用保護人這種大義的方式去求取讓你奸我，{color=#FF0000}這是『不義』\n不是義。{/color}若我直接上告這件事給母親，則會被媽媽罵辜負人\n家的恩惠，這是『不祥』。想說讓婢女直接轉告我的想法，又怕這樣不\n夠真誠。"
    y "所以我寫了這篇詩，希望可以表達出來。但又怕兄長你不懂，\n所以我寫了些露骨的鄙靡之詞，這樣你就會自以為懂的就過來了。"
    show char3_3 at right, slightly_higher
    hide char3_2
    y "唉！如果你有用禮約束自己，這樣就不會心中有愧了。我希望\n這樣念叨過兄長，可以用禮束縛著自己，不要再以亂易亂了！"
    hide char2_1
    show bg36
    white "我覺得你各位應該需要旁白我，上面在講：TM的！你個垃圾，\n假癡情，沒禮教的死王八羔子。\n{color=#FF0000}(咳咳，抱歉本我露出。){/color}"
    show bg37
    white "沒有啦，以上是鶯鶯想聽《有點甜》，但張生用唱三民主義的調來唱，\n所以鶯鶯很氣。為什麼不要把調練好再過來，只會想著自己，然後私自\n傳封Email，卻不會自己走過來敲門自彈自唱嗎？"
    show bg38
    white "說完後，鶯鶯也就離開了。你失魂甚久，最後只好拖著疲憊的身軀\n翻過牆，用頭撞了撞杏樹，帶著髮梢上無處可逃的落葉片子，踩著\n蹣跚的步伐回家了。"
    show bg39
    white "數個夜晚，你倚著窗，窗前獨唱著{color=#FF0000}如願中的「而我將愛你所愛的人間 \n願你所願的笑顏」{/color}方唱罷，眼光忽滅，視線模糊了起來，欲要闔上\n小眼珠子打個盹。"
    scene bg4
    show bg40
    white "突然一個人拿著枕頭往你臉上拷過去，你昏昏迷迷間，看見的是一個人\n，你趕緊定睛一看，發現正是紅娘。"
    r "沒事了，沒事了，先別睡覺了。"
    show bg41
    white "只見紅娘，把枕頭在你家擺好排整齊，將衾鋪成後就走了。而你趕緊揉\n了揉眼睛，危坐起身反覆猶疑，懷疑自己仍處在夢寐之中，但還是修謹\n自身。確認看看領帶有沒有鬆，不對這時是確認衣冠正不正。確認完後\n，你就端坐著不敢亂動。"
    scene bg4
    show bg43
    white "不久後，紅娘攙扶著鶯鶯走進來，{color=#FF0000}『侍兒扶起嬌無力』{/color}潤紅中帶點羞赧，\n像是青蘋果最後也熟紅，想用力支楞著嬌軀時卻有些無力的頹軟下。"
    show bg44
    white "像嬌媚的柔骨臥在紅娘的攙扶裡，只見她的丹青眉微皺，眼緣綴著一滴\n嬌憐淚，那是個與以往端莊模樣完全相異的她。"
    show bg45
    white "將晚是夕，月十八日，斜掛的月晶瑩，皎潔的白光照著幽床半張。"
    white "你的身體恍若神仙飄去，{color=#FF0000}不是啊！底下十八禁要不要描啊！我描一點好了，不要說我色。{/color}"
    show bg46
    white "{color=#FF0000}樹欲搖因風不止，鳥欲鳴因枝椏所眷{/color}，相連為枝，風勢忽大，\n乃樹大搖而枝頭葉晃，響響如鈴，間於心緒。\n枝立而壓雀身，雀嬌而媚嗔，千囀啁啾，胭脂粉塵輕抹枝椏，\n一口唾沫，{color=#FF0000}兩抹暗紅落枝頭。{/color}"
    white "輕描淡寫，不對，這一部沒有十八禁標籤，所以點到為止。"
    show bg47
    white "雞鳴，寺鐘鳴響，天將曉了。紅娘催促著鶯鶯，鶯鶯此時嬌聲\n婉轉，啼哭生憐，紅娘趕緊攙扶著她，最終鶯鶯一夕無言。"
    show bg48
    z "我不是在做夢吧？"
    white "及明，你睹舊妝鉛粉尚留臂中，暗香滿盈衣袖，晶瑩的淚珠尚留床席。\n此後十餘天，杳不復知鶯鶯消息。"
    show bg49
    white "你寫了會真詩，但尚未做完，就讓紅娘捎去給了鶯鶯。"
    show bg50
    white "此後一個月，你倆關係賊好的，朝時偷偷出門，將暮時偷偷回家，\n一同相約於此前西廂之所。"
    show bg51
    menu:
        "你突然有一天狼性大發，有了一個想法？"
        "「去做」":
            jump end4
        "「不，我要抑制狼性」":
            pass
    show bg52
    white "你每次事畢都會問一次鄭姨的看法，但鶯鶯總說，我不可奈何！"
    menu:
        "你就想去跟鄭姨說，但你已然到要入長安的時候了，此時有兩個選項......"
        "「去告訴鄭姨」":
            jump tell_zheng
        "「選擇去長安」":
            jump story5
    return

label tell_zheng:
    show char2 at right, slightly_higher
    y "沒關係的，我會去說的......"
    hide char2
    menu:
        "「義無反顧地去找鄭姨。」":
            jump specialend1
        "「還是算了，聽鶯鶯的話。」":
            jump story5
    return

label end4:
    show bg42
    window hide
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「后宮王-你的姿色未減，仍是一條好漢」{/color}"
    return

label story5:
    show bg53
    white "不久後，你選擇去了長安，將想法告訴鶯鶯後，鶯鶯並未為難你什麼\n，但她愁怨的眸光卻瞞不住你。"
    white "要走的前一個晚上，鶯鶯沒有再來。你就這樣去往了長安。"
    show bg54
    white "數月後，張生回到蒲州，在崔家住了幾個月。"
    show bg55
    white "人們總說崔家小姐出眾，藝是頂尖的，但卻讓人看不出來；\n言是敏辯的，卻很少出去應酬。"
    show bg56
    white "她對你的情意深厚，卻從未說出口，常常在艷麗的面容上微蹙著眉頭\n，像愁怨鎖心頭。眼中盡是幽邃，卻從未展現，像無知的女孩子。\n明明有顆喜怨瞋心，但卻從不讓人看見過。"
    show bg57
    white "有天深幽的天氣，她獨自操琴，愁容未解，弦中淒惻。\n你在旁邊偷偷聽到了，求鶯鶯再彈一次，但她卻未曾撫過琴。"
    show bg61
    white "剩下後來的事各位也知道了，張生未能中第逗留京師，兩人之間互相\n傳信，信中內容也在時人中流傳。"
    window hide
    scene bg4
    show poem1 at shrink_bg
    with Pause(2.0)
    window show
    white "後來便有了著名的元稹的{color=#FF0000}會真詩三十韻{/color}......"
    white "而之所以讓後人廣為嘆息，讓現代人認為張生渣的緣由，是他後來在\n評價鶯鶯中說道:"
    show bg62
    show char3 at right, slightly_higher
    z "{color=#FF0000}大凡天之所命尤物也，不妖其身，必妖於人。使崔氏子遇合富貴，\n乘寵嬌，不為雲，不為雨，為蛟為螭，吾不知其所變化矣。{/color}"
    z "{color=#FF0000}昔殷之辛，周之幽，據百萬之國，其勢甚厚。然而一女子敗之，\n潰其眾，屠其身，至今為天下僇笑。予之德不足以勝妖孽，是用忍情。{/color}"
    hide char3
    show bg63
    white "唉！他將鶯鶯訴之為紅顏禍水，{color=#FF0000}而不想想自己的問題{/color}，這是\n出於求而不得的心，張生的心中必然有鶯鶯，但這麼形容連我\n也想把張生扒下去。"
    white "一日他想求見鶯鶯，但鶯鶯拒絕了他，兩人互相寫了首詩後，\n從此兩人再不復見。"
    window hide
    show bg64
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「平凡的少年與錯過的愛情-張生傳 完」{/color}"
    return


label end3:
    window hide
    with Pause(2.0)
    show bg16
    window show
    "恭喜獲得結局{color=#FF0000}「牢中乞兒-在異世界的牢房蹲過三年」{/color}"
    return


label specialend1:
    $ honkai = 0
    scene bg4
    show screen shaky_texts
    white "沒有想到有人會選擇這個選項，真是讓本旁白受驚了！"
    white "但你應該知道這代表什麼吧？🫠🫠🫠"
    white "現在我們跳出世界的框架，來個問答吧！🙃🙃🙃"
    window hide
    menu:
        "{color=#FF0000}如果你是鶯鶯的話，你怎麼看你被一個人糾纏{/color}":
            pass
    menu:
        "{color=#FF0000}你認為張生壞不壞嗎？{/color}":
            pass
    menu:
        "壞":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
        "不壞":
            pass
    menu:
        "{color=#FF0000}如果你是鶯鶯的話，你真的理解你自己的心嗎？{/color}":
            pass
    menu:
        "{color=#FF0000}你真的認識張生嗎？{/color}":
            pass
    menu:
        "{color=#FF0000}你為什麼選擇給張生第一次呢？{/color}":
            pass
    menu:
        "因為我愛張生":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
        "因為想逃離媽媽的掌控，做一次真正的女人":
            pass
    window hide
    menu:
        "{color=#FF0000}如果你是鶯鶯的話，你會希望一切能重來嗎？{/color}":
            pass
    menu:
        "{color=#FF0000}鶯鶯傳已經是數年以前的故事了...{/color}":
            pass
    menu:
        "{color=#FF0000}如果能重來，你還會愛上他嗎？{/color}":
            pass
    menu:
        "會":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
        "不會":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
        "我...不知道...":
            pass
    menu:
        "{color=#FF0000}現在你回到張生的視角，如果一切重來，你還會\n愛著鶯鶯嗎？{/color}":
            pass
    menu:
        "愛":
            pass
        "不愛":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
    menu:    
        "{color=#FF0000}你愛著鶯鶯嗎？{/color}":
            pass
    menu:
        "愛":
            pass
        "不愛":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
    menu:
        "{color=#FF0000}現在輪到螢幕前的你了！{/color}":
            pass
    menu:    
        "{color=#FF0000}張生愛鶯鶯嗎？{/color}":
            pass
    menu:
        "愛":
            pass
        "不愛":
            pass
        "我...不知道...":
            $ honkai +=1
            "崩壞值+1，目前崩壞值:{color=#FF0000}[honkai]{/color}"
    if honkai >= 3:
        jump badend
    if honkai == 0:
        jump specialend_zero
    white "看來這次你命很好..."
    window hide
    hide screen shaky_texts
    scene bg15
    with Pause(2.0)
    white "恭喜獲得特殊結局{color=#FF0000}「愛你的鶯鶯」{/color}，能走到這一步，你也是\n很不容易。"
    return
    

label specialend_zero:
    scene bg4
    with dissolve
    aaa "真的沒想到，你竟然可以到這......"
    aaa "你是開掛了吧？"
    hide screen shaky_texts
    show bg58 at screen_shake
    li "可惡被發現了！只能這樣了！"
    show bg59 at screen_shake
    with Pause(1.0)
    with dissolve
    show bg60 at screen_shake
    "恭喜獲得結局{color=#FF0000}「破裂的真相-虛假世界中的虛假世界」{/color}"
    return


label badend:
    window hide
    with Pause(2.0)
    scene bg4
    show bg14
    show screen shaky_texts
    aaa "看來你沒能逃過一劫，只能看看下個實驗體，會不會耐用\n一點......"
    "恭喜獲得特殊結局{color=#FF0000}「School Day-斬殺結局，你被賜予了\n大男人剖腹產。」{/color}"
    return

transform screen_shake:
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0

screen shaky_texts:
    for i in range(35):
        $ xpos = renpy.random.randint(0, 1500)
        $ ypos = renpy.random.randint(0, 900)
        $ word = renpy.random.choice(["崩", "潰", "亂", "錯", "啊", "！","💀"])

        add Text(word, size=40, color="#FF0000") at ShakeAnim:
            xpos xpos
            ypos ypos

transform ShakeAnim:
    parallel:
        linear 0.05 xoffset -5 yoffset -5
        linear 0.05 xoffset 5 yoffset 5
        repeat

label isekai:
    scene bg4
    show bg65
    menu:
        "你不知道該去哪裡，此時冒出三個選擇..."
        "「去長安」":
            jump specialstory1
        "「去無名客棧」":
            jump isekai2
        "「去路邊小徑上廁所」":
            jump TRALALERO
    return

label isekai2:
    show bg66
    white "你走入了無名客棧內，聽說這裡很奇異，沒錯...我說的是人很\n奇異！"
    white "此時有三個人吸引了你的目光，那三個人模樣很奇異......"
    show bg68
    menu:
        "「第一個奇異的人」":
            show char7 at truecenter
            jump describe_char7
        "「第二個奇異的人」":
            show char11 at truecenter
            jump describe_char11
        "「第三個奇異的人」":
            show char10 at truecenter
            jump describe_char10
        "「看完三人的樣貌了」":
            pass
    menu:
        "「你選擇要跟誰攀談呢？」"
        "「第一個奇異的人」":
            show char7 at truecenter
            jump isekai3
        "「第二個奇異的人」":
            show char11 at truecenter
            jump isekai4
        "「第三個奇異的人」":
            show char10 at truecenter
            jump isekai5
    return

label isekai3:
    show bg68
    hide char7
    show char7 at right,slightly_higher
    show char3 at left,slightly_higher
    z"在下一書生也，想像你一樣學習如何除魔衛道。"
    dan "我？呵，教你點東西倒不難……只怕你吃不了這苦頭。"
    show bg76
    white "從這天起，你與但丁進行了高強度訓練..."
    scene bg4
    show bg77
    white "有一日你與但丁聽到有女子喊救命，原來是那個張生尚未見過的鶯鶯\n正呼喊著。"
    show bg78
    white "只見鶯鶯的面前有著一隻惡魔，此時但丁手起刀落解決了牠..."
    show bg79
    white "從此鶯鶯愛上了但丁...而張生在殺魔的道路上愈走愈遠，\n直到但丁望塵莫及......"
    window hide
    show bg80
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「屠魔者，張生也-女人只會影響我拔刀的速度」{/color}"
    return

label isekai4:
    show bg68
    hide char11
    show char11 at right,slightly_higher
    show char3 at left,slightly_higher
    z "在下張生也，不知閣下為何穿著如此奇異呢？"
    chan"你好阿，我是成振宇，我不知道什麼原因就來到這了..."
    show bg81
    white "你們倆人剛進行攀談，世界立刻大變，來到了首爾，此時你\n們面前出現了E級地下城..."
    white "你們當即決定向內探索，結果遇到了雙重地下城..."
    show bg83
    white "神殿內部矗立著數十座巨大石像，中間一尊特別巨大、手持\n權杖與聖杯，神情詭異。"
    white "而你突然動作了起來，很倒楣的你成為了犧牲者..."
    window hide
    scene bg4
    show bg82
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「雕像下的亡魂-一份來自首爾的死亡凝視」{/color}"
    return

label isekai5:
    show bg68
    hide char10
    show char10 at right,slightly_higher
    show char3 at left,slightly_higher
    z "你好在下張生你這身盔甲看起來很有特色，是從大秦來的嗎？"
    gob "我不知道你在說什麼..."
    z "啊，抱歉。只是第一次見到像你這樣不露面的武人。你平時都在做\n什麼？"
    gob "殺哥布林。"
    z "哥布林？那是什麼樣的妖邪？"
    gob "骯髒、殘忍、卑鄙。若你見過他們對女人做的事，你就不會再問\n這種話了。"
    z "……我可以學習嗎？你這樣的本事，我很想知道。"
    gob "不建議。但……你還活著，表示你還沒犯下致命錯誤。"
    show bg84
    white "突然世界大變，你與哥殺突然來到了一個洞穴前..."
    scene bg4
    show bg85
    white "你被一隻哥布林偷襲而亡...但你奇蹟般的重生了..."
    window hide
    show bg86
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「關於我轉生到異世界成為哥布林這檔事」{/color}"
    return


label describe_char7:
    "這個人有一頭銀白色的頭髮，穿著一身血紅大氅，攜帶著不合時代的\n槍械......"
    hide char7
    jump isekai2

label describe_char11:
    "這個人看起來平凡瘦弱，有著一頭黑色短髮，前方有些微碎瀏海。"
    hide char11
    jump isekai2

label describe_char10:
    "這個人帶著深灰色金屬頭盔，眼神是凌厲般的血紅。"
    hide char10
    jump isekai2


label specialstory1:
    show bg69
    white "你在長安的路上，被時光警察誤撞了，結果就來到了那一年的\n《頂級廚師》..."
    show bg70
    white "一番機緣巧合下，你成為了這裡的評審......"
    show bg71
    white "你也很幸運地看到了熟悉的小胖......"
    show bg75
    white "很快的，一盤新鮮的九轉大腸就出爐了！"
    show bg72
    n1 "是故意的，還是不小心的..."
    show bg74
    n2 "是故意的..."
    scene bg4
    show bg67
    white "評審們依序嘗了一口原汁原味..."
    show bg73
    white "當你咬了一口後說出了一句話...真香啊..."
    window hide
    show bg75
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「九轉大腸-那一年的腸汁依舊保留著它的原汁原味」{/color}"
    return

label TRALALERO:
    show bg87
    show char3 at left,slightly_higher
    show char12 at right,
    dra "你好我是美式山海經推銷員，你要成為我們的一員嗎？"
    z "你是？"
    dra "我是{color=#FF0000}tralalero tralala{/color}的信徒，來傳播{color=#FF0000}tralalero tralala{/color}的。"
    show bg88
    white "你雖然感到奇怪，但由於實在是太魔性了，你就一起推廣\n了！"
    window hide
    show bg89
    with Pause(2.0)
    window show
    "恭喜獲得結局{color=#FF0000}「Tralalero tralala～～～」{/color}"
    return