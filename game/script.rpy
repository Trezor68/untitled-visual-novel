# Postavy ---Definování postav---
define narrator = nvl_narrator
define renko = Character("Renko Usami", color="#e90000")
define maribel = Character("Maribel Hearn", color="#f1d900")
define renkomom = Character("Renčina Mamka")
define n = Character(None, kind=adv)

# Audio ---Definování hudby---
define audio.witch = "audio/BGM/Hagall_EccentricWitchsShop.mp3"
define audio.rusted_chain = "audio/BGM/Hagall_RustedChain.ogg"
define audio.durring_the_lesson = "audio/BGM/Durring-a-Lesson.mp3"
define audio.promenade = "audio/BGM/Promenade.mp3"
define audio.gfc1 = "audio/BGM/gfc1.mp3"

# Pointy ---Budou důležité později ve hře---
default mystery = 0
default fantasy = 0


# Postavy ---Body k postavám. Čím více bodů, tím víc o té postavě víme. (Takzvaně se budou přidávat informace na screenu o postavách)---
default renko_usami = 0
default maribel_hearn = 0
default sumireko_usami = 0



label start:

    scene bg universe

    play music gfc1

    centered "Ahojky. Zdravím vás! "
    extend "Usami Renko jméno mé! "
    extend "Jsem už nějakej ten pátek studentkou vysoké školy. "
    extend "Chodím celkem na zvláštní obor, ale to je prozatím fuk. "
    extend "Miluju noční oblohu. "
    extend "Dokonce jsem schopná určit přesný čas při pohledu na hvězdy! "
    extend "Ne, že by byly tady ve městě nějaké hvězdy vidět, "
    extend "ale když se dostanu jednou za čas do přírody, tak je vidím! "
    extend "Bohužel studium je těžké "
    extend "a nemám dostatek příležitostí se dostat ven z města. "
    extend "Takže se musím spokojit s pár malýma hvězdičkama. "
    $ renko_usami = renko_usami + 1

    nvl clear
     
    centered "Chodím do třídy se svou nejlepší kamarádkou. "
    extend "Jmenuje se Maribel Hearn. "
    $ maribel_hearn = maribel_hearn + 1
    extend "Celkem zajímavé jméno, nemyslíte? "
    extend "Zní hodně evropsky! "
    extend "S Maribel se bavíme prakticky od dětství a máme společné zájmy. "
    extend "Myslím, že nás nic nerozdělí! "
    extend "S Maribel chodíme do našeho klubu. "
    extend "Nic moc se toho tam neděje, "
    extend "takže to spíš bereme jako odpočívarnu po škole. "
    extend "Škola pro mě vůbec není jednoduchá. "
    extend "Vůbec nechápu, jak mě rodiče mohli do takové školy vůbec přihlásit. " 
    extend "Hlavním předmětem je tu totiž Fyzika! "
    extend "Oh ano, já co by nejradši vlítla do světa fantazie se musím učit fyziku. "
    extend "Fyzika je tak omezující! "
    extend "Nemám jí vůbec ráda. "
    extend "Fujky! "

    nvl clear

    centered "Vždycky jsem věřila v nějaké to nadpřirozeno. "
    extend "Věřila jsem, "
    extend "že za hranicema našeho chápání je něco víc. "
    extend "Něco, co si ani nedokážeme vlastníma myšlenkama představit. "
    extend "Nemluvím teďka o věcech, "
    extend "co byste našli v nějakých fantasy knížkách, či horrorech. "
    extend "Mluvím o opravdovém nadpřirozenu. "
    extend "Duchové určitě existují, " 
    extend "ale nejspíš né v takové formě, v jaký si je představujem. "
    extend "Nikdo nemůže přesně vědět jak vypadají. "
    extend "Jestli mají stejné vnímání světa jako my. "
    extend "Kdo ví.. "

    nvl clear

    centered "Vždycky mě to fascinovalo. "
    extend "Chtěla jsem něco takového vidět. "
    extend "Něco fantastického. "
    extend "Něco, co lidské oko nemůže zahlídnout. "
    extend "Ale jak jsem už předtím řekla. "
    extend "Není to něco, "
    extend "co by mohl normální člověk vidět. "

    nvl clear

    centered "Existuje tu však i jiný druh nadpřirozena. "
    extend "Nadpřirozeno o kterém víme! "
    extend "Nejdřív jsem to Maribel nevěřila, "
    extend "ale po určité události vím, "
    extend "že je to pravda. "
    extend "Když jsme si prohlíželi deník snů, "
    extend "co tu po sobě nechala zakladatelka klubu, "
    extend "Usami Sumireko, "
    $ sumireko_usami = sumireko_usami + 1
    extend "moje dávná předchůdkyně, "
    extend "věděli jsme, že to co jsme zažily nebyl jenom sen. "
    extend "Navíc, "
    extend "dvojtý sen není úplně něco, co se běžně stává. "
    extend "Vlastně se to nestává nikdy. "

    nvl clear

    stop music fadeout 2.0
    scene black with fade

    centered "O čem to mluvím ptáte se? "
    extend "Hehe. "

    nvl clear

    centered "Dobře, řeknu vám to."


    jump chapter1