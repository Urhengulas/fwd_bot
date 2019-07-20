from emoji import emojize

START_TEXT = emojize(
    """Hallo!
Ich bin der Blitzer-Bot :rotating_light: für den Landkreis RT. Gerne kannst Du mir eine Nachricht schreiben, die ich dann an die Administratoren :busts_in_silhouette: weiterleite. Bitte beschreibe möglichst präzise aber kurz und in einer einzigen Nachricht, wo der Blitzer :camera: steht :blush:

Deine chat id: {}
""",
    use_aliases=True
)

THANK_TEXT = emojize(
    """Vielen Dank!
Nach kurzer Prüfung werden die Admins den Blitzer in den Channel https://t.me/BlitzerKreisRT Posten. Schau doch direkt Mal rein und abonniere uns!
""",
    use_aliases=True
)
