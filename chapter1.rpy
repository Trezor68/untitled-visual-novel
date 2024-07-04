define renko = Character("Renko Usami", color="#e90000")
define maribel = Character("Maribel Hearn", color="#f1d900")
define renkomom = Character("Renčina Mamka")
define n = Character(None, kind=adv)

label chapter1:
   play music "Hagall_EccentricWitchsShop.mp3" fadein 5.0

   n "Bylo ráno, letní vzduch zaplnil místnost"

   n "Ranko otevřela okno do pokoje."

   renko "Ranní vzduch je vždycky tak příjemný."

   n "Říkala si Renko mezitím co si stlala postel."

   n "Ranní vzduch je vskutku příjemný."

   n "Zvlášť v takových vedrech."

   n "V přesné poledne je vůbec zázrak, "
   extend "že takový žár přežijete."

   n "Poslední dobou jsou fakt neskutečný vedra a Renko si to moc dobře uvědomovala."

   renko "Hmm, ranní rutinu mám hotovou, měla bych jít dolů si jít dát snídani."

menu:

   "Jít dolu":

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

   n "Před ní už na ní čekaly schody."

   n "Vždycky když ty schody vidí, tak si vzpomene na tu onu událost."

   n "Renko se jednou pokusila o půlnoci si jít pro nějaký zákusek a díky nízkýmu tlaku se na těch schodech málem zabila."

   n "Znáte to, když rychle vstanete z postele tak po určité době díky nízkému tlaku ztrácíte rovnováhu a táhne vás to k zemi."

   n "A i když se to stalo před několika týdny, pro Renko to bylo jako včera."

   n "Stále měla ten velký strach, že jí to znova chytí."

   n "Tenhle strach byl ale nesmyslný a Renko není hloupá holka, takže si to moc dobře uvědomovala."

   n "I tak měla strach." 
    
   n "I když si uvědomovala, že se nic takového už stát nemůže, protože je na nohách několik minut a tenhle stav z kterýho má tak moc velký strach nastává po pár sekundách toho co vstaneš, tak ten strach má zakořeněný hluboko ve svém podvědomí."

   n "Ten nepříjemný pocit toho, že se mohla díky tomuhle škaredě zranit."

   renko "Renko, jsi silná holka! To zvládneš!"

   renko "Já co se zajímám o okultismus abych se bála schodů? To je opravdu, ale opravdu zlý vtip."

   renko "Hahahahahaha."

   n "Renko se začala smát, protože je to jeden z její způsobů, jak zahnat strach."

   n "Po pár sekundách jí to ale přešlo a sešla schody dolů."

   n "Když sešla dolů, vešla do kuchyně kde už byla nachystaná snídaně."

   renko "Ohhh! Smažený vajíčka! Děkuju mami."

   n "Řekla Renko a pustila se do jídla."

   renko "Mňam, to je dobrý!"

   renkomom "Jsem ráda, že ti chutná."

   renkomom "A jez trošku rychleji, za chvilku ti začíná škola!"

   renko "No joo, dobře."

   n "Renko všechno narvala do sebe, vzala baťoh a utíkala ven."

   renko "Měj se mamiii!"

   n "Mamka na ní zamávala a Renko se vydala směrem do školy."

   stop music fadeout 1.0

   n "Škola nebyla od jejího domu moc daleko, takže nešla nějak extra dlouho."

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

   renko "Poslyš, Mary, nepříjde ti to blbý mi takhle skákat takhle lidem na hlavu?"

   maribel "Rennn, prosím tě. Víš přece, že skáču na hlavu jenom tobě, hehe."

   renko "To je ještě horší..."

   maribel "Horší?"

   renko "Mohla jsem umřít na zástavu srdce!! Víš jak jsem se tě lekla?"

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


