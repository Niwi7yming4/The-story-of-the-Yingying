# 遊戲腳本位於此檔案。

# 聲明該遊戲使用的角色。 color 參數
# 為角色的名稱著色。

define z = Character("張生")
define white = Character("旁白")
define y = Character("鶯鶯")
define zf = Character("鄭婦")

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
    scene gameover1
    " "
    white "如果某一日他能看見來自異世界的鶯鶯傳會發現自己原來這麼渣，\n恭喜獲得結局{color=#FF0000}「孤老終生-打了一輩子的光棍還在適不我值」{/color}"
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
    show char3 at right
    white "便去附近的河邊洗漱，你在離開寺廟前看見了外邊曬著女子衣物\n，但那時並沒有多想。"
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
    show bg4
    show bg7 at shrink_bg
    hide bg2
    " "
    white "是歲，鎮守蒲州的將領渾瑊甫亡，宦官丁文雅不善用兵，\n故軍不領旨，四處趁喪而亂，奪蒲州百姓之金銀。"
    white "而當時蒲州有名的大家崔家，財產甚厚，又有諸多奴僕，\n雖暫居於普救寺，但覺惶恐不安，不知所措。"
    show bg8 
    hide bg7
    " "
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
    scene gameover2
    " "
    show gameover2
    white "在京城娶了一女，一生汲汲營營，沒有什麼功過。\n恭喜獲得結局{color=#FF0000}「中庸之輩-一輩子什麼大事都沒幹，死了連渣都不剩」{/color}"
    return

label story3:
    scene bg10
    hide bg8
    white "過了十多天後，廉使杜確奉天子之命，來主持戎節，\n重新下令軍隊，平定軍亂。"
    show bg4
    show bg9
    hide bg10
    show char3 at left, slightly_higher
    show char4 at right, slightly_higher
    white "鄭厚張之德甚，遂飾饌邀請張生前來，在中堂宴飲。\n\n{color=#FF0000}中堂{/color}：三進院落中，室內必有中堂，一般置兩高几、一條案、兩太師椅，再配個八仙桌，意指一家的四平八穩、中正平和。"
    show char4_2 at right, slightly_higher
    hide char4
    zf "我只是個未亡人，帶著幼兒們，卻不幸遇上了兵亂，自己都難以保身，\n我還有那些尚還年幼的兒女們，而正因為你讓他們都活了下來，這豈是平凡的恩情所能比擬的？\n今天我就讓他們以仁兄之禮拜見，冀以報您的恩情！"
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
    show char4_3 at right, slightly_higher
    zf "是張兄救妳的命，不然妳早被擄去做壓寨夫人了，哪還能像\n現在用病推辭呢？"
    show bg11
    " "
    white "過了一段時間後，一位女子方出閨，穿著一身常服，面容姣好，\n沒有用新妝粉飾。香鬟垂落於眉旁，臉上銷紅沉韻，面上未抹脂粉，卻若光輝動人。"
    white "張生頓時感到驚訝，急忙對她行禮，女子則坐於鄭婦旁。"
    white "由於是鄭婦強迫著她出來的，斜視凝望著門戶，看起來\n內心有些怨懟，心思也不在此處。"
    menu:
        "「初次見面，不知姑娘芳齡？」":
            zf "天子甲子歲之七月，到了現在貞元庚辰年，如今\n她已經十七有餘了！"
        "「我可以娶妳嗎？」":
            zf "公子你要先納個採、問個名，我會考慮一下的。"
        "「妳就是崔鶯鶯嗎？我是來自2025年的穿越者，我是妳的大粉絲，可以跟妳要個簽名嗎？」":
            zf "大粉絲是什麼碗糕嗎？2025年是什麼？我記得現在不是貞元庚辰年嗎？"
    white "目前0.1劇情先到這裡 by梁倡瑋，0.2修改了一點版面，手機有跑版問題，再修改一次"





