import sys
print ("Введите имя вашего персонажа:")
name = (input ())
a = f"Теперь вас зовут {name}."
ds = f"{name}"
dss = f"Он вежливо спросил, не знаете ли вы человека по имени {name}."
sss = f"Вы спокойно ответили ему, что {name} - это вы."
asx = f"Остались только вы, {name}."
print (a)
print ("После долгого путешествия вы наконец прибываете в Столицу! Перед вами Врата Балдура. ")
print ("Вы решаете зайти в таверну \"Веселый цыпленок\". Вас встречает хозяин таверны. Он очень рад очередному гостю, и сразу начинает расспрашивать вас о вашем путешествии. Вы делитесь с ним своей историей, он очень внимательно и с большим интересом слушает. Во время вашего рассказа, хозяин таверны предлагает вам еду, за счет заведения. Какую еду вы веберете?")
eda = [ "1.Жареная курица", "2.Куриный суп", "3.Вареная курица с картошкой"]
print (eda)
b = int (input()) 
match b:
    case 1:
        print (eda[0]) 
        print ("Вы отведали вкуснейшей жареной курицы")
    case 2:
        print (eda[1])
        print ("Вы отведали вкуснейший куриный суп")
    case 3:
        print (eda[2])
        print ("Вы отведали вкуснейшую курицу с картошкой")
print ("После плотного ужина вы наконец решаете отдохнуть. Вы можете снять комнату на ночь в таверне или же переночевать у своих давних знакомых. Что выберете? ")
print ("1.Переночевать в таверне")
print ("2.Переночевать у знакомых")
c = int (input()) 
match c:
    case 1:
        print("Вы спрашиваете у хозяина таверны, сколько будет стоить комната. Хозяин отвечает, что комната будет стоить 50 золотых, но вам, как новому посетителю, он сделает скидку 10 золотых. " )
        print("Вы удивлены подобной щедростью и с радостью принимаете данное предложение")
        print ("Вас проводили до комнаты.")
        print ("Зайдя в комнату, вы ощущаете приятный запах сирени.")
        print ("Перед вами располагается двухспальная кровать, рядом с ней стоит аккуратный прикроватный столик.")
        print ("Вы чувствуете, что усталость начинает одолевать вас.")
        print ("Вы ложитесь спать. Кровать оказалась очень мягкой и удобной, поэтому вы уснули почти мгновенно.")
        print ("Вы очень хорошо выспались и просыпаетесь с очень хорошим настроением.")
        print ("Но ваше хорошее настроение продлилось недолго...")
        print ("Сразу после пробуждения вы обнаружили, что проснулись совершенно в другом месте.")
        print ("Это был какой-то подвал с камерами, напоминающий тюрьму. Напротив вашей решетки находилась небольшая лестница, должно быть это выход.")
        print ("Вы быстро вскочили со своей \"двухспальной кровати\", а на самом деле, с обычной койки.")
        print ("Приблизившись к своей решетке, вы с ужасом обнаруживаете, что вы в этом подвале не одни.")
        print ("По правую руку от вас, находятся еще несколько таких же камер как ваша, из которых доносятся очень неприятные звуки.")
        print ("Вы в панике начинаете искать способ открыть решетку.")
        print ("Осмотрев свою камеру, вы приходите к выводу, что своими силами из нее не выбраться...")
        print ("Прошел день с момента вашего заключения.")
        print ("За это время никто так и не появился.")
        print ("Вы очень голодны, вас мучает жажда.")
        print ("Прошел еще один день...")
        print ("Все ваши попытки выбраться закончились неудачей.")
        print ("Вы полностью истощены.")
        print ("К этому времени звуки из соседних камер прекратились. Видимо ваши \"соседи\" находились здесь гораздо дольше.")
        print ("От постоянного одиночества, голода и чувства тревоги, ваше сознание начинает давай сбои, вы чувствуете что сходите с ума.")
        print ("Вся надежда остается на ваших знакомых...")
        print ("Вы вините себя в том, что доверились хозяину таверны, по сути первому встречному, который просто был вежлив к вам.")
        print ("Вскоре вы вовсе потеряли счет времени.")
        print ("Вдруг, вы слышите чьи-то шаги, доносящиеся со стороны лестницы.")
        print ("Вы надетесь что этот человек вам поможет.")
        print ("Но надежда эта умерла, как только вы увидели этого человека...")
        print ("В подвал спустился человек в черной мантии, неся на руках какого-то гнома.")
        print ("Видимо, очередную жертву.")
        print ("Не обращая на вас внимания, человек в черном отнес гнома в камеру, после чего вы услышали ужасные звуки.")
        print ("Через несколько минут, человек вышел из камеры, держа в руке отрезанную кисть гнома!")
        print ("Находясь в состоянии шока, вы не могли издать ни звука.")
        print ("Вскоре убийца подошел к вашей камере, и произнес фразу от которой вас бросило в дрожь.")
        print (asx)
        print ("С этими словами убийца открыл вашу камеру.")
        print ("В вашем состоянии сопротивление было попросту невозможным..")
        print ("Убийца повалил вас на пол.")
        print ("Видимо тот факт, что вы должны были стать последней жертвой, раззадорил его.")
        print ("Перед тем как убить, он захотел вас помучить.")
        print ("Вы начали ощущать очень сильную боль.")
        print ("В этот момент ваше сознание вновь дало сбой, все мысли спутались, пребывание в заключении губительно сказалось на вашей психике и на сознании в целом.")
        print ("Через мгновение вы слышите как в подвал вбегает несколько человек.")
        print ("Вы чувствуете как убица отпрянул от вас и с криком побежал в сторону этих людей.")
        print ("Через несколько секунд вы слышите свист стрелы или арбалетного болта, после чего чье-то тело с грохотом падает на пол.")
        print ("\"-Ну и бойня.\"")
        print ("\"-Он держал их здесь, как скот\"")
        print ("\"-Смотрите! Здесь кто-то есть, кто-то живой!\"")
        print ("\"-Эй, вы впорядке?\"")
        print ("\"-Бедняжка... \"")
        print ("\"-Сержант Вацлав, мы осмотрели остальные камеры, все мертвы\"")
        print ("\"-Столько жертв, а ради чего?\"")
        print ("\"-Ладно, ребята, вытаскивайте трупы и везите их в морг\"")
        print ("\"-А что делать этим беднягой?\"")
        print ("\"-Отнести в \"Лечебницу Йозефки\"\"")
        print ("\"-Может там смогут помочь...\"")
        sys.exit ("Поздравляю! Вы прошли игру на концовку \"Пациент №101\"")
        
    case 2:
        print("Несмотря на предложение и уговоры хозяина таверны остаться ночевать здесь, вы все же решили переночевать у знакомых. Перед вами узкие улочки Врат Балдура. По пути к дому знакомых, ваше внимание привлекает оружейная лавка \"У Золтана\". Вы вспоминаете, как во время вашего путешествия вас предупреждали, что во Вратах Балдура просто необходимо всегда иметь при себе оружие, \"для вашей же безопасности\". Зайти в лавку \"У Золтана\"?  ")
        print("1.да")
        print("2.нет")
        d = int (input())
        if d == 1:
            print ("Вы зашли в в оружейную лавку, вас встретил бородатый гном.")
            print ("Вы говорите, что вам необходим небольшой кинжал \"для самообороны\". Услышав это, дварф усмехнулся и предложил вам на выбор:")
            klinok = {"стилет", "чинкуэда"}
            print (klinok)
            print ("Ваш выбор? (введите полное название кинжала)")
            na = (input())
            ne = f"Вы выбрали {na} "
            print (ne)
            print ("Вам сразу понравилось это оружие, и вы без промедления купили его.")
            print ("После покупки, вы со спокойной душой пошли к своим знакомым.")
            print ("У своих знакомых вы ложитесь спать, за ночь не происходило ничего особенного, поэтому вы хорошо выспались")
            print ("Утром знакомые пошли показывать вам город.")
            print ("Вы вышли на площадь.")
            print ("Перед вами огромная ярмарка! Вы с интересом наблюдаете как стремительно и усетливо здесь течет жизнь.")
            print ("Продавец старается привлечь твое внимание и заинтересовать своими товарами.")
            print ("Но ваши знакомые говорят вам не вестись на их предложения и кроме этого, называют всех этих торговцев шарлатанами и обманщиками.")
            print ("Вы решаете прислушаться к совету знакомых.")
            print ("После площади знакомые повели вас в банк, чтобы забрать свои деньги, а помимо этого завести для вас счет на котором будут храниться ваши деньги.")
            print ("Как они сказали, это поможет сохранить ваши деньги в безопасности.")
            print ("Но перед тем как зделать счет, вам необходимо пройти тестирование на умственные способности.")
            print ("Как заявили представители банка, это небольшая формальность.")
            print ("Вас задевает тот факт, что кто-то сомневается в ваших умственных способностях.")
            print ("Но выбора, похоже у вас нет.")
            print ("Решите 5 примеров чтобы мы могли измерить уровень вашего интеллекта")
            
            print ("Сколько будет 2 + 2: ")
            def f(x):
                return x + 2
            res = f(2)
            r1 = (input())
            print ("Сколько будет 5 - 3: ")
            def f(x, y):
                return x - y
            res1 = f(5, 3)
            r2 = (input())
            print ("Сколько будет 5 * 7: ")
            def f(x, y):
                return x * y
            res2 = f(5, 7)
            r3 = (input())
            print ("Сколько будет 625/5: ")
            def f(x, y):
                return x / y
            res3 = f(625, 5)
            r4 = (input())
            print ("Сколько будет 9 + 14 * 36: ")
            def f(x, y, z):
                return x + y * z
            res4 = f(9, 14, 36)
            r5 = (input())
            print ("Во время проверки ваших результатов, со второго этажа банка внезапно выбегает испуганный посетитель.")
            print ("Стража сразу побежала наверх, проверить что там произошло.")
            print ("Подняться наверх?")
            print ("1.Подняться")
            print ("2.Скорее покинуть банк")
            e = int (input())
            match e:
                case 1:
                    print ("Вы аккуратно поднимаетесь по лестнице.")
                    print ("Уже очень скоро вы начинаете ощущать ужасный запах.")
                    print ("Поднявшись на второй этаж, вы с ужасом обнаруживаете изуродованное тело без правой руки.")
                    print ("На одной из стен вы видите нарисованный символ черепа с отпечатками ладоней по бокам.")
                    print ("Вы спрашиваете одного из стражников об этом символе.")
                    print ("Он рассказывает вам о том, что уже в течение нескольких месяцев по всему городу находят трупы.")
                    print ("И у всех этих трупов отсутствует правая рука.")
                    print ("Стражник считает что в этом замешан древний культ последователей Баала.")
                    print ("Баал - бог насилия. Давным давно в его честь был основан культ последователей Баала.")
                    print ("Для вступления в культ было необходимо совершить убийство определенного человека, с последующим отрезанием руки, в доказательство своего поступка.")
                    print ("Стражник полагает что в городе появился именно такой \"последователь\".")
                    print ("А теперь стражник просит вас удалится с места преступления.")
                    print ("По дороге к лестнице, вы случайно натыкаетесь на окровавленый клочек бумаги.")
                    print ("Вы пытаетесь разглядеть что на нем написано.")
                    print ("Вы обнаруживаете, что эта бумажка - это список жертв Баала!")
                    print ("Из-за крови, вы можете разобрать далеко не все имена")
                    person = {"имя": "Патриция", "возраст": "неразборчиво", "адрес": "\"Золотая голубка\"" }
                    person2 = {"неразборчиво"}
                    person3 = {"имя": "Золтан", "возраст": 124, "адрес": "\"У Золтана\""}
                    person4 = {"имя": "неразборчиво", "возраст": 46, "адрес": "\"Городской Банк\""}
                    print (person)
                    print (person2)
                    print (person3)
                    print (person4)
                    print ("Просматривая список, вы с ужасом читаете последнее имя - это ваше имя!")
                    person5 = {"имя": ds, "возраст": 25, "адрес": "\"неразборчиво\""}
                    print (person5)
                    print ("Вы понимаете, что действовать необходимо как можно скорее!")
                    print ("Вы быстро спускаетесь к своим знакомым и рассказываете то, что узнали.")
                    print ("Они сказали вам как можно быстрее бежать на пристань, там спросить капитана \"Галки\", Эдварда Кенуэя.")
                    print ("За некоторую плату он сможет обеспечить вам охрану и быстро вывести из города. ")
                    print ("Вы выбежали из банка и понеслись на пристань.")
                    print ("Теперь абсолютно каждый человек на улице вызывает у вас подозрение и страх.")
                    print ("Внезапно ваш путь преграждает человек в черной мантии.")
                    print ("Вы сразу понимаете что это не просто прохожий...")
                    print ("Вы поворачиваете в другую сторону и начинаете бежать куда глаза глядят.")
                    print ("После непродолжительного побега, вы попали на хорошо знакомую вам улочку.")
                    print ("В центре этой улицы красовалась вывеска \"Веселый цыпленок\".")
                    print ("Вы вбегаете в таверну и сразу же ощущаете облегчение.")
                    print ("К вам подошел хозяин таверны.")
                    print ("Он обеспокоенно спросил, что с вами случилось.")
                    print ("Вы в подробностях рассказали что с вами произошло.")
                    print ("Хозяин таверны, не скрывая своего волнения, предложил свою помощь.")
                    print ("Он сказал вам, что вы можете выйти через заднюю дверь на кухне, после вы сможете довольно быстро добраться до пристани.")
                    print ("Вы очень благодарны хозяину и сразу же идете с ним к той двери.")
                    print ("Зайдя в кухню, вы с ужасом обнаруживаете пустую комнату, в середине которой стоит тот самый человек в черном!")
                    print ("Вы понимаете, что этот хозяин таверны, все время лишь притворялся вашим другом, а на самом деле работает с этим убийцей!")
                    print ("Убийца медленно начинает приближаться к вам, а хозяин таверны в это время выбегает из комнаты, после чего запирает за собой дверь.")
                    print ("Назад пути нет!")
                    print ("Убийца достает кинжал с изогнутым лезвием и делает выпад в вашу сторону, вы пытаетесь увернуться, но вам не хватает ловкости, вас ранили в руку.")
                    print ("Следующий удар мог стать для вас смертельным, если бы не кинжал, который вы раннее купили в лавке \"У Золтана\". ")
                    print ("Кинжал впился в убийцу по рукоять.")
                    print ("Убийца рухнул на пол. Вокруг уже бездыханного тела начала образовываться красная лужа.")
                    print ("Вас охватывает паника и страх.")
                    print ("А вдруг хозяин таверны вернется и закончит начатое этим убийцей??")
                    print ("Вы быстро осматриваете комнату.")
                    print ("Ваше внимание привлекает неприметная дверь в конце комнаты")
                    print ("\"Видимо это та самая дверь о которой говорил хозяин, не все сказанное им было ложью!\"")
                    print ("Вы выбегаете из таверны, и направляетесь к пристани.")
                    print ("На пристани вы довольно долго искали \"Галку\". Но уже совсем скоро вы нашли и корабль и капитана.")
                    print ("Вы изложили капитану всю ситуацию.")
                    print ("После недолгих раздумий, Эдвард согласился вывести вас из города.")
                    print ("Эти события оставили огромный след в вашей жизни.")
                    print ("Каждую ночь вас мучают кошмары связанные той самой кухней в той самой таверне.")
                    print ("Вы не уверены до конца, был ли хозяин таверны таким же преступником как и убийца, или же он был ли жетвой, и его заставляли помогать \"последователям Баала\".")
                    print ("Вы этого уже никогда не узнаете, но ведь это и не так важно.")
                    print ("Единственное что вы знаете наверняка, вы никогда не вернетесь во Врата Балдура. Вы решили начать новую жизнь, жизнь подальше от больших городов.")
                    print ("Вы поселились в небольшой уютной деревушке \"Эльсвелл\".")
                    print ("Здесь вы наконец смогли отпустить прошлое, и начать новую, счастливую жизнь.")
                    sys.exit ("Поздравляю! Вы прошли игру на концовку \"Новая жизнь\"")
                case 2:
                    print ("Вы со своими знакомыми поспешили как можно скорее покинуть банк и уйти от этого места куда подальше")
                    print ("Вы со своими знакомыми поспешили как можно скорее покинуть банк и уйти от этого места куда подальше.  ")
                    print ("Ваши знакомые предложили пойти домой, вы полностью поддерживаете это предложение.")
                    print ("По пути домой, ваши знакомые решили зайти в магазин, купить продуктов к ужину.")
                    print ("Вы остались на улице, после происшествия в банке вам не хотелось заходить в какие-либо здания, кроме дома знакомых.")
                    print ("Вдруг, вас кто-то окликивает.")
                    print ("Вы оборачиваетесь и видите человека в черной мантии.")
                    print ("Его голос излучал спокойствие и доброту.")
                    print (dss)
                    print ("Своими манерами этот человек произвел на вас положительное впечатление.")
                    print (sss)
                    print ("После вашей фразы, лицо незнакомца изменилось, он начал улыбаться.")
                    print ("Вы не понимаете, что могло вызвать у него улыбку, и решаете спросить его об этом.")
                    print ("Неуспели вы закончить свой вопрос, как вашу грудь пронзила сильная боль.")
                    print ("Незнакомец с огромной силой вонзил кинжал с изогнутым лезвием вам между ребер.")
                    print ("У вас потемнело в глазах, вы чувствуете что начинаете захлебываться кровью.")
                    print ("Через несколько мгновений вы перестаете ощущать что-либо.")
                    print ("Последнее что вы ощутили, были губы незнакомца, котороые прильнули к вашему уху, и фразу: \"Во славу Баала\"...")
                    sys.exit ("Поздравляю! Вы прошли игру на концовку\"Жертва Баала\".")
        if d == 2:
            print ("Вы решили проигнорировать это предупреждение.")
            print ("Вскоре вы дошли до дома своих знакомых.")
            print ("У своих знакомых вы ложитесь спать, за ночь не происходило ничего особенного, поэтому вы хорошо выспались")
            print ("Утром знакомые пошли показывать вам город.")
            print ("Вы вышли на площадь.")
            print ("Перед вами огромная ярмарка! Вы с интересом наблюдаете как стремительно и усетливо здесь течет жизнь.")
            print ("Продавец старается привлеч твое внимание и заинтересовать своими товарами.")
            print ("Но ваши знакомые говорят вам не вестись на их предложения и кроме этого, называют всех этих торговцев шарлатанами и обманщиками.")
            print ("Вы решаете прислушаться к совету знакомых.")
            print ("После площади знакомые повели вас в банк, чтобы забрать свои деньги, а помимо этого завести для вас счет на котором будут храниться ваши деньги.")
            print ("Как они сказали, это поможет сохранить ваши деньги в безопасности.")
            print ("Но перед тем как зделать счет, вам необходимо пройти тестирование на умственные способности.")
            print ("Как заявили представители банка, это небольшая формальность.")
            print ("Вас задевает тот факт, что кто-то сомневается в ваших умственных способностях.")
            print ("Но выбора, похоже у вас нет.")
            print ("Решите 5 примеров чтобы мы могли измерить уровень вашего интеллекта")
            
            print ("Сколько будет 2 + 2: ")
            def f(x):
                return x + 2
            res = f(2)
            r1 = (input())
            print ("Сколько будет 5 - 3: ")
            def f(x, y):
                return x - y
            res1 = f(5, 3)
            r2 = (input())
            print ("Сколько будет 5 * 7: ")
            def f(x, y):
                return x * y
            res2 = f(5, 7)
            r3 = (input())
            print ("Сколько будет 625/5: ")
            def f(x, y):
                return x / y
            res3 = f(625, 5)
            r4 = (input())
            print ("Сколько будет 9 + 14 * 36: ")
            def f(x, y, z):
                return x + y * z
            res4 = f(9, 14, 36)
            r5 = (input())
            print ("Во время проверки ваших результатов, со второго этажа банка внезапно выбегает испуганный посетитель.")
            print ("Стража сразу побежала наверх, проверить что там произошло.")
            print ("Подняться наверх?")
            print ("1.Подняться")
            print ("2.Скорее покинуть банк")
            e = int (input())
            match e:
                case 1:
                    print ("Вы аккуратно поднимаетесь по лестнице.")
                    print ("Уже очень скоро вы начинаете ощущать ужасный запах.")
                    print ("Поднявшись на второй этаж, вы с ужасом обнаруживаете изуродованное тело без правой руки.")
                    print ("На одной из стен вы видите нарисованный символ черепа с отпечатками ладоней по бокам.")
                    print ("Вы спрашиваете одного из стражников об этом символе.")
                    print ("Он рассказывает вам о том, что уже в течение нескольких месяцев по всему городу находят трупы.")
                    print ("И у всех этих трупов отсутствует правая рука.")
                    print ("Стражник считает что в этом замешан древний культ последователей Баала.")
                    print ("Баал - бог насилия. Давным давно в его честь был основан культ последователей Баала.")
                    print ("Для вступления в культ было необходимо совершить убийство определенного человека, с последующим отрезанием руки, в доказательство своего поступка.")
                    print ("Стражник полагает что в городе появился именно такой \"последователь\".")
                    print ("А теперь стражник просит вас удалится с места преступления.")
                    print ("По дороге к лестнице, вы случайно натыкаетесь на окровавленый клочек бумаги.")
                    print ("Вы пытаетесь разглядеть что на нем написано.")
                    print ("Вы обнаруживаете, что эта бумажка - это список жертв Баала!")
                    print ("Из-за крови, вы можете разобрать далеко не все имена")
                    person = {"имя": "Патриция", "возраст": "неразборчиво", "адрес": "\"Золотая голубка\"" }
                    person2 = {"неразборчиво"}
                    person3 = {"имя": "Золтан", "возраст": 124, "адрес": "\"У Золтана\""}
                    person4 = {"имя": "неразборчиво", "возраст": 46, "адрес": "\"Городской Банк\""}
                    print (person)
                    print (person2)
                    print (person3)
                    print (person4)
                    print ("Просматривая список, вы с ужасом читаете последнее имя - это ваше имя!")
                    person5 = {"имя": ds, "возраст": 25, "адрес": "\"неразборчиво\""}
                    print (person5)
                    print ("Вы понимаете, что действовать необходимо как можно скорее!")
                    print ("Вы быстро спускаетесь к своим знакомым и рассказываете то, что узнали.")
                    print ("Они сказали вам как можно быстрее бежать на пристань, там спросить капитана \"Галки\", Эдварда Кенуэя.")
                    print ("За некоторую плату он сможет обеспечить вам охрану и быстро вывести из города. ")
                    print ("Вы выбежали из банка и понеслись на пристань.")
                    print ("Теперь абсолютно каждый человек на улице вызывает у вас подозрение и страх.")
                    print ("Внезапно ваш путь преграждает человек в черной мантии.")
                    print ("Вы сразу понимаете что это не просто прохожий...")
                    print ("Вы поворачиваете в другую сторону и начинаете бежать куда глаза глядят.")
                    print ("После непродолжительного побега, вы попали на хорошо знакомую вам улочку.")
                    print ("В центре этой улицы красовалась вывеска \"Веселый цыпленок\".")
                    print ("Вы вбегаете в таверну и сразу же ощущаете облегчение.")
                    print ("К вам подошел хозяин таверны.")
                    print ("Он обеспокоенно спросил, что с вами случилось.")
                    print ("Вы в подробностях рассказали что с вами произошло.")
                    print ("Хозяин таверны, не скрывая своего волнения, предложил свою помощь.")
                    print ("Он сказал вам, что вы можете выйти через заднюю дверь на кухне, после вы сможете довольно быстро добраться до пристани.")
                    print ("Вы очень благодарны хозяину и сразу же идете с ним к той двери.")
                    print ("Зайдя в кухню, вы с ужасом обнаруживаете пустую комнату, в середине которой стоит тот самый человек в черном!")
                    print ("Вы понимаете, что этот хозяин таверны, все время лишь притворялся вашим другом, а на самом деле работает с этим убийцей!")
                    print ("Убийца медленно начинает приближаться к вам, а хозяин таверны в это время выбегает из комнаты, после чего запирает за собой дверь.")
                    print ("Назад пути нет!")
                    print ("Убийца достает кинжал с изогнутым лезвием и делает выпад в вашу сторону, вы пытаетесь увернуться, но вам не хватает ловкости, вас ранили в ногу.")
                    print ("Собрав все свои силы, вы пытаетесь оттолкнуть убийцу. Как бы вам сейчас пригодился нож...")
                    print ("Ваш толчок заставил убийцу врасплох.")
                    print ("В эту секунду вы, краем глаза, замечаете дверь на улицу о которой говорил хозяин таверны.")
                    print ("Воспользовавшись моментом, вы выбегаете на улицу, из вашей ноги течет кровь.")
                    print ("Вы пытаетесь убежать, но ваша рана не дает этого сделать.")
                    print ("Ваш побег длился недолго. Вскоре убийца догнал вас.")
                    print ("Он повалил вас на землю, вы почувствовали сильную, пронзающую боль в районе живота, после чего потеряли сознание.")
                    print ("Через некоторое время, вы очнулись на больничной койке.")
                    print ("Возле вас находилась лекарша, которая, увидев что вы проснулись, сразу же побежала звать кого-то.")
                    print ("После чего в комнату вошли ваши знакомые.")
                    print ("Они рассказали, что вас спасли проходящие неподалеку стражники.")
                    print ("Но убийцу поймать так и не удалось.")
                    print ("Теперь вы в безопасности, но надолго ли?")
                    print ("Нет сомнений в том, что убийца постарается завершить начатое.")
                    print ("Тем более сейчас, когда вы прикованы к больничной койке.")
                    print ("Вы не знаете, доживете ли до своей выписки.")
                    print ("Одна радость, ваши знакомые обещают быть с вами всё время, пока вас не выпишут.")
                    print ("Их поддержка дает вам надежду.")
                    print ("Возможно, вы все же переживете все эти события...")
                    sys.exit ("Поздравляю! Вы прошли игру на концовку\"Надежда есть...\".")
                case 2:
                    print ("Вы со своими знакомыми поспешили как можно скорее покинуть банк и уйти от этого места куда подальше.  ")
                    print ("Ваши знакомые предложили пойти домой, вы полностью поддерживаете это предложение.")
                    print ("По пути домой, ваши знакомые решили зайти в магазин, купить продуктов к ужину.")
                    print ("Вы остались на улице, после происшествия в банке вам не хотелось заходить в какие-либо здания, кроме дома знакомых.")
                    print ("Вдруг, вас кто-то окликивает.")
                    print ("Вы оборачиваетесь и видите человека в черной мантии.")
                    print ("Его голос излучал спокойствие и доброту.")
                    print (dss)
                    print ("Своими манерами этот человек произвел на вас положительное впечатление.")
                    print (sss)
                    print ("После вашей фразы, лицо незнакомца изменилось, он начал улыбаться.")
                    print ("Вы не понимаете, что могло вызвать у него улыбку, и решаете спросить его об этом.")
                    print ("Неуспели вы закончить свой вопрос, как вашу грудь пронзила сильная боль.")
                    print ("Незнакомец с огромной силой вонзил кинжал с изогнутым лезвием вам между ребер.")
                    print ("У вас потемнело в глазах, вы чувствуете что начинаете захлебываться кровью.")
                    print ("Через несколько мгновений вы перестаете ощущать что-либо.")
                    print ("Последнее что вы ощутили, были губы незнакомца, которые прильнули к вашему уху, и фразу: \"Во славу Баала\"...")
                    sys.exit ("Поздравляю! Вы прошли игру на концовку\"Жертва Баала\".")






