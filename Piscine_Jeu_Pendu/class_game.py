import os, sys, pygame, random, json, time
from english_words import english_words_set


class Game:
    def __init__(
        self, screen, width, height, base_dir, player_name="Anon", temps_total=60
    ):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.BASE_DIR = base_dir
        self.clock = pygame.time.Clock()

        self.TEMPS_TOTAL = temps_total

        self.pseudo_joueur = player_name

        # Initialisation variables de partie
        self.theWord = ""
        self.lettres_tapees = set()
        self.lettres_trouvees = set()
        self.nbEssai = 6
        self.mot_cache = ""
        self.score = 0
        self.debut_temps = 0
        self.lettres_revelees_par_aide = set()

        # Fonts
        self.title_font = pygame.font.Font(None, 60)
        self.word_font = pygame.font.Font(None, 50)
        self.letters_font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 20)

        # Images
        self.imageBackground = None
        try:
            bg_path = os.path.join(self.BASE_DIR, "assets", "backGround.jpg")
            self.imageBackground = pygame.image.load(bg_path)
            self.imageBackground = pygame.transform.scale(
                self.imageBackground, (self.WIDTH, self.HEIGHT)
            )
        except:
            print("Background non trouvé")

        self.tips_img = None
        self.lightbulb_rect = pygame.Rect(self.WIDTH - 85, self.HEIGHT - 550, 80, 80)
        try:
            tips_path = os.path.join(self.BASE_DIR, "assets", "tips.png")
            self.tips_img = pygame.image.load(tips_path)
            self.tips_img = pygame.transform.scale(
                self.tips_img, (self.lightbulb_rect.width, self.lightbulb_rect.height)
            )
        except:
            print("Tips image non trouvée")

        self.button_color = (142, 255, 44)
        self.button_rect = pygame.Rect(self.WIDTH - 90, 20, 70, 30)
        self.font = pygame.font.Font(None, 25)
        self.text_button = self.font.render("Close", True, (255, 255, 255))

        # Mots

        self.LISTE_MOTS = [w.lower() for w in english_words_set if w.isalpha()]
        if not self.LISTE_MOTS:
            try:
                with open("fallbacks\fallback_words.txt", "r", encoding="utf-8") as f:
                    self.LISTE_MOTS = [
                        line.strip().lower() for line in f if line.strip()
                    ]
            except FileNotFoundError:
                # Au cas où le fichier fallback n'existe pas non plus
                self.LISTE_MOTS = []
                print("Aucun mot disponible, fallback non trouvé.")

        # Score
        self.FICHIER_CLASSEMENT = os.path.join(self.BASE_DIR, "leaderboard.json")

        # Variables de partie
        self.pseudo_joueur = ""
        self.theWord = ""
        self.lettres_tapees = set()
        self.lettres_trouvees = set()
        self.nbEssai = 6
        self.mot_cache = ""
        self.score = 0
        self.debut_temps = 0
        self.lettres_revelees_par_aide = set()

    def charger_classement(self):
        try:
            with open(self.FICHIER_CLASSEMENT, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def sauvegarder_classement(self, liste):
        try:
            with open(self.FICHIER_CLASSEMENT, "w", encoding="utf-8") as f:
                json.dump(liste, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("Erreur sauvegarde classement:", e)

    def choisir_mot_aleatoire(self):
        mot = random.choice(self.LISTE_MOTS).lower()
        while len(mot) < 4:
            mot = random.choice(self.LISTE_MOTS).lower()
        return mot

    def proposer_lettre(self, lettre):
        lettre = lettre.lower()
        if lettre in self.lettres_tapees or not lettre.isalpha() or len(lettre) != 1:
            return
        self.lettres_tapees.add(lettre)

        if lettre in self.theWord:
            if lettre not in self.lettres_trouvees:
                self.lettres_trouvees.add(lettre)
                if lettre not in self.lettres_revelees_par_aide:
                    self.score += 10
        else:
            self.nbEssai -= 1
            self.score = max(0, self.score - 5)

        self.mot_cache = " ".join(
            [l if l in self.lettres_trouvees else "_" for l in self.theWord]
        )

    def utiliser_aide(self):
        lettres_dispo = [l for l in self.theWord if l not in self.lettres_trouvees]
        if lettres_dispo:
            l = random.choice(lettres_dispo)
            self.lettres_trouvees.add(l)
            self.lettres_tapees.add(l)
            self.lettres_revelees_par_aide.add(l)
            self.mot_cache = " ".join(
                [c if c in self.lettres_trouvees else "_" for c in self.theWord]
            )
            self.score = max(0, self.score - 15)

    def dessiner_pendu(self, erreurs):
        s = self.screen
        pygame.draw.line(s, (0, 0, 0), (100, 515), (250, 515), 5)
        pygame.draw.line(s, (0, 0, 0), (150, 515), (150, 225), 5)
        pygame.draw.line(s, (0, 0, 0), (150, 300), (200, 225), 5)
        pygame.draw.line(s, (0, 0, 0), (150, 225), (250, 225), 5)
        pygame.draw.line(s, (0, 0, 0), (250, 225), (250, 250), 5)
        if erreurs >= 1:
            pygame.draw.circle(s, (0, 0, 0), (250, 270), 20, 3)
        if erreurs >= 2:
            pygame.draw.line(s, (0, 0, 0), (250, 290), (250, 350), 3)
        if erreurs >= 3:
            pygame.draw.line(s, (0, 0, 0), (250, 310), (230, 340), 3)
        if erreurs >= 4:
            pygame.draw.line(s, (0, 0, 0), (250, 310), (270, 340), 3)
        if erreurs >= 5:
            pygame.draw.line(s, (0, 0, 0), (250, 350), (230, 390), 3)
        if erreurs >= 6:
            pygame.draw.line(s, (0, 0, 0), (250, 350), (270, 390), 3)

    def dessiner_interface(self):
        if self.imageBackground:
            self.screen.blit(self.imageBackground, (0, 0))
        else:
            self.screen.fill((255, 255, 255))

        title = self.title_font.render("Hangman Game", True, (200, 0, 0))
        self.screen.blit(title, (self.WIDTH // 2 - title.get_width() // 2, 30))

        mot_surface = self.word_font.render(self.mot_cache, True, (0, 0, 0))
        self.screen.blit(
            mot_surface, (self.WIDTH // 2 - mot_surface.get_width() // 2, 150)
        )

        lettres_proposees = ", ".join(sorted(self.lettres_tapees))
        ligneTitre = self.letters_font.render(
            "Letters already proposed:", True, (0, 0, 0)
        )
        ligneRep = self.letters_font.render(lettres_proposees, True, (0, 0, 0))
        self.screen.blit(ligneTitre, (350, 220))
        self.screen.blit(ligneRep, (350, 255))

        self.dessiner_pendu(6 - self.nbEssai)

        pygame.draw.rect(
            self.screen, self.button_color, self.button_rect, border_radius=10
        )
        self.screen.blit(
            self.text_button, (self.button_rect.x + 11, self.button_rect.y + 7)
        )

        # barre de vie
        ratio_vie = max(0, self.nbEssai / 6)
        pygame.draw.rect(self.screen, (200, 200, 200), (355, 470, 300, 25))
        coul = (
            (142, 255, 44)
            if ratio_vie > 0.5
            else (240, 220, 80) if ratio_vie > 0.2 else (255, 100, 100)
        )
        pygame.draw.rect(self.screen, coul, (355, 470, int(300 * ratio_vie), 25))
        vie_text = self.small_font.render(f"Lives: {self.nbEssai}/6", True, (0, 0, 0))
        self.screen.blit(vie_text, (355, 450))

        if self.tips_img:
            self.screen.blit(
                self.tips_img, (self.lightbulb_rect.x, self.lightbulb_rect.y)
            )

        elapsed = int(time.time() - self.debut_temps)
        restant = max(0, self.TEMPS_TOTAL - elapsed)
        pygame.draw.rect(self.screen, (200, 200, 200), (355, 380, 250, 18))
        pygame.draw.rect(
            self.screen,
            (100, 150, 255),
            (355, 380, int(250 * (restant / self.TEMPS_TOTAL)), 18),
        )
        timer_text = self.small_font.render(f"Time left: {restant}s", True, (0, 0, 0))
        self.screen.blit(timer_text, (355, 360))

        score_text = self.small_font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (50, 125))

    def ecran_pseudo_initial(self):
        saisie = True
        pseudo = ""
        while saisie:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if pseudo.strip() == "":
                            pseudo = "Anon"
                        return pseudo
                    elif e.key == pygame.K_BACKSPACE:
                        pseudo = pseudo[:-1]
                    elif e.unicode.isprintable() and len(pseudo) < 12:
                        pseudo += e.unicode

            if self.imageBackground:
                self.screen.blit(self.imageBackground, (0, 0))
            else:
                self.screen.fill((255, 255, 255))
            title = self.title_font.render("Hangman Game", True, (200, 0, 0))
            self.screen.blit(title, (self.WIDTH // 2 - title.get_width() // 2, 30))
            invite = self.word_font.render("Enter your name:", True, (0, 0, 0))
            self.screen.blit(invite, (self.WIDTH // 2 - invite.get_width() // 2, 180))
            pseudo_surf = self.word_font.render(pseudo + "|", True, (0, 0, 0))
            self.screen.blit(
                pseudo_surf, (self.WIDTH // 2 - pseudo_surf.get_width() // 2, 260)
            )
            pygame.display.flip()
            self.clock.tick(30)

    def afficher_fin_de_partie(self, gagne):
        elapsed = int(time.time() - self.debut_temps)
        restant = max(0, self.TEMPS_TOTAL - elapsed)
        if gagne:
            self.score += int(restant * 2)

        classement = self.charger_classement()
        classement.append(
            {"name": self.pseudo_joueur, "score": self.score, "date": int(time.time())}
        )
        classement = sorted(classement, key=lambda x: x["score"], reverse=True)[:20]
        self.sauvegarder_classement(classement)

        top5 = classement[:5]
        affichage = True
        while affichage:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    affichage = False

            if self.imageBackground:
                self.screen.blit(self.imageBackground, (0, 0))
            else:
                self.screen.fill((255, 255, 255))

            titre = self.title_font.render("Game Over", True, (200, 0, 0))
            self.screen.blit(titre, (self.WIDTH // 2 - titre.get_width() // 2, 30))
            if gagne:
                res = self.title_font.render("You won!", True, (142, 255, 44))
            else:
                res = self.title_font.render(
                    f"Lost! Word: {self.theWord}", True, (255, 0, 0)
                )
            self.screen.blit(res, (self.WIDTH // 2 - res.get_width() // 2, 110))

            score_t = self.word_font.render(f"Score: {self.score}", True, (0, 0, 0))
            self.screen.blit(score_t, (self.WIDTH // 2 - score_t.get_width() // 2, 200))

            y = 280
            header = self.letters_font.render("Top 5 leaderboard:", True, (0, 0, 0))
            self.screen.blit(header, (self.WIDTH // 2 - header.get_width() // 2, y))
            y += 40
            for i, entree in enumerate(top5):
                ligne = self.small_font.render(
                    f"{i+1}. {entree['name']} - {entree['score']}", True, (0, 0, 0)
                )
                self.screen.blit(ligne, (self.WIDTH // 2 - ligne.get_width() // 2, y))
                y += 30

            footer = self.small_font.render(
                "Press any key or click to return / exit", True, (0, 0, 0)
            )
            self.screen.blit(
                footer, (self.WIDTH // 2 - footer.get_width() // 2, self.HEIGHT - 120)
            )
            pygame.display.flip()
            self.clock.tick(30)

    def run(self):
        self.pseudo_joueur = self.ecran_pseudo_initial()
        self.theWord = self.choisir_mot_aleatoire()
        self.lettres_tapees = set()
        self.lettres_trouvees = set()
        self.nbEssai = 6
        self.mot_cache = "_ " * len(self.theWord)
        self.score = 0
        self.debut_temps = time.time()

        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                elif e.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(e.pos):
                        running = False
                    elif self.lightbulb_rect.collidepoint(e.pos):
                        self.utiliser_aide()
                elif e.type == pygame.KEYDOWN:
                    if e.unicode and e.unicode.isalpha():
                        self.proposer_lettre(e.unicode)

            self.dessiner_interface()

            if "_" not in self.mot_cache:
                self.afficher_fin_de_partie(True)
                running = False
            elif self.nbEssai <= 0:
                self.afficher_fin_de_partie(False)
                running = False
            else:
                elapsed = int(time.time() - self.debut_temps)
                if elapsed >= self.TEMPS_TOTAL:
                    self.afficher_fin_de_partie(False)
                    running = False

            pygame.display.flip()
            self.clock.tick(60)
