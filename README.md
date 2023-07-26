#TIKTOK VIEWS GENERATOR




ce dépôt contient un bot en Python qui utilise la bibliothèque Selenium pour interagir avec TikTok. Le bot ouvre le lien TikTok spécifié toutes les 2 minutes, reste sur la page pendant 45 secondes, puis se déconnecte. Veuillez utiliser ce code de manière responsable et respecter les politiques d'utilisation de TikTok.

Instructions d'installation (Kali Linux) :
1. Assurez-vous que Python est installé :
   - Kali Linux est livré avec Python préinstallé. Vous pouvez vérifier la version de Python avec la commande suivante :
   ```
   python3 --version
   ```

2. Installez Google Chrome :
   - Pour exécuter le bot, vous aurez besoin du navigateur Google Chrome. Si vous ne l'avez pas déjà installé, vous pouvez le télécharger et l'installer à partir du site officiel de Google Chrome.

3. Installez le pilote ChromeDriver :
   - ChromeDriver est un pilote nécessaire pour que Selenium puisse interagir avec Google Chrome. Téléchargez le ChromeDriver qui correspond à la version de votre Google Chrome à partir du site officiel de ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Une fois téléchargé, extrayez l'archive et notez le chemin vers le fichier `chromedriver`.

4. Clonez le dépôt GitHub :
   ```
   git clone https://github.com/Drpickle-git/Tiktok-views-gen
   ```

5. Naviguez dans le répertoire du projet :
   ```
   cd Tiktok-views-gen
   ```

6. Installez les dépendances :
   ```
   pip3 install selenium
   ```

7. Modifiez le chemin du pilote ChromeDriver :
   - Ouvrez le fichier `Main.py` dans un éditeur de texte.
   - Recherchez la ligne avec `driver_path = '/chemin/vers/le/ChromeDriver'`.
   - Remplacez `'/chemin/vers/le/ChromeDriver'` par le chemin réel vers le fichier `chromedriver` que vous avez téléchargé précédemment.

8. Exécutez le bot :
   ```
   python3 bot_script.py
   ```

9. Le bot commencera à visiter le lien TikTok spécifié toutes les 2 minutes, restera sur la page pendant 45 secondes, puis se déconnectera. Vous pouvez arrêter le bot à tout moment en appuyant sur `Ctrl + C`.

Assurez-vous de toujours respecter les politiques et conditions d'utilisation de TikTok et du site web auquel vous interagissez avec le bot. N'utilisez pas ce bot à des fins malveillantes ou pour enfreindre les règles du site web. Utilisez-le uniquement à des fins éducatives ou avec l'autorisation appropriée des administrateurs du site.
