default lahev_s_vodou = False

label chapter1:
   centered "Kapitola 1."

   pause 3.0

   scene bg bedroom with dissolve

   play music witch fadein 5.0

   n "Bylo ráno, letní vzduch zaplnil místnost."

   n "Renko otevřela okno do pokoje."

   show renko usami smile

   $ renko_usami = renko_usami + 1

   renko "Ranní vzduch je vždycky tak osvěžující."

   hide renko

   n "Říkala si Renko mezitím co si stlala postel."

   n "Ranní vzduch je vskutku osvěžující."

   n "Zvlášť v takových vedrech."

   n "V přesné poledne je vůbec zázrak, "
   extend "že takový žár přežijete."

   n "V ten moment je to fakt boj o holí život."

   n "Poslední dobou jsou fakt neskutečný vedra a Renko si to moc dobře uvědomovala."

   show renko usami smile

   renko "Hmm, ranní rutinu mám hotovou, měla bych si jít dolu pro snídani."

   hide renko

menu:

   "Jít dolu":

      show renko usami smile

      renko "Měla bych jít rychle dolů a nasnídat se abych všechno stíhala."

      n "Řekla si Renko, hodila si tašku přes rameno a otevřela dveře od pokoje."

      jump chapter1_1

   "Ještě se okolo porozhlídnout":

      $ lahev_s_vodou = True

      n "Renko ale měla pocit, že na něco zapomněla a tak se radši ještě podívala po pokoji."

      renko "Hmmm, mám pocit, že jsem zapomněla na něco velmi důležitého, ale co by to mohlo být?"

      n "Říkala si Renko mezitím, co se koukala po pokoji."

      n "Najednou si na stole všimla flašky."

      renko "Ohhhhh!!!"

      n "Byla to lahev s vodou."

      renko "Jak jsem mohla zapomenout na něco tak důležitého?!"

      renko "Bych určitě umřela řízní kdybych si to sebou nevzala. O můj bože, jsem tak ráda, že jsem si na to vzpomněla."

      n "Renko si dala flašku s vodou do tašky a otevřela dveře od pokoje."

      jump chapter1_1



label chapter1_1:

   scene bg schody

   n "Před ní už na ní čekaly schody."

   n "Vždycky když ty schody vidí, tak si vzpomene na tu onu událost."

   n "Renko se jednou pokusila o půlnoci si jít pro nějaký zákusek a díky nízkýmu tlaku se na těch schodech málem zabila."

   renko "Ouch."

   n "Znáte to, když rychle vstanete z postele tak po určité době díky nízkému tlaku ztrácíte rovnováhu a táhne vás to k zemi."

   n "A i když se to stalo před několika týdny, pro Renko to bylo jako včera."

   n "Stále měla ten velký strach, že jí to znova chytí."

   n "Tenhle strach byl ale nesmyslný a Renko není hloupá holka, takže si to moc dobře uvědomovala."

   n "I tak měla strach." 
    
   n "I když si uvědomovala, že se nic takového už stát nemůže, protože je na nohách několik minut a tenhle stav z kterýho má tak moc velký strach nastává po pár sekundách toho co vstaneš, tak ten strach má zakořeněný hluboko ve svém podvědomí."

   n "Ten nepříjemný pocit toho, že se mohla díky tomuhle škaredě zranit."

   renko "Renko, jsi silná holka! To zvládneš!"

   renko "Já co se zajímám o okultismus abych se bála schodů? To je ode mě opravdu, ale opravdu hloupučké!"

   renko "Hahahahahaha."

   n "Renko se začala smát, protože je to jeden z její způsobů, jak zahnat strach."

   n "Po pár sekundách jí to ale přešlo a sešla schody dolů."

   n "Schody naprosto poraženy. říkala si."

   n "Když sešla dolů, vešla do kuchyně kde už byla nachystaná snídaně."

   scene bg kitchen

   renko "Ohhh! Smažené ukulele s rajskou kedlubnou. Děkuju mami."

   n "Řekla Renko a pustila se do jídla."

   renko "Mňam, to je dobrý!"

   renkomom "Jsem ráda, že ti chutná."

   renkomom "A jez trošku rychleji, za chvilku ti začíná škola!"

   renko "No joo, dobře."

   n "Renko všechno narvala do sebe, vzala baťoh a utíkala ven."

   renko "Měj se mamiii!"

   n "Mamka na ní zamávala a Renko se vydala směrem do školy."

   stop music fadeout 1.5

   scene bg way_to_school

   n "Škola nebyla od jejího domu moc daleko, takže nešla nějak extra dlouho."

   play music promenade fadein 5.0  volume 0.75

   n "Vlastně jí stačilo jít pár minut a už viděla školu."

   n "Renko se teda vydala směrem ke dveřím. "
   extend "Když v tom jí někdo skočil na záda."

   n "Byla to Maribel, "
   extend "její nejlepší kamarádka."

   maribel "Ren, ahoooooj!!!!"

   n "Maribel je velmi energetická dívka."
   
   n "Oproti Renko má furt hlavu v oblacích."

   n "Maribel je ten typ dívky, co věří v každou mětskou legendu co uslyší."

   n "Renko se jí vždycky snaží vysvětlit, jak moc velká je to blbost, ale Maribel nikdy nevypadá, že by jí nějak extra poslouchala."

   renko "Poslyš, Mary, nepříjde ti to blbý skákat takhle lidem na hlavu?"

   maribel "Rennn, prosím tě. Víš přece, že skáču na hlavu jenom tobě, hehe."

   renko "To je ještě horší..."

   maribel "Horší?"

   renko "Mohlo se mi zastavit srdíčko a mohla jsem umřít!"

   renko "Už teďka jsem tu mohla začít poletovat jako pomstichtivý duch!"

   n "Renko se nelekla, "
   extend "už je na tohle celkem zvyklá."

   n "Řekla to jenom proto, "
   extend "protože by radši na tohle zvyklá nebyla."

   maribel "Promiiiň."

   n "Maribel vypadala, že jí je to opravdu líto."

   n "Moc si vážila přátelství, "
   extend "co s Renko má a určitě jí nechtěla zabít."

   renko "To je v pohodě Mary. "
   extend "Jenom to už příště prosím nedělej."

   stop music fadeout 1.5

   n "A tak obě holky šly, až spolu konečně došly do školy."

   scene bg school1

   play music durring_the_lesson fadein 5.0

   n "Přišly jen tak akorát. Zrovna v ten čas, co bylo na chodbě nejvíc lidí."

   n "A jelikož měli skřínku obě na jiném místě, tak se tu taky rozdělily."

   n "Renko si nasadile přezuvky a vešla do třídy."

   scene bg school2

   n "Posadila se do lavice a zanedlouho začla první hodina."

   n "Hodina Japonštiny."

   n "To Renko relativně ještě šlo, protože u toho nemusela až tak moc přemýšlet."

   n "Horší byly až další hodiny, kde se učily už trošku víc technický věci."

   n "Z toho Renko už začla bolet hlava."

   n "Nebylo to jen díky té výuce, ale i díky tomu jak velké vedro bylo."

   n "Po době, kterou by někteří mohli považovat za nekonečně dlouhou, zazvonil zvonek na polední přestávku."

   n "Renko si konečně uvědomila, že už je volná a sáhla si pro pití do tašky."

   if lahev_s_vodou:

      n "Oh, tady je! Řekla si Renko a vzala si flašku do ruky."

      renko "Haha, jsem opravdu ráda, že jsem si to pití vzala!"

      n "Renko se napila ozvěžující vody a podívala se z okna."

      renko "Možná když je teďka ta polední přestávka, mohla bych se trošku projít po škole."

      menu:
         "Jít se projít":

            renko "Ano, to je dobrý nápad. Tak jdem na to!"

            n "Řekla si Renko, zvedla se z lavice a vyrazila na chodbu."

            renko "Tak jsem na chodbě, kam teď?"

            menu:
               "Do kafetérie":

                  n "Najednou Renko napadlo, že by mohla zajít do kafetérie."

               "Někam jinam":
                  
                  n "Prvně Renko napadlo, že by mohla jít do Kafetérie,"
                  extend "ale pak si řekla, že by mohla jít někam jinam."


         "Zůstat ve třídě":

            renko "Nahhh, kam bych chodila v takovém horku. Tady jsem aspoň ve stíně."

            n "Řekla si Renko a zůstala ve třídě."

            jump chapter1_2
      

   else:

      n "Renko šmátrala po tašce, ale ať už se snažila sebevíc, svoje pití nemohla najít."

      renko "Kde jsem ho sakra dala?"

      jump chapter1_2

label chapter1_2:      

   n "A tak zazvonil zvonec a začaly odpolední hodiny."

   return


















label bad_end1:

   n "A tak Renko umřela na žízeň."

   n "Špatný konec 1"

   return
      





