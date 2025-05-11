screen characters():

    tag menu

    use game_menu(_("Postavy"), scroll="viewport"):

        style_prefix "characters"
            

        has vbox:
            spacing 10
        
        # Bruh moment ---Tahle zpráva se ukáže, pokud čtenář přečetl starou belu.
        if renko_usami == 0:
            text _("Nepřečetl jsi ani první blok a už tě zajímaj postavy, které si ani nepotkal? Upaluj číst! Nic tu zatím není!")
        
        # Hlavní Postavy ---Seznam hlavních postav---
        if renko_usami >= 1:

            text("{b}Hlavní Postavy:\n") at center

            text _("Renko Usami") at center

            if renko_usami >= 2:

                image "../images/_CHARACTERS/Renko Usami/Renko Usami Smile.png" zoom 0.4 at center

            text _("Renko je hlavní postavou tohoto příběhu! Je studentkou na vysoké škole a její koníček je pozorování hvězd.\n") yalign 0.5 at center
        

        if maribel_hearn >= 1:
            text _("Maribel Hearn") at center
            text _("Renčinina kamarádka!\n\n\n") at center


        
        # Zmínky ---Postavy co se jen mihly, nebo byli párkrát zmíněny. Nevyskytují se v příběhu.---
        if sumireko_usami >= 1:
            text("{b}Zmínky:\n") at center

            text _("Sumireko Usami") at center
            text _("Sumireko je zakladatelkou klubu tajných pečetí.") at center